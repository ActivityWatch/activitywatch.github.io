#!/usr/bin/env python3
"""Unit tests for update-downloads.py macOS architecture picking."""

import importlib.util
import unittest
from pathlib import Path

_SCRIPT = Path(__file__).resolve().parent / "update-downloads.py"
_spec = importlib.util.spec_from_file_location("update_downloads", _SCRIPT)
ud = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(ud)


def _asset(name: str) -> dict:
    return {
        "name": name,
        "browser_download_url": f"https://example.test/{name}",
    }


B5_ASSETS = [
    _asset("activitywatch-tauri-v0.14.0b5-macos-arm64.dmg"),
    _asset("activitywatch-tauri-v0.14.0b5-macos-arm64.zip"),
    _asset("activitywatch-tauri-v0.14.0b5-macos-x86_64.dmg"),
    _asset("activitywatch-tauri-v0.14.0b5-macos-x86_64.zip"),
    _asset("activitywatch-v0.14.0b5-macos-arm64.dmg"),
    _asset("activitywatch-v0.14.0b5-macos-arm64.zip"),
    _asset("activitywatch-v0.14.0b5-macos-x86_64.dmg"),
    _asset("activitywatch-v0.14.0b5-macos-x86_64.zip"),
    _asset("activitywatch-v0.14.0b5-windows-x86_64-setup.exe"),
    _asset("activitywatch-v0.14.0b5-windows-x86_64.zip"),
    _asset("activitywatch-v0.14.0b5-linux-x86_64.zip"),
    _asset("activitywatch-linux-x86_64.AppImage"),
    _asset("activitywatch-v0.14.0b5-linux-x86_64.deb"),
]

STABLE_INTEL_ONLY = [
    _asset("activitywatch-v0.13.2-macos-x86_64.dmg"),
    _asset("activitywatch-v0.13.2-macos-x86_64.zip"),
    _asset("activitywatch-v0.13.2-windows-x86_64-setup.exe"),
    _asset("activitywatch-v0.13.2-windows-x86_64.zip"),
    _asset("activitywatch-v0.13.2-linux-x86_64.zip"),
]


class PickPerArchTests(unittest.TestCase):
    def test_b5_lists_both_macos_arches_and_prefers_non_tauri(self):
        dmgs = ud._pick_per_arch(B5_ASSETS, r"macos.*\.dmg$")
        names = [a["name"] for a in dmgs]
        self.assertEqual(
            names,
            [
                "activitywatch-v0.14.0b5-macos-arm64.dmg",
                "activitywatch-v0.14.0b5-macos-x86_64.dmg",
            ],
        )

    def test_single_arch_release_still_lists_the_one_dmg(self):
        dmgs = ud._pick_per_arch(STABLE_INTEL_ONLY, r"macos.*\.dmg$")
        self.assertEqual(
            [a["name"] for a in dmgs],
            ["activitywatch-v0.13.2-macos-x86_64.dmg"],
        )

    def test_legacy_pick_drops_intel_on_dual_arch_release(self):
        # Guard the bug: a single _pick on macos*.dmg kept only arm64 because
        # that filename is shorter than the x86_64 sibling.
        picked = ud._pick(B5_ASSETS, r"macos.*\.dmg$")
        self.assertEqual(picked["name"], "activitywatch-v0.14.0b5-macos-arm64.dmg")

    def test_platforms_for_b5_exposes_intel_and_apple_silicon(self):
        platforms = ud.platforms_for(
            {"tag_name": "v0.14.0b5", "assets": B5_ASSETS},
            include_packages=False,
        )
        macos = next(p for p in platforms if p["name"] == "macOS")
        descs = [a.get("description", "") for a in macos["assets"]]
        self.assertTrue(any("Apple Silicon" in d for d in descs))
        self.assertTrue(any("Intel" in d for d in descs))
        titles = [a["title"] for a in macos["assets"]]
        self.assertEqual(titles.count(".dmg"), 2)
        self.assertEqual(titles.count(".zip"), 2)

    def test_platforms_for_stable_intel_only_unchanged(self):
        platforms = ud.platforms_for(
            {"tag_name": "v0.13.2", "assets": STABLE_INTEL_ONLY},
            include_packages=False,
        )
        macos = next(p for p in platforms if p["name"] == "macOS")
        self.assertEqual(
            [a["title"] + a.get("description", "") for a in macos["assets"]],
            [".dmg (recommended) (Intel)", ".zip (Intel)"],
        )


if __name__ == "__main__":
    unittest.main()
