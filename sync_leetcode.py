import os
import re
import time
from pathlib import Path

import requests


# =========================
# CONFIG
# =========================

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
    "Origin": "https://leetcode.com",
    "x-csrftoken": CSRF,
    "User-Agent": "Mozilla/5.0",
}


# =========================
# GRAPHQL HELPER
# =========================

def graphql(query, variables, operation_name):
    response = requests.post(
        LEETCODE_URL,
        json={
            "operationName": operation_name,
            "variables": variables,
            "query": query,
        },
        headers=headers,
        cookies=cookies,
        timeout=30,
    )

    response.raise_for_status()

    result = response.json()

    if result.get("errors"):
        print("GraphQL error:")
        print(result["errors"])
        return None

    return result.get("data")


# =========================
# GET ACCEPTED SUBMISSIONS
# =========================

SUBMISSIONS_QUERY = """
query submissionList(
    $offset: Int!,
    $limit: Int!,
    $lastKey: String,
    $questionSlug: String
) {
    submissionList(
        offset: $offset,
        limit: $limit,
        lastKey: $lastKey,
        questionSlug: $questionSlug
    ) {
        lastKey
        hasNext
        submissions {
            id
            statusDisplay
            lang
            timestamp
            question {
                title
                titleSlug
                questionFrontendId
            }
        }
    }
}
"""


def get_submissions(slug):
    data = graphql(
        SUBMISSIONS_QUERY,
        {
            "offset": 0,
            "limit": 20,
            "lastKey": None,
            "questionSlug": slug,
        },
        "submissionList",
    )

    if not data:
        return []

    result = data.get("submissionList")

    if not result:
        return []

    return [
        submission
        for submission in result.get("submissions", [])
        if submission.get("statusDisplay") == "Accepted"
    ]


# =========================
# GET SOURCE CODE
# =========================

SOURCE_QUERY = """
query submissionDetails($submissionId: Int!) {
    submissionDetails(submissionId: $submissionId) {
        code
        lang
        runtime
        memory
        timestamp
    }
}
"""


def get_source_code(submission_id):
    data = graphql(
        SOURCE_QUERY,
        {
            "submissionId": int(submission_id)
        },
        "submissionDetails",
    )

    if not data:
        return None

    details = data.get("submissionDetails")

    if not details:
        return None

    return details


# =========================
# LANGUAGE -> EXTENSION
# =========================

LANGUAGE_EXTENSIONS = {
    "python": ".py",
    "python3": ".py",
    "java": ".java",
    "cpp": ".cpp",
    "c++": ".cpp",
    "c": ".c",
    "javascript": ".js",
    "typescript": ".ts",
    "kotlin": ".kt",
    "kotlinlang": ".kt",
    "swift": ".swift",
    "go": ".go",
    "golang": ".go",
    "rust": ".rs",
    "ruby": ".rb",
    "php": ".php",
    "csharp": ".cs",
    "c#": ".cs",
    "scala": ".scala",
    "dart": ".dart",
    "sql": ".sql",
}


def get_extension(language):
    language = language.lower().strip()

    return LANGUAGE_EXTENSIONS.get(language, ".txt")


# =========================
# SAFE FILENAME
# =========================

def clean_filename(name):
    name = name.lower()

    name = re.sub(r"[^a-z0-9]+", "_", name)

    name = name.strip("_")

    return name


# =========================
# CHOOSE FOLDER
# =========================

def choose_folder(title):
    title_lower = title.lower()

    folders = {
        "array": "Arrays",
        "string": "Strings",
        "linked list": "Linked_List",
        "tree": "Trees",
        "graph": "Graphs",
        "stack": "Stack",
        "queue": "Queue",
        "matrix": "Matrix",
        "math": "Math",
        "backtracking": "Backtracking",
        "binary": "Bit_Manipulation",
    }

    for keyword, folder in folders.items():
        if keyword in title_lower:
            return folder

    return "Other"


# =========================
# MAIN
# =========================

def main():

    print("Starting LeetCode sync...")
    print(f"Username: {USERNAME}")

    # Get recent accepted submissions.
    # We use the existing recent-accepted query because it gives
    # us the problems we need to inspect.
    recent_query = """
    query recentAcSubmissions($username: String!, $limit: Int!) {
        recentAcSubmissionList(
            username: $username,
            limit: $limit
        ) {
            title
            titleSlug
            timestamp
            statusDisplay
            lang
        }
    }
    """

    data = graphql(
        recent_query,
        {
            "username": USERNAME,
            "limit": 100,
        },
        "recentAcSubmissions",
    )

    if not data:
        print("Could not retrieve submissions.")
        return

    submissions = data.get("recentAcSubmissionList", [])

    submissions = [
        x for x in submissions
        if x.get("statusDisplay") == "Accepted"
    ]

    print(f"Found {len(submissions)} accepted submissions.")

    # One entry per problem.
    unique = {}

    for submission in submissions:

        slug = submission["titleSlug"]

        if slug not in unique:
            unique[slug] = submission

    print(f"Unique problems: {len(unique)}")

    # Process every problem.
    for submission in unique.values():

        title = submission["title"]
        slug = submission["titleSlug"]

        print()
        print(f"Processing: {title}")

        # Get submission history for this problem.
        accepted = get_submissions(slug)

        if not accepted:
            print("  No accepted submission found.")
            continue

        # First accepted submission returned is normally the latest.
        latest = accepted[0]

        submission_id = latest["id"]

        print(f"  Submission ID: {submission_id}")

        # Retrieve actual code.
        details = get_source_code(submission_id)

        if not details:
            print("  Could not retrieve source code.")
            continue

        code = details.get("code")

        if not code:
            print("  Source code was empty.")
            continue

        language = details.get("lang", submission.get("lang", "text"))

        extension = get_extension(language)

        filename = clean_filename(title) + extension

        folder = choose_folder(title)

        directory = Path(folder)

        directory.mkdir(
            parents=True,
            exist_ok=True
        )

        filepath = directory / filename

        # Don't overwrite an existing solution.
        if filepath.exists():
            print(f"  Already exists: {filepath}")
            continue

        filepath.write_text(
            code,
            encoding="utf-8"
        )

        print(f"  Created: {filepath}")

        time.sleep(1)

    print()
    print("LeetCode sync finished.")


if __name__ == "__main__":
    main()
