import os
import requests
import base64
import re
import time

USERNAME = os.environ["LEETCODE_USERNAME"]
SESSION = os.environ["LEETCODE_SESSION"]
CSRF = os.environ["LEETCODE_CSRFTOKEN"]

LEETCODE_URL = "https://leetcode.com/graphql"

cookies = {
    "LEETCODE_SESSION": SESSION,
    "csrftoken": CSRF,
}

headers = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com/",
    "x-csrftoken": CSRF,
}

query = """
query recentAcSubmissions($username: String!, $limit: Int!) {
  recentAcSubmissionList(username: $username, limit: $limit) {
    title
    titleSlug
    timestamp
    lang
  }
}
"""

response = requests.post(
    LEETCODE_URL,
    json={
        "query": query,
        "variables": {
            "username": USERNAME,
            "limit": 100
        }
    },
    headers=headers,
    cookies=cookies,
    timeout=30,
)

response.raise_for_status()

data = response.json()

submissions = data.get("data", {}).get("recentAcSubmissionList", [])

if not submissions:
    print("No accepted submissions found.")
    exit(0)

print(f"Found {len(submissions)} accepted submissions.")

# Remove duplicates
seen = set()
unique_submissions = []

for submission in submissions:
    slug = submission["titleSlug"]

    if slug not in seen:
        seen.add(slug)
        unique_submissions.append(submission)

print(f"Unique problems: {len(unique_submissions)}")

# For now, print what was found.
# The next version will retrieve the actual source code
# and create the GitHub files.

for submission in unique_submissions:
    print(
        submission["title"],
        "|",
        submission["titleSlug"],
        "|",
        submission["lang"]
    )
