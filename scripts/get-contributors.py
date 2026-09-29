import re
from pathlib import Path

script_dir = Path(__file__).parent
root_dir = script_dir.parent

# regexp for github profile urls
github_profile_re = re.compile(r"https://github.com/([^/\"]+)")

search_file = root_dir / "_includes" / "tables" / "github-stats.html"

usernames = []
with search_file.open() as f:
    for line in f:
        match = github_profile_re.search(line)
        if match:
            usernames.append(match.group(1))
            print(match.group(1))

print(f"Found {len(usernames)} usernames")

contributors_file = root_dir / "_data" / "contributors.yml"
with contributors_file.open("w") as f:
    for username in usernames:
        f.write(f"- {username}\n")
print(f"Updated {contributors_file}")
