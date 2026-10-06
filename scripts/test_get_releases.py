#!/usr/bin/env python3
"""Unit tests for get-releases.py release filtering."""

import importlib.util
import unittest
from pathlib import Path

_SCRIPT = Path(__file__).resolve().parent / "get-releases.py"
_spec = importlib.util.spec_from_file_location("get_releases", _SCRIPT)
gr = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(gr)


def _release(tag: str, created: str, name=None, draft=False) -> dict:
    return {
        "name": tag if name is None else name,
        "tag_name": tag,
        "created_at": created,
        "html_url": f"https://example.test/{tag}",
        "draft": draft,
    }


class FormatReleasesTest(unittest.TestCase):
    def test_keeps_stable_and_beta_releases(self):
        out = gr.format_releases(
            [
                _release("v0.14.0", "2026-10-06T00:00:00Z"),
                _release("v0.14.0b8", "2026-09-18T00:00:00Z"),
                _release("v0.13.2", "2024-10-05T00:00:00Z"),
            ]
        )
        self.assertEqual([r["tag"] for r in out], ["v0.14.0", "v0.14.0b8", "v0.13.2"])

    def test_skips_drafts_nightlies_and_research_builds(self):
        out = gr.format_releases(
            [
                _release("v0.14.0b9", "2026-10-06T00:00:00Z", draft=True),
                _release("v0.14.0dev20260723", "2026-07-23T00:00:00Z"),
                _release("v0.14.0dev202607121", "2026-07-12T00:00:00Z"),
                _release("v0.14.0b5-research", "2026-09-09T00:00:00Z"),
                _release("v0.14.0b5", "2026-09-07T00:00:00Z"),
            ]
        )
        self.assertEqual([r["tag"] for r in out], ["v0.14.0b5"])

    def test_sorted_newest_first(self):
        out = gr.format_releases(
            [
                _release("v0.12.0", "2023-09-26T00:00:00Z"),
                _release("v0.14.2", "2026-09-22T00:00:00Z"),
            ]
        )
        self.assertEqual([r["tag"] for r in out], ["v0.14.2", "v0.12.0"])

    def test_empty_name_falls_back_to_tag(self):
        out = gr.format_releases([_release("v0.4.12", "2019-08-13T00:00:00Z", name="")])
        self.assertEqual(out[0]["title"], "v0.4.12")
        self.assertEqual(
            set(out[0]), {"title", "tag", "date", "url"}
        )


if __name__ == "__main__":
    unittest.main()
