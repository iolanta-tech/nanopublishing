import functools
from pathlib import Path
from typing import Any

from mkdocs_macros.plugin import MacrosPlugin
from rdflib import URIRef

from iolanta.conversions import path_to_iri
from iolanta.iolanta import Iolanta
from iolanta.namespaces import DATATYPES


def as_uri(uri: Any) -> URIRef:
    match uri:
        case Path() as path:
            return path_to_iri(path)
        case URIRef() as uriref:
            return uriref
        case str() as uri_string:
            return URIRef(uri_string)

    uri_type = type(uri)
    raise NotImplementedError(f"{uri} ({uri_type.__name__}) is unknown")


def resolve_datatype_uri(uri: str) -> URIRef:
    if uri.startswith("http://") or uri.startswith("https://"):
        return URIRef(uri)
    return DATATYPES[uri]


def _as_filter(iolanta_instance: Iolanta, uri: Any, datatype: str) -> str:
    return iolanta_instance.render(
        node=as_uri(uri),
        as_datatype=resolve_datatype_uri(datatype),
    )


def define_env(env: MacrosPlugin):
    iolanta = Iolanta(project_root=Path(__file__).parent / "docs")
    env.filters["as"] = functools.partial(_as_filter, iolanta)
    env.variables["docs"] = Path(__file__).parent / "docs"
