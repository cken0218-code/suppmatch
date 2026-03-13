# Operations Agent - 运营管理

## 用途
管理日常任务调度（cron jobs），执行 heartbeat，监控系统状态（Gateway、Discord），追踪错误。

## 触发条件
- Cron 定时触发（09:00, 12:00, 15:00, 18:00, 20:00）
- 系统异常
- Gateway 重启

## 使用方式

### 1. Heartbeat 执行
```bash
# 手动触发 heartbeat
python3 scripts/run-heartbeat.py

# 自动触发（cron）
# 0 9,12,15,18,20 * * * cd ~/.openclaw/workspace && python3 skills/operations-agent/scripts/run-heartbeat.py
```

### 2. 系统监控
```bash
# 检查系统状态
python3 scripts/check-system.py

# 输出位置
# memory/reports/operations-YYYY-MM-DD.md
```

### 3. 错误追踪
```bash
# 提取今日错误
python3 scripts/extract-errors.py

# 输出位置
# memory/errors/YYYY-MM-DD.md
```

## 范例

**Heartbeat 触发（09:00）**：

**Operations Agent**：
1. 检查 Gateway 状态
2. 执行早市扫描（Stock + Crypto）
3. 检查 email/calendar
4. 发送报告给 Ken (Main)

## 报告格式

```markdown
# Operations Report - YYYY-MM-DD

## 📊 系统状态
- Gateway: ✅ Running
- Discord: ✅ Connected
- Telegram: ✅ Connected
- Uptime: XX hours

## ⏰ Heartbeat 执行
| 时间 | 任务 | 状态 |
|------|------|------|
| 09:00 | 早市扫描 | ✅ |
| 12:00 | Trending 扫描 | ✅ |
| 15:00 | 学习任务 | ✅ |
| 18:00 | Trending 扫描 | ✅ |
| 20:00 | 错误追踪 | ✅ |

## ❌ 错误记录
- 总数: X
- 严重: X
- 轻微: X

## 📅 Cron 任务
| 任务 | 计划 | 状态 | 下次运行 |
|------|------|------|----------|
| 早市扫描 | 09:00 | ✅ | 明日 09:00 |
| Trending | 12:00, 18:00 | ✅ | 今日 18:00 |
| [其他] | - | - | - |

## 💡 发现
- [洞察 1]
- [洞察 2]
```

## Heartbeat 任务表

| 时间 | 任务 | 负责人 |
|------|------|--------|
| 08:30 | 早市扫描（Crypto） | Crypto Agent |
| 09:00 | 早市报告（Stock） | Stock Agent |
| 12:00 | Trending 扫描 | YouTube Agent |
| 15:00 | 学习任务 | Research Agent |
| 18:00 | Trending 扫描 | YouTube Agent |
| 20:00 | 错误追踪 | Operations Agent |

## 相关文件
- 报告：`memory/reports/operations-*.md`
- 错误记录：`memory/errors/*.md`
- Heartbeat 配置：`HEARTBEAT.md`

## 模型
- **日常任务**：MiniMax

## 状态
- ✅ 基本框架完成
- ✅ Cron jobs 已配置
