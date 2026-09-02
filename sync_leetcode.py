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

    try:
        result = response.json()
    except ValueError:
        print("HTTP status:", response.status_code)
        print("Non-JSON response:", response.text[:500])
        return None

    if response.status_code != 200:
        print("HTTP status:", response.status_code)
        print("Response:", result)
        return None

    if result.get("errors"):
        print("GraphQL error:")
        print(result["errors"])
        return None

    return result.get("data")


# =========================
# GET SUBMISSION HISTORY
# =========================

def get_submission_page(offset, limit=20):

    query = """
    query submissionList(
        $offset: Int!,
        $limit: Int!
    ) {
        submissionList(
            offset: $offset,
            limit: $limit
        ) {
            submissions {
                id
                statusDisplay
                lang
                timestamp
                question {
                    title
                    titleSlug
                }
            }
        }
    }
    """

    return graphql(
        query,
        {
            "offset": offset,
            "limit": limit,
        },
        "submissionList",
    )


# =========================
# SOURCE CODE
# =========================

def get_source_code(submission_id):

    query = """
    query submissionDetails($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) {
            code
        }
    }
    """

    data = graphql(
        query,
        {
            "submissionId": int(submission_id)
        },
        "submissionDetails"
    )

    if not data:
        return None

    return data.get("submissionDetails")


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

    name = re.sub(
        r"[^a-z0-9]+",
        "_",
        name
    )

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
# CHECK TARGET FILE
# =========================

def get_target_path(title, language):

    extension = get_extension(language)

    filename = clean_filename(title) + extension

    folder = choose_folder(title)

    return Path(folder) / filename


# =========================
# MAIN
# =========================

def main():

    print("Starting LeetCode sync...")
    print(f"Username: {USERNAME}")
    print()

    offset = 0
    page_size = 20

    checked_problems = set()

    while True:

        print(
            f"Fetching submissions "
            f"{offset + 1}-{offset + page_size}..."
        )

        data = get_submission_page(
            offset,
            page_size
        )

        if not data:

            print()
            print("Could not retrieve submission history.")
            return

        result = data.get("submissionList")

        if not result:

            print()
            print("No submission list returned.")
            return

        submissions = result.get(
            "submissions",
            []
        )

        if not submissions:

            print()
            print("No more submissions found.")
            break

        print(
            f"Received {len(submissions)} submissions."
        )

        # ==========================================
        # Process submissions in the order returned.
        # LeetCode returns newest submissions first.
        # ==========================================

        for submission in submissions:

            if submission.get("statusDisplay") != "Accepted":
                continue

            question = submission.get("question")

            if not question:
                continue

            title = question.get("title")
            slug = question.get("titleSlug")

            if not title or not slug:
                continue

            # --------------------------------------
            # We only need to process each problem
            # once during this run.
            # --------------------------------------

            if slug in checked_problems:
                continue

            checked_problems.add(slug)

            language = submission.get(
                "lang",
                "text"
            )

            filepath = get_target_path(
                title,
                language
            )

            print()
            print(f"Processing: {title}")
            print(f"  Language: {language}")
            print(f"  Expected file: {filepath}")

            # --------------------------------------
            # FILE ALREADY EXISTS
            # --------------------------------------

            if filepath.exists():

                print(
                    f"  Already exists: {filepath}"
                )

                continue

            # --------------------------------------
            # THIS IS THE FIRST MISSING FILE
            # --------------------------------------

            submission_id = submission.get("id")

            if not submission_id:

                print(
                    "  Submission ID missing."
                )

                continue

            print(
                f"  Missing file found!"
            )

            print(
                f"  Submission ID: {submission_id}"
            )

            # --------------------------------------
            # Retrieve source code ONLY NOW.
            # --------------------------------------

            details = get_source_code(
                submission_id
            )

            if not details:

                print(
                    "  Could not retrieve source code."
                )

                continue

            code = details.get("code")

            if not code:

                print(
                    "  Source code was empty."
                )

                continue

            # --------------------------------------
            # Create directory
            # --------------------------------------

            filepath.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            # --------------------------------------
            # Create ONE solution
            # --------------------------------------

            filepath.write_text(
                code,
                encoding="utf-8"
            )

            print()
            print(
                f"  Created: {filepath}"
            )

            print()
            print(
                "Found and created ONE new solution."
            )

            print(
                "Stopping this sync now."
            )

            # ======================================
            # IMPORTANT:
            # STOP THE ENTIRE SCRIPT.
            # ======================================

            return

        # ==========================================
        # If fewer than 20 were returned, this was
        # the final page.
        # ==========================================

        if len(submissions) < page_size:

            print()
            print(
                "Reached the end of submission history."
            )

            break

        offset += page_size

        time.sleep(0.5)

    # =========================
    # NOTHING NEW
    # =========================

    print()
    print("================================")
    print("LeetCode sync finished.")
    print(
        f"Problems checked: {len(checked_problems)}"
    )
    print("No new solution found.")
    print("================================")


if __name__ == "__main__":
    main()
