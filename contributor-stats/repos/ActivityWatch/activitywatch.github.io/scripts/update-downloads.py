from datetime import datetime, timezone, timedelta
from pathlib import Path
import re
import requests


def is_older(dt: str, td: timedelta):
    now = datetime.now(tz=timezone.utc)
    created_at = datetime.fromisoformat(dt.strip("Z")).replace(tzinfo=timezone.utc)
    return created_at < now - td


if __name__ == "__main__":
    r = requests.get(
        "https://api.github.com/repos/ActivityWatch/activitywatch/releases"
    )
    data = r.json()

    # Filter away prereleases
    data = filter(lambda r: not r["prerelease"] and not r["draft"], data)

    # Filter away very recent releases (<1h old)
    data = filter(lambda r: is_older(r["created_at"], timedelta(hours=1)), data)

    data = sorted(data, key=lambda r: r["created_at"])
    latest_release = data[-1]["tag_name"]
    print(f"Latest release: {latest_release}")

    p = Path("_data/downloads.yml")

    with open(p, "r") as f:
        orig = f.read()
        new = re.sub(r"v[0-9.]+", latest_release, orig)

    if new == orig:
        print("No change")
    else:
        with open(p, "w") as f:
            f.write(new)
        print(f"Wrote to {p}")
