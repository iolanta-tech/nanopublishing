---
name: nanopublish
description: Build, sign, check, and publish nanopublications from Markdown files whose RDF assertion is encoded as YAML-LD frontmatter.
---

# Nanopublish

Use this skill when the user wants to publish a nanopublication from a Markdown file.

## Input

The main argument is a Markdown file path. The YAML-LD frontmatter is parsed as one JSON-LD document, and `jeeves.py` derives the nanopub assertion, provenance, and publication-info graphs from that source structure.

```yaml
"@context":
  ...
$nanopublication:
  $assertion:
    ...
  prov:wasAttributedTo: ...
npx:describes: ...
```

Examples:
- `docs/examples/odyssey-2001/europa-is-a-satellite-of-jupiter/index.md`

## Commands

Run these commands from the skill directory:

```bash
cd /home/anatoly/projects/nanopublishing/skills/nanopublish
```

The `publish` command is provided by the local `j` project in this directory, not by the repository root `j` CLI.

- `j publish <markdown-file>`
  Builds an unsigned nanopub from the Markdown frontmatter sections, signs it, writes the signed TriG next to the source Markdown as `signed.<stem>.trig`, publishes it, and prints the final trusty URI.

- `j publish <markdown-file> --dry-run`
  Prints the unsigned nanopub in TriG.

- `j publish <markdown-file> --output <file.trig>`
  Signs the nanopub and writes the signed TriG to the given file without publishing.

- `j check <signed-file.trig>`
  Validates a signed nanopub via the Rust `nanopub` CLI.

## After Publishing

- Update `npx:supersedes` in the Markdown source to the trusty URI printed by `j publish`.
- Do not edit the signed `signed.<stem>.trig`; it is immutable once published.
- The updated `npx:supersedes` value is the input for the next publication in the version chain.

## Namespace Guidance

If the Markdown needs nanopub-local terms that should end up under the final trusty URI, mint them in the nanopub placeholder namespace:

- Use `http://purl.org/nanopub/temp/np/`
- Not `http://purl.org/nanopub/temp/`

Example:

```yaml
"@context":
  - npthis: http://purl.org/nanopub/temp/np/
$id: npthis:is-satellite-of
```

This lets signing rewrite the term into the nanopub-local URI space of the final signed nanopub.

## Implementation Notes

- `j publish ...` must be run from `skills/nanopublish/`, because that is the Python project that exposes the `publish` subcommand.
- A normal `j publish path/to/index.md` run keeps a local signed file at `path/to/signed.index.trig`.
- Unsigned nanopubs are assembled locally with `rdflib`.
- `jeeves.py` derives the nanopub graph split from the expanded YAML-LD source structure rather than expecting assertion-only frontmatter.
- Signing and checking are delegated to `nanopub` on `PATH`.
- The skill expects the user's nanopub profile at `~/.nanopub/profile.yml`.

## When To Update

Update this skill text if any of these change:
- the expected input format
- the publish, dry-run, or check commands
- the nanopub-local placeholder namespace convention
- the dependency on the Rust `nanopub` CLI
