# Multi-Agent Orchestrator - 快速參考卡

## 🎯 五層架構

```
╔═══════════════════════════════════════════════════════╗
║  PLANNER      │  策略與增長  │ youtube/income/content ║
║  ARTIFICER    │  編碼與製作  │ github/git/script     ║
║  SCOUT        │  研究與情報  │ search/scan/analyze   ║
║  INQUISITOR   │  安全與系統  │ audit/api/monitor     ║
║  LOGISTICS    │  個人工具    │ cron/backup/workflow  ║
╚═══════════════════════════════════════════════════════╝
```

## 🚀 快速命令

| 任務 | 命令 |
|------|------|
| 查看狀態 | `orchestrator status` |
| YouTube 分析 | `orchestrator planner:yt-analytics` |
| 收入追蹤 | `orchestrator planner:income` |
| 內容創作 | `orchestrator planner:content` |
| GitHub 操作 | `orchestrator artifactory:github` |
| 網頁搜尋 | `orchestrator scout:search --query="..."` |
| 安全審計 | `orchestrator audit full` |
| 研究流程 | `orchestrator research "topic"` |
| 發布影片 | `orchestrator publish video` |

## 📋 完整命令列表

### PLANNER (策略與增長)
```bash
orchestrator planner:yt-analytics      # YouTube 數據分析
orchestrator planner:income            # 收入追蹤
orchestrator planner:content           # 內容創作
```

### ARTIFICER (編碼與製作)
```bash
orchestrator artifactory:github        # GitHub CLI
orchestrator artifactory:git          # Git 自動化
orchestrator artifactory:scaffold     # 應用腳手架
orchestrator artifactory:script       # 影片腳本
orchestrator artifactory:thumbnail    # 縮圖生成
```

### SCOUT (研究與情報)
```bash
orchestrator scout:search --query=    # DuckDuckGo 搜尋
orchestrator scout:scan               # Skills 掃描
orchestrator scout:analyze            # 數據分析
```

### INQUISITOR (安全與系統)
```bash
orchestrator inquisitor:audit         # 安全審計
orchestrator inquisitor:api           # API 安全
orchestrator inquisitor:monitor       # 系統監控
```

### LOGISTICS (個人工具)
```bash
orchestrator logistics:cron           # Cron 管理
orchestrator logistics:backup         # 備份管理
orchestrator logistics:workflow      # 工作流觸發
```

## 🔀 組合命令

```bash
# 研究 → 分析 → 創作
orchestrator research "AI trends 2026"

# 腳本 → 縮圖 → 發布
orchestrator publish video

# 完整安全審計
orchestrator audit full
```

## 📊 任務分類關鍵詞

| PILLAR | 關鍵詞 |
|--------|--------|
| PLANNER | youtube, view, subscribe, revenue, income, content, strategy, growth |
| ARTIFICER | code, git, script, build, create, scaffold, thumbnail, github |
| SCOUT | search, scan, analyze, research, trend, find, discover |
| INQUISITOR | security, audit, risk, monitor, api, system, health |
| LOGISTICS | schedule, backup, workflow, trigger, cron, timer |

## 🛠️ 故障排除

| 問題 | 解決方案 |
|------|----------|
| 命令未找到 | 確認 `orchestrator.sh` 在 PATH 中 |
| Agent 無響應 | 檢查對應 skill 是否安裝 |
| 權限錯誤 | 確認腳本有執行權限 (`chmod +x`) |

## 📁 文件結構

```
multi-agent-orchestrator-local/
├── SKILL.md              # 完整文檔
├── orchestrator.sh       # CLI 入口
├── config.sh             # 配置檔案
├── README_QUICK.md       # 快速參考
└── examples/
    ├── research_flow.sh
    ├── publish_flow.sh
    └── audit_flow.sh
```

## 🔗 相關 Skills

- **PLANNER**: youtube-analytics-local, income-tracker-local, content-creator-local
- **ARTIFICER**: github, git-automation, app-scaffold-local, video-script-writer-local
- **SCOUT**: ddg-web-search, skill-scanner, data-analyzer-local
- **INQUISITOR**: security-audit, api-security-check, system-monitor
- **LOGISTICS**: cron-manager, backup-manager, workflow-trigger-local

---
*最後更新: 2026-02-19*
