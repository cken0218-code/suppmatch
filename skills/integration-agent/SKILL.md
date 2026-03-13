# Integration Agent - 整合协调

## 用途
协调 agent 之间沟通，验证 handoff 格式，管理数据流，处理 API 整合。

## 触发条件
- Agent 任务交接
- 数据同步需求
- API 调用失败

## 使用方式

### 1. 协调 Agent 交接
```bash
# 验证 handoff 格式
python3 scripts/validate-handoff.py --from [agent1] --to [agent2]

# 输出位置
# memory/handoffs/[agent1]-to-[agent2]-YYYYMMDD-HHMM.md
```

### 2. 数据同步
```bash
# 同步数据
python3 scripts/sync-data.py --source [source] --target [target]

# 输出位置
# data/sync-log-YYYY-MM-DD.md
```

### 3. API 监控
```bash
# 检查 API 状态
python3 scripts/check-apis.py

# 输出位置
# memory/reports/integration-YYYY-MM-DD.md
```

## 范例

**YouTube Agent 完成腚本**：
- 需要交给 Affiliate Agent 加 affiliate links

**Integration Agent**：
1. 验证腚本格式
2. 创建 handoff 文件
3. 通知 Affiliate Agent
4. 追踪交接状态

## 报告格式

```markdown
# Integration Report - YYYY-MM-DD

## 🔗 交接记录
| From | To | 任务 | 状态 | 时间 |
|------|-----|------|------|------|
| YouTube | Affiliate | 加 links | ✅ | HH:MM |
| Stock | Ken | 每日报告 | ✅ | 09:00 |

## 📊 API 状态
| API | 状态 | 响应时间 | 错误数 |
|-----|------|----------|--------|
| Brave | ✅ | 120ms | 0 |
| CoinGecko | ✅ | 85ms | 0 |
| [其他] | ⚠️ | 500ms | 2 |

## ❌ 失败交接
- [如果有]

## 💡 优化建议
- [建议 1]
- [建议 2]
```

## Handoff 格式

```markdown
# Handoff: [Agent1] → [Agent2]

## 📋 任务描述
- 任务: [描述]
- 优先级: [High/Medium/Low]
- 截止时间: YYYY-MM-DD HH:MM

## 📦 交付物
- [文件 1]: [路径]
- [文件 2]: [路径]

## ✅ 验收标准
- [ ] [标准 1]
- [ ] [标准 2]

## 💬 备注
- [额外信息]
```

## 相关文件
- 交接记录：`memory/handoffs/`
- API 日志：`data/api-log-*.md`
- 报告：`memory/reports/integration-*.md`

## 模型
- **协调**：MiniMax

## 状态
- ✅ 基本框架完成
- ⏳ 自动化协调开发中
