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

LEETCODE_URL = "https://leetcode.com/graphql/"

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
# GET ALL SOLVED PROBLEMS
# =========================

def get_solved_page(skip, limit=100):
    query = """
    query userProgressQuestionList($filters: UserProgressQuestionListInput) {
        userProgressQuestionList(filters: $filters) {
            totalNum
            questions {
                frontendId
                title
                titleSlug
                lastSubmittedAt
            }
        }
    }
    """

    return graphql(
        query,
        {
            "filters": {
                "questionStatus": "SOLVED",
                "skip": skip,
                "limit": limit,
            }
        },
        "userProgressQuestionList",
    )


def get_all_solved_problems():
    solved = []
    skip = 0
    limit = 100

    while True:
        print(f"Fetching solved problems {skip + 1}-{skip + limit}...")

        data = get_solved_page(skip, limit)

        if not data:
            return None

        result = data.get("userProgressQuestionList")

        if not result:
            return None

        questions = result.get("questions", [])
        total = result.get("totalNum", 0)

        solved.extend(questions)

        print(f"  Received {len(questions)} problems. Total reported: {total}")

        if not questions or len(solved) >= total:
            break

        skip += len(questions)
        time.sleep(0.5)

    # Remove duplicate slugs while preserving LeetCode's order.
    unique = {}
    for problem in solved:
        slug = problem.get("titleSlug")
        if slug and slug not in unique:
            unique[slug] = problem

    return list(unique.values())


# =========================
# GET ACCEPTED SUBMISSION
# =========================

def get_accepted_submission(slug):
    query = """
    query submissionList(
        $offset: Int!,
        $limit: Int!,
        $questionSlug: String
    ) {
        submissionList(
            offset: $offset,
            limit: $limit,
            questionSlug: $questionSlug
        ) {
            submissions {
                id
                statusDisplay
                lang
                timestamp
            }
        }
    }
    """

    data = graphql(
        query,
        {
            "offset": 0,
            "limit": 20,
            "questionSlug": slug,
        },
        "submissionList",
    )

    if not data:
        return None

    result = data.get("submissionList")
    if not result:
        return None

    accepted = [
        submission
        for submission in result.get("submissions", [])
        if submission.get("statusDisplay") == "Accepted"
    ]

    return accepted[0] if accepted else None


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
        {"submissionId": int(submission_id)},
        "submissionDetails",
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
    return LANGUAGE_EXTENSIONS.get(language.lower().strip(), ".txt")


# =========================
# SAFE FILENAME
# =========================

def clean_filename(name):
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    return name.strip("_")


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
# EXISTING FILE DETECTION
# =========================

def normalize_tokens(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def problem_already_exists(title, frontend_id, expected_path):
    # First: exact path used by the automatic sync.
    if expected_path.exists():
        return True, expected_path

    title_tokens = normalize_tokens(title)
    frontend_id = str(frontend_id or "").strip()

    # Second: recognize older/manual filenames in the repository.
    # A numeric prefix such as 004_ is matched against LeetCode's
    # frontend problem number. This avoids confusing similarly named
    # problems such as "Median of Two Sorted Arrays" and "... II".
    for path in Path(".").rglob("*"):
        if not path.is_file():
            continue

        if ".git" in path.parts:
            continue

        if path.suffix.lower() not in set(LANGUAGE_EXTENSIONS.values()) | {".txt"}:
            continue

        stem = path.stem.lower()
        numbers = re.match(r"^(\d+)[_-]", stem)

        if numbers and frontend_id:
            if str(int(numbers.group(1))) == str(int(frontend_id)):
                return True, path

        # For non-numbered files, require an exact normalized title.
        if normalize_tokens(stem) == title_tokens:
            return True, path

    return False, expected_path


# =========================
# MAIN
# =========================

def main():
    print("Starting LeetCode sync...")
    print(f"Username: {USERNAME}")
    print()

    problems = get_all_solved_problems()

    if problems is None:
        print()
        print("Could not retrieve the complete solved-problem list.")
        print("Nothing was changed.")
        return

    print()
    print(f"LeetCode solved problems found: {len(problems)}")
    print("Searching for the first problem not yet in GitHub...")

    checked = 0

    # Newest solved/last-submitted problems are returned first.
    # The script intentionally creates ONLY ONE missing solution per run.
    for problem in problems:
        title = problem.get("title")
        slug = problem.get("titleSlug")
        frontend_id = problem.get("frontendId")

        if not title or not slug:
            continue

        checked += 1

        accepted = get_accepted_submission(slug)

        if not accepted:
            continue

        language = accepted.get("lang", "text")
        extension = get_extension(language)
        expected_path = (
            Path(choose_folder(title)) /
            (clean_filename(title) + extension)
        )

        exists, existing_path = problem_already_exists(
            title,
            frontend_id,
            expected_path,
        )

        if exists:
            print(f"Already synced: {title} -> {existing_path}")
            continue

        submission_id = accepted.get("id")

        print()
        print("================================")
        print("NEW SOLUTION FOUND")
        print(f"Problem: {title}")
        print(f"Submission ID: {submission_id}")
        print(f"Language: {language}")
        print(f"File: {expected_path}")
        print("================================")

        if not submission_id:
            print("Submission ID missing. Nothing changed.")
            return

        details = get_source_code(submission_id)

        if not details:
            print("Could not retrieve source code. Nothing changed.")
            return

        code = details.get("code")

        if not code:
            print("Source code was empty. Nothing changed.")
            return

        expected_path.parent.mkdir(parents=True, exist_ok=True)
        expected_path.write_text(code, encoding="utf-8")

        print()
        print(f"Created: {expected_path}")
        print("ONE new solution created.")
        print("Stopping now so the workflow can commit exactly one solution.")
        return

    print()
    print("================================")
    print("LeetCode sync finished.")
    print(f"Problems checked: {checked}")
    print("Every checked solved problem already exists in GitHub.")
    print("No new solution created.")
    print("================================")


if __name__ == "__main__":
    main()
