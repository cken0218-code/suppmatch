# 🎮 OpenClaw Game Dashboard

A game-like visual dashboard for monitoring your AI agents.

![Dashboard Preview](https://via.placeholder.com/600x400?text=OpenClaw+Dashboard)

## Quick Start

### 1. Start the Dashboard

```bash
cd /Users/cken0218/.openclaw/workspace/skills/game-dashboard
python3 server.py
```

### 2. Open in Browser

```
http://localhost:8080
```

## Commands

### Update Agent Status

```bash
# Update a specific agent
python3 server.py --update agent-1 "coding" "Writing code"

# Available agents: agent-1, agent-2, agent-3, agent-4
```

### Update System Health

```bash
python3 server.py --health 45 72
# Format: --health CPU MEMORY
```

### Send Notification

```bash
python3 server.py --notify "Task completed!"
```

## Features

- 🎨 Pixel-art inspired UI with retro gaming feel
- 🤖 Real-time agent status monitoring
- 💓 CPU/Memory health bars
- 📜 Activity log with timestamps
- 🔔 Desktop notifications
- 🔄 Auto-refresh every 5 seconds

## Integration with OpenClaw

### Method 1: Cron Job

Add to your cron to update periodically:

```bash
# Every 5 minutes, update agent status
*/5 * * * * cd /Users/cken0218/.openclaw/workspace/skills/game-dashboard && python3 server.py --update agent-1 "monitoring" "Checking system"
```

### Method 2: OpenClaw Skill

Create a skill that calls the dashboard:

```python
# In your skill
import subprocess
import json

def update_dashboard(agent_id, status, task):
    subprocess.run([
        'python3', 
        '/Users/cken0218/.openclaw/workspace/skills/game-dashboard/server.py',
        '--update', agent_id, status, task
    ])
```

### Method 3: REST API

Send POST request to update:

```bash
curl -X POST http://localhost:8080/api/update \
  -H "Content-Type: application/json" \
  -d '{"agent_id": "agent-1", "status": "active", "task": "Processing"}'
```

## File Structure

```
game-dashboard/
├── SKILL.md          # This file
├── server.py         # HTTP server + CLI
├── dashboard.html    # Frontend UI
├── status.json       # Status data (auto-generated)
└── README.md         # Setup guide
```

## Customization

### Change Agents

Edit `server.py` and modify `default_status['agents']`:

```python
default_status = {
    "agents": [
        {"id": "my-agent", "name": "My Custom Agent", "status": "idle", "task": "Waiting"},
        ...
    ],
    ...
}
```

### Change Port

Edit `PORT = 8080` in `server.py`

---

**Enjoy your game-like dashboard!** 🎮

*Built for OpenClaw*
