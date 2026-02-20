# Multi-Agent Orchestrator (Local)

本地化多代理編排系統 - 參考 SATOSHI'S SQUAD COMMAND 架構

## 架構總覽

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    [ THE ORCHESTRATOR - 本地智能調度中心 ]                  ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐             ║
║  │  [ PLANNER ]    │ │ [ ARTIFICER ]   │ │    [ SCOUT ]    │             ║
║  │  策略與增長     │ │  編碼與製作     │ │   研究與情報    │             ║
║  ├─────────────────┤ ├─────────────────┤ ├─────────────────┤             ║
║  │ • youtube-     │ │ • github        │ │ • ddg-web-     │             ║
║  │   analytics    │ │ • git-automation│ │   search       │             ║
║  │ • income-      │ │ • app-scaffold  │ │ • skill-       │             ║
║  │   tracker      │ │ • video-script  │ │   scanner      │             ║
║  │ • content-     │ │ • thumbnail     │ │ • data-        │             ║
║  │   creator      │ │                 │ │   analyzer     │             ║
║  └─────────────────┘ └─────────────────┘ └─────────────────┘             ║
║                                                                           ║
║  ┌─────────────────┐ ┌─────────────────┐                               ║
║  │ [ INQUISITOR ]  │ │  [ LOGISTICS ]  │                               ║
║  │  安全與系統     │ │   個人工具      │                               ║
║  ├─────────────────┤ ├─────────────────┤                               ║
║  │ • security-     │ │ • cron-manager  │                               ║
║  │   audit         │ │ • backup-      │                               ║
║  │ • api-security  │ │   manager      │                               ║
║  │ • system-      │ │ • workflow-    │                               ║
║  │   monitor      │ │   trigger      │                               ║
║  └─────────────────┘ └─────────────────┘                               ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

## 五大支柱 (PILLARS)

### 1. [ PLANNER ] - 策略與增長引擎
**職責**: 分析、規劃、優化 ROI

| Agent | 功能 | 用途 |
|-------|------|------|
| `youtube-analytics` | YouTube 數據分析 | 追蹤觀看、訂閱、收益 |
| `income-tracker` | 多渠道收入管理 | 追蹤各平台收入 |
| `content-creator` | 內容創作助手 | 標題、描述、標籤生成 |

### 2. [ ARTIFICER ] - 編碼與製作工坊
**職責**: 開發、製作、自動化輸出

| Agent | 功能 | 用途 |
|-------|------|------|
| `github` | GitHub 操作 | PR、Issues、Actions |
| `git-automation` | Git 自動化 | commit、push、merge |
| `app-scaffold-local` | 應用腳手架 | 快速建立專案 |
| `video-script-writer` | 影片腳本生成 | AI 腳本創作 |
| `thumbnail-generator` | 縮圖文案 | 吸引點擊 |

### 3. [ SCOUT ] - 研究與情報中心
**職責**: 搜尋、掃描、分析

| Agent | 功能 | 用途 |
|-------|------|------|
| `ddg-web-search` | DuckDuckGo 搜尋 | 無 API key 網頁搜尋 |
| `skill-scanner` | Skills 掃描 | 發現新工具 |
| `data-analyzer` | 數據分析 | CSV/Excel 分析 |

### 4. [ INQUISITOR ] - 安全與系統守護者
**職責**: 審計、安全、監控

| Agent | 功能 | 用途 |
|-------|------|------|
| `security-audit` | 安全審計 | 系統風險評估 |
| `api-security-check` | API 安全檢查 | 敏感信息洩露 |
| `system-monitor` | 系統監控 | CPU/記憶體/磁碟 |

### 5. [ LOGISTICS ] - 個人效率工具箱
**職責**: 調度、備份、自動化

| Agent | 功能 | 用途 |
|-------|------|------|
| `cron-manager` | Cron 任務管理 | 定時任務調度 |
| `backup-manager` | 備份管理 | 配置與資料備份 |
| `workflow-trigger` | 工作流觸發 | 簡化自動化流程 |

## 使用場景

### 場景 1: YouTube 影片發布流程
```
PLANNER (youtube-analytics) → 分析上次影片表現
  ↓
ARTIFICER (video-script-writer) → 撰寫新腳本
  ↓
ARTIFICER (thumbnail-generator) → 生成縮圖
  ↓
ARTIFICER (github) → commit 到 repo
  ↓
LOGISTICS (workflow-trigger) → 觸發發布流程
  ↓
PLANNER (income-tracker) → 追蹤新收益
```

