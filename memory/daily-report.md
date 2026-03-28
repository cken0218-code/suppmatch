# Daily AI Report

> 每日自动推送到 Telegram

---

## 设置

### Cron
```
# 每日 9:00 发送 Daily Report
0 9 * * * openclaw trigger heartbeat daily-report
```

### 内容格式

```
🐱 Daily AI Report
━━━━━━━━━━━━━━━━

✅ 完成任務
- prompt optimisation

🔄 進行中
- YouTube automation (80%)

💡 建議
- 可以做 AI 影片系統

📋 Active Tasks
[HIGH] 2 | [MEDIUM] 2 | [LOW] 3
```

---

## 触发方式

1. **Cron 自动** - 每日 9:00
2. **手动** - `/report`

---

## 实现

用 `message` tool 发送到 Telegram：
```python
message(
  channel="telegram",
  action="send",
  target="user:296260245",
  message="🐱 Daily AI Report..."
)
```
