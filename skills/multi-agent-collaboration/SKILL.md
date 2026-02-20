---
name: multi-agent-collaboration
description: 多Agent协作系统 - 线性流水线、并行执行、AI辩论三大模式
version: 1.0.0
author: local
license: MIT
---

# Multi-Agent Collaboration - 多Agent协作系统

## 功能
- 线性流水线：任务1 → 任务2 → 任务3
- 并行依赖图：多个任务同时执行
- AI辩论：多个 Agent 讨论最佳方案

## 使用场景

### 1. 软件开发（编码→测试→文档→审查）
### 2. 内容创作（研究→写作→编辑→发布）
### 3. 数据分析（收集→清洗→分析→可视化）

---

## 模式 1: 线性流水线（Pipeline）

**适用场景**: 有明确顺序的任务

### 使用方式
```
"用流水线模式帮我开发一个 skill：编码→测试→文档→审查"
```

### 执行流程
```
1. Agent 1: 编码 (GLM-5)
   ↓ (完成)
2. Agent 2: 测试 (MiniMax)
   ↓ (完成)
3. Agent 3: 文档 (GLM-5)
   ↓ (完成)
4. Agent 4: 审查 (GLM-5)
   ↓ (完成)
最终交付: 生产级代码 + 测试 + 文档 + 审查报告
```

### 配置示例
```bash
# 步骤 1: 编码
session_spawn \
  --model "zai/glm-5" \
  --message "开发一个 [功能] skill，包含完整代码"

# 等待完成

# 步骤 2: 测试
session_spawn \
  --model "minimax/m2.5" \
  --message "为刚才的代码编写测试，确保覆盖率 > 80%"

# 等待完成

# 步骤 3: 文档
session_spawn \
  --model "zai/glm-5" \
  --message "为这个 skill 编写详细的使用文档"

# 等待完成

# 步骤 4: 审查
session_spawn \
  --model "zai/glm-5" \
  --message "审查代码质量、测试覆盖、文档完整性，给出改进建议"
```

---

## 模式 2: 并行依赖图（Parallel）

**适用场景**: 独立任务，可同时执行

### 使用方式
```
"用并行模式帮我：1) 研究 YouTube automation 2) 研究 AI 趋势 3) 研究网赚工具"
```

### 执行流程
```
┌─ Agent 1: 研究 YouTube automation
├─ Agent 2: 研究 AI 趋势         (同时执行)
└─ Agent 3: 研究网赚工具
   ↓ (全部完成)
合并报告: 综合三个方向的研究结果
```

### 配置示例
```bash
# 同时启动 3 个 Agent
session_spawn --model "zai/glm-5" --message "研究 YouTube automation 最新趋势" &
PID1=$!

session_spawn --model "minimax/m2.5" --message "研究 AI 趋势（OpenAI, Anthropic, 开源项目）" &
PID2=$!

session_spawn --model "zai/glm-5" --message "研究网赚工具和策略" &
PID3=$!

# 等待所有完成
wait $PID1 $PID2 $PID3

# 合并结果（由主 Agent 处理）
# 主 Agent 会收到所有子 Agent 的完成通知
```

---

## 模式 3: AI辩论（Debate）

**适用场景**: 需要多个观点、寻找最佳方案

### 使用方式
```
"用AI辩论模式帮我分析：应该专注于 YouTube automation 还是 Local Business Automation？"
```

### 执行流程
```
Agent A (支持 YouTube): 列出优势、数据、案例
   ↓
Agent B (支持 Local Business): 列出优势、数据、案例
   ↓
Agent C (中立): 分析两者优劣、提出综合方案
   ↓
主 Agent: 总结辩论，给出最终建议
```

### 配置示例
```bash
# Agent A: 支持方
session_spawn \
  --model "zai/glm-5" \
  --message "作为支持 YouTube automation 的专家，列出这个方向的所有优势、成功案例、潜在收益"

# Agent B: 反对方
session_spawn \
  --model "minimax/m2.5" \
  --message "作为支持 Local Business Automation 的专家，列出这个方向的所有优势、成功案例、潜在收益"

# Agent C: 中立方
session_spawn \
  --model "zai/glm-5" \
  --message "作为中立分析师，对比两个方向，分析优劣，提出综合方案或建议"

# 等待所有完成

# 主 Agent 总结
# 在主 session 中总结三个 Agent 的观点，给出最终建议
```

---

## 实战案例

### 案例 1: 开发 content-creator Skill（流水线）
```
1. 编码 Agent: "开发一个 content-creator skill，用于生成 YouTube 视频标题和描述"
2. 测试 Agent: "为这个 skill 编写测试用例，验证各种输入"
3. 文档 Agent: "编写使用文档，包含示例和最佳实践"
4. 审查 Agent: "审查代码质量、测试覆盖、文档完整性"
```

### 案例 2: 研究市场机会（并行）
```
1. Agent 1: "研究 YouTube automation 市场（2026-2027）"
2. Agent 2: "研究 AI 工具市场（2026-2027）"
3. Agent 3: "研究网赚工具市场（2026-2027）"
→ 合并报告，找出最佳机会
```

### 案例 3: 决策分析（辩论）
```
1. Agent A: "支持专注高 CPM niche（Space/Science）的论点"
2. Agent B: "支持专注高流量 niche（Celebrity Gossip）的论点"
3. Agent C: "对比分析，提出平衡策略"
→ 给出最终建议
```

---

## 模型分配策略

### 基于 Token 优化
- **GLM-5**: 复杂任务（编码、深度分析、决策）
- **MiniMax**: 日常任务（测试、文档、简单研究）

### 基于容灾机制
- 主 Agent: GLM-5
- 如果失败，自动切换到 MiniMax

---

## 协作结果合并

### 流水线模式
- 每个步骤的结果传递给下一步
- 最终输出: 完整的产品（代码+测试+文档+审查）

### 并行模式
- 所有结果汇总到主 Agent
- 主 Agent 整合、去重、总结
- 最终输出: 综合报告

### 辩论模式
- 收集所有观点
- 主 Agent 分析、对比、总结
- 最终输出: 决策建议

---

## 使用方式

### 快速启动
```
"用流水线模式帮我开发一个 [功能] skill"
"用并行模式帮我研究 [主题1] [主题2] [主题3]"
"用AI辩论模式帮我分析：[问题]"
```

### 自定义配置
```
"用流水线模式，步骤：
1. 用 GLM-5 编码
2. 用 MiniMax 测试
3. 用 GLM-5 写文档"
```

---

## 技术实现

### sessions_spawn 工具
用于创建子 Agent session

### sessions_send 工具
用于向子 Agent 发送消息

### sessions_list 工具
用于查看所有子 Agent 状态

### sessions_history 工具
用于获取子 Agent 的执行结果

---

## 限制与注意

### 资源限制
- 建议同时运行的 Agent 数: ≤ 3
- 每个 Agent 的 timeout: 10 分钟

### 模型选择
- 复杂任务用 GLM-5
- 简单任务用 MiniMax
- 自动 fallback 确保稳定

### 结果合并
- 需要主 Agent 整合结果
- 避免 token 超限

---

## 高级功能（未来）

### 动态调整
- 根据任务复杂度自动选择模型
- 根据执行时间动态调整

### 学习优化
- 记录每个 Agent 的表现
- 优化任务分配策略

### 质量控制
- 自动审查每个 Agent 的输出
- 不合格重新执行

---

**目标**: 通过多Agent协作，提高效率，完成复杂任务！
