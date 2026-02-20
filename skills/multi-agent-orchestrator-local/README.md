# Multi-Agent Orchestrator Local

## 🎯 快速開始

```bash
# 基本使用 - 描述你的需求
"分析我的 YouTube 數據"
"搜索 AI 工具趨勢"
"創建一個新的 skill"

# 指定 Agent 群組
"@planner 分析頻道"
"@artificer 創建項目"
"@scout 研究市場"
```

## 📦 Agent 群組

| 群組 | 職責 | 關鍵詞 |
|------|------|--------|
| **THE PLANNER** | 增長策略、內容創作 | youtube、分析、收入、內容 |
| **THE ARTIFICER** | 代碼開發、自動化 | 代碼、git、項目、發布 |
| **THE SCOUT** | 研究分析、情報收集 | 研究、搜索、趨勢、數據 |
| **THE INQUISITOR** | 安全審計、系統監控 | 安全、監控、審計、錯誤 |
| **LOGISTICS** | 個人工具、資源管理 | 備份、觸發、token |

## 🔧 複雜任務模式

```bash
# 流水線 (Pipeline)
"用流水線：研究 → 創作 → 發布"

# 並行 (Parallel)  
"並行：搜索 A、搜索 B、搜索 C"

# 辯論 (Debate)
"辯論：YouTube vs B站，哪個更好？"
```

## 📊 成本優化

- **90% 任務** → MiniMax (日常)
- **10% 任務** → GLM-5 (複雜)

## 🔗 整合 Skills

直接調用現有 skills：
- `youtube-analytics-local`
- `content-creator-local`
- `github`
- `skill-scanner`
- `automation-workflows`
- `system-monitor`
- `security-audit`

## 📖 詳細文檔

查看 [SKILL.md](SKILL.md) 獲取完整架構和使用說明。

---

**參考**: SATOSHI'S SQUAD COMMAND 架構
