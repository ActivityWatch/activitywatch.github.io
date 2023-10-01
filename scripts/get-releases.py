#!/usr/bin/env python3
from pathlib import Path

import requests
import yaml

# Replace with your own repo's owner and name
owner = "ActivityWatch"
repo = "activitywatch"


def fetch_all_releases(owner, repo):
    page = 1
    all_releases = []

    while True:
        url = f"https://api.github.com/repos/{owner}/{repo}/releases?page={page}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to fetch data: {response.status_code}")
            break

        releases = response.json()
        if not releases:
            break

        all_releases.extend(releases)
        page += 1

    return all_releases


releases = fetch_all_releases(owner, repo)

# Create a list to store the formatted releases
formatted_releases = []

# NOTE: we want to get the commit date "created_at", not the tag date "published_at"
#       in particular for oopsied: https://github.com/ActivityWatch/activitywatch/releases/tag/v0.10.0

for release in sorted(releases, key=lambda r: r["created_at"], reverse=True):
    formatted_release = {
        "title": release["name"],
        "tag": release["tag_name"],
        "date": release["created_at"],
        "link": release["html_url"],
        "type": "release",
    }
    formatted_releases.append(formatted_release)

# Write to YAML file
project_root = Path(__file__).parent.parent
data_folder = project_root / "_data"
with open(data_folder / "releases.yml", "w") as f:
    yaml.dump(formatted_releases, f, sort_keys=False)

print(f"Successfully saved {len(formatted_releases)} releases to file")
