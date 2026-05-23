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
- validate the result independently

This skill is **not** for creating a standalone `.ttl` file from scratch.

## Required resources

Always load these bundled resources before semantifying:

- [rules.md](rules.md) — mandatory modeling, YAML-LD, entity-resolution, and validation rules.
- [writer-prompt.md](writer-prompt.md) — instructions for the role that edits the Markdown file.
- [validator-prompt.md](validator-prompt.md) — instructions for the read-only validation role.

## Mandatory two-role workflow

Every semantification must use two separate roles:

1. **Writer** — reads the target file and `rules.md`, resolves entities, edits the Markdown file in place, and runs `pyld expand <file>` before handoff.
2. **Validator** — reads the target file and `rules.md`, does not edit files, runs `pyld expand <file>` and `iolanta <file> --as kglint/json`, inspects Iolanta `assertions` and `labels`, and reports rule findings.

When the runtime permits subagents, run the writer and validator as separate agents using the bundled prompt files. The writer owns edits to the target Markdown file. The validator owns no files and must remain read-only.

If the runtime does not permit subagents, do **not** silently fall back to an ordinary single-role semantification. Stop and tell the user that this skill requires the writer/validator workflow and needs subagent authorization or a runtime that supports it.

## Workflow

1. **Orient**
   - Inspect the current frontmatter and body.
   - If linked-data frontmatter already exists, treat the task as a revision, not a rewrite.
   - Load `rules.md`, `writer-prompt.md`, and `validator-prompt.md`.

2. **Writer pass**
   - Follow `writer-prompt.md`.
   - Preserve the document body unless the user asked to revise prose too.
   - Keep the graph close to what the prose actually claims. Do not over-formalize weak implications.
   - Verify every external RDF term introduced by the semantification before using it. This applies to all external classes, properties, individuals, ontology terms, vocabulary terms, and URL identifiers.
   - Use `find-url-for` or direct dereference against an authoritative linked-data source for external term verification. Do not invent, guess, or pattern-construct CURIEs or URLs.
   - If an external term cannot be verified, do not use it. Mint a document-scoped local term only when the notion is genuinely document-specific; otherwise stop and ask the user which verified term to use.
   - Run `pyld expand <file>` before handoff.

3. **Validator pass**
   - Follow `validator-prompt.md`.
   - Run both validation commands:
     ```bash
     pyld expand path/to/file.md
     iolanta path/to/file.md --as kglint/json
     ```
   - Read the full Iolanta JSON output, not just `assertions`.
   - Remember that Iolanta loads the containing directory, so sibling RDF content may affect validation results.

4. **Fix pass**
   - If the validator reports blockers, the writer fixes them.
   - Re-run the validator once after fixes.
   - If blockers remain after the second validator pass, summarize them and ask the user how to proceed.

## Validation setup and failure handling

The `pyld` CLI used by this skill comes from `yaml-ld`; `PyLD` is the Python library, not the CLI command this skill uses. `iolanta` is installed from the separate `iolanta` package and should install `pyld` transitively through `yaml-ld`.

If a command is missing or unavailable, report the setup issue clearly. Recommended install commands:

```bash
python3 -m pip install --user iolanta
```

If the user is working inside an active virtualenv, recommend installing there instead:

```bash
python3 -m pip install iolanta
```

Distinguish failure modes explicitly:

- `command not found` — tool is not installed or not on `PATH`.
- installed but not on `PATH` — command may be in a Python user or virtual environment that the current shell is not using.
- cache/state directory not writable — environment or sandbox problem.
- network or context-resolution failure — environment or sandbox problem.
- long-running `iolanta` — use a long timeout; no output yet is not by itself an error.

If `pyld expand` succeeds and `iolanta` fails, report whether the failure looks like PATH/setup, cache/state, network, timeout, or Iolanta-specific graph rendering.

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

Do not add local labels to external URIs merely to satisfy Iolanta. First verify that the URI exists and exposes valid Linked Data for the intended term. Local labels are allowed only for verified external URIs that render poorly.

## Notes

- Prefer incremental edits over replacing a whole frontmatter block unless the existing one is clearly unsalvageable.
- This skill intentionally covers Markdown frontmatter workflows only. It does not replace standalone `.ttl` creation.
