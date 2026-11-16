#!/usr/bin/env python3
"""Fail if any <script type="application/ld+json"> block in the built site is invalid JSON.

Search engines silently drop structured data that does not parse, so a broken
block only shows up as a lost rich result. Run after `make build`:

    python3 scripts/check_jsonld.py _site
"""

import json
import re
import sys
from pathlib import Path

LDJSON = re.compile(
    r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.S | re.I,
)


def check_html(html: str) -> list[str]:
    """Return one error message per ld+json block that fails to parse."""
    errors = []
    for i, block in enumerate(LDJSON.findall(html)):
        try:
            json.loads(block)
        except json.JSONDecodeError as e:
            errors.append(f"block {i}: {e}")
    return errors


def main(site: Path) -> int:
    pages = sorted(site.rglob("*.html"))
    if not pages:
        print(f"No HTML files under {site}", file=sys.stderr)
        return 1
    failed = blocks = 0
    for page in pages:
        html = page.read_text(encoding="utf-8", errors="replace")
        blocks += len(LDJSON.findall(html))
        for err in check_html(html):
            failed += 1
            print(f"{page}: {err}", file=sys.stderr)
    print(f"Checked {blocks} JSON-LD blocks in {len(pages)} pages: {failed} invalid")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1] if len(sys.argv) > 1 else "_site")))
