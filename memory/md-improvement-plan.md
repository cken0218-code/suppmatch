# MD 改进计划 — 2026-03-13

> **Created**: 2026-03-13 18:38
> **Priority**: 🟡 Medium
> **Goal**: 根据用户使用情况优化 MD 文件

---

## 📊 当前问题分析

### 问题 1：MD 文件太多、太长

**现状**：
- AGENTS.md: 966 行（太大）
- L0-core.md: 170 行（还好）
- SOUL.md: 61 行（还好）
- USER.md: 62 行（还好）
- HEARTBEAT.md: 211 行（太大）
- TOOLS.md: 227 行（太大）

**影响**：
- 每次启动读取大量内容
- Token 消耗高
- 可能截断
- 重复信息多

---

### 问题 2：启动时必读文件太多

**现状**：
```
1. memory/L0-core.md
2. memory/L1-daily/今天.md
3. memory/L1-daily/昨日.md
4. SOUL.md
5. USER.md
```

**影响**：
- 5 个文件，- 可能超过 context window
- 如果某个文件很大，会导致截断

---

### 问题 3：信息重复

**现状**：
- Multi-Agent 架构在 L0-core.md 和 AGENTS.md 都有
- Model 切换规则在 AGENTS.md 有
- 品控机制在 AGENTS.md 和 memory/qc-mechanism.md 都有
- Skills 位置在多个文件重复列出

**影响**：
- 维护困难
- 更新时容易遗漏
- 信息冗余

---

### 问题 4：缺少关键信息

**现状**：
- ❌ 没有记录用户常用任务
- ❌ 没有记录用户习惯模式
- ❌ 没有记录用户反馈历史
- ❌ 没有记录错误学习

**影响**：
- 每次启动都要重新学习
- 重复犯错
- 无法持续改进

---

## 🎯 改进建议

### 建议 1：精简 AGENTS.md（优先级：⭐⭐⭐）

**目标**：966 行 → 300 行（减少 69%）

**方法**：
1. **删除重复内容**：
   - Multi-Agent 架构（移到 L0-core.md）
   - 品控机制（移到 memory/qc-mechanism.md）
   - Handoff 系统（移到 memory/handoff-template.md）
   
2. **保留核心**：
   - Every Session
   - Model 切换规则
   - 三大主力方向
   - Safety
   - External vs Internal
   - 自主解决原则

3. **使用链接代替重复**：
   ```markdown
   详见：memory/ai-company-architecture.md
   ```

**预期效果**：
- ✅ 减少 69% 内容
- ✅ 加快启动速度
- ✅ 减少 token 消耗

---

### 建议 2：优化启动时必读（优先级：⭐⭐⭐）

**目标**：5 个文件 → 2 个文件

**方法**：
1. **合并 L0-core.md + SOUL.md + USER.md**：
   - 创建 `memory/identity-compact.md`
   - 包含：身份 + 灵魂 + 用户偏好
   - 100 行以内

2. **保留 L1-daily（当日 + 昨日）**：
   - 继续读取
   - 保持最新信息

**预期效果**：
- ✅ 减少 60% 启动文件
- ✅ 避免 context window 截断
- ✅ 保留最新日志

---

### 建议 3：创建用户习惯记录（优先级：⭐⭐）

**目标**：记录用户使用模式，  改进系统

**方法**：
1. **创建 `memory/user-patterns.md`**：
   ```markdown
   # 用户习惯记录
   
   ## 常用任务（按频率排序）
   1. YouTube 内容创作（每周 2-3 次）
   2. 投资分析（每日）
   3. Newsletter 发布（每周）
   4. Skills 扫描（每周）
   
   ## 反馈历史
   - 2026-03-13: 建议用 GLM-5 做 primary（采纳）
   - 2026-03-13: 建议简化 AGENTS.md（待采纳）
   
   ## 错误学习
   - 2026-03-13: API fail → 切换到 MiniMax-M2.1
   ```

2. **每次 heartbeat 更新**

**预期效果**：
- ✅ 持续学习用户偏好
- ✅ 避免重复犯错
- ✅ 改进系统

---

### 建议 4：拆分大文件（优先级：⭐）

**目标**：HEARTBEAT.md, TOOLS.md 太长

**方法**：
1. **HEARTBEAT.md**（211 行）：
   - 保留核心规则（50 行）
   - 详细任务移到 `memory/heartbeat-tasks.md`

2. **TOOLS.md**（227 行）：
   - 保留核心信息（50 行）
   - 详细配置移到 `memory/tools-detail.md`

**预期效果**：
- ✅ 减少 76% 内容
- ✅ 加快启动速度
- ✅ 保留详细信息

---

## 📊 改进优先级

| 建议 | 优先级 | 效果 | 工作量 |
|------|--------|------|--------|
| 精简 AGENTS.md | ⭐⭐⭐ | 减少 69% 内容 | 30 分钟 |
| 优化启动时必读 | ⭐⭐⭐ | 减少 60% 启动文件 | 20 分钟 |
| 创建用户习惯记录 | ⭐⭐ | 持续改进 | 15 分钟 |
| 拆分大文件 | ⭐ | 减少 76% 内容 | 25 分钟 |

---

## 🚀 推荐执行顺序

### Phase 1：核心改进（立即执行）
1. ✅ 精简 AGENTS.md（966 → 300 行）
2. ✅ 创建 `memory/identity-compact.md`
3. ✅ 更新启动时必读（5 → 2 个文件）

### Phase 2：持续改进（本周内）
1. ✅ 创建 `memory/user-patterns.md`
2. ✅ 开始记录用户反馈

### Phase 3：长期优化（下周）
1. ⏳ 拆分 HEARTBEAT.md
2. ⏳ 拆分 TOOLS.md

---

## 💡 预期整体效果

| 指标 | 现在 | 改进后 | 提升 |
|------|------|--------|------|
| **启动时间** | ~5 秒 | ~2 秒 | 60% ↓ |
| **Token 消耗（启动）** | ~3k tokens | ~1k tokens | 67% ↓ |
| **Context window 使用** | ~20% | ~10% | 50% ↓ |
| **维护难度** | 高 | 中 | - |
| **信息重复** | 多 | 少 | 70% ↓ |

---

## 🎯 下一步行动

**需要你决定**：
1. **立即执行 Phase 1**？（精简 AGENTS.md + 优化启动）
2. **全部执行**？（Phase 1-3）
3. **其他建议**？

**🐱 等你决定！**

---

**Created by**: Ken AI Assistant
**Date**: 2026-03-13 18:38
**Status**: Waiting for user approval
