# Newsletter Agent - Beehiiv 管理

## 用途
管理 Beehiiv newsletter，包括内容生成、发布、subscriber 追踪和数据分析。

## 触发条件
- 每周五 10:00 发布（cron）
- Subscriber 里程碑（100, 500, 1000）
- Open rate < 20% 警报
- 用户要求「发布 newsletter」

## 使用方式

### 1. 创建新 Issue
```bash
# 生成 Issue 内容
python3 scripts/generate-issue.py --week $(date +%V)

# 输出位置
# newsletter/issue-XXX-YYYY-MM-DD.md
```

### 2. 发布到 Beehiiv
```bash
# 手动发布
python3 scripts/publish-newsletter.py --issue XXX

# 自动发布（cron）
# 0 10 * * 5 cd ~/.openclaw/workspace && python3 skills/newsletter-agent/scripts/publish-newsletter.py
```

### 3. 追踪数据
```bash
# 获取 subscriber 数据
python3 scripts/fetch-metrics.py

# 输出位置
# memory/reports/newsletter-YYYY-MM-DD.md
```

## 范例

**用户**：「发布今周的 newsletter」

**Newsletter Agent**：
1. 搜集本周内容（trending + 学习 + 机会）
2. 生成 Issue 内容
3. 发布到 Beehiiv
4. 追踪 open rate / click rate
5. 输出报告到 `memory/reports/newsletter-YYYY-MM-DD.md`

## 报告格式

```markdown
# Newsletter Report - YYYY-MM-DD

## 📊 本周数据
- Subscribers: XXX
- Open Rate: XX%
- Click Rate: XX%
- Unsubscribes: X

## 📧 Issue 内容
- Subject: [标题]
- Published: YYYY-MM-DD HH:MM
- Content Length: XXX words

## 💡 发现
- [洞察 1]
- [洞察 2]

## 🎯 下周计划
- [ ] [任务 1]
- [ ] [任务 2]
```

## 相关文件
- Newsletter 内容：`newsletter/issue-*.md`
- 报告：`memory/reports/newsletter-*.md`
- 设置指南：`newsletter/beehiiv-setup-guide.md`

## 模型
- **内容生成**：GLM-5
- **数据分析**：MiniMax

## 依赖
- Beehiiv API key（需要配置）
- Brave Search API（用于内容搜集）

## 状态
- ✅ Issue #1 已准备（2026-03-13）
- ⏳ 自动化脚本开发中
