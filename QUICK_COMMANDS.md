# OpenClaw Command Center

快速命令列表，等你起身可以用。

## 🚀 常用命令

### Game Dashboard
```bash
# 睇dashboard
open http://localhost:8081/

# 更新狀態
python3 /Users/cken0218/.openclaw/workspace/skills/game-dashboard/server.py --update agent-1 "working" "Task name"
python3 /Users/cken0218/.openclaw/workspace/skills/game-dashboard/server.py --notify "Message"
python3 /Users/cken0218/.openclaw/workspace/skills/game-dashboard/server.py --health 30 45
```

### AI News
```bash
# 生成daily report
python3 /Users/cken0218/.openclaw/workspace/skills/ai-news-monitor/monitor.py
```

### Stocks
```bash
# 澳洲股票report
python3 /Users/cken0218/.openclaw/workspace/skills/aus-stock-tracker/stock-tracker.py --aus --report

# save history
python3 /Users/cken0218/.openclaw/workspace/skills/aus-stock-tracker/stock-tracker.py --aus --save
```

### Skills
```bash
# list所有skills
ls /Users/cken0218/.openclaw/workspace/skills/

# 睇某個skill
ls /Users/cken0218/.openclaw/workspace/skills/[skill-name]/
```

### OpenClaw
```bash
# restart gateway
openclaw gateway restart

# check status
openclaw status
```

## 📁 有用既File

- Memory: `/Users/cken0218/.openclaw/workspace/memory/2026-02-21.md`
- Daily Report: `/Users/cken0218/.openclaw/workspace/skills/ai-news-monitor/daily_report.md`
- Dashboard: `http://localhost:8081/`

---
*Updated: 2026-02-21*
