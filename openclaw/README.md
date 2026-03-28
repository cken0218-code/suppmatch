# OpenClaw System

> 完整既 AI Agent 系统架构

---

## 📂 结构

```
openclaw/
├── agents/           # Agent 定义
│   ├── commander.md  # AI CEO
│   ├── planner.md   # Strategy
│   ├── research.md  # Research
│   ├── builder.md   # Developer
│   ├── content.md   # Content
│   └── reviewer.md  # QA
│
├── memory/          # 记忆系统
│   ├── tasks.md     # 任务清单
│   ├── knowledge/   # 知识库
│   ├── daily/       # 每日日志
│   └── weekly/     # 週摘要
│
├── workflow/        # 工作流程
│   ├── youtube.md
│   ├── xiaohongshu.md
│   └── ig.md
│
├── prompts/         # Prompt 库
│   ├── content_prompt.md
│   └── research_prompt.md
│
├── logs/           # 日志
└── reports/        # 报告
```

---

## 🔄 执行流程

```
User → Commander → Planner → Research/Builder/Content → Reviewer → Memory → User
```

---

## 📋 Commands

| 命令 | 功能 |
|------|------|
| /task | 创建任务 |
| /tasks | 列出任务 |
| /work | 执行任务 |
| /report | 生成报告 |
