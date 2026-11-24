#!/usr/bin/env python3
"""
Regenerate _data/releases.yml (desktop) and _data/releases_android.yml from
GitHub releases, for the /timeline/ page. The Pages build runs it through
`make update-downloads`, so new releases appear on the next deploy.

Skips drafts, dev/nightly builds and Research Edition builds. Set GITHUB_TOKEN
to avoid the unauthenticated rate limit.
"""

import os
import re
import sys
from pathlib import Path

import requests
import yaml

owner = "ActivityWatch"

# Not shown on the timeline: nightlies (v0.14.0dev20260723) and the separate
# Research Edition (v0.14.0b5-research).
SKIP_TAG = re.compile(r"dev\d|-research")


def fetch_all_releases(owner, repo):
    headers = {}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    page = 1
    all_releases = []

    while True:
        url = f"https://api.github.com/repos/{owner}/{repo}/releases?page={page}&per_page=100"
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        releases = response.json()
        if not releases:
            break

        all_releases.extend(releases)
        page += 1

    return all_releases


def format_releases(releases):
    # NOTE: we want to get the commit date "created_at", not the tag date "published_at"
    #       in particular for oopsied: https://github.com/ActivityWatch/activitywatch/releases/tag/v0.10.0
    return [
        {
            "title": release["name"] or release["tag_name"],
            "tag": release["tag_name"],
            "date": release["created_at"],
            "url": release["html_url"],
        }
        for release in sorted(releases, key=lambda r: r["created_at"], reverse=True)
        if not release["draft"] and not SKIP_TAG.search(release["tag_name"])
    ]


def main():
    data_folder = Path(__file__).parent.parent / "_data"
    cache_folder = data_folder.parent / ".timeline-cache"
    for repo, filename in [
        ("activitywatch", "releases.yml"),
        ("aw-android", "releases_android.yml"),
    ]:
        output = data_folder / filename
        cached = cache_folder / filename
        try:
            formatted_releases = format_releases(fetch_all_releases(owner, repo))
        except requests.RequestException as exc:
            if cached.exists():
                published = yaml.safe_load(cached.read_text()) or []
                committed = yaml.safe_load(output.read_text()) or []
                by_tag = {release["tag"]: release for release in published}
                by_tag.update({release["tag"]: release for release in committed})
                combined = sorted(
                    by_tag.values(), key=lambda r: r["date"], reverse=True
                )
                output.write_text(yaml.safe_dump(combined, sort_keys=False))
            print(
                f"WARNING: keeping existing {filename}; release refresh failed: {exc}",
                file=sys.stderr,
            )
        else:
            with open(output, "w") as f:
                yaml.dump(formatted_releases, f, sort_keys=False)
            print(f"Saved {len(formatted_releases)} {repo} releases to {filename}")
        cache_folder.mkdir(exist_ok=True)
        cached.write_bytes(output.read_bytes())


if __name__ == "__main__":
    main()
