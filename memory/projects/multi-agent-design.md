# Multi-Agent 分工设计方案

**目标**: 将单一 main agent 拆分为多个专业 agent

---

## 建议架构

### 1️⃣ Main Agent (Ken)
- **职责**: 对外通信、统筹协调、记忆管理
- **模型**: MiniMax (日常) / GLM-5 (复杂决策)
- **位置**: Discord / 直接对话

### 2️⃣ YouTube Agent 📺
- **职责**: 
  - Trending content 监控
  - 内容创作协助
  - 标题/描述生成
  - 发布排程
- **模型**: MiniMax-M2.5
- **触发**: YouTube 相关任务

### 3️⃣ Stock Agent 💰
- **职责**:
  - 澳洲股票每日报告
  - Signal 分析
  - 历史数据追踪
- **模型**: MiniMax-M2.5
- **cron**: 每日 09:00

### 4️⃣ Research Agent 📚
- **职责**:
  - Skills 扫描
  - 趋势分析
  - 学习新概念
- **模型**: GLM-5 (需要推理)
- **cron**: 每日 12:00 / 18:00

---

## 实现方式

### Option A: Subagents (简单)
- 用 `sessions_spawn` 创建 subagents
- Main agent 派任务
- 适合：cron jobs、后台任务

### Option B: 多 Channel (推荐)
- 每个 agent 有独立 Discord channel
- Main agent 统筹
- 适合：需要清晰分工

### Option C: Skills 分离
- 用现有 skill 系统
- 不同 skill 处理不同领域
- 适合：渐进式迁移

---

## 下一步

1. ✅ 确定架构 (呢份文档)
2. ✅ 决定实现方式 (Skills 分离)
3. ✅ 创建 YouTube Agent skill
4. ✅ 创建 Stock Agent skill
5. ⏳ 创建 Research Agent skill
6. ⏳ 配置 cron jobs

---

## 待讨论

1. 你想用边种方式实现？ ✅ 已决定: Skills 分离
2. 要唔要即刻开始整 YouTube Agent？ ✅ 已完成!
