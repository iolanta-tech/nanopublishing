---
name: semantify
description: Formalizes the contents of an existing Markdown file into linked-data frontmatter in the same file. Use when a user wants prose in a `.md` document turned into JSON-LD/YAML-LD frontmatter, with entity resolution, in-place editing, `pyld expand` validation for linked-data syntax, and Iolanta validation for graph rendering.
---

# Semantify Markdown

## Argument: Markdown file

The user should provide a Markdown file path. If they instead point at an open or attached Markdown file, use that. If the file is unclear, ask.

This skill is for **in-place formalization**:
- read the Markdown body
- extract the main entities and relationships
- write linked-data frontmatter into the **same file**

This skill is **not** for creating a standalone `.ttl` file from scratch.

## Workflow

1. **Read the file**
   - Inspect the current frontmatter and body.
   - If linked-data frontmatter already exists, treat the task as a revision, not a rewrite.

2. **Model the subject, not the markdown wrapper**
   - By default, formalize the domain the text is asserting about, not the Markdown file as a publication artifact.
   - Only model the Markdown document itself as `schema:CreativeWork`, `schema:TechArticle`, or similar when the user explicitly wants bibliographic metadata or the document really is the subject.
   - Prefer simple, robust vocabularies already used in the repo (`schema`, `rdfs`, `rdf`, `dct`, `skos`, `owl`) unless a stronger vocabulary is clearly needed.
   - Keep the graph close to what the prose actually claims. Do not over-formalize weak implications.

3. **Resolve entities**
   - For people, places, organizations, works, concepts, standards, products, or technologies, use the [find-url-for](../find-url-for/SKILL.md) skill when a stable linked-data URI is needed.
   - Prefer existing URIs over minting local ones.
   - Only mint local IRIs for concepts that are specific to the document and have no suitable external URI.

4. **Write frontmatter into the same file**
   - Use YAML frontmatter with JSON-LD keys such as `"@context"` and `"@included"`.
   - Preserve the document body unless the user asked to revise prose too.
   - Prefer `@included` over `@graph`.
   - Prefer a document-root node plus a small number of supporting nodes when needed.

5. **Validate in two stages**
   - First run `pyld expand <file>` to validate that the frontmatter is valid JSON-LD/YAML-LD.
   - Then run `iolanta <file> --as kglint/json` when graph linting or rendering validation matters.
   - Treat those as different checks:
     - `pyld expand` succeeding means the linked-data frontmatter is syntactically valid and expandable.
     - Iolanta failures such as `Facet not found` or label-resolution problems are Iolanta-specific and do not by themselves prove the YAML-LD is invalid.

## Rules

- `R00` Quote JSON-LD keyword keys in YAML where they must remain `@`-keywords, especially in `"@context"` and `"@included"`.
- `R01` In the document body, prefer the dollar-convenience context `https://json-ld.org/contexts/dollar-convenience.jsonld` so you can use `$id` and `$type` instead of quoted `"@id"` and `"@type"`. Do not try to use `$`-keywords inside `"@context"`.
- `R02` Do not quote ordinary YAML scalar values unless quoting is needed to avoid ambiguity. In particular, prefer unquoted language tags, URLs, CURIEs, and simple strings such as `en`, `https://schema.org/`, `wd:Q188639`, or `Types of SSDs`.
- `R03` Prefer concise contexts. Add only prefixes you actually use.
- `R04` Default to modeling the subject domain, concept, class, scheme, or entities described by the prose, not the Markdown file as an article about them.
- `R05` When a property is already typed as `@id` by the context, prefer a bare IRI/CURIE scalar for simple values. Use `$id` only when that node also needs its own attached properties.
- `R06` Do not add `rdfs:label` or `schema:name` to external Wikidata, DBpedia, VIAF, or similar entity URIs unless there is a concrete validation reason to carry a local label.
- `R07` By default, assume the Markdown may later become a nanopublication. When minting local resources for such a file, do not use bare fragment IRIs like `#Thing`. Bind a prefix such as `this:` to `http://purl.org/nanopub/temp/np/` and mint the resource under that namespace instead, for example `this:Thing`.
- `R08` If you mint a local resource, give it a human-readable label or name in the same graph.
- `R09` If you reference another document by URL or relative document IRI and Iolanta needs a label for it, add a second node with the same `@id` and a `schema:name` or `rdfs:label`.
- `R10` Prefer simple predicates that are likely to render well in the current toolchain. Avoid ontology-heavy shapes unless they materially improve the graph.
- `R11` Local IRIs must be usable in validation. If a minted URI is not dereferenceable, give it a local `rdfs:label` or `schema:name` in the same graph.
- `R12` If you use document-local fragments, they must be coherent with the document IRI. Do not use arbitrary fragment identifiers without a stable document context.
- `R13` If you use a full URL for a referenced resource and it appears in object position, add a labeled node for that same `@id` when Iolanta needs a human-readable label.
- `R14` Be cautious with Wikidata predicates and other external predicates that may render poorly in Iolanta. Prefer clearer public predicates when available; otherwise expect that rendering may be worse than syntactic validity.

## Validation commands

```bash
pyld expand path/to/file.md
```

Use this to confirm the frontmatter expands as JSON-LD.

```bash
iolanta path/to/file.md --as kglint/json
```

Use this to inspect how Iolanta materializes and labels the graph. Read the full output, not just `assertions`.

## Iolanta discipline

When running Iolanta:

1. Read the **entire** JSON output.
2. Do not look only at `assertions`; also inspect `labels`.
3. Remember that Iolanta loads the **whole directory**, not just the target file.
4. If stdout is not valid JSON, the validation did not succeed. Fix the environment and rerun.
5. Use the longest practical timeout because Iolanta may load remote content.

If `assertions` is non-empty:

- do **not** silently rewrite the graph until `assertions` becomes empty
- summarize the assertions for the user
- ask the user what to do with them:
  - fix them as real modeling problems
  - treat them as Iolanta-specific rendering quirks
  - ignore them for now
- only make assertion-driven edits after the user decides

## Notes

- A file can be valid linked-data frontmatter under `pyld expand` and still fail in Iolanta. Report that distinction clearly.
- Iolanta loads the containing directory, so sibling RDF content may affect validation results.
- Prefer incremental edits over replacing a whole frontmatter block unless the existing one is clearly unsalvageable.
- This skill intentionally covers Markdown frontmatter workflows only. It does not replace standalone `.ttl` creation.
