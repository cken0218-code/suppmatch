# ClawHub Skills 建议 — 2026-03-13 Week 11

> **Created**: 2026-03-13 13:50
> **Frequency**: 每周五
> **Next Scan**: 2026-03-20

---

## 🎯 本周发现的 3 个有用 Skills

### 🥇 Skill 1: self-improving-agent

**名称**: `self-improving-agent`
**来源**: ClawHub (pskoett)
**类型**: 自我改进系统

**用途**：
- 捕获学习、错误和修正
- 实现持续改进
- 自动记录用户纠正

**触发条件**：
- 命令或操作意外失败时
- 用户纠正时（"No, that's wrong...", "Actually..."）
- 发现优化机会时

**为什么建议安装**：
1. **补充史莱姆系统**
   - 史莱姆系统：技能演化
   - self-improving-agent：错误学习
   - 两者互补

2. **自动记录错误**
   - 不需要手动记录到 `memory/errors/`
   - 自动捕获用户反馈
   - 避免重复犯错

3. **持续改进**
   - 每次对话都在学习
   - 不会重复相同错误
   - 提升用户体验

**预期效果**：
- 错误率降低 30-50%
- 用户纠正减少
- 自主学习能力增强

**安装命令**：
```bash
clawhub install self-improving-agent
```

**风险评估**：🟢 低风险
- 只读记录，不修改系统
- 可随时卸载

---

### 🥈 Skill 2: Veryfi Skill

**名称**: `veryfi`
**来源**: ClawHub (Veryfi)
**类型**: OCR + 收据处理
**发布日期**: 2026-03-02（非常新！）

**用途**：
- OCR 识别（收据、发票、文档）
- 自动提取结构化数据
- 支持多种文档类型

**为什么建议安装**：
1. **收入追踪自动化**
   - 自动处理收入收据
   - 提取金额、日期、来源
   - 简化 `income-tracker-local` skill

2. **投资文档处理**
   - 处理股票交易确认单
   - 提取交易数据
   - 自动记录到投资系统

3. **成本管理**
   - 追踪业务支出
   - 自动分类
   - 简化报税

**预期效果**：
- 手动数据输入减少 80%
- 收入追踪自动化
- 报税准备简化

**安装命令**：
```bash
clawhub install veryfi
```

**风险评估**：🟡 中风险
- 需要 Veryfi API key（免费层可用）
- 处理敏感财务数据
- 建议先测试

**替代方案**：
- 如果担心隐私，可以用本地 OCR（Tesseract）
- 或者继续手动输入

---

### 🥉 Skill 3: Agent Orchestrator

**名称**: `agent-orchestrator`
**来源**: ClawHub (aatmaan1)
**类型**: 多 agent 编排

**用途**：
- 元 agent 技能
- 分解复杂任务为子任务
- 生成专门的 sub-agents
- 协调多个 agents 工作

**为什么建议安装**：
1. **增强 Multi-Agent 系统**
   - 已有：multi-agent-collaboration skill
   - Agent Orchestrator：更智能的编排
   - 自动生成 sub-agent SKILL.md

2. **复杂任务自动化**
   - 例如："制作一个 YouTube 视频"
     - Sub-agent 1: 研究 trending
     - Sub-agent 2: 写脚本
     - Sub-agent 3: 生成语音
     - Sub-agent 4: 剪辑视频

3. **动态技能生成**
   - 根据任务自动创建临时 skills
   - 任务完成后可删除
   - 灵活性极高

**预期效果**：
- 复杂任务处理能力 +3 倍
- 自动化程度提升
- 减少人工干预

**安装命令**：
```bash
clawhub install agent-orchestrator
```

**风险评估**：🟡 中风险
- 需要较强系统资源
- 可能与现有 multi-agent 系统冲突
- 建议先测试再全面使用

**何时使用**：
- 复杂多步骤任务
- 需要动态生成 agents
- 现有 skills 无法覆盖的场景

---

## 📊 Skills 对比

| Skill | 优先级 | 风险 | 预期收益 | 与现有系统整合 |
|-------|--------|------|----------|----------------|
| self-improving-agent | 🟢 最高 | 低 | 错误率 -30-50% | 补充史莱姆系统 |
| Veryfi | 🟡 中 | 中 | 数据输入 -80% | 收入追踪自动化 |
| Agent Orchestrator | 🟡 中 | 中 | 复杂任务 +3倍 | 增强多 agent 系统 |

---

## 🎯 安装建议

### 立即安装（本周）
**self-improving-agent**
- **原因**：零风险，直接受益
- **整合**：与史莱姆系统互补
- **时间**：5 分钟安装 + 测试

### 观察后安装（1-2 周）
**Veryfi**
- **原因**：需要 API key，涉及隐私
- **准备**：注册 Veryfi 免费账户
- **测试**：先处理非敏感文档

### 等待时机安装
**Agent Orchestrator**
- **原因**：可能与现有系统冲突
- **条件**：当现有 multi-agent 不够用时
- **测试**：在隔离环境先测试

---

## 🔍 其他发现的 Skills（不推荐现在安装）

### Capability Evolver
**用途**: AI agents 自我进化引擎
**不推荐原因**: 
- 与史莱姆系统功能重叠
- 更复杂，可能冲突
- 先完善史莱姆系统

### Clawdr
**用途**: 约会 app 自动化
**不推荐原因**: 
- 与工作目标无关
- 潜在道德问题
- 不适合企业使用

---

## 📅 下次扫描（2026-03-20）

**扫描重点**：
1. 搜索 "ClawHub new skills March 2026"
2. 检查已安装 skills 的更新
3. 寻找 YouTube automation 相关 skills
4. 寻找 Newsletter 相关 skills

**追踪已建议 skills**：
- [ ] self-improving-agent：是否安装？
- [ ] Veryfi：是否注册 API？
- [ ] Agent Orchestrator：是否需要？

---

## 💡 安装决策流程

```
收到建议
    ↓
评估风险（低/中/高）
    ↓
低风险 → 立即安装
中风险 → 观察 1-2 周
高风险 → 暂不安装
    ↓
安装后测试
    ↓
记录效果
```

---

## 📝 安装后追踪

如果安装任何 skill，记录到：
- `memory/skills-ecosystem.md`（更新列表）
- `memory/L1-daily/YYYY-MM-DD.md`（记录安装）
- `skills/skill-genome.json`（史莱姆系统记录）

---

## 🔗 相关资源

### ClawHub 官网
- https://www.clawhub.com
- 搜索 skills
- 查看文档

### 学习资源
- "How to Use ClawHub" (xCloud, 2026-03-12)
- "7 Essential OpenClaw Skills" (KDnuggets, 2026-03-03)
- "Best ClawHub Skills Guide" (DataCamp, 2026-03)

---

**Created by**: Ken AI Assistant
**Date**: 2026-03-13 13:50
**Status**: 3 skills 建议，等待用户决定
**Next Scan**: 2026-03-20（每周五）
