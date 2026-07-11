#!/usr/bin/env python3
"""Regenerate _data/downloads.yml from the ActivityWatch GitHub releases.

Writes the latest stable release, plus — when it is newer than that stable —
the latest pre-release, so betas/nightlies newer than stable are surfaced too.

Download links are built from each release's *actual* assets rather than by
substituting a version number into a fixed template, so it survives asset
naming changes between versions (e.g. the v0.14 `tauri` builds and macOS
moving from x86_64 to arm64).
"""

import os
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests
import yaml

API = "https://api.github.com/repos/ActivityWatch/activitywatch/releases"

# Static (non-GitHub) distribution links, appended per platform for the stable
# release only — package managers and the Play Store track stable, not betas.
PACKAGE_LINKS = {
    "Windows": [
        {"title": "Chocolatey", "url": "https://chocolatey.org/packages/activitywatch"},
    ],
    "Linux": [
        {"title": "AUR", "description": ", for Arch Linux and Manjaro",
         "url": "https://aur.archlinux.org/packages/activitywatch-bin/"},
        {"title": "nixpkgs", "description": ", for NixOS",
         "url": "https://search.nixos.org/packages?query=activitywatch&show=activitywatch"},
    ],
    "macOS": [
        {"title": "Homebrew", "url": "https://formulae.brew.sh/cask/activitywatch"},
    ],
}

# Android has no GitHub release assets; it's always just the Play Store link.
ANDROID = {
    "name": "Android",
    "assets": [
        {"title": "Play Store", "description": " (beta)",
         "url": "https://play.google.com/store/apps/details?id=net.activitywatch.android"},
    ],
}

# Per platform: (asset-name regex, button title, extra description).
# description may be a callable taking the matched asset.
PLATFORM_SPECS = {
    "Windows": [
        (r"windows.*setup\.exe$", "Installer", " (recommended)"),
        (r"windows.*\.zip$", ".zip", ""),
    ],
    "Linux": [
        (r"linux.*x86_64\.zip$", ".zip", ""),
        (r"\.AppImage$", ".AppImage", ""),
        (r"\.deb$", ".deb", ""),
    ],
    "macOS": [
        (r"macos.*\.dmg$", ".dmg", lambda a: " (recommended)" + _arch(a)),
        (r"macos.*\.zip$", ".zip", lambda a: _arch(a)),
    ],
}


def _arch(asset: dict) -> str:
    name = asset["name"].lower()
    if "arm64" in name or "aarch64" in name:
        return " (Apple Silicon)"
    if "x86_64" in name or "amd64" in name:
        return " (Intel)"
    return ""


def _pick(assets: list, pattern: str):
    """First asset matching pattern, preferring the plain (non-tauri) build."""
    cands = [a for a in assets if re.search(pattern, a["name"], re.I)]
    cands.sort(key=lambda a: ("tauri" in a["name"].lower(), len(a["name"])))
    return cands[0] if cands else None


def platforms_for(release: dict, include_packages: bool) -> list:
    assets = release["assets"]
    platforms = []
    for name, specs in PLATFORM_SPECS.items():
        entries = []
        for pattern, title, desc in specs:
            a = _pick(assets, pattern)
            if not a:
                continue
            entry = {"title": title, "url": a["browser_download_url"]}
            d = desc(a) if callable(desc) else desc
            if d:
                entry["description"] = d
            entries.append(entry)
        if include_packages:
            entries += PACKAGE_LINKS.get(name, [])
        if entries:
            platforms.append({"name": name, "assets": entries})
    return platforms


def build_block(release: dict, include_packages: bool, with_android: bool) -> dict:
    platforms = platforms_for(release, include_packages)
    if with_android:
        platforms.append(ANDROID)
    return {"version": release["tag_name"], "platforms": platforms}


def is_older(dt: str, td: timedelta) -> bool:
    created = datetime.fromisoformat(dt.replace("Z", "+00:00"))
    return created < datetime.now(tz=timezone.utc) - td


if __name__ == "__main__":
    headers = {"Accept": "application/vnd.github+json"}
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    releases = requests.get(API, headers=headers, timeout=30).json()

    # Ignore drafts and anything <1h old (assets may still be uploading).
    releases = [r for r in releases
                if not r["draft"] and is_older(r["created_at"], timedelta(hours=1))]
    releases.sort(key=lambda r: r["created_at"])

    stable = [r for r in releases if not r["prerelease"]]
    if not stable:
        raise SystemExit("No stable release found")
    latest_stable = stable[-1]

    data = {"stable": build_block(latest_stable, include_packages=True, with_android=True)}

    # Surface the latest pre-release only if it's newer than the latest stable.
    newer_pre = [r for r in releases
                 if r["prerelease"] and r["created_at"] > latest_stable["created_at"]]
    if newer_pre:
        latest_pre = newer_pre[-1]
        data["prerelease"] = build_block(latest_pre, include_packages=False, with_android=False)
        print(f"Stable: {latest_stable['tag_name']}; newer pre-release: {latest_pre['tag_name']}")
    else:
        print(f"Stable: {latest_stable['tag_name']} (no newer pre-release)")

    p = Path("_data/downloads.yml")
    header = "# Generated by scripts/update-downloads.py — do not edit by hand.\n"
    p.write_text(header + yaml.safe_dump(data, sort_keys=False, allow_unicode=True))
    print(f"Wrote {p}")
