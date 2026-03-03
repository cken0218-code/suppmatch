# OpenClaw Multi-Agent Demo

## 呢个系最简单嘅 Multi-Agent 示范

**运作方式：**
1. Main Agent (我) 分配任务
2. Sub-Agent 1: Researcher
3. Sub-Agent 2: Writer
4. Main Agent 整合结果

**即刻试：**
---

## Demo 1: 两步流水线

**Step 1:** Research Agent 搵料
**Step 2:** Writer Agent 写文

### Example Task:
"帮我搵 2026 年 3 个最 hot 嘅 AI agent framework，然后用广东话写一个 IG 贴文介绍"

**Multi-Agent 流程：**
```
Main Agent
    ↓
Spawn Research Agent (task: 搵 frameworks)
    ↓
等 research 完成
    ↓
Spawn Writer Agent (task: 写 IG 贴文)
    ↓
整合结果 → 回复用户
```

---

## Demo 2: 并行执行

**同时跑多个 agents：**
- Agent A: 搵 GitHub trending
- Agent B: 搵 X trending
- Agent C: 搵 Product Hunt

**然后整合所有结果**

---

## 想试边个？

1. **两步流水线** - 简单，易理解
2. **并行执行** - 快，但复杂啲

---

## 同 CrewAI 嘅分别

| OpenClaw Subagent | CrewAI |
|-------------------|--------|
| 即刻用到 | 要配置 LLM |
| 用现有 model | 可以自定义 model |
| 简单直接 | 功能更强大 |
| 适合快速 demo | 适合生产环境 |

---

*Created: 2026-02-25*
