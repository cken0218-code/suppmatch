# Knowledge Base 设计

**目标**: 建立类似 hsiinho 既 Obsidian Vault 系统

---

## 📂 目录结构

```
knowledge-base/
├── core/           # 核心文件 (身份、规则、目标)
├── youtube/       # YouTube 相关
├── stock/         # 股票相关
├── research/     # 研究资料
├── projects/      # 项目文档
└── archive/      # 归档
```

---

## 🎯 每个文件夹用途

### core/
- L0-core.md (核心认知)
- 身份定义
- 规则文件

### youtube/
- 频道分析
- Trending 报告
- 内容创意
- 排程记录

### stock/
- 每日报告
- Signal 记录
- 分析模板

### research/
- Skills 扫描报告
- 趋势分析
- 学习笔记

### projects/
- SuppMatch
- 其他项目

---

## 🔗 Link 规范

使用 Wikilink 格式：
```
[[folder/filename]]
```

例如：
- [[core/L0-core]]
- [[youtube/trending-2026-02]]
- [[stock/signals-cba]]

---

## 🏷️ Tag 规则

| Tag | 用途 | 示例 |
|-----|------|------|
| #ai-editable | AI 可修改 | #ai-editable |
| #important | 重要 | #important |
| #todo | 待办 | #todo |
| #done | 已完成 | #done |
| #research | 研究中 | #research |

---

## 🔧 Git Hooks

### post-commit (可选)
每次 commit 后自动通知

---

## 📝 使用方式

1. 新建笔记 → 放对应文件夹
2. 使用 Wikilink 互相链接
3. 用 tag 标记状态
4. 定期 commit 到 Git

---

## ✅ 与现有系统整合

- **memory/** → 已有的记忆系统
- **knowledge-base/** → 新的结构化知识库
- **skills/** → Agent 技能

---

*最后更新: 2026-02-22*
