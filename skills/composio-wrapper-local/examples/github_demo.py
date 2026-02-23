"""GitHub Integration Examples"""
from composio_wrapper import ComposioWrapper

wrapper = ComposioWrapper()

# List all open issues
print("=== Listing GitHub Issues ===")
issues = wrapper.github_list_issues(
    owner="my-org",
    repo="my-repo",
    state="open"
)
print(f"Found {len(issues)} open issues")

# Create a new issue
print("\n=== Creating GitHub Issue ===")
issue = wrapper.github_create_issue(
    owner="my-org",
    repo="my-repo",
    title="New Feature Request",
    body="Please add this feature..."
)
print(f"Created issue: {issue}")

# List pull requests
print("\n=== Listing Pull Requests ===")
prs = wrapper.github_list_prs(
    owner="my-org",
    repo="my-repo",
    state="all"
)
print(f"Found {len(prs)} pull requests")

# Get recent commits
print("\n=== Getting Recent Commits ===")
commits = wrapper.github_get_commits(
    owner="my-org",
    repo="my-repo",
    limit=5
)
print(f"Found {len(commits)} commits")
