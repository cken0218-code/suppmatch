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

### Threads Monitoring
```bash
# 測試 Threads trending 抓取
cd /Users/cken0218/.openclaw/workspace/skills/threads-automation
python3 scripts/fetch-threads-trending.py --output output/

# 分析內容
python3 scripts/analyze-content.py --input output/ --model glm-5

# 查看報告
cat output/$(date +%Y-%m-%d)*.md
```

### MCP (Model Context Protocol)
```bash
# 測試 MCP 連線
cd /Users/cken0218/.openclaw/workspace/skills/mcp-test
python3 test-mcp-connection.py

# 查看日誌
tail -f /tmp/openclaw/mcp-*.log
```

### Skills
```bash
# 清點 skills 數量
ls ~/.openclaw/workspace/skills/ | wc -l

# list所有skills
ls /Users/cken0218/.openclaw/workspace/skills/

# 睇某個skill
ls /Users/cken0218/.openclaw/workspace/skills/[skill-name]/

# ClawHub 已安裝 skills
clawhub list
```

### OpenClaw
```bash
# restart gateway
openclaw gateway restart

# check status
openclaw status

# 查看 quota
cat /Users/cken0218/.openclaw/workspace/memory/quota-state.json
```

## 📁 有用既File

### Memory
- **核心認知**: `/Users/cken0218/.openclaw/workspace/memory/L0-core.md`
- **今日日誌**: `/Users/cken0218/.openclaw/workspace/memory/L1-daily/$(date +%Y-%m-%d).md`
- **昨日日誌**: `/Users/cken0218/.openclaw/workspace/memory/L1-daily/$(date -v-1d +%Y-%m-%d).md`
- **記憶索引**: `/Users/cken0218/.openclaw/workspace/memory/MEMORY.md`

### Reports
- **AI News**: `/Users/cken0218/.openclaw/workspace/skills/ai-news-monitor/daily_report.md`
- **Stock History**: `/Users/cken0218/.openclaw/workspace/skills/aus-stock-tracker/history/`
- **Threads Trending**: `/Users/cken0218/.openclaw/workspace/skills/threads-automation/output/`

### Config
- **OpenClaw Config**: `~/.openclaw/openclaw.json`
- **Quota State**: `memory/quota-state.json`
- **Dashboard**: `http://localhost:8081/`

---
*Updated: 2026-03-10*
