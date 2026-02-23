"""Unit Tests for Composio Wrapper"""
import os
import tempfile
import unittest
from unittest.mock import patch, MagicMock

# Set environment variable before importing
os.environ["COMPOSIO_API_KEY"] = "test_key"

from composio_wrapper import ComposioWrapper


class TestComposioWrapper(unittest.TestCase):
    """Test cases for ComposioWrapper class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.wrapper = ComposioWrapper(api_key="test_key")
    
    def test_initialization(self):
        """Test wrapper initialization."""
        self.assertEqual(self.wrapper.api_key, "test_key")
        self.assertIsNotNone(self.wrapper._client)
    
    def test_health_check(self):
        """Test health check function."""
        health = self.wrapper.health_check()
        self.assertIn("composio_available", health)
        self.assertIn("api_key_configured", health)
        self.assertIn("status", health)
    
    def test_list_available_tools(self):
        """Test listing available tools."""
        tools = self.wrapper.list_available_tools()
        self.assertIsInstance(tools, list)
        self.assertIn("github_list_issues", tools)
        self.assertIn("slack_send_message", tools)
        self.assertIn("sheets_read", tools)
    
    def test_file_write_and_read(self):
        """Test file write and read operations."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            temp_path = f.name
            f.write("Test content")
        
        try:
            # Write
            result = self.wrapper.file_write(temp_path, "New content")
            self.assertTrue(result["success"])
            
            # Read
            result = self.wrapper.file_read(temp_path)
            self.assertTrue(result["success"])
            self.assertEqual(result["content"], "New content")
        finally:
            os.unlink(temp_path)
    
    def test_file_list(self):
        """Test file list operation."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create some files
            open(os.path.join(tmpdir, "file1.txt"), 'w').close()
            open(os.path.join(tmpdir, "file2.txt"), 'w').close()
            
            files = self.wrapper.file_list(tmpdir)
            self.assertIn("file1.txt", files)
            self.assertIn("file2.txt", files)
    
    def test_github_list_issues(self):
        """Test GitHub list issues (mocked)."""
        result = self.wrapper.github_list_issues(
            owner="test-owner",
            repo="test-repo"
        )
        self.assertIsInstance(result, list)
    
    def test_github_create_issue(self):
        """Test GitHub create issue (mocked)."""
        result = self.wrapper.github_create_issue(
            owner="test-owner",
            repo="test-repo",
            title="Test Issue",
            body="Test body"
        )
        self.assertIn("success", result)
    
    def test_slack_send_message(self):
        """Test Slack send message (mocked)."""
        result = self.wrapper.slack_send_message(
            channel="#test",
            message="Test message"
        )
        self.assertIn("success", result)
    
    def test_sheets_read(self):
        """Test Google Sheets read (mocked)."""
        result = self.wrapper.sheets_read(
            spreadsheet_id="test-id",
            range_name="Sheet1!A1"
        )
        self.assertIn("spreadsheet_id", result)
    
    def test_sheets_write(self):
        """Test Google Sheets write (mocked)."""
        result = self.wrapper.sheets_write(
            spreadsheet_id="test-id",
            range_name="Sheet1!A1",
            values=[["Test", "Value"]]
        )
        self.assertIn("success", result)
    
    def test_search_web(self):
        """Test web search (mocked)."""
        result = self.wrapper.search_web("test query", num_results=5)
        self.assertIsInstance(result, list)
    
    def test_search_github(self):
        """Test GitHub search (mocked)."""
        result = self.wrapper.search_github("test query", limit=10)
        self.assertIsInstance(result, list)


class TestComposioWrapperWithoutKey(unittest.TestCase):
    """Test wrapper behavior without API key."""
    
    def test_initialization_without_key(self):
        """Test wrapper initialization without API key."""
        # Clear environment variable if set
        with patch.dict(os.environ, {}, clear=True):
            wrapper = ComposioWrapper()
            # File operations should still work
            health = wrapper.health_check()
            self.assertFalse(health["api_key_configured"])


if __name__ == "__main__":
    unittest.main()
