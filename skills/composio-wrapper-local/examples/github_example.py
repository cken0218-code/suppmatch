"""
GitHub Integration Example for Composio Wrapper

This example demonstrates GitHub-related tool usage.
"""

import os
from dotenv import load_dotenv
from composio_wrapper import ComposioWrapper, ComposioConfig

# Load environment variables
load_dotenv()


def main():
    api_key = os.getenv("COMPOSIO_API_KEY")
    if not api_key:
        print("Error: COMPOSIO_API_KEY not set")
        return
    
    config = ComposioConfig(api_key=api_key)
    wrapper = ComposioWrapper(config)
    
    user_id = "github_demo_user"
    
    print("=== GitHub Integration Demo ===\n")
    
    try:
        # Create session
        session = wrapper.create_session(user_id)
        print("✅ Session created\n")
        
        # Example 1: List issues from a repository
        print("1. Listing issues from composiohq/composio...")
        result = wrapper.execute_tool(
            user_id=user_id,
            tool_name="github_list_issues",
            params={
                "owner": "composiohq",
                "repo": "composio",
                "state": "open"
            }
        )
        
        if result.success:
            print(f"   ✅ Found {len(result.data.get('issues', []))} open issues")
            # Print first 3 issues
            issues = result.data.get('issues', [])[:3]
            for issue in issues:
                print(f"   - #{issue.get('number')}: {issue.get('title')}")
        else:
            print(f"   ❌ Error: {result.error}")
        
        print()
        
        # Example 2: Get repository info
        print("2. Getting repository info...")
        result = wrapper.execute_tool(
            user_id=user_id,
            tool_name="github_get_repo",
            params={
                "owner": "composiohq",
                "repo": "composio"
            }
        )
        
        if result.success:
            data = result.data
            print(f"   ✅ Repository: {data.get('full_name')}")
            print(f"   ⭐ Stars: {data.get('stargazers_count')}")
            print(f"   🍴 Forks: {data.get('forks_count')}")
            print(f"   📝 Open Issues: {data.get('open_issues_count')}")
        else:
            print(f"   ❌ Error: {result.error}")
            
        print()
        
        # Example 3: List pull requests
        print("3. Listing pull requests...")
        result = wrapper.execute_tool(
            user_id=user_id,
            tool_name="github_list_pulls",
            params={
                "owner": "composiohq",
                "repo": "composio",
                "state": "open"
            }
        )
        
        if result.success:
            pulls = result.data.get('pulls', [])
            print(f"   ✅ Found {len(pulls)} open pull requests")
            for pr in pulls[:3]:
                print(f"   - #{pr.get('number')}: {pr.get('title')}")
        else:
            print(f"   ❌ Error: {result.error}")
            
        print()
        
        # Example 4: List commits
        print("4. Listing recent commits...")
        result = wrapper.execute_tool(
            user_id=user_id,
            tool_name="github_list_commits",
            params={
                "owner": "composiohq",
                "repo": "composio",
                "per_page": 5
            }
        )
        
        if result.success:
            commits = result.data.get('commits', [])
            print(f"   ✅ Found {len(commits)} recent commits")
            for commit in commits[:3]:
                msg = commit.get('commit', {}).get('message', '').split('\n')[0]
                print(f"   - {msg[:50]}...")
        else:
            print(f"   ❌ Error: {result.error}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
