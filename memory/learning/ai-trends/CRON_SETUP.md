# AI Trends Research Automation - Cron Setup

## Quick Setup

```bash
# Method 1: Using the setup script
~/.openclaw/workspace/scripts/setup-research-schedule.sh cron

# Method 2: Direct crontab
echo "0 2 * * * ~/.openclaw/workspace/scripts/ai-trends-research.sh full >> ~/.openclaw/workspace/memory/learning/ai-trends/cron.log 2>&1" | crontab -

# Method 3: Manual edit
crontab -e
# Add: 0 2 * * * ~/.openclaw/workspace/scripts/ai-trends-research.sh full >> ~/.openclaw/workspace/memory/learning/ai-trends/cron.log 2>&1
```

## Cron Service Status (macOS)

```bash
# Check if cron is running
sudo cron status

# Start cron if needed
sudo cron start

# Enable cron on boot
sudo launchctl enable system/cron
sudo launchctl start system/cron
```

## Schedule Details

- **Time**: 02:00 daily (within 01:00-09:00 window)
- **Output**: `memory/learning/ai-trends/cron.log`

## Verify Installation

```bash
crontab -l | grep ai-trends
```

---
*Generated: 2026-02-20*
