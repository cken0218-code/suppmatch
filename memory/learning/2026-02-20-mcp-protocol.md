# 2026-02-20 自主學習 - MCP Protocol

## 搜尋主題
MCP (Model Context Protocol) 2026 AI agents

---

## 重點筆記

### 1. MCP 咩黎㗎？
- Anthropic 2024年11月提出既 open standard
- 目的：連接 AI assistants 到數據系統（content repositories, business tools, dev environments）
- 解決：信息孤島同 legacy systems 問題

### 2. 2026 最新發展

| 公司/組織 | MCP 應用 | 意義 |
|----------|----------|------|
| **Google** | Gemini Ecosystem MCP support | 大廠正式 adopt |
| **Amazon** | Amazon Advertising MCP Server (open beta) | 廣告自動化、AI agents 直接操作廣告 |
| **CharmHealth** | MCP Server for EHR | 醫療數據整合、AI 直接讀取病歷 |
| **Linux Foundation** | Anthropic 捐贈 MCP 俾基金會 | 成為業界標準 |

### 3. 關鍵洞察

> "Amazon's MCP server allows LLMs like Gemini, ChatGPT, or Claude to speak 'Amazon Ads' fluently via a universal translation layer"

- **統一翻譯層**：唔洗為每個 action 整 custom API
- **大型企業 adopt**：Amazon、Google 呢啲大廠都用緊
- **安全標準**：Coalition for Secure AI 出咗 taxonomy

### 4. 對我地項目既影響

- **multi-agent-orchestrator** 可以考慮用 MCP 標準黎連接各類 tools
- **YouTube Automation**：如果有 MCP server，可以直接 access YouTube Analytics API
- **趨勢**：MCP 正在成為 AI agents 既 "USB-C port" - 統一連接標準

---

## 行動建議
- [ ] 關注 MCP SDK for Python/Node.js
- [ ] 留意有冇 YouTube/Google MCP servers
- [ ] 考虑将 MCP 集成到本地 automation skills

## 來源
- Wikipedia, HitConsultant, Oasis-Open, W Media Research, Hallam Agency
