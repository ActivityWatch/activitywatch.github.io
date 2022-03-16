from __future__ import annotations

import os
import logging
import functools
import itertools
from pathlib import Path
from datetime import datetime, date
from collections import defaultdict
from typing import Callable, Any

import pandas as pd
from github import Github
from github.Repository import Repository
from joblib import Memory
from tqdm import tqdm

logger = logging.getLogger(__name__)

gh: Github

# FIXME: Use path relative to script, not working dir
memory = Memory("./.cache/github-stats")


def _is_bot(username):
    return "[bot]" in username


def _sort_dict_by_value(d: dict) -> dict:
    return {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}


@memory.cache
def _comments_by_user(repo_fullname: str, since: datetime) -> dict[str, int]:
    logger.info(" - Getting comments by user...")
    repo: Repository = gh.get_repo(repo_fullname)
    comments_by_user: dict[str, int] = defaultdict(int)
    for comment in repo.get_issues_comments(since=since):
        if _is_bot(comment.user.login):
            continue
        comments_by_user[comment.user.login] += 1
    return _sort_dict_by_value(comments_by_user)


@memory.cache
def _issues_by_user(repo_fullname: str, since: datetime) -> dict[str, int]:
    logger.info(" - Getting issues by user...")
    repo: Repository = gh.get_repo(repo_fullname)
    issues_by_user: dict[str, int] = defaultdict(int)
    for issue in repo.get_issues(state="all", since=since):
        # TODO: Don't count issues tagged as invalid
        if issue.created_at < since:
            continue
        issues_by_user[issue.user.login] += 1
    return _sort_dict_by_value(issues_by_user)


@memory.cache
def _pr_comments_by_user(repo_fullname: str, since: datetime) -> dict[str, int]:
    logger.info(" - Getting PR comments by user...")
    repo: Repository = gh.get_repo(repo_fullname)
    pr_comments_by_user: dict[str, int] = defaultdict(int)
    for pr_comment in repo.get_pulls_comments(since=since):
        pr_comments_by_user[pr_comment.user.login] += 1
    return _sort_dict_by_value(pr_comments_by_user)


@memory.cache
def _issues_stats(repo_fullname: str, since: datetime) -> dict[str, int]:
    # return the number of closed issues
    logger.info(" - Getting opened/closed issues...")
    repo: Repository = gh.get_repo(repo_fullname)
    opened = 0
    closed = 0
    for issue in repo.get_issues(state="all", since=since):
        if issue.created_at < since:
            opened += 1
        if issue.closed_at and issue.closed_at < since:
            closed += 1
    return {"opened": opened, "closed": closed}


@memory.cache
def _submitted_prs(repo_fullname: str, since: datetime):
    # returns the number of merged PRs
    logger.info(" - Getting submitted PRs...")
    repo: Repository = gh.get_repo(repo_fullname)
    count = 0
    for pr in repo.get_pulls(state="all", sort="created", direction="desc"):
        if pr.created_at < since:
            break
        count += 1
    return count


@memory.cache
def _merged_prs_by_user(repo_fullname: str, since: datetime) -> dict[str, int]:
    # returns the number of merged PRs per user
    logger.info(" - Getting merged PRs...")
    repo: Repository = gh.get_repo(repo_fullname)
    merged_prs_by_user: dict[str, int] = defaultdict(int)
    for pr in repo.get_pulls(state="closed", sort="updated", direction="desc"):
        if pr.updated_at < since:
            break
        if not pr.merged or pr.merged_at < since:
            continue
        merged_prs_by_user[pr.user.login] += 1
    return merged_prs_by_user


# "I" wrote this with Github Copilot, don't trust it...
@memory.cache
def _get_active_days_by_user(
    repo_fullname: str, since: datetime
) -> dict[str, set[date]]:
    # return a dict with the active dates per contributor
    logger.info(" - Getting active days by user...")
    repo: Repository = gh.get_repo(repo_fullname)
    active_days_by_user = defaultdict(set)
    for issue in repo.get_issues(state="all", since=since):
        if issue.created_at < since:
            continue
        active_days_by_user[issue.user.login].add(issue.created_at.date())
    for pr in repo.get_pulls(state="all", sort="created", direction="desc"):
        if pr.created_at < since:
            continue
        active_days_by_user[pr.user.login].add(pr.created_at.date())
    for pr in repo.get_pulls(state="closed", sort="updated", direction="desc"):
        if pr.updated_at < since:
            continue
        if not pr.merged or pr.merged_at < since:
            continue
        active_days_by_user[pr.user.login].add(pr.merged_at.date())
    return active_days_by_user


