"""Nanopublication publish: Markdown-LD via yaml-ld -> nanopub."""

from __future__ import annotations

import re
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import rdflib
import sh
import yaml
import yaml_ld
from rdflib import Dataset, Graph, Literal, Namespace, URIRef
from yaml_ld.document_loaders.default import DEFAULT_DOCUMENT_LOADER
from yaml_ld.document_loaders.local_file import LocalFileDocumentLoader
from yaml_ld.to_rdf import ToRDFOptions


NP = Namespace("http://www.nanopub.org/nschema#")
PROV = Namespace("http://www.w3.org/ns/prov#")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")
TEMP_NP = Namespace("http://purl.org/nanopub/temp/np/")
PROFILE_PATH = Path.home() / ".nanopub" / "profile.yml"
PRODUCTION_REGISTRY = "https://registry.knowledgepixels.com/np/"
TEST_REGISTRY = "https://test.registry.knowledgepixels.com/np/"
SITE_BASE = "https://nanopublishing.iolanta.tech/"
SITE_CONTEXT_BASE = f"{SITE_BASE}context/"


def _local_site_document_loader(source: str, options: dict) -> dict:
    if source.startswith(SITE_CONTEXT_BASE):
        relative_path = source.removeprefix(SITE_BASE)
        local_path = Path(__file__).resolve().parents[2] / "docs" / relative_path
        return LocalFileDocumentLoader()(local_path.as_uri(), options)

    return DEFAULT_DOCUMENT_LOADER(source, options)


def _dataset_from_markdown_ld(path: Path) -> Dataset:
    path = path.expanduser().resolve()
    if not path.is_file():
        raise FileNotFoundError(path)

    nq = yaml_ld.to_rdf(
        path,
        ToRDFOptions(
            format="application/n-quads",
            document_loader=_local_site_document_loader,
        ),
    )
    return Dataset().parse(data=nq, format="nquads")


def _load_profile() -> dict:
    return yaml.safe_load(PROFILE_PATH.read_text())


def _now_literal() -> Literal:
    return Literal(datetime.now(timezone.utc).replace(tzinfo=None), datatype=XSD.dateTime)


def _copy_graph_fragments(
    source_dataset: Dataset,
    destination_graph: Graph,
    subject: rdflib.term.Node,
    predicate: URIRef,
) -> None:
    default_graph = source_dataset.default_context
    graph_by_id = {
        graph.identifier: graph
        for graph in source_dataset.contexts()
        if graph.identifier != default_graph.identifier
    }

    for _, _, graph_id in default_graph.triples((subject, predicate, None)):
        for triple in graph_by_id.get(graph_id, Graph()):
            destination_graph.add(triple)


def _build_nanopub(path: str, derived_from: str = "") -> Dataset:
    profile = _load_profile()
    source_dataset = _dataset_from_markdown_ld(Path(path))
    creation_time = _now_literal()

    dataset = Dataset()
    dataset.bind("np", NP)
    dataset.bind("prov", PROV)
    dataset.bind("xsd", XSD)

    for prefix, namespace in source_dataset.namespaces():
        dataset.bind(prefix, namespace)

    nanopub_uri = TEMP_NP[""]
    head_uri = TEMP_NP["Head"]
    assertion_uri = TEMP_NP["assertion"]
    provenance_uri = TEMP_NP["provenance"]
    pubinfo_uri = TEMP_NP["pubinfo"]

    head = Graph(dataset.store, head_uri)
    assertion = Graph(dataset.store, assertion_uri)
    provenance = Graph(dataset.store, provenance_uri)
    pubinfo = Graph(dataset.store, pubinfo_uri)

    source_default_graph = source_dataset.default_context
    nanopub_predicate = TEMP_NP["nanopublication"]
    roots = list(source_default_graph.subjects(nanopub_predicate, None))
    nanopub_nodes = list(source_default_graph.objects(None, nanopub_predicate))

    if nanopub_nodes:
        for nanopub_node in nanopub_nodes:
            _copy_graph_fragments(source_dataset, assertion, nanopub_node, assertion_uri)

            for _, predicate, obj in source_default_graph.triples((nanopub_node, None, None)):
                if predicate == assertion_uri:
                    continue
                provenance.add((assertion_uri, predicate, obj))

        for root in roots:
            for _, predicate, obj in source_default_graph.triples((root, None, None)):
                if predicate == nanopub_predicate:
                    continue
                pubinfo.add((nanopub_uri, predicate, obj))
    else:
        _copy_graph_fragments(source_dataset, assertion, None, assertion_uri)
        _copy_graph_fragments(source_dataset, provenance, None, provenance_uri)
        _copy_graph_fragments(source_dataset, pubinfo, None, pubinfo_uri)

    if len(assertion) == 0 and len(provenance) == 0 and len(pubinfo) == 0:
        for triple in source_default_graph:
            assertion.add(triple)

    head.add((nanopub_uri, rdflib.RDF.type, NP.Nanopublication))
    head.add((nanopub_uri, NP.hasAssertion, assertion_uri))
    head.add((nanopub_uri, NP.hasProvenance, provenance_uri))
    head.add((nanopub_uri, NP.hasPublicationInfo, pubinfo_uri))

    provenance.add((assertion_uri, PROV.generatedAtTime, creation_time))
    if derived_from.strip():
        provenance.add((assertion_uri, PROV.wasDerivedFrom, URIRef(derived_from.strip())))

    pubinfo.add((nanopub_uri, PROV.generatedAtTime, creation_time))
    pubinfo.add((nanopub_uri, PROV.wasAttributedTo, URIRef(profile["orcid_id"])))

    return dataset


