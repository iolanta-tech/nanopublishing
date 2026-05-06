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
- `R07` By default, assume the Markdown may later become a nanopublication. When minting local resources for such a file, do not use bare fragment IRIs like `#Thing`. Bind a prefix such as `this:` to `http://purl.org/nanopub/temp/np/` and mint the resource under that namespace instead, for example `this:Thing`.
- `R08` If you mint a local resource, give it a human-readable label or name in the same graph.
- `R08a` Mint identifiers only for nodes that need to be referred to from another part of the document or graph. Prefer blank nodes for inline supporting nodes that are described once and never referenced elsewhere.
- `R09` If you reference another document by URL or relative document IRI and Iolanta needs a label for it, add a second node with the same `$id` or `"@id"` and a `schema:name` or `rdfs:label`.
- `R10` Prefer simple predicates that are likely to render well in the current toolchain. Avoid ontology-heavy shapes unless they materially improve the graph.
- `R11` Local IRIs must be usable in validation. If a minted URI is not dereferenceable, give it a local `rdfs:label` or `schema:name` in the same graph.
- `R12` If you use document-local fragments, they must be coherent with the document IRI. Do not use arbitrary fragment identifiers without a stable document context.
- `R13` If you use a full URL for a referenced resource and it appears in object position, add a labeled node for that same `$id` or `"@id"` when Iolanta needs a human-readable label.
- `R14` Be cautious with Wikidata predicates and other external predicates that may render poorly in Iolanta. Prefer clearer public predicates when available; otherwise expect that rendering may be worse than syntactic validity.

## Entity Resolution

- For people, places, organizations, works, concepts, standards, products, technologies, reusable classes, and reusable properties, use the `find-url-for` skill when a stable linked-data URI is needed.
- Before minting a local URI for any reusable concept, class, property, standard, product, or technology, try `find-url-for` and prefer an established linked-data URI when one fits.
- Prefer existing URIs over minting local ones.
- Only mint local IRIs for concepts that are specific to the document and have no suitable external URI.

## Modeling Focus

- Formalize the knowledge asserted by the prose, not the Markdown file as a publication artifact.
- Only model the Markdown document itself as `schema:CreativeWork`, `schema:TechArticle`, or similar when the user explicitly wants bibliographic metadata or the document really is the subject.
- Keep the graph close to what the prose actually claims.
- Do not over-formalize weak implications.
