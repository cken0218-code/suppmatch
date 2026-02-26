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

- [ ] Xiaohongshu trending 监控 - Deadline: 2026-03-15 - Agent: research-agent
- [ ] Threads trending 监控 - Deadline: 2026-03-10 - Agent: threads-automation
- [ ] Email SMTP Setup - Deadline: 2026-03-05 - 等待：Gmail App Password
- [ ] MCP 整合 Phase 1-4 - Deadline: 2026-04-01 - Agent: multi-agent-collaboration
- [ ] 史莱姆技能进化系统 - Deadline: 2026-03-20 - Agent: skill-creator

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

**已安装**: 13 个
**详细**: `memory/skills-ecosystem.md`

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
