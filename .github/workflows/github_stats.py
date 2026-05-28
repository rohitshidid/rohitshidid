#!/usr/bin/env python3
"""
Computes GitHub stats and writes them into README.md between the markers:
    <!-- GITHUB-STATS:START -->  ...  <!-- GITHUB-STATS:END -->

Run by .github/workflows/update-stats.yml. Reads:
    GH_TOKEN        - a GitHub token (PAT recommended for private-contribution counts)
    STATS_USERNAME  - the GitHub login to report on (default: rohitshidid)
    README_PATH     - path to the README (default: README.md)
"""
import os
import re
import sys
import datetime
import requests

API = "https://api.github.com/graphql"
USERNAME = os.environ.get("STATS_USERNAME", "rohitshidid")
TOKEN = os.environ.get("GH_TOKEN")
README_PATH = os.environ.get("README_PATH", "README.md")

if not TOKEN:
    sys.exit("Missing GH_TOKEN environment variable.")

HEADERS = {"Authorization": f"bearer {TOKEN}"}


def gql(query, variables=None):
    resp = requests.post(
        API, json={"query": query, "variables": variables or {}}, headers=HEADERS, timeout=30
    )
    resp.raise_for_status()
    payload = resp.json()
    if "errors" in payload:
        raise RuntimeError(payload["errors"])
    return payload["data"]


def get_profile():
    """Account creation date, total PRs authored, total PRs merged."""
    q = """
    query($login:String!){
      user(login:$login){
        createdAt
        prsAuthored: pullRequests { totalCount }
        prsMerged: pullRequests(states: MERGED) { totalCount }
      }
    }"""
    u = gql(q, {"login": USERNAME})["user"]
    created_year = int(u["createdAt"][:4])
    return created_year, u["prsAuthored"]["totalCount"], u["prsMerged"]["totalCount"]


def get_total_stars():
    """Sum of stargazers across owned, non-fork repos (paginated)."""
    q = """
    query($login:String!, $cursor:String){
      user(login:$login){
        repositories(first:100, after:$cursor, ownerAffiliations:OWNER, isFork:false){
          totalCount
          pageInfo { hasNextPage endCursor }
          nodes { stargazerCount }
        }
      }
    }"""
    stars, cursor = 0, None
    while True:
        repos = gql(q, {"login": USERNAME, "cursor": cursor})["user"]["repositories"]
        stars += sum(n["stargazerCount"] for n in repos["nodes"])
        if not repos["pageInfo"]["hasNextPage"]:
            break
        cursor = repos["pageInfo"]["endCursor"]
    return stars


def commits_in_window(frm, to):
    q = """
    query($login:String!, $from:DateTime!, $to:DateTime!){
      user(login:$login){
        contributionsCollection(from:$from, to:$to){
          totalCommitContributions
          restrictedContributionsCount
        }
      }
    }"""
    c = gql(q, {"login": USERNAME, "from": frm, "to": to})["user"]["contributionsCollection"]
    return c["totalCommitContributions"] + c["restrictedContributionsCount"]


def get_commit_counts(created_year):
    now = datetime.datetime.now(datetime.timezone.utc)
    this_year = now.year

    all_time = 0
    for y in range(created_year, this_year + 1):
        frm = f"{y}-01-01T00:00:00Z"
        to = f"{y}-12-31T23:59:59Z"
        all_time += commits_in_window(frm, to)

    last_year = commits_in_window(
        (now - datetime.timedelta(days=365)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    )
    return all_time, last_year


def build_table(stars, all_time, last_year, prs, prs_merged):
    return (
        "<!-- GITHUB-STATS:START -->\n"
        "### Rohit's · GitHub Stats\n\n"
        "| Metric | Count |\n"
        "|--------|-------|\n"
        f"| Total Stars Earned | `{stars}` |\n"
        f"| Total Commits (All Time) | `{all_time}` |\n"
        f"| Total Commits (Last Year) | `{last_year}` |\n"
        f"| Total PRs Authored | `{prs}` |\n"
        f"| Total PRs Merged | `{prs_merged}` |\n"
        "<!-- GITHUB-STATS:END -->"
    )


def main():
    created_year, prs, prs_merged = get_profile()
    stars = get_total_stars()
    all_time, last_year = get_commit_counts(created_year)
    table = build_table(stars, all_time, last_year, prs, prs_merged)

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    new_content, n = re.subn(
        r"<!-- GITHUB-STATS:START -->.*?<!-- GITHUB-STATS:END -->",
        table,
        content,
        flags=re.DOTALL,
    )
    if n == 0:
        sys.exit("Markers not found in README. Keep the GITHUB-STATS:START/END comments.")

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Updated stats: stars={stars}, all_time={all_time}, last_year={last_year}, "
          f"prs={prs}, merged={prs_merged}")


if __name__ == "__main__":
    main()
