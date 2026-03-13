# Skill 推荐系统 - Skill Recommendation System

> **Created**: 2026-03-13 19:18
> **Last Updated**: 2026-03-13 19:18
> **Purpose**: 根据用户习惯推荐 Skills，主动发现有用工具

---

## 🎯 系统目标

1. **分析用户习惯** - 从 `memory/user-patterns.md` 提取使用模式
2. **匹配 ClawHub Skills** - 根据模式推荐相关 skills
3. **主动提案** - 不需要用户询问，自动推荐

---

## 📊 推荐算法

### Step 1: 分析用户习惯

**数据来源**: `memory/user-patterns.md`

**提取信息**：
- 常用任务（按频率）
- 兴趣领域
- 反馈历史
- 错误类型

### Step 2: 匹配 ClawHub Skills

**匹配规则**：
```
如果 用户常用任务 == "YouTube 内容创作"
    推荐: video-editing, thumbnail-generator, youtube-seo

如果 用户常用任务 == "投资分析"
    推荐: stock-analyzer, crypto-tracker, market-sentiment

如果 用户常用任务 == "Newsletter"
    推荐: email-automation, content-curator, rss-aggregator
```

### Step 3: 评估推荐

**评分标准**：
- **相关性**: 与用户任务的匹配度（0-100）
- **实用性**: 实际带来的价值（0-100）
- **风险**: 安装风险（低/中/高）
- **成本**: 是否免费

**推荐优先级**：
```
优先级 = (相关性 + 实用性) / 2 - 风险系数
```

---

## 📋 当前推荐（基于用户习惯）

### 高优先级推荐

#### 1. video-editing ⭐⭐⭐
**相关性**: 95%（用户常用 YouTube 内容创作）
**用途**: 自动视频编辑、剪辑、字幕
**风险**: 🟢 低
**来源**: ClawHub (video-tools)
**安装**: `clawhub install video-editing`

---

#### 2. email-automation ⭐⭐⭐
**相关性**: 90%（用户常用 Newsletter）
**用途**: Email 自动化、定时发送、A/B testing
**风险**: 🟢 低
**来源**: ClawHub (email-tools)
**安装**: `clawhub install email-automation`

---

#### 3. content-curator ⭐⭐
**相关性**: 85%（用户常用内容创作）
**用途**: 自动收集内容、摘要生成
**风险**: 🟢 低
**来源**: ClawHub (content-tools)
**安装**: `clawhub install content-curator`

---

### 中优先级推荐

#### 4. market-sentiment ⭐⭐
**相关性**: 80%（用户常用投资分析）
**用途**: 市场情绪分析、新闻聚合
**风险**: 🟡 中（需要 API key）
**来源**: ClawHub (finance-tools)
**安装**: `clawhub install market-sentiment`

---

#### 5. workflow-automation ⭐⭐
**相关性**: 75%（用户喜欢自动化）
**用途**: 工作流自动化、任务调度
**风险**: 🟢 低
**来源**: ClawHub (automation-tools)
**安装**: `clawhub install workflow-automation`

---

## 🔄 自动化流程

### 每周推荐（周五 13:50）

**触发条件**: Heartbeat（每周五）
**流程**：
1. 读取 `memory/user-patterns.md`
2. 分析常用任务
3. 搜索 ClawHub 相关 skills
4. 生成推荐列表
5. 保存到 `memory/skill-recommendations-YYYY-WXX.md`
6. 通知用户

**输出格式**：
```markdown
# Skill 推荐 — 2026-WXX

## 🎯 本周推荐（基于你的使用习惯）

### 🥇 高优先级
1. **video-editing** - 自动视频编辑
   - 相关性: 95%
   - 原因: 你常用 YouTube 内容创作
   - 安装: `clawhub install video-editing`

2. **email-automation** - Email 自动化
   - 相关性: 90%
   - 原因: 你常用 Newsletter
   - 安装: `clawhub install email-automation`

## 💡 为什么推荐？
- 基于你过去 7 天的使用模式
- 优先选择低风险、高价值的 skills
- 符合你的三大主力方向

## 🎯 安装建议
- 立即安装: video-editing, email-automation
- 观察后安装: market-sentiment
```

---

## 📊 推荐历史

### 2026-W11 (Mar 10-16)

**已推荐**：
1. ✅ self-improving-agent（已安装）
2. ⏳ video-editing（待决定）
3. ⏳ email-automation（待决定）

---

## 💡 智能推荐规则

### 规则 1: 频率匹配
```
如果 用户任务频率 > 每周 3 次
    推荐优先级 +20%
```

### 规则 2: 反馈加权
```
如果 用户之前给正面反馈
    同类 skills 推荐优先级 +30%
```

### 规则 3: 风险过滤
```
如果 风险 == 高
    推荐优先级 -50%
```

### 规则 4: 成本优化
```
如果 免费
    推荐优先级 +10%
```

---

## 🎯 下次推荐时间

**下次推荐**: 2026-03-20 13:50（下周五）
**基于数据**: 2026-03-13 to 2026-03-20

---

## 📝 待办

- [ ] 研究 ClawHub API（自动搜索 skills）
- [ ] 实现推荐算法（Python 脚本）
- [ ] 创建自动化 cron job
- [ ] 测试推荐准确性

---

**Created by**: Ken AI Assistant
**Date**: 2026-03-13 19:18
**Status**: System Designed
**Next Recommendation**: 2026-03-20 13:50
