# MEMORY.md - 索引

> **Last Updated**: 2026-02-23
> **⚠️ NOTE**: 此文件只做索引，详细内容在子文件中

---

## 基本信息

- **名**: shikiouo
- **时区**: Asia/Taipei
- **语言**: 繁体中文
- **习惯**: 夜瞓（晏啲先搵佢）

---

## 📂 记忆系统索引

```
memory/
├── L0-core.md              # 核心认知 ⭐
├── L1-daily/               # 每日日志
├── L2-weekly/              # 週摘要
├── L3-monthly/             # 月摘要
├── learning/               # 学习记录
│   ├── ai-trends-2026-02.md
│   ├── mcp-research-2026-02.md
│   └── threads-multi-agent-2026-02.md
├── projects/               # 项目细节
│   └── aus-stock-tracker.md
├── skills-ecosystem.md     # Skills 生态
└── openclaw-practices.md   # OpenClaw 实践
```

---

## 🎯 主要项目

### YouTube Automation ✅
- 高潜力 niches：Tech/AI ($35-45 CPM)
- 详细：`memory/learning/ai-trends-2026-02.md`

### 澳股分析工具 ✅
- 13 隻股票 + 5 个技术指标
- 详细：`memory/projects/aus-stock-tracker.md`

### Local Business Automation
- $300-500/month/client（最易入门）

---

## 🤖 Models 配置

| Model | Provider | 用途 |
|-------|----------|------|
| GLM-5 | Zai | 复杂任务 |
| MiniMax-M2.5 | MiniMax | 日常对话 |

**详细规则**: 见 AGENTS.md

---

## ⏰ 待办 / 目标（含 deadline）

### 高優先級
- [ ] **MCP 整合 Phase 1-4** - Deadline: 2026-04-01（22日）- Agent: multi-agent-collaboration
  - Phase 1 (3月11-17日): GitHub MCP Server ✅
  - Phase 2 (3月18-24日): Discord MCP Server
  - Phase 3 (3月25-31日): N8N MCP Server
  - Phase 4 (4月1日): 完整系統整合
  - **詳細計劃**: `memory/projects/mcp-integration.md`

- [ ] Xiaohongshu trending 監控 - Deadline: 2026-03-15（5日）- Agent: research-agent

- [ ] 史萊姆技能進化系統 - Deadline: 2026-03-20（10日）- Agent: skill-creator

### 已完成 ✅
- [x] Threads trending 監控 - Deadline: 2026-03-10 ✅ **已完成** (2026-03-10 23:24)
- [x] Email SMTP Setup - Deadline: 2026-03-05 ✅ **已完成** (2026-03-10 23:46)

---

## 📊 重要决定索引

| 日期 | 决定 | 详细 |
|------|------|------|
| 2026-02-20 | 澳股工具上线 | `memory/projects/aus-stock-tracker.md` |
| 2026-02-20 | AI Trends 分析 | `memory/learning/ai-trends-2026-02.md` |
| 2026-02-20 | MCP 研究 | `memory/learning/mcp-research-2026-02.md` |
| 2026-02-22 | Threads 学习 | `memory/learning/threads-multi-agent-2026-02.md` |
| 2026-02-23 | AGENTS.md v2.0 | 新增 TOC、Debug 节 |

---

## 🦞 Skills 生态

**總數**: 59 個（workspace/skills/）
**ClawHub 已安裝**: 15 個
**詳細**: `memory/skills-ecosystem.md`

### ClawHub 已安裝 Skills（15個）
1. github (1.0.0)
2. agent-audit (1.0.0)
3. openclaw-token-save (1.0.0)
4. ddg-web-search (1.0.0)
5. automation-workflows (0.1.0)
6. xiaohongshu (1.0.1)
7. daily-trending (1.0.0)
8. productivity (1.0.3)
9. github-ai-trends (1.1.0)
10. ai-automation-workflows (0.1.5)
11. news-aggregator-skill (0.1.0)
12. x-post-automation (1.0.0)
13. coingecko (1.0.0)
14. memory-manager (1.0.0)
15. memoclaw (1.15.0)

---

## 📋 OpenClaw 实践

**详细**: `memory/openclaw-practices.md`

---

## 🔐 API Keys

**加密位置**: `~/.openclaw/secrets.gpg`（已加密）

**解密方式**:
```bash
gpg -d ~/.openclaw/secrets.gpg > /tmp/secrets.json
# 用完记得删除：rm /tmp/secrets.json
```

**包含的 Keys**:
- YouTube Data API ✅
- Brave Search ✅
- X (Twitter) API ✅
- MiniMax API ✅
- Composio ✅

**⚠️ 注意**: 原始 openclaw.json 仍保留明文配置，敏感 key 已移至加密檔

---

## 📅 每周报告

- 2026-W8: `memory/weekly-summary-2026-W8.md`

---

*此文件保持简洁（<3KB），详细内容在子文件中*
