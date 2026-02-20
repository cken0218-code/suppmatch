# AI Trends Research Automation System

## 📁 File Structure

```
~/.openclaw/workspace/
├── scripts/
│   ├── ai-trends-research.sh       # Main research automation script
│   └── setup-research-schedule.sh  # Cron/Launchd setup utility
├── config/
│   ├── research-topics.txt         # Research topics list
│   └── com.openclaw.ai-trends-research.plist  # macOS launchd plist
└── memory/
    └── learning/
        ├── ai-trends/              # Daily research outputs
        │   └── YYYY-MM-DD-research.md
        └── weekly-summary.md       # Weekly aggregated summary
```

## 🚀 Quick Start

### Manual Run
```bash
~/.openclaw/workspace/scripts/ai-trends-research.sh full
```

### Setup Schedule
```bash
# Install cron job (runs daily at 2 AM)
~/.openclaw/workspace/scripts/setup-research-schedule.sh cron

# Check status
~/.openclaw/workspace/scripts/setup-research-schedule.sh status
```

## ⏰ Schedule

**Daily Run**: 02:00 (within 01:00-09:00 window)

## 📋 Research Topics

1. YouTube Automation
2. AI Tools 2026
3. Content Trends
4. Multi-agent Systems
5. Niche Opportunities

## 🔧 Manual Cron Setup (if needed)

```bash
# Add to crontab
echo "0 2 * * * ~/.openclaw/workspace/scripts/ai-trends-research.sh full >> ~/.openclaw/workspace/memory/learning/ai-trends/cron.log 2>&1" | crontab -

# View crontab
crontab -l
```

## 📊 Output

- **Daily Research**: `memory/learning/ai-trends/YYYY-MM-DD-research.md`
- **Weekly Summary**: `memory/learning/weekly-summary.md`
- **Discord DM**: Notifications sent to ken000ken
- **Logs**: `memory/learning/ai-trends/research-YYYY-MM-DD.log`

## 🔄 Workflow

1. **Fetch**: web_search for latest AI trends
2. **Research**: Deep dive into topics
3. **Record**: Save to daily markdown
4. **Analyze**: Extract key insights
5. **Update**: MEMORY.md with long-term insights
6. **Notify**: Discord DM with summary
7. **Summarize**: Weekly aggregation

## 📝 Customize

Edit `~/.openclaw/workspace/config/research-topics.txt` to modify research topics.

---

*System created: 2026-02-20*
