# Game Dashboard Skill

A game-like visual dashboard for OpenClaw showing agent status, system health, and activity.

## Overview

This skill creates a web-based dashboard with game-like visuals showing:
- 🤖 Agent status (active/idle/busy)
- 💓 System health (CPU, memory)
- 📝 Activity log
- 🎮 Task queue

## Files

```
game-dashboard/
├── SKILL.md
├── server.py          # Simple HTTP server
├── dashboard.html     # Game-like UI
├── status.json        # Status data file
└── README.md
```

## Usage

### Start Dashboard Server

```bash
python3 /Users/cken0218/.openclaw/workspace/skills/game-dashboard/server.py
```

The dashboard will be available at: `http://localhost:8080`

### Update Agent Status

```bash
# Update a single agent
python3 /Users/cken0218/.openclaw/workspace/skills/game-dashboard/server.py --update agent-1 "coding" "Active"

# Update system health
python3 /Users/cken0218/.openclaw/workspace/skills/game-dashboard/server.py --health 45 72

# Show notification
python3 /Users/cken0218/.openclaw/workspace/skills/game-dashboard/server.py --notify "Task completed!"
```

### Open in Browser

```bash
open http://localhost:8080
```

## Integration with OpenClaw

Add to your workflow:

```
1. Create a skill command that calls this dashboard
2. Use cron to update status periodically
3. Show notifications for important events
```

## Features

- 🎨 Pixel-art style UI
- 🔄 Auto-refresh every 5 seconds
- 📊 Visual health bars
- 🔔 Notification popups
- 📜 Activity log

---
*Created: 2026-02-21*
