# Composio Wrapper Local Skill for OpenClaw

A unified local skill that connects OpenClaw to Composio's 1000+ toolkits, providing seamless access to GitHub, Google Sheets, Slack, search, and file operations.

## Features

- **GitHub Integration**: List issues, create issues, view PRs, get commits
- **Google Sheets**: Read and write data to spreadsheets
- **Slack**: Send messages to channels
- **Search**: Web and GitHub search capabilities
- **File Operations**: Read, write, and list local files
- **Unified Interface**: Single wrapper for all Composio tools

## Installation

```bash
cd ~/.openclaw/workspace/skills/composio-wrapper-local
pip install -r requirements.txt
```

## Configuration

### Environment Variables

Set your Composio API key in your environment:

```bash
export COMPOSIO_API_KEY="ak_x3qztZT62u54lI2Lztfs"
```

Or create a `.env` file in the skill directory:

```bash
COMPOSIO_API_KEY=ak_x3qztZT62u54lI2Lztfs
```

### OpenClaw Integration

Load the skill in your OpenClaw configuration:

```yaml
skills:
  - name: composio-wrapper
    path: ~/.openclaw/workspace/skills/composio-wrapper-local
    config:
      api_key: ${COMPOSIO_API_KEY}
```

## Usage

### Python API

```python
from composio_wrapper import ComposioWrapper

# Initialize with API key
wrapper = ComposioWrapper(api_key="ak_x3qztZT62u54lI2Lztfs")

# Health check
print(wrapper.health_check())

# List GitHub issues
issues = wrapper.github_list_issues(owner="user", repo="repo", limit=10)
print(issues)

# Create a GitHub issue
result = wrapper.github_create_issue(
    owner="user",
    repo="repo",
    title="Bug found",
    body="Description of the bug"
)

# Read Google Sheet
sheet_data = wrapper.sheets_read(
    spreadsheet_id="abc123",
    range_name="Sheet1!A1:B10"
)

# Write to Google Sheet
wrapper.sheets_write(
    spreadsheet_id="abc123",
    range_name="Sheet1!A1",
    values=[["Name", "Value"], ["Test", 123]]
)

# Send Slack message
wrapper.slack_send_message(
    channel="#general",
    message="Hello from OpenClaw!"
)

# Search web
results = wrapper.search_web("OpenClaw documentation", num_results=5)

# File operations
wrapper.file_write("/tmp/test.txt", "Hello World!")
content = wrapper.file_read("/tmp/test.txt")
files = wrapper.file_list("/tmp")
```

### Available Functions

| Function | Description |
|----------|-------------|
| `github_list_issues(owner, repo, state, limit)` | List repository issues |
| `github_create_issue(owner, repo, title, body)` | Create a new issue |
| `github_list_prs(owner, repo, state)` | List pull requests |
| `github_get_commits(owner, repo, limit)` | Get recent commits |
| `sheets_read(spreadsheet_id, range_name)` | Read sheet data |
| `sheets_write(spreadsheet_id, range_name, values)` | Write to sheet |
| `slack_send_message(channel, message)` | Send Slack message |
| `search_web(query, num_results)` | Web search |
| `search_github(query, limit)` | GitHub search |
| `file_read(file_path)` | Read local file |
| `file_write(file_path, content)` | Write local file |
| `file_list(directory)` | List directory |
| `health_check()` | Check connection |
| `list_available_tools()` | List all tools |

## Directory Structure

```
composio-wrapper-local/
├── SKILL.md           # This documentation
├── README.md          # Quick start guide
├── requirements.txt   # Python dependencies
├── composio_wrapper.py # Main module
├── config/
│   ├── examples.yaml  # Example configurations
│   └── templates.yaml # Template configs
├── examples/
│   ├── github_demo.py  # GitHub examples
│   ├── sheets_demo.py   # Google Sheets examples
│   └── slack_demo.py    # Slack examples
└── tests/
    └── test_wrapper.py # Unit tests
```

## Configuration File Examples

### Basic Configuration (config/examples.yaml)

```yaml
# Composio Wrapper Configuration Examples

# GitHub Settings
github:
  default_owner: "my-org"
  default_repo: "my-repo"
  default_state: "open"
  default_limit: 20

# Google Sheets Settings
sheets:
  default_range: "Sheet1!A:Z"
  batch_size: 100

# Slack Settings
slack:
  default_channel: "#general"
  message_format: "text"

# Search Settings
search:
  default_num_results: 10
  timeout_seconds: 30
```