### 場景 2: 市場研究與內容策略
```
SCOUT (ddg-web-search) → 搜尋 trending topics
  ↓
SCOUT (skill-scanner) → 發現新工具/技術
  ↓
SCOUT (data-analyzer) → 分析數據趨勢
  ↓
PLANNER (content-creator) → 生成內容計劃
  ↓
LOGISTICS (cron-manager) → 設定定期監控
```

### 場景 3: 系統維護與安全審計
```
INQUISITOR (system-monitor) → 檢查系統狀態
  ↓
INQUISITOR (security-audit) → 安全審計
  ↓
INQUISITOR (api-security-check) → API 安全檢查
  ↓
LOGISTICS (backup-manager) → 自動備份
  ↓
LOGISTICS (cron-manager) → 設定定期維護
```

## 快速開始

### 基本查詢
```bash
# 查詢 YouTube 數據
youtube-analytics --channel=your-channel

# 追蹤收入
income-tracker --report=monthly

# 搜尋資訊
ddg-web-search --query="AI trends 2026"
```

### 組合工作流
```bash
# 研究 → 創作 → 發布
research_and_publish --topic="AI automation"

# 安全審計
full-audit --include-api --include-system
```

## 調度邏輯

### 任務分類算法

```
IF 任務 contains ["youtube", "view", "subscribe", "revenue"] THEN
    ROUTE TO PLANNER
ELSE IF 任務 contains ["code", "git", "script", "build", "create"] THEN
    ROUTE TO ARTIFICER
ELSE IF 任務 contains ["search", "scan", "analyze", "research"] THEN
    ROUTE TO SCOUT
ELSE IF 任務 contains ["security", "audit", "risk", "monitor"] THEN
    ROUTE TO INQUISITOR
ELSE IF 任務 contains ["schedule", "backup", "workflow", "trigger"] THEN
    ROUTE TO LOGISTICS
END
```

### 優先級處理

| 優先級 | 場景 | 處理方式 |
|--------|------|----------|
| 🔴 URGENT | 系統錯誤、安全漏洞 | 立即通知 + 執行修復 |
| 🟡 HIGH | 高價值任務 | 優先調度 + 詳細報告 |
| 🟢 NORMAL | 日常任務 | 標準隊列處理 |
| ⚪ LOW | 背景維護 | 批量處理 + 低資源 |

## 配置

### 環境變數

```bash
# OpenClaw 配置
export ORCHESTRATOR_DEFAULT_MODEL="zai/glm-5"
export ORCHESTRATOR_ENABLE_LOGGING=true
export ORCHESTRATOR_LOG_LEVEL="info"
```

### 自定義路由

在 `~/.openclaw/orchestrator/config.yaml` 中配置：

```yaml
routing:
  custom_rules:
    - pattern: ".*youtube.*"
      target: PLANNER
      priority: HIGH
    - pattern: ".*security.*"
      target: INQUISITOR
      priority: URGENT

agents:
  youtube-analytics:
    enabled: true
    timeout: 60s
  security-audit:
    enabled: true
    timeout: 120s
```

## 最佳實踐

### ✅ 推薦

- 使用明確的任務描述以獲得準確路由
- 定期執行安全審計
- 保持 cron 任務簡單明確
- 使用 backup-manager 定期備份

### ⚠️ 避免

- 避免在同一個對話中混合完全無關的任務
- 避免設置過長的超時時間
- 避免忽略安全警告

## 擴展指南

### 添加新 Agent

1. 在對應 PILLAR 下添加配置
2. 更新路由算法
3. 添加使用文檔
4. 測試整合

### 自定義工作流

```yaml
workflows:
  my_custom_flow:
    steps:
      - agent: ddg-web-search
        input: "{query}"
      - agent: data-analyzer
        input: "{results}"
      - agent: content-creator
        input: "{analysis}"
```

## 故障排除

### 常見問題

| 問題 | 解決方案 |
|------|----------|
| Agent 無響應 | 檢查 cron 狀態、重新啟動 |
| 路由錯誤 | 檢查任務關鍵詞配置 |
| 數據錯誤 | 執行 data-analyzer 驗證 |

### 調試模式

```bash
# 啟用詳細日誌
export ORCHESTRATOR_LOG_LEVEL=debug

# 測試路由
orchestrator-diagnose --task="your task here"
```

## 版本歷史

- **v1.0.0** (2026-02-19): 初始版本，基於 SATOSHI'S SQUAD COMMAND 架構本地化

## 授權

MIT License - 完全本地化，無外部依賴
