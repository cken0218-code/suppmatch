# MCP (Model Context Protocol) 研究

> **Date**: 2026-02-20
> **Complete Report**: `memory/learning/mcp-research-2026-02-20.md` (~80 pages)

---

## 核心結論

**MCP 已經成為 AI 工具整合的事實標準**

- ✅ **全面採用**: OpenAI、Google、Microsoft、AWS 全都支持
- 📈 **快速增長**: 註冊伺服器近 2000 個（9 個月增長 407%）
- 🏢 **企業驗證**: Block (Square) 報告 50-75% 時間節省
- 🔄 **生態成熟**: 多 SDK、多語言、多雲端支援

---

## MCP 是什麼？

**AI 的 USB-C** — 統一標準讓任何 AI 可以連接任何工具/數據源

- **解決問題**: 打破 AI 與數據的隔閡
- **核心能力**: Resources（資源）+ Tools（工具）+ Prompts（提示範本）
- **架構**: Client-Server 模式，JSON-RPC 2.0 通訊

---

## 主要玩家

| 公司 | 角色 | MCP 應用 |
|------|------|----------|
| Anthropic | 創建者 | Claude 深度整合 |
| OpenAI | 支援者 | ChatGPT 整合 |
| Google | 支援者 | Gemini, Google Cloud |
| Microsoft | 支援者 | Azure, Semantic Kernel |
| AWS | 支援者 | Bedrock, Quick Suite |
| Block | 早期採用者 | Goose agent（數千員工使用） |

---

## OpenClaw 整合機會

### 高優先級
1. **File System MCP** — 讓 agent 讀寫 workspace 檔案
2. **Git MCP** — 版本控制操作
3. **Web Fetch MCP** — 研究/數據收集能力
4. **Shell/Command MCP** — 系統命令執行

### 整合方式
- Skills 可以包裝成 MCP Servers
- 外部 MCP Servers 可以被 OpenClaw agents 使用
- 實現跨 agent 的 context 共享

---

## 安全考量

### ⚠️ 已知風險
- Prompt injection 通過工具描述
- Tool poisoning（工具描述被篡改）
- 憑證外洩風險

### ✅ 緩解措施
- 伺服器 allowlisting
- 用戶 consent flows
- OAuth 憑證管理
- 監控與日誌記錄

---

## 行動項目

1. [ ] **Phase 1 (Week 1-2)**: 建立 MCP SDK 基礎設施
2. [ ] **Phase 2 (Week 3-4)**: 整合外部 MCP Servers
3. [ ] **Phase 3 (Week 5-6)**: 實現 agent context 共享
4. [ ] **Phase 4 (Week 7-8)**: 安全審計與文檔

---

## 相關資源

- [MCP 官網](https://modelcontextprotocol.io)
- [GitHub](https://github.com/modelcontextprotocol)
- [Block 案例研究](https://block.github.io/goose/blog/2025/04/21/mcp-in-enterprise/)

---
*Last updated: 2026-02-20*