def _store_dataset(dataset: Dataset, destination: Path) -> None:
    destination.write_text(dataset.serialize(format="trig"))


def _default_signed_output_path(source_path: str) -> Path:
    source = Path(source_path).expanduser().resolve()
    return source.with_name(f"signed.{source.stem}.trig")


def _sign_with_rust_cli(dataset: Dataset) -> tuple[Path, str]:
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        unsigned_path = tmpdir_path / "unsigned.trig"
        signed_path = tmpdir_path / f"signed.{unsigned_path.name}"
        _store_dataset(dataset, unsigned_path)

        output = str(sh.nanopub("sign", str(unsigned_path)))
        match = re.search(r"^URI:\s+(https://w3id\.org/np/\S+)$", output, re.MULTILINE)
        if not match:
            raise RuntimeError(f"Could not parse signed nanopub URI from output:\n{output}")
        if not signed_path.is_file():
            raise RuntimeError(f"Signed nanopub not created at {signed_path}")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".trig", prefix="signed-nanopub-") as handle:
            persisted_signed_path = Path(handle.name)
        shutil.copyfile(signed_path, persisted_signed_path)
        return persisted_signed_path, match.group(1)


def _publish_signed_file(signed_path: Path, test_server: bool = False) -> None:
    registry = TEST_REGISTRY if test_server else PRODUCTION_REGISTRY
    sh.curl(
        "--silent",
        "--show-error",
        "--fail-with-body",
        "-H",
        "Content-Type: application/trig",
        "--data-binary",
        f"@{signed_path}",
        registry,
    )


def publish(
    path: str,
    test_server: bool = False,
    derived_from: str = "",
    dry_run: bool = False,
    output: str = "",
):
    """Build a nanopub from a Markdown-LD file (yaml-ld), sign, publish or write TriG."""
    dataset = _build_nanopub(path, derived_from=derived_from)

    if output and output.strip():
        out_path = Path(output).expanduser().resolve()
        signed_path, source_uri = _sign_with_rust_cli(dataset)
        try:
            shutil.copyfile(signed_path, out_path)
        finally:
            signed_path.unlink(missing_ok=True)
        print(source_uri)
        print(f"Wrote {out_path}")
        return

    if dry_run:
        print(dataset.serialize(format="trig"))
        return

    signed_path, source_uri = _sign_with_rust_cli(dataset)
    out_path = _default_signed_output_path(path)
    try:
        shutil.copyfile(signed_path, out_path)
        _publish_signed_file(signed_path, test_server=test_server)
    finally:
        signed_path.unlink(missing_ok=True)
    print(source_uri)
    print(f"Wrote {out_path}")


def check(path: str):
    """Validate a signed nanopublication TriG using the Rust nanopub CLI."""
    output = str(sh.nanopub("check", str(Path(path).expanduser().resolve()))).strip()
    if output:
        print(output)
