---
name: validate-rdf-iolanta
description: Validates RDF using Iolanta kglint on Turtle/RDF files or Markdown with YAML-LD frontmatter. Requires a file path. Runs iolanta with --as kglint/json, interprets assertions and labels, and addresses issues (e.g. uri-label-identical). Use when the user asks to validate RDF, TTL, YAML-LD in Markdown, check ontology or data, or run iolanta.
---

# Validate RDF with Iolanta (kglint)

## Argument: file path

The file path to validate is provided by the user. Determine it in this order:
1. **Explicit path** in the user's message (e.g. "validate another-order.ttl", "validate publications/foo/index.md")
2. **@-mentioned file** (e.g. user attaches or references a file with @)
3. **Currently focused or open file** in the editor
4. **Ask** if none of the above applies

Supported inputs include **`.ttl` / RDF** and **`.md` (or `.markdown`) whose RDF is in YAML-LD in the frontmatter** (JSON-LD 1.1 serialized as YAML).

## How validation works

Iolanta loads the **whole directory** in which the requested file is located (not just that file). Everything in that directory that Iolanta treats as RDF-related data for that run is in scope—so **auxiliary `.ttl` or other RDF in the same folder** affects the result. Prefer keeping each publication in its own directory or only co-locating files you intend to load together.

Validation uses the **kglint** facet, which emits **one JSON report** (today with top-level **`assertions`** and **`labels`**). Future versions may add fields or change shape—**the rule is unchanged: consume the whole thing.**

## Command

```bash
iolanta <file> --as kglint/json
```

Examples:
- `iolanta another-order.ttl --as kglint/json`
- `iolanta publications/types-of-ssds/index.md --as kglint/json`

**Mandatory: read every word kglint prints (stdout).** Nothing in the instructions tells you to look at **`assertions` alone**—that would be a mistake.

1. Capture the **complete** kglint JSON on **stdout** (no `jq`, no piping to extract one key, no stopping after the first screen).
2. Read it **from the first character to the last**—every top-level key, every array element, every nested object, every string, every `labels` entry, every `triples` block, every `node` / `s` / `p` / `o`, and the full **`assertions`** list (even when it is empty: confirm it is `[]`, not missing).
3. **Only after** you have taken in the **entire** report do you summarize what kglint said for the user. **Do not** equate “validation” with “`assertions` is empty” without having read **`labels`** and everything else in the same payload.

**What the sections mean (after you have read them in full):**

- **`assertions`** — Lint findings. Empty `[]` means no findings **in that array**; it does not replace reading **`labels`** or any other part of the report.
- **`labels`** — How Iolanta **labels** nodes and **which triples** it associates with them—the primary place to see whether the **materialized graph** matches intent.

You may redirect **stderr** (e.g. `2>/dev/null`) to hide PyLD noise, but **stdout must be the complete single JSON object.** If stdout is not valid JSON (e.g. permission errors from Iolanta trying to write `~/.local/state/iolanta/`), fix the environment and re-run—do not assume validation from a partial pipe.

**Timeout:** Iolanta loads the directory and may pull remote content (e.g. Wikidata, schema.org). Use the **maximum timeout** the tooling supports when running this command (e.g. 600000 ms / 10 minutes) so validation can complete. Do not conclude the document is valid without successfully running Iolanta and checking the report.

**Agent / non-interactive shells:** If `iolanta` is not on `PATH`, prefix with pyenv shims, e.g. `PATH="$HOME/.pyenv/shims:$PATH" iolanta …` (or rely on `pyenv local` in the project and a shell that loads pyenv).

## Kglint output schema

The output is a JSON object (currently with at least these top-level keys—**read whatever is actually present in full**):

- **`assertions`** — Array of lint findings. **Empty `[]` means no entries in this array**, not “stop reading.” Each assertion has:
  - `severity`: `"error"` or `"warning"`
  - `code`: assertion code (see below)
  - `target`: the node or triple the finding refers to (URI/blank node object, or full triple)
  - `message`: human-readable explanation

- **`labels`** — Array of label entries (one per URI/blank node): `node` (type, value, **computed label**) and **`triples`** (how that node connects in the graph). **Essential for validation:** confirms what Iolanta actually materialized and how IRIs read to humans. Lint can be clean while the graph is still wrong—`labels` is the sanity check.

**Assertion codes and how to fix:**

| Code | Meaning | Fix |
|------|---------|-----|
| `uri-label-identical` | URI has no usable label; rendered label equals the URI. | Add `rdfs:label` or `schema:name` (with language tag where appropriate) **in the same graph** for that resource, or ensure the URI is dereferenceable so Iolanta can load a label. For **ontology-only** fixes, add the label in the ontology TTL if the URI is a class/property defined there. |
| `uri-label-identical` (referenced documents) | **Object** of `dct:references`, `schema:url`, etc. is a bare `https://…` document IRI with no label in the loaded graph. | Add a **second node** in `@included` (YAML-LD) with the **same `@id`** as that URL and a `schema:name` / `rdfs:label`, so the referenced resource carries a human-readable label. |
| `blank-label-identical` | Blank node has no usable label. | Add or fix label for that blank node in the data/ontology. |
| `literal-looks-like-uri` | Literal value looks like a URL. | Consider using a URI reference instead of a literal. |
| `literal-looks-like-qname` | Literal value looks like a QName (e.g. `ex:foo`). | Consider using a URI reference instead of a literal. |

## Workflow

1. Determine the file to validate (see "Argument: file path" above).
2. Run `iolanta <file> --as kglint/json` using the file path from step 1, with **maximum timeout** (e.g. 600000 ms) so remote loading can complete.
3. Read the **entire** stdout **line by line and structure by structure** until the JSON ends. Do not prioritize **`assertions`** over **`labels`** or skim either. If anything in **`assertions`** is non-empty, there are lint issues to fix (use `code`, `target`, `message`).
4. For each assertion, use `code`, `target`, and `message` to fix (see table above).
5. Re-run `iolanta <file> --as kglint/json` and repeat until you have again read the **full** new report, **`assertions`** is `[]`, and **`labels`** (and the rest of the JSON) matches the intended graph.

## Example invocation

**User:** "validate another-order.ttl"  
**Agent:** Determines file path → runs `iolanta … --as kglint/json` → reads **the complete JSON output, every key and nested value** → reports what **`labels`** and **`assertions`** (and anything else present) show → fixes issues → re-runs and again reads the **full** output.

**User:** "validate the SSD publication" (with `publications/types-of-ssds/index.md` open)  
**Agent:** Same: **full** kglint stdout, end to end, before concluding.

## Notes

- A PyLD `SyntaxWarning` about `@` is from the dependency, not your TTL; safe to ignore.
- Use absolute or correct relative path for `<file>` so the intended directory (and thus sibling RDF) is loaded.
- **Scope:** kglint validates **RDF-shaped content** Iolanta extracts (including YAML-LD in Markdown). It does **not** by itself prove **nanopublication** well-formedness (TriG head / assertion / provenance / publication-info graphs); use a nanopub validator or pipeline when you generate full nanopubs.
