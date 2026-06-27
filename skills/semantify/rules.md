# Semantify Rules

These rules are mandatory for both the writer and validator roles.

- `R00` Quote JSON-LD keyword keys in YAML where they must remain `@`-keywords, especially `"@context"` and any JSON-LD keyword definitions inside the context.
- `R01` In the graph body, prefer the dollar-convenience context `https://json-ld.org/contexts/dollar-convenience.jsonld` so you can use `$included`, `$id`, and `$type` instead of quoted `"@included"`, `"@id"`, and `"@type"`. Keep `"@context"` itself quoted, and do not use `$`-keywords inside local context definitions.
- `R02` Do not quote ordinary YAML scalar values unless quoting is needed to avoid ambiguity. In particular, prefer unquoted language tags, URLs, CURIEs, and simple strings such as `en`, `https://schema.org/`, `wd:Q188639`, or `Types of SSDs`.
- `R03` Prefer concise contexts. Add only prefixes you actually use.
- `R04` Default to modeling the subject domain, concept, class, scheme, or entities described by the prose, not the Markdown file as an article about them.
- `R05` When a property is already typed as `@id` by the context, prefer a bare IRI/CURIE scalar for simple values. Use `$id` only when that node also needs its own attached properties.
- `R05a` Prefer inline node objects over separate flat top-level nodes when the node is first introduced through a relationship and needs description there. Inline is better than flat by default for hand-maintained YAML-LD. Use separate top-level nodes only when that improves reuse, readability, or validation.
- `R05b` Avoid redundant inverse-ish edges when one direction already expresses the relationship clearly. Add both directions only when they materially improve querying, rendering, or interoperability.
- `R05c` When the RDF predicate direction points away from the node where the YAML would be clearest, prefer JSON-LD `$reverse` over inventing inverse predicates or flattening the related nodes. Verify that expansion still emits the intended forward triples.
- `R06` Do not add `rdfs:label` or `schema:name` to external Wikidata, DBpedia, VIAF, or similar entity URIs unless there is a concrete validation reason to carry a local label.
- `R07` By default, assume the Markdown may later become a nanopublication. When minting local resources for such a file, do not use bare fragment IRIs like `#Thing`. Bind a prefix such as `this:` to `http://purl.org/nanopub/temp/np/` and mint the resource under that namespace instead, for example `this:Thing`. If the user or document context says the file is not a nanopublication, do not introduce `this:`; use coherent document-local identifiers instead.
- `R08` If you mint a local resource, give it a human-readable label or name in the same graph.
- `R08a` Mint identifiers only for nodes that need to be referred to from another part of the document or graph. Prefer blank nodes for inline supporting nodes that are described once and never referenced elsewhere.
- `R09` If you reference another document by URL or relative document IRI and Iolanta needs a label for it, add a second node with the same `$id` or `"@id"` and a `schema:name` or `rdfs:label`.
- `R10` After predicate resolution (`R15`), among verified external candidates that fit the intended relation, prefer simpler predicates likely to render well in the current toolchain. This does **not** authorize minting local predicates for Mermaid/Iolanta label convenience.
- `R11` Local IRIs must be usable in validation. If a minted URI is not dereferenceable, give it a local `rdfs:label` or `schema:name` in the same graph.
- `R12` If you use document-local fragments, they must be coherent with the document IRI. Do not use arbitrary fragment identifiers without a stable document context.
- `R13` If you use a full URL for a referenced resource and it appears in object position, add a labeled node for that same `$id` or `"@id"` when Iolanta needs a human-readable label.
- `R14` When a verified external predicate fits the intended relation but renders poorly in Iolanta, reuse it anyway unless a different verified external predicate fits better. Poor rendering is a non-blocker, not grounds to mint a local property.
- `R15` Before minting a document-local **property** IRI:
  - identify **2–3 verified external candidates**, or document why the relation is not addressable by public vocabularies at all;
  - mint only when the relation is genuinely document-specific and no suitable external URI exists after edge-resolution search;
  - minting solely for Mermaid/Iolanta edge labels is insufficient (`R10`, `R14`);
  - reusing an external predicate with semantic stretch requires a one-line stretch note in the writer handoff **Predicate choices** section.
  - Example — theory-internal dependency *"phenomenon depends on principle"*:
    ```
    Considered: dcterms:requires (domain too bibliographic);
                RO:0002502 (causally upstream of — direction/stretch mismatch).
    Reusing: schema:dependsOn — close enough; stretch: theory-internal, not software.
    ---
    Considered: dcterms:relation, prov:wasDerivedFrom, skos:broader — none fit epistemic dependency.
    Minting: doc:isPredicatedOn — document-specific epistemic relation; no public URI after LOV + RO + schema.org search.
    ```

## Entity Resolution

Distinguish **node resolution** (entities) from **edge resolution** (predicates).

### Node resolution

- For people, places, organizations, works, concepts, standards, products, technologies, and reusable classes, use the `find-url-for` skill when a stable linked-data URI is needed.
- Before minting a local URI for any reusable concept, class, standard, product, or technology, try `find-url-for` and prefer an established linked-data URI when one fits.

### Edge resolution

- For properties and relations between nodes, use `find-url-for` with LOV term search when the notion is a relation (see `find-url-for` skill).
- `find-url-for` may return no relation hits — still search before minting: schema.org index (`pyld get http://schema.org`), RO (`http://purl.obolibrary.org/obo/RO_*`), `dcterms:`, `prov:`, and dereference candidates from known ontologies.
- For schema.org classes and properties, do not guess from labels or URL patterns. `pyld get http://schema.org` may be used as the authoritative compact schema.org term index; a schema.org term is verified only when the exact local name appears in the returned context and maps to the intended `schema:<Term>` IRI. Use `pyld get http://schema.org/<Term>` when richer linked-data evidence for the specific term is needed.
- Follow `R15` before minting any document-local property IRI.

### General

- Prefer existing URIs over minting local ones.
- Only mint local IRIs for concepts that are specific to the document and have no suitable external URI.

## Modeling Focus

- Formalize the knowledge asserted by the prose, not the Markdown file as a publication artifact.
- Only model the Markdown document itself as `schema:CreativeWork`, `schema:TechArticle`, or similar when the user explicitly wants bibliographic metadata or the document really is the subject.
- Keep the graph close to what the prose actually claims.
- Do not over-formalize weak implications.
