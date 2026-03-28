# 🏢 Agents - Multi-Agent 系统

> **位置**: `agents/`

---

## Agent 列表

| Agent | Model | 职责 |
|-------|-------|------|
| **Commander** | GLM-5 | 解析命令、建立任务、派发工作 |
| **Planner** | GLM-5 | 任务拆解、workflow 设计 |
| **Builder** | GLM-5 | 写程式、debug、系统架构 |
| **Content** | MiniMax | 小红书、YouTube script、社媒 |
| **Research** | MiniMax | 信息搜集、research、趋势 |
| **Reviewer** | MiniMax | 质量检查、审核、review |

---

## 执行流程

```
User → Commander → Planner → Workers → Reviewer → Commander → User
```

---

## 调用方式

```python
sessions_spawn(runtime="subagent", task="...", label="commander/planner/builder/content/research/reviewer")
```
