---
name: cron-manager
description: Cron 任务管理 skill - 管理 OpenClaw 定时任务
version: 1.0.0
author: local
license: MIT
---

# Cron Manager Skill

## 功能
- 管理定时任务
- 监控任务执行状态
- 查看任务日志
- 故障排查

## OpenClaw Cron 命令

### 查看所有任务
```bash
openclaw cron list
openclaw cron list --include-disabled
```

### 添加任务
```bash
# 每日 09:00 执行
openclaw cron add \
  --name "Morning Report" \
  --cron "0 9 * * *" \
  --tz "Asia/Taipei" \
  --session isolated \
  --message "Generate daily report" \
  --announce
```

### 运行任务
```bash
# 立即运行
openclaw cron run <job-id>

# 强制运行
openclaw cron run <job-id> --force
```

### 查看任务历史
```bash
openclaw cron runs <job-id>
```

### 禁用/启用任务
```bash
# 禁用
openclaw cron update <job-id> --disable

# 启用
openclaw cron update <job-id> --enable
```

## 常用 Cron 表达式

```
每分钟: * * * * *
每小时: 0 * * * *
每天 09:00: 0 9 * * *
每天 12:00 & 18:00: 0 12,18 * * *
每周一 09:00: 0 9 * * 1
每月 1 号 00:00: 0 0 1 * *
```

## 故障排查

### 任务未执行
1. 检查任务是否启用
2. 检查 cron 表达式
3. 查看错误日志
4. 检查 Gateway 状态

### 任务执行失败
1. 查看运行历史
2. 检查错误信息
3. 验证任务配置
4. 检查 model 权限

## 最佳实践

✅ 使用有意义的任务名称
✅ 设置适当的超时时间
✅ 配置错误通知
✅ 定期审查任务列表
✅ 测试新任务（先手动运行）

## 监控脚本

检查所有任务状态：
```bash
openclaw cron list --json | jq '.[] | {name, enabled, lastStatus}'
```
