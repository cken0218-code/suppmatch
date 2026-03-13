# 品控机制 - Quality Control System

> **Created**: 2026-03-13
> **Version**: 1.0

---

## 🎯 核心理念

每个 Agent 完成任务后，**必须**输出固定格式报告到 `memory/reports/`，Ken (Main) 每日审阅一次。

---

## 📋 报告格式标准

### 通用格式（所有 Agents）

```markdown
# [Agent Name] Report - YYYY-MM-DD HH:MM

## 📊 任务概览
- 总任务: X
- 完成: X
- 失败: X
- 完成率: XX%

## ✅ 完成的任务
1. **[任务 1]** - ✅ 完成
   - 输出: [文件路径]
   - 用时: XX 秒

2. **[任务 2]** - ✅ 完成
   - 输出: [文件路径]
   - 用时: XX 秒

## ❌ 失败的任务
- [如果有]

## 💡 发现和洞察
- [洞察 1]
- [洞察 2]

## 🎯 下一步
- [ ] [任务 1]
- [ ] [任务 2]

---
**Agent**: [Agent Name]
**Model**: [GLM-5 / MiniMax]
**Duration**: XX minutes
**Report ID**: [AGENT]-YYYYMMDD-HHMM
```

---

## 📊 报告分类

### Level 1: 任务报告（Task Reports）
- **频率**: 每次任务完成后
- **内容**: 单个任务详情
- **位置**: `memory/reports/[agent]-task-[ID].md`

### Level 2: 日报（Daily Reports）
- **频率**: 每日 20:00
- **内容**: 当日所有任务汇总
- **位置**: `memory/reports/[agent]-YYYY-MM-DD.md`

### Level 3: 周报（Weekly Reports）
- **频率**: 每周日 20:00
- **内容**: 本周所有 agents 汇总
- **位置**: `memory/reports/weekly-YYYY-WXX.md`

### Level 4: 月报（Monthly Reports）
- **频率**: 每月 1 号 09:00
- **内容**: 上月所有 agents 汇总
- **位置**: `memory/reports/monthly-YYYY-MM.md`

---

## 🔍 Ken (Main) 审阅流程

### 每日审阅（20:00）

1. **检查所有 agents 日报**
   ```bash
   # 读取今日所有报告
   ls memory/reports/*-$(date +%Y-%m-%d).md
   ```

2. **QA Agent 评分**
   - QA Agent 会自动审阅所有报告
   - 给出评分（A/B/C/D/F）

3. **异常处理**
   - 如果评分 < C → 立即修正
   - 如果错误率 > 10% → 通知用户

4. **记录到 L1-daily**
   ```markdown
   # 2026-03-13 每日日志

   ## 📊 今日报告
   - YouTube Agent: A (92/100)
   - Newsletter Agent: B (85/100)
   - Stock Agent: A (95/100)
   - 平均分: 91/100 ✅
   ```

---

## 📝 报告模板（按 Agent）

### YouTube Agent
```markdown
# YouTube Agent Report - YYYY-MM-DD

## 📊 本周数据
- Trending 扫描: X 次
- 腚本生成: X 条
- 发布视频: X 条

## 📺 内容表现
| 视频 | 观看 | 点赞 | 评论 | CTR |
|------|------|------|------|-----|
| [视频 1] | XXX | XX | X | X.X% |

## 💡 发现
- [洞察]

## 🎯 下周计划
- [ ] [任务]
```

### Newsletter Agent
```markdown
# Newsletter Agent Report - YYYY-MM-DD

## 📧 Issue 信息
- Issue #: XXX
- Subject: [标题]
- Published: YYYY-MM-DD HH:MM

## 📊 数据
- Subscribers: XXX
- Open Rate: XX%
- Click Rate: XX%

## 💡 发现
- [洞察]
```

### Stock Agent
```markdown
# Stock Agent Report - YYYY-MM-DD

## 📈 市场概览
- ASX 200: [涨/跌] X.XX%
- 扫描股票: XX 只
- 信号: X BUY / X HOLD / X SELL

## 🔥 顶级机会
1. [股票]: RSI XX, ADX XX
2. [股票]: RSI XX, ADX XX

## ⚠️ 警报
- [如果有]
```

---

## ✅ 品控检查清单

### 自动检查（QA Agent）
- [ ] 报告格式正确
- [ ] 数据准确性
- [ ] 时间戳有效
- [ ] 文件路径正确
- [ ] 无拼写错误

### 手动检查（Ken Main）
- [ ] 内容质量
- [ ] 洞察价值
- [ ] 下一步可行性
- [ ] 与战略一致性

---

## 🚨 异常处理

### 评分 < C（需要修正）
1. QA Agent 标记问题
2. 通知相关 Agent
3. Agent 重新执行任务
4. QA Agent 重新评分

### 错误率 > 10%（需要通知）
1. 立即通知用户
2. 提供错误详情
3. 建议解决方案
4. 等待用户决策

---

## 📊 成功指标

| 指标 | 目标 | 当前 |
|------|------|------|
| 报告完成率 | 100% | - |
| 平均评分 | > B (85) | - |
| 错误率 | < 5% | - |
| Ken 审阅时间 | < 10 分钟 | - |

---

## 🔗 相关文件

- 报告目录：`memory/reports/`
- 错误记录：`memory/errors/`
- QA 报告：`memory/reports/qa-*.md`
- 每日日志：`memory/L1-daily/*.md`

---

**Created by**: Ken AI Assistant
**Date**: 2026-03-13
**Status**: Active
