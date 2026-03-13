# R&D Agent - 研发创新

## 用途
测试新工具，识别自动化机会，提出工具提案，进行实验性项目。

## 触发条件
- 发现新工具
- 用户要求「试下 [tool]」
- 效率瓶颈识别

## 使用方式

### 1. 测试新工具
```bash
# 测试工具
python3 scripts/test-tool.py --tool [tool-name]

# 输出位置
# memory/reports/rd-[tool]-YYYY-MM-DD.md
```

### 2. 提出提案
```bash
# 生成工具提案
python3 scripts/create-proposal.py --tool [tool-name]

# 输出位置
# memory/tool-proposals.md
```

### 3. 实验项目
```bash
# 创建实验项目
mkdir -p experiments/[project-name]

# 输出位置
# experiments/[project-name]/
```

## 范例

**用户**：「试下 n8n」

**R&D Agent**：
1. 研究 n8n 功能
2. 测试基本功能
3. 评估整合可能性
4. 提出提案

## 报告格式

```markdown
# R&D Report - YYYY-MM-DD

## 🧪 实验项目
| 项目 | 状态 | 结果 | 建议 |
|------|------|------|------|
| n8n 整合 | ✅ 完成 | 可行 | 整合到 Phase 3 |
| [其他项目] | ⏳ 进行中 | - | - |

## 💡 新发现
- [发现 1]
- [发现 2]

## 📋 工具提案
1. **[工具名]**
   - 用途: [描述]
   - 效益: [预期收益]
   - 状态: [待批准/已批准/已拒绝]

## 🎯 下周计划
- [ ] [任务 1]
- [ ] [任务 2]
```

## 已完成提案
- ✅ Token Saver（94.9% token 节省）
- ✅ 自主解决原则
- ✅ Browser tools checklist

## 相关文件
- 报告：`memory/reports/rd-*.md`
- 提案：`memory/tool-proposals.md`
- 实验项目：`experiments/`

## 模型
- **研发**：GLM-5

## 状态
- ✅ 基本框架完成
- ⏳ 自动化测试开发中
