"""MkDocs hooks for nanopublishing docs."""

from __future__ import annotations

import re
from pathlib import Path


FRONTMATTER_PATTERN = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)
TRUSTY_URI_PATTERN = re.compile(r"^@prefix this:\s*<([^>]+)>\s*\.\s*$", re.MULTILINE)
FIRST_HEADER_PATTERN = re.compile(r"^(# .+)$", re.MULTILINE)


def _extract_frontmatter(path: Path) -> str | None:
    source = path.read_text(encoding="utf-8")
    match = FRONTMATTER_PATTERN.match(source)
    if not match:
        return None

    return match.group(1).rstrip()


def _extract_trusty_uri(path: Path) -> str | None:
    source = path.read_text(encoding="utf-8")
    match = TRUSTY_URI_PATTERN.search(source)
    if not match:
        return None

    return match.group(1)


def on_page_markdown(markdown: str, page, config, files) -> str:  # noqa: ANN001
    """Insert the exact authored YAML frontmatter before example page content."""
    if not page.file.src_uri.startswith("examples/"):
        return markdown

    if not page.file.abs_src_path:
        return markdown

    signed_path = Path(page.file.abs_src_path).with_name("signed.index.trig")
    if signed_path.is_file():
        trusty_uri = _extract_trusty_uri(signed_path)
        if trusty_uri:
            page.meta["nanopub_trusty_url"] = trusty_uri
            page.meta["nanopub_download_url"] = "signed.index.trig"

    frontmatter = _extract_frontmatter(Path(page.file.abs_src_path))
    if not frontmatter:
        return markdown

    details_block = (
        '<details markdown="1">\n'
        "<summary>Assertion</summary>\n\n"
        f"```yaml\n{frontmatter}\n```\n"
        "</details>\n\n"
    )

    match = FIRST_HEADER_PATTERN.search(markdown)
    if not match:
        return f"{details_block}{markdown}"

    insert_at = match.end()
    return f"{markdown[:insert_at]}\n\n{details_block}{markdown[insert_at:].lstrip()}"
