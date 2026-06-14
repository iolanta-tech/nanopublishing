# Project guidance

- `.claude/skills/` is a symlink to `../skills/`. Both paths resolve to the same inode, so an edit through one updates the other. Always edit skill files via the canonical `skills/<name>/SKILL.md` path; never `cp` between the two locations.
- Do not run `uv run` or `uv sync` at the repository root unless asked; it creates untracked `uv.lock` files the project does not commit.

## Subdirectory guidance

(none yet)