def main() -> None:
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    global gh
    gh = Github(GITHUB_TOKEN)
    since = datetime(2012, 1, 1)

    repostats: dict[str, dict] = {}

    for repo in tqdm(list(gh.get_user("ActivityWatch").get_repos())):
        if repo.name not in [
            "activitywatch",
            "activitywatch-old",
            "docs",
            "aw-core",
            "aw-client",
            "aw-client-js",
            "aw-server",
            "aw-server-rust",
            "aw-watcher-window",
            "aw-watcher-afk",
            "aw-watcher-input",
            "aw-webui",
            "aw-qt",
            "activitywatch.github.io",
        ]:
            continue
        logger.info(f"Processing for {repo.name}...")

        repostats[repo.name] = {
            "comments_by_user": _comments_by_user(repo.full_name, since=since),
            "issues_by_user": _issues_by_user(repo.full_name, since=since),
            "pr_comments_by_user": _pr_comments_by_user(repo.full_name, since=since),
            "issues": _issues_stats(repo.full_name, since=since),
            "merged_prs_by_user": _merged_prs_by_user(repo.full_name, since=since),
            "submitted_prs": _submitted_prs(repo.full_name, since=since),
            "active_days_by_user": _get_active_days_by_user(
                repo.full_name, since=since
            ),
        }

    # pprint(repostats)
    # FIXME: pprint should use sort_dicts=False (added in Python 3.8)
    # pprint(repostats["activitywatch"])

    all_users = set(
        user
        for repo in repostats.values()
        for user in (
            set(repo["comments_by_user"].keys())
            | set(repo["issues_by_user"].keys())
            | set(repo["pr_comments_by_user"].keys())
            | set(repo["merged_prs_by_user"].keys())
        )
    )
    print(f"Total contributors: {len(all_users)}")

    # Compute stats for each repo
    for name, stats in repostats.items():
        df = pd.DataFrame(
            [
                (
                    user,
                    stats["issues_by_user"].get(user, 0),
                    stats["comments_by_user"].get(user, 0),
                    stats["pr_comments_by_user"].get(user, 0),
                    stats["submitted_prs"],
                    stats["merged_prs_by_user"].get(user, 0),
                    # active days
                    stats["active_days_by_user"].get(user, set()),
                )
                for user in all_users
            ],
            columns=[
                "user",
                "issues",
                "comments",
                "pr_comments",
                "submitted_prs",
                "merged_prs",
                "active_days_by_user",
            ],
        )
        df["total"] = (
            df["issues"] + df["comments"] + df["pr_comments"] + df["merged_prs"]
        )
        df = df.sort_values("total", ascending=False)
        df = df.set_index("user")
        stats["df"] = df

    def df_total(repostats: dict[str, pd.DataFrame]) -> pd.DataFrame:
        # Sum all repo stats into one dataframe
        df: pd.DataFrame = None
        for stats in repostats.values():
            if df is None:
                df = stats["df"]
            else:
                # print(df.columns)
                # print(stats["df"].columns)
                # output: ['issues', 'comments', 'pr_comments', 'submitted_prs', 'merged_prs', 'active_days_by_user', 'total']

                # note that active_days_by_user is a set, so it's not additive

                df["issues"] += stats["df"]["issues"]
                df["comments"] += stats["df"]["comments"]
                df["pr_comments"] += stats["df"]["pr_comments"]
                df["merged_prs"] += stats["df"]["merged_prs"]
                df["submitted_prs"] += stats["df"]["submitted_prs"]
                df["total"] += (
                    stats["df"]["issues"]
                    + stats["df"]["comments"]
                    + stats["df"]["pr_comments"]
                    + stats["df"]["merged_prs"]
                )

                # here the sets in active_days_by_user are added together too
                days_by_name = defaultdict(set)
                for name, days in itertools.chain(
                    df["active_days_by_user"].iteritems(),
                    stats["df"]["active_days_by_user"].iteritems(),
                ):
                    if isinstance(days, float):
                        continue
                    days_by_name[name].update(days)

                df["active_days_by_user"] = pd.Series(
                    list(days_by_name.values()),
                    index=list(days_by_name.keys()),
                    dtype=object,
                )

        df["no_active_days_by_user"] = df["active_days_by_user"].apply(lambda x: len(x))
        df = df.sort_values("total", ascending=True)
        return df

    df = df_total(repostats)

    pd.set_option("display.max_rows", None, "display.max_columns", None)
    print(
        df[
            [
                "issues",
                "comments",
                "pr_comments",
                "total",
                "merged_prs",
                "no_active_days_by_user",
            ]
        ].iloc[-15:]
    )
    print(df.columns)

    savepath = Path("github-activity-table.html")
    with savepath.open("w") as f:
        html = df.to_html()
        f.write(html)
    print(f"Written to {savepath}")
    print("Done!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
