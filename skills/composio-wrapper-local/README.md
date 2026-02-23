# Composio Wrapper Local Skill

A unified local skill for OpenClaw that provides access to Composio's 1000+ toolkits.

## Quick Setup

```bash
cd ~/.openclaw/workspace/skills/composio-wrapper-local
pip install -r requirements.txt
```

## Set API Key

```bash
export COMPOSIO_API_KEY="ak_x3qztZT62u54lI2Lztfs"
```

## Quick Usage

```python
from composio_wrapper import ComposioWrapper

# Initialize
wrapper = ComposioWrapper()

# Check health
print(wrapper.health_check())

# Use tools
issues = wrapper.github_list_issues(owner="user", repo="repo")
wrapper.slack_send_message(channel="#general", message="Hello!")
wrapper.sheets_read(spreadsheet_id="abc", range_name="Sheet1!A1")
```

## Files

- `composio_wrapper.py` - Main module
- `SKILL.md` - Full documentation
- `README.md` - This file
- `requirements.txt` - Dependencies
- `config/` - Configuration examples
- `examples/` - Usage examples

## Documentation

See [SKILL.md](SKILL.md) for complete documentation.
