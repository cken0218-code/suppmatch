#!/usr/bin/env python3
"""
Composio Wrapper Local Skill for OpenClaw

This skill provides a unified interface to Composio's 1000+ toolkits,
including GitHub, Google Sheets, Slack, and more.

Requirements:
    - COMPOSIO_API_KEY environment variable
    - pip install composio-core

Usage:
    from composio_wrapper import ComposioWrapper
    
    wrapper = ComposioWrapper()
    result = wrapper.github_list_issues(owner="user", repo="repo")
"""

import os
from typing import Any, Dict, List, Optional

try:
    from composio import Composio, ComposioToolSet
    COMPOSIO_AVAILABLE = True
except ImportError:
    COMPOSIO_AVAILABLE = False


class ComposioWrapper:
    """
    Unified wrapper for Composio toolkits.
    
    Provides easy access to common integrations:
    - GitHub: Issues, PRs, commits
    - Google Sheets: Read/write operations
    - Slack: Send messages
    - Search: Web search functionality
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Composio wrapper.
        
        Args:
            api_key: Composio API key. Falls back to COMPOSIO_API_KEY env var.
        """
        self.api_key = api_key or os.environ.get("COMPOSIO_API_KEY")
        self._client = None
        self._toolset = None
        
        if self.api_key and COMPOSIO_AVAILABLE:
            self._initialize_client()
        elif not COMPOSIO_AVAILABLE:
            print("Warning: composio-core not installed. Install with: pip install composio-core")
    
    def _initialize_client(self):
        """Initialize Composio client and toolset."""
        try:
            self._client = Composio(api_key=self.api_key)
            self._toolset = ComposioToolSet(api_key=self.api_key)
            print("✓ Composio client initialized successfully")
        except Exception as e:
            print(f"✗ Failed to initialize Composio client: {e}")
    
    # ==================== GITHUB ====================
    
    def github_list_issues(
        self,
        owner: str,
        repo: str,
        state: str = "open",
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """List issues in a repository."""
        if not COMPOSIO_AVAILABLE:
            return [{"error": "composio-core not installed"}]
        
        try:
            # Use ComposioToolSet to execute GitHub actions
            return self._execute_action(
                action="github_list_issues",
                owner=owner,
                repo=repo,
                state=state
            )
        except Exception as e:
            return [{"error": str(e)}]
    
    def github_create_issue(
        self,
        owner: str,
        repo: str,
        title: str,
        body: str = ""
    ) -> Dict[str, Any]:
        """Create a new issue in a repository."""
        if not COMPOSIO_AVAILABLE:
            return {"error": "composio-core not installed"}
        
        try:
            return self._execute_action(
                action="github_create_issue",
                owner=owner,
                repo=repo,
                title=title,
                body=body
            )
        except Exception as e:
            return {"error": str(e)}
    
    def github_list_prs(
        self,
        owner: str,
        repo: str,
        state: str = "open"
    ) -> List[Dict[str, Any]]:
        """List pull requests in a repository."""
        if not COMPOSIO_AVAILABLE:
            return [{"error": "composio-core not installed"}]
        
        try:
            return self._execute_action(
                action="github_list_prs",
                owner=owner,
                repo=repo,
                state=state
            )
        except Exception as e:
            return [{"error": str(e)}]
    
    def github_get_commits(
        self,
        owner: str,
        repo: str,
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """Get recent commits from a repository."""
        if not COMPOSIO_AVAILABLE:
            return [{"error": "composio-core not installed"}]
        
        try:
            return self._execute_action(
                action="github_get_commits",
                owner=owner,
                repo=repo
            )
        except Exception as e:
            return [{"error": str(e)}]
    
    # ==================== GOOGLE SHEETS ====================
    
    def sheets_read(
        self,
        spreadsheet_id: str,
        range_name: str
    ) -> Dict[str, Any]:
        """Read data from a Google Sheet."""
        if not COMPOSIO_AVAILABLE:
            return {"error": "composio-core not installed"}
        
        try:
            return self._execute_action(
                action="googlesheets_read_values",
                spreadsheet_id=spreadsheet_id,
                range=range_name
            )
        except Exception as e:
            return {"error": str(e)}
    
    def sheets_write(
        self,
        spreadsheet_id: str,
        range_name: str,
        values: List[List[Any]]
    ) -> Dict[str, Any]:
        """Write data to a Google Sheet."""
        if not COMPOSIO_AVAILABLE:
            return {"error": "composio-core not installed"}
        
        try:
            return self._execute_action(
                action="googlesheets_update_values",
                spreadsheet_id=spreadsheet_id,
                range=range_name,
                values=values
            )
        except Exception as e:
            return {"error": str(e)}
    
    def sheets_create(
        self,
        title: str,
        sheet_id: str = "0"
    ) -> Dict[str, Any]:
        """Create a new Google Sheet."""
        if not COMPOSIO_AVAILABLE:
            return {"error": "composio-core not installed"}
        
        try:
            return self._execute_action(
                action="googlesheets_create_spreadsheet",
                title=title
            )
        except Exception as e:
            return {"error": str(e)}
    
    # ==================== SLACK ====================
    
    def slack_send_message(
        self,
        channel: str,
        message: str
    ) -> Dict[str, Any]:
        """Send a message to a Slack channel."""
        if not COMPOSIO_AVAILABLE:
            return {"error": "composio-core not installed"}
        
        try:
            return self._execute_action(
                action="slack_send_message",
                channel=channel,
                text=message
            )
        except Exception as e:
            return {"error": str(e)}
    
    def slack_list_channels(self) -> List[Dict[str, Any]]:
        """List Slack channels."""
        if not COMPOSIO_AVAILABLE:
            return [{"error": "composio-core not installed"}]
        
        try:
            return self._execute_action(action="slack_list_channels")
        except Exception as e:
            return [{"error": str(e)}]
    
    # ==================== SEARCH ====================
    
    def search_web(
        self,
        query: str,
        num_results: int = 10
    ) -> List[Dict[str, Any]]:
        """Search the web for information."""
        if not COMPOSIO_AVAILABLE:
            return [{"error": "composio-core not installed"}]
        
        try:
            return self._execute_action(
                action="web_search",
                query=query
            )
        except Exception as e:
            return [{"error": str(e)}]
    
    def search_github(
        self,
        query: str,
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """Search GitHub repositories."""
        if not COMPOSIO_AVAILABLE:
            return [{"error": "composio-core not installed"}]
        
        try:
            return self._execute_action(
                action="github_search_code",
                query=query
            )
        except Exception as e:
            return [{"error": str(e)}]
    
    # ==================== FILE OPERATIONS ====================
    
    def file_read(
        self,
        file_path: str
    ) -> Dict[str, Any]:
        """Read a file from the local filesystem."""
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            return {
                "file_path": file_path,
                "content": content,
                "success": True
            }
        except Exception as e:
            return {"error": str(e)}
    
    def file_write(
        self,
        file_path: str,
        content: str
    ) -> Dict[str, Any]:
        """Write content to a local file."""
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                f.write(content)
            return {
                "file_path": file_path,
                "success": True
            }
        except Exception as e:
            return {"error": str(e)}
    
    def file_list(
        self,
        directory: str = "."
    ) -> List[str]:
        """List files in a directory."""
        try:
            return os.listdir(directory)
        except Exception as e:
            return [f"Error: {str(e)}"]
    
    def file_delete(
        self,
        file_path: str
    ) -> Dict[str, Any]:
        """Delete a local file."""
        try:
            os.remove(file_path)
            return {
                "file_path": file_path,
                "success": True
            }
        except Exception as e:
            return {"error": str(e)}
    
    # ==================== COMPOSIO CORE ====================
    
    def _execute_action(
        self,
        action: str,
        **kwargs
    ) -> Any:
        """Execute a Composio action using the toolset."""
        if not self._toolset:
            raise RuntimeError("Composio toolset not initialized")
        
        try:
            # Use the ComposioToolSet to execute actions
            response = self._toolset.execute_action(
                action_name=action,
                input_params=kwargs
            )
            return response
        except Exception as e:
            # Return structured error for missing/mocked tools
            return {
                "action": action,
                "error": str(e),
                "status": "mocked",
                "params": kwargs
            }
    
    def list_available_actions(self) -> List[str]:
        """List all available Composio actions."""
        if not COMPOSIO_AVAILABLE:
            return []
        
        try:
            # Return common actions available in Composio
            return [
                # GitHub
                "github_list_issues",
                "github_create_issue",
                "github_list_prs",
                "github_get_commits",
                "github_search_code",
                "github_get_pull_request",
                # Google Sheets
                "googlesheets_read_values",
                "googlesheets_update_values",
                "googlesheets_create_spreadsheet",
                # Slack
                "slack_send_message",
                "slack_list_channels",
                "slack_get_message",
                # Search
                "web_search",
                # File operations
                "file_read",
                "file_write",
                "file_list"
            ]
        except Exception:
            return []
    
    # ==================== UTILITY ====================
    
    def health_check(self) -> Dict[str, Any]:
        """Check the health of the Composio connection."""
        return {
            "composio_available": COMPOSIO_AVAILABLE,
            "api_key_configured": bool(self.api_key),
            "client_initialized": bool(self._client),
            "toolset_ready": bool(self._toolset),
            "status": "healthy" if (COMPOSIO_AVAILABLE and self.api_key) else "degraded"
        }
    
    def list_available_tools(self) -> List[str]:
        """List all available tools in this wrapper."""
        return [
            "github_list_issues",
            "github_create_issue",
            "github_list_prs",
            "github_get_commits",
            "sheets_read",
            "sheets_write",
            "sheets_create",
            "slack_send_message",
            "slack_list_channels",
            "search_web",
            "search_github",
            "file_read",
            "file_write",
            "file_list",
            "file_delete",
            "health_check",
            "list_available_actions"
        ]


def main():
    """Demo function to test the wrapper."""
    wrapper = ComposioWrapper()
    
    print("\n=== Composio Wrapper Demo ===\n")
    print(f"Composio SDK available: {COMPOSIO_AVAILABLE}")
    print(f"Available tools: {wrapper.list_available_tools()}")
    print(f"\nHealth check: {wrapper.health_check()}")
    
    # Test file operations (always work without API key)
    print("\n--- Testing File Operations ---")
    test_file = "/tmp/composio_test.txt"
    result = wrapper.file_write(test_file, "Hello from Composio Wrapper!")
    print(f"File write: {result}")
    
    result = wrapper.file_read(test_file)
    print(f"File read: {result}")
    
    result = wrapper.file_list("/tmp")
    print(f"File list: {result}")


if __name__ == "__main__":
    main()
