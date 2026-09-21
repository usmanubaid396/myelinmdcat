import os
import json
import subprocess
import requests
from google import genai

def get_pr_diff():
    """Fetches the diff for the current pull request."""
    result = subprocess.run(
        ["git", "diff", "origin/main...HEAD"],
        capture_output=True,
        text=True
    )
    diff = result.stdout
    # Truncate if diff exceeds reasonable token budget
    return diff[:40000] if len(diff) > 40000 else diff

def post_comment(comments_url, body, token):
    """Posts Gemini's response back to the GitHub PR."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    payload = {"body": body}
    response = requests.post(comments_url, headers=headers, json=payload)
    response.raise_for_status()

def main():
    gemini_key = os.environ.get("GEMINI_API_KEY")
    github_token = os.environ.get("GITHUB_TOKEN")
    event_payload = json.loads(os.environ.get("EVENT_PAYLOAD", "{}"))

    if not gemini_key or not github_token:
        print("Missing required environment secrets.")
        return

    # Determine comment endpoint
    if "pull_request" in event_payload:
        comments_url = event_payload["pull_request"]["comments_url"]
    else:
        comments_url = event_payload["issue"]["comments_url"]

    # Gather repository changes
    diff = get_pr_diff()
    if not diff.strip():
        print("No diff detected.")
        return

    # Initialize Gemini client
    client = genai.Client(api_key=gemini_key)

    prompt = f"""
You are a senior technical reviewer and assistant embedded inside this GitHub repository.
Review the following pull request git diff.

Tasks:
1. Provide a concise summary of what changed.
2. Flag any potential bugs, security issues, or regressions.
3. If this contains data/content files (like JSON, questions, or config), verify formatting and structure consistency.
4. Give a clear verdict: [LGTM] or [Action Needed].

Git Diff:
```diff
{diff}
