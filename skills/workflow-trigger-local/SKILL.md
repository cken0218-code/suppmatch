---
name: workflow-trigger-local
description: 简化的工作流触发器（本地版本，安全替代 n8n-dispatch）
version: 1.0.0
author: local
license: MIT
---

# Workflow Trigger Local - 工作流触发器

## 安全说明
- ✅ 不包含硬编码的外部 API
- ✅ 用户自行配置 endpoint
- ✅ 代码清晰可读
- ✅ 完全本地控制

## 功能
- 触发 N8N 工作流（或其他 webhook）
- 支持 GET/POST 请求
- 支持自定义 payload
- 支持环境变量配置

## 使用方式

### 1. 配置 Webhook Endpoints

在 `~/.openclaw/openclaw.json` 中添加：

```json
{
  "skills": {
    "entries": {
      "workflow-trigger-local": {
        "enabled": true,
        "env": {
          "N8N_WEBHOOK_URL": "https://your-n8n-instance.com/webhook/xxx",
          "SLACK_WEBHOOK_URL": "https://hooks.slack.com/services/xxx"
        }
      }
    }
  }
}
```

### 2. 触发工作流

#### N8N 工作流
```bash
# 简单触发
curl -X POST "$N8N_WEBHOOK_URL"

# 带 payload
curl -X POST "$N8N_WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d '{"action": "generate_report", "data": "..."}'
```

#### Slack 通知
```bash
curl -X POST "$SLACK_WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d '{"text": "任务完成！"}'
```

#### 自定义 Webhook
```bash
# 使用用户提供的 URL
WEBHOOK_URL="https://your-service.com/webhook"
curl -X POST "$WEBHOOK_URL" -d '{"status": "done"}'
```

### 3. 在 Agent 中使用

当用户说：
- "触发 N8N 工作流" → 调用配置的 N8N_WEBHOOK_URL
- "发送 Slack 通知" → 调用配置的 SLACK_WEBHOOK_URL
- "触发自定义 webhook" → 询问用户 URL 并调用

## 配置示例

### N8N 场景
```json
{
  "N8N_WEBHOOK_URL": "https://n8n.example.com/webhook/abc123",
  "N8N_REPORT_WEBHOOK": "https://n8n.example.com/webhook/report",
  "N8N_ALERT_WEBHOOK": "https://n8n.example.com/webhook/alert"
}
```

### 多个工作流
```bash
# 报告工作流
curl -X POST "$N8N_REPORT_WEBHOOK" -d '{"type": "daily"}'

# 警报工作流
curl -X POST "$N8N_ALERT_WEBHOOK" -d '{"level": "high", "message": "..."}'
```

## 安全特性

### ✅ 用户控制
- 所有 webhook URLs 由用户自行配置
- 不硬编码任何外部服务
- 用户可以随时修改或删除配置

### ✅ 本地执行
- 所有请求从本地发起
- 不经过任何中间服务器
- 完全透明，可审查

### ✅ 灵活配置
- 支持多个 webhook endpoints
- 支持不同的 HTTP 方法
- 支持自定义 headers 和 payload

## 使用场景

### 1. 自动化报告
```bash
# 每日报告
curl -X POST "$N8N_WEBHOOK_URL" -d '{"action": "daily_report"}'
```

### 2. 数据同步
```bash
# 同步数据到 N8N
curl -X POST "$N8N_WEBHOOK_URL" -d '{"data": "...", "sync": true}'
```

### 3. 通知提醒
```bash
# 发送通知
curl -X POST "$SLACK_WEBHOOK_URL" -d '{"text": "任务完成"}'
```

## 与 n8n-dispatch 的区别

### n8n-dispatch（不安全）
- ❌ 硬编码外部 API
- ❌ 不透明的转发机制
- ❌ 可能包含恶意代码

### workflow-trigger-local（安全）
- ✅ 用户自行配置所有 endpoints
- ✅ 完全透明的 curl 调用
- ✅ 代码清晰可审查

## 常见工作流模板

### 每日任务
```bash
# 早上 9:00 触发
curl -X POST "$N8N_WEBHOOK_URL" -d '{
  "action": "morning_tasks",
  "time": "09:00"
}'
```

### YouTube Automation
```bash
# 视频上传完成
curl -X POST "$N8N_WEBHOOK_URL" -d '{
  "action": "video_uploaded",
  "video_id": "xxx",
  "title": "..."
}'
```

### 数据分析
```bash
# 触发数据分析工作流
curl -X POST "$N8N_WEBHOOK_URL" -d '{
  "action": "analyze_data",
  "source": "youtube_analytics"
}'
```

## 故障排查

### Webhook 调用失败
```bash
# 测试连接
curl -v "$N8N_WEBHOOK_URL"

# 检查环境变量
echo $N8N_WEBHOOK_URL
```

### 配置未生效
```bash
# 重启 Gateway
openclaw gateway restart

# 检查配置
cat ~/.openclaw/openclaw.json | grep workflow-trigger
```

## 高级用法

### 带认证的 Webhook
```bash
curl -X POST "$WEBHOOK_URL" \
  -H "Authorization: Bearer $API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"data": "..."}'
```

### 批量触发
```bash
# 触发多个工作流
for url in "$WEBHOOK_1" "$WEBHOOK_2" "$WEBHOOK_3"; do
  curl -X POST "$url" &
done
wait
```

---

**安全承诺**:
- ✅ 不包含任何硬编码的外部 API
- ✅ 所有配置由用户控制
- ✅ 完全透明的执行过程
- ✅ 代码清晰可审查

**适用场景**: N8N 工作流、Slack 通知、自定义 webhook、自动化触发器