### Full Configuration (config/templates.yaml)

```yaml
# Full Template Configuration
# Copy to config.yaml and customize

version: "1.0"
settings:
  api_key_env: "COMPOSIO_API_KEY"
  debug: false
  timeout: 60

github:
  enabled: true
  default_owner: ""
  default_repo: ""
  max_results: 100

sheets:
  enabled: true
  default_spreadsheet_id: ""
  default_range: "Sheet1"

slack:
  enabled: true
  default_channel: ""
  mention_users: []

search:
  enabled: true
  default_engine: "web"
  safe_search: true

file_operations:
  enabled: true
  base_directory: "."
  allowed_extensions:
    - ".txt"
    - ".json"
    - ".yaml"
    - ".csv"
```

## Examples

### GitHub Examples (examples/github_demo.py)

```python
"""GitHub Integration Examples"""
from composio_wrapper import ComposioWrapper

wrapper = ComposioWrapper()

# List all open issues
issues = wrapper.github_list_issues(
    owner="my-org",
    repo="my-repo",
    state="open"
)
print(f"Found {len(issues)} open issues")

# Create a new issue
issue = wrapper.github_create_issue(
    owner="my-org",
    repo="my-repo",
    title="New Feature Request",
    body="Please add this feature..."
)
print(f"Created issue: {issue}")

# List pull requests
prs = wrapper.github_list_prs(
    owner="my-org",
    repo="my-repo",
    state="all"
)

# Get recent commits
commits = wrapper.github_get_commits(
    owner="my-org",
    repo="my-repo",
    limit=5
)
```

### Google Sheets Examples (examples/sheets_demo.py)

```python
"""Google Sheets Integration Examples"""
from composio_wrapper import ComposioWrapper

wrapper = ComposioWrapper()

# Read data from a sheet
data = wrapper.sheets_read(
    spreadsheet_id="abc123xyz",
    range_name="Data!A1:D10"
)
print("Sheet data:", data)

# Write data to a sheet
values = [
    ["Name", "Email", "Phone"],
    ["John Doe", "john@example.com", "555-1234"],
    ["Jane Smith", "jane@example.com", "555-5678"]
]
result = wrapper.sheets_write(
    spreadsheet_id="abc123xyz",
    range_name="Contacts!A1",
    values=values
)
print(f"Wrote {result['rows_written']} rows")
```

### Slack Examples (examples/slack_demo.py)

```python
"""Slack Integration Examples"""
from composio_wrapper import ComposioWrapper

wrapper = ComposioWrapper()

# Send a simple message
result = wrapper.slack_send_message(
    channel="#notifications",
    message="🚀 Deployment completed successfully!"
)
print(f"Message sent: {result['success']}")

# Send formatted message
message = """
*Daily Report*
- Tasks completed: 5
- In progress: 3
- Blocked: 1
"""
wrapper.slack_send_message(
    channel="#daily-updates",
    message=message
)
```

## Troubleshooting

### API Key Issues

```bash
# Check if API key is set
echo $COMPOSIO_API_KEY

# Set the API key
export COMPOSIO_API_KEY="ak_x3qztZT62u54lI2Lztfs"
```

### Composio SDK Not Installed

```bash
pip install composio-core
```

### Health Check

Run health check to diagnose issues:

```python
from composio_wrapper import ComposioWrapper

wrapper = ComposioWrapper()
health = wrapper.health_check()
print(health)
```

Expected output for healthy state:
```json
{
  "composio_available": true,
  "api_key_configured": true,
  "client_initialized": true,
  "status": "healthy"
}
```

## API Reference

### ComposioWrapper Class

#### `__init__(self, api_key=None)`

Initialize the wrapper with an optional API key.

#### `health_check(self) -> Dict[str, Any]`

Returns the health status of the wrapper.

#### `list_available_tools(self) -> List[str]`

Returns a list of all available tool functions.

## Contributing

To add new tool integrations:

1. Import the tool from `composio.tools`
2. Create a wrapper method in the `ComposioWrapper` class
3. Add the method to `list_available_tools()`
4. Update documentation

## License

This skill is part of the OpenClaw project.
