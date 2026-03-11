# Money Ideas Hourly - 每小时赚钱 Idea

## 用途
每小时自动发送 1 个适合用户嘅赚钱 idea 到 Telegram

## 触发条件
- Cron job 每小时触发
- 只在活跃时段（08:00-23:00）发送

## 用户画像
- 📍 香港
- 💬 唔想沟通（内容创作）
- 🆕 新手
- 💰 预算 $0-300 HKD

## Idea 库

### Easy（新手友好）
1. **AI 热点废片**（$0, $300-900/月）
2. **小红书 AI 工具**（$0, $1500-3000/月）
3. **香港餐厅废片**（$0, $500-1000/月）
4. **AI 股市分析**（$0, $600-1500/月）
5. **AI 小说生成**（$0, $200-800/月）

### Medium（要学习）
6. **Seedance 2.0 AI 剧**（$100-450, $500-2000/月）
7. **香港 WhatsApp Bot**（$0-200, $2000-5000/月）
8. **小红书香港生活**（$0, $1000-3000/月）

### Advanced（高回报）
9. **YouTube Automation 系统**（$200-500, $2000-5000/月）
10. **Multi-Agent 赚钱系统**（$300-800, $3000-8000/月）

## 执行步骤

### 1. 检查时间
```python
current_hour = datetime.now().hour
if 8 <= current_hour <= 23:
    send_idea()
```

### 2. 获取下一个 idea
- 读取 `memory/money-ideas-state.json`
- 获取 `current_idea_id`
- 下一个 id = current_id + 1
- 如果超过 10，循环到 1

### 3. 格式化消息
使用模板：
```
💰 **赚钱 Idea #{id}**: {name}

📊 **基本信息**
• 类型: {type}
• 启动成本: {cost}
• 风险: {risk}

💵 **预期收入**
• 首月: {month1}
• 3 个月: {month3}
• 6 个月: {month6}

🎯 **执行步骤**
{steps}

🤖 **我帮你做**
{ai_help}

👤 **你要做**
{user_work}
```

### 4. 发送到 Telegram
```python
message(
    action="send",
    channel="telegram",
    target="296260245",
    message=formatted_message
)
```

### 5. 更新状态
```python
state = {
    "current_idea_id": next_id,
    "last_sent": datetime.now().isoformat()
}
write to memory/money-ideas-state.json
```

## Cron 设置

```bash
# 每小时发送（08:00-23:00）
0 8-23 * * * openclaw cron run --skill money-ideas-hourly
```

## 状态文件

`memory/money-ideas-state.json`:
```json
{
  "current_idea_id": 1,
  "last_sent": "2026-03-07T01:40:00+08:00",
  "total_sent": 1
}
```

## 注意事项
- 深夜（00:00-07:59）唔发送
- 如果用户话「停止」，立即停止 cron
- 如果用户对某个 idea 感兴趣，可以提供详细执行计划

## 示例输出

**Idea #1**:
```
💰 **赚钱 Idea #1**: AI 热点废片（YouTube）

📊 **基本信息**
• 类型: 废片
• 启动成本: $0 HKD
• 风险: 低

💵 **预期收入**
• 首月: $0-100 HKD
• 3 个月: $300-900 HKD
• 6 个月: $600-1500 HKD

🤖 **我帮你做**
全自动化：扫 trending、写脚本、配音、剪片

👤 **你要做**
Upload 视频（2 分钟）
```
