# QA Agent - 品质控制

## 用途
审阅所有 agent 输出，检测错误，给出品质评分（A/B/C/D/F），提供改进建议。

## 触发条件
- 每个 agent 任务完成后
- 每日 20:00（综合报告）
- 错误率 > 10% 警报

## 使用方式

### 1. 审阅 Agent 输出
```bash
# 审阅特定 agent
python3 scripts/qa-review.py --agent [agent-name]

# 审阅所有 agents
python3 scripts/qa-review.py --all
```

### 2. 品质评分
```python
# 评分标准
A (90-100): 完美，无错误
B (80-89): 良好，小问题
C (70-79): 可接受，有改进空间
D (60-69): 勉强，需要修正
F (<60): 不合格，需要重做
```

### 3. 生成报告
```bash
# 每日 QA 报告
python3 scripts/generate-qa-report.py

# 输出位置
# memory/reports/qa-YYYY-MM-DD.md
```

## 范例

**YouTube Agent 完成任务**：
- 生成了 YouTube 腚本

**QA Agent**：
1. 检查腚本内容
2. 验证格式
3. 检查 affiliate links
4. 给出评分（例如：B）
5. 提供改进建议

## 报告格式

```markdown
# QA Report - YYYY-MM-DD

## 📊 整体评分
- 平均分: XX/100 (Grade: X)
- 完成率: XX%
- 错误率: X.X%

## 🤖 Agent 表现
| Agent | 任务数 | 评分 | 错误数 | 状态 |
|-------|--------|------|--------|------|
| YouTube | 5 | A (92) | 0 | ✅ |
| Newsletter | 1 | B (85) | 1 | ⚠️ |
| Stock | 7 | A (95) | 0 | ✅ |

## ❌ 发现的错误
1. **Newsletter Agent**:
   - 问题: Subject line 太长
   - 建议: 缩短到 50 字符内
   
2. **[其他错误]**

## 💡 改进建议
- [建议 1]
- [建议 2]

## 🎯 明日重点
- [ ] [任务 1]
- [ ] [任务 2]
```

## 审阅清单

### Content Agents (YouTube, Newsletter, Blog)
- [ ] 内容准确性
- [ ] 格式正确性
- [ ] Affiliate links 有效
- [ ] SEO 优化
- [ ] 拼写/语法

### Analysis Agents (Stock, Crypto)
- [ ] 数据准确性
- [ ] 计算正确性
- [ ] 趋势判断合理
- [ ] 免责声明

### Infrastructure Agents (MCP, Evolution)
- [ ] 代码可运行
- [ ] API 连接正常
- [ ] 错误处理完善

## 品质标准

| 等级 | 分数 | 描述 | 行动 |
|------|------|------|------|
| A | 90-100 | 完美 | 无需修改 |
| B | 80-89 | 良好 | 小改进 |
| C | 70-79 | 可接受 | 需要优化 |
| D | 60-69 | 勉强 | 需要修正 |
| F | <60 | 不合格 | 需要重做 |

## 相关文件
- 报告：`memory/reports/qa-*.md`
- 错误记录：`memory/errors/*.md`
- 改进建议：`memory/improvements/*.md`

## 模型
- **品质分析**：GLM-5

## 状态
- ✅ 框架设计完成
- ⏳ 自动化审阅开发中
