# Handoff Template - Agent 任务交接格式

> **Created**: 2026-03-13
> **Version**: 1.0

---

## 🎯 核心理念

Agent 之间传递任务**必须**使用标准格式，确保信息完整、可追踪、可审计。

---

## 📋 Handoff 格式

```markdown
# Handoff: [Agent1] → [Agent2]

## 📋 基本信息
- **From**: [Agent1 Name]
- **To**: [Agent2 Name]
- **时间**: YYYY-MM-DD HH:MM
- **Handoff ID**: [AGENT1]-to-[AGENT2]-YYYYMMDD-HHMM
- **优先级**: [🔴 High / 🟡 Medium / 🟢 Low]

---

## 🎯 任务描述
[简短描述任务内容]

---

## 📦 交付物

### 文件
- `[文件 1]`: [描述]
- `[文件 2]`: [描述]

### 数据
- **数据 1**: [描述]
- **数据 2**: [描述]

### 链接
- [链接 1]: [描述]
- [链接 2]: [描述]

---

## ✅ 验收标准
- [ ] [标准 1]
- [ ] [标准 2]
- [ ] [标准 3]

---

## 📝 执行建议
1. [建议 1]
2. [建议 2]
3. [建议 3]

---

## ⚠️ 注意事项
- [注意事项 1]
- [注意事项 2]

---

## 💬 备注
[额外信息]

---

## 📊 状态
- [ ] 待接收
- [ ] 进行中
- [ ] 已完成
- [ ] 需要返工

---

**Created by**: [Agent1 Name]
**Approved by**: Ken (Main) / [如果需要]
**Status**: [Pending / In Progress / Completed]
```

---

## 📊 Handoff 流程

### Step 1: 创建 Handoff
```bash
# 创建 handoff 文件
python3 skills/integration-agent/scripts/create-handoff.py \
  --from [agent1] \
  --to [agent2] \
  --task "[任务描述]"
```

### Step 2: 验证格式
```bash
# Integration Agent 验证
python3 skills/integration-agent/scripts/validate-handoff.py \
  --file memory/handoffs/[filename].md
```

### Step 3: 通知接收方
```bash
# 发送通知
python3 skills/integration-agent/scripts/notify-agent.py \
  --agent [agent2] \
  --handoff [handoff-id]
```

### Step 4: 执行任务
- 接收方 Agent 执行任务
- 更新 handoff 状态

### Step 5: 完成/返工
- ✅ 完成 → 关闭 handoff
- ❌ 返工 → 创建返工 handoff

---

## 📝 常见 Handoff 场景

### 场景 1: YouTube Agent → Affiliate Agent
**任务**: 为 YouTube 腚本添加 affiliate links

```markdown
# Handoff: YouTube Agent → Affiliate Agent

## 📋 基本信息
- **From**: YouTube Agent
- **To**: Affiliate Agent
- **时间**: 2026-03-13 14:00
- **Handoff ID**: youtube-to-affiliate-20260313-1400
- **优先级**: 🟡 Medium

## 🎯 任务描述
为「15 AI Tools Trending 2026」腚本添加 CustomGPT affiliate link

## 📦 交付物
- `youtube-scripts/2026-03-13-ai-tools-trending.md`: YouTube 腚本（已完成）
- 需要在以下位置插入 affiliate link:
  1. Tool #5 (CustomGPT) → 插入 landing page link
  2. 结尾 CTA → 插入 affiliate link

## ✅ 验收标准
- [ ] CustomGPT affiliate link 正确插入
- [ ] Landing page link 有效
- [ ] 腚本流畅度不受影响
- [ ] 符合 YouTube 政策

## 📝 执行建议
1. 使用 `landing-pages/customgpt/index.html` 作为链接
2. 在腚本中自然插入（唔好太硬销）
3. 保持「教育性」而非「推销性」

## ⚠️ 注意事项
- 唔好过度推销
- 确保链接可追踪

## 💬 备注
CustomGPT 提供 20% recurring commission，系重点产品

## 📊 状态
- [x] 待接收
- [ ] 进行中
- [ ] 已完成
- [ ] 需要返工
```

### 场景 2: Stock Agent → Ken (Main)
**任务**: 报告重要投资机会

```markdown
# Handoff: Stock Agent → Ken (Main)

## 📋 基本信息
- **From**: Stock Agent
- **To**: Ken (Main)
- **时间**: 2026-03-13 09:00
- **Handoff ID**: stock-to-ken-20260313-0900
- **优先级**: 🔴 High

## 🎯 任务描述
报告 BAP/AD8 超卖机会（连续 3 天确认）

## 📦 交付物
- `memory/reports/stock-2026-03-13.md`: 每日报告
- `data/asx-prices.csv`: 价格数据

## ✅ 验收标准
- [ ] Ken 审阅报告
- [ ] 决定是否通知用户
- [ ] 如果通知，提供操作建议

## 📝 执行建议
1. 重点突出 BAP/AD8 机会
2. 提供风险提示
3. 加免责声明

## ⚠️ 注意事项
- 呢个系投资建议，要小心处理
- 必须加免责声明

## 📊 状态
- [x] 待接收
- [x] 进行中
- [ ] 已完成
```

---

## 🔍 Integration Agent 职责

### 验证 Handoff
```python
def validate_handoff(file_path):
    """验证 handoff 格式"""
    required_fields = [
        'From', 'To', '时间', 'Handoff ID', '优先级',
        '任务描述', '交付物', '验收标准', '状态'
    ]
    
    # 检查所有必填字段
    for field in required_fields:
        if field not in content:
            return False, f"Missing field: {field}"
    
    return True, "Valid handoff"
```

### 追踪状态
```python
def track_handoff_status(handoff_id):
    """追踪 handoff 状态"""
    status = {
        'pending': 0,
        'in_progress': 0,
        'completed': 0,
        'needs_rework': 0
    }
    
    # 更新状态
    # ...
    
    return status
```

---

## 📊 Handoff 统计

| 指标 | 目标 | 当前 |
|------|------|------|
| 格式正确率 | 100% | - |
| 平均交接时间 | < 5 分钟 | - |
| 返工率 | < 5% | - |
| 遗漏率 | 0% | - |

---

## 📁 文件位置

- Handoff 文件：`memory/handoffs/[from]-to-[to]-YYYYMMDD-HHMM.md`
- 模板：`memory/handoff-template.md`
- Integration Agent：`skills/integration-agent/`

---

## 🔗 相关文件

- Integration Agent SKILL.md：`skills/integration-agent/SKILL.md`
- 品控机制：`memory/qc-mechanism.md`
- 报告格式：`memory/qc-mechanism.md#报告格式标准`

---

**Created by**: Ken AI Assistant
**Date**: 2026-03-13
**Status**: Active
