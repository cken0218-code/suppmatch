---
name: token-maximizer
description: Token 最大化利用系统 - 在重置前自动用完剩余 Token
version: 1.0.0
author: local
license: MIT
---

# Token Maximizer - Token 最大化利用系统

## 功能
- 监测 Token 使用情况
- 在 Token 重置前 1 小时自动执行高消耗任务
- 最大化 Token 利用率

## 当前 Token 信息
- **Plan**: 每 5 小时重置
- **当前剩余**: 96% (4h 16m 后重置)
- **下次重置**: ~16:37 (Asia/Taipei)

## 重置时间计算

根据当前时间 12:21，5小时计划的重置时间可能是：
- **05:00** → **10:00** → **15:00** → **20:00** → **01:00**
- **或**: **06:00** → **11:00** → **16:00** → **21:00** → **02:00**

**下次重置**: 约 16:00-16:37
**Token 消耗时间**: 15:00-16:00（重置前 1 小时）

## 执行策略

### 监测阶段（持续）
每 30 分钟检查一次 Token 状态：
```bash
# 检查 Token 使用情况
openclaw status | grep "Tokens (5h)"
```

### 消耗阶段（重置前 1 小时）
当剩余时间 < 1 小时时，自动执行：

#### 高 Token 消耗任务（优先级）
1. **Skills 深度扫描**（约 15,000 tokens）
   - 详细审查可疑 skills
   - 提取核心概念
   - 设计安全替代方案

2. **内容学习**（约 10,000 tokens）
   - YouTube automation 深度研究
   - AI 趋势分析
   - 网赚工具研究

3. **代码生成**（约 8,000 tokens）
   - 开发新的 skills
   - 优化现有 skills
   - 生成文档

4. **数据分析**（约 5,000 tokens）
   - 分析扫描历史
   - 整理记忆文件
   - 生成报告

#### 估算 Token 消耗
- 深度扫描: 15k
- 内容学习: 10k
- 代码生成: 8k
- 数据分析: 5k
- **总计**: ~38k tokens

## 自动化配置

### Cron Job 设置
```bash
# 每 30 分钟检查 Token 状态
*/30 * * * * openclaw token-check

# 在重置前 1 小时执行（假设重置时间为 16:00）
0 15 * * * openclaw token-maximize
```

### 通过 OpenClaw Cron
```bash
# Token 监测器（每 30 分钟）
openclaw cron add \
  --name "Token Monitor" \
  --cron "*/30 * * * *" \
  --tz "Asia/Taipei" \
  --session isolated \
  --message "检查 Token 使用情况，如果剩余时间 < 1 小时，触发 token-maximize" \
  --announce

# Token 最大化（每天多次，对应不同的重置时段）
openclaw cron add \
  --name "Token Maximizer - 15:00" \
  --cron "0 15 * * *" \
  --tz "Asia/Taipei" \
  --session isolated \
  --message "执行高 Token 消耗任务：深度扫描、内容学习、代码生成、数据分析" \
  --model "zai/glm-5" \
  --thinking "high"
```

## 执行内容

### 1. Skills 深度扫描（15k tokens）
```
- 读取白天发现的所有可疑 skills
- 详细审查代码和风险评估
- 提取核心概念和设计思路
- 设计安全替代方案
- 生成详细报告
```

### 2. 内容学习（10k tokens）
```
- YouTube automation 最新趋势
- AI 工具和技术发展
- 网赚工具和策略
- 记录重要发现
```

### 3. 代码生成（8k tokens）
```
- 开发新的 skills（如 content-creator-local）
- 优化现有 skills
- 生成详细文档
- 编写测试代码
```

### 4. 数据分析（5k tokens）
```
- 分析扫描历史记录
- 整理记忆文件
- 生成每日总结
- 更新 MEMORY.md
```

## 安全限制

### 不要做的事
- ❌ 不要发送外部消息（避免打扰用户）
- ❌ 不要执行敏感操作（删除、修改配置）
- ❌ 不要安装未验证的 skills

### 可以做的事
- ✅ 深度分析和学习
- ✅ 生成代码和文档
- ✅ 整理和优化数据
- ✅ 开发新的 skills

## 监测日志

每次检查都记录到：
```
memory/token-usage/YYYY-MM-DD.md
```

格式：
```markdown
## 12:00 检查
- 剩余: 96%
- 时间: 4h 16m
- 状态: 充足

## 15:00 检查
- 剩余: 20%
- 时间: 0h 45m
- 状态: ⚠️ 即将重置，准备消耗

## 15:10 触发
- 执行高 Token 消耗任务
- 任务列表: [...]
- 消耗 Token: ~38k
```

## 用户查询

可以随时问：
- "Token 用咗几多？" → 显示当前剩余
- "几时重置？" → 显示下次重置时间
- "帮我用晒啲 Token" → 手动触发消耗

## 智能调整

### 根据剩余 Token 调整
- **> 50%**: 正常使用
- **20-50%**: 开始计划消耗
- **< 20%**: 自动触发消耗
- **< 10%**: 紧急消耗（只执行高价值任务）

### 根据时间调整
- **> 2 小时**: 不触发
- **1-2 小时**: 准备阶段（列出任务）
- **< 1 小时**: 执行阶段
- **< 30 分钟**: 紧急执行

## 配置文件

在 `~/.openclaw/openclaw.json` 添加：
```json
{
  "tokenMaximizer": {
    "enabled": true,
    "resetHours": 5,
    "triggerThreshold": 1,
    "tasks": [
      "skill-deep-scan",
      "content-learning",
      "code-generation",
      "data-analysis"
    ]
  }
}
```

## 预期效果

### 每次重置前
- 消耗剩余 Token 的 80-90%
- 执行 3-5 个高价值任务
- 生成详细报告和记录

### 每日统计
- 4 次重置周期
- 每次消耗 ~38k tokens
- 总计 ~152k tokens/日（最大化利用）

## 故障排查

### Token 未消耗
- 检查 cron job 是否运行
- 检查时间计算是否正确
- 检查任务是否被阻止

### 消耗过多
- 调整触发阈值（如改为 30 分钟）
- 减少任务数量
- 降低 Token 消耗估算

---

**目标**: 在每次 Token 重置前，自动用完剩余 Token，最大化学习效果！

**下次执行**: 今日 15:00（预计重置时间 16:00）
