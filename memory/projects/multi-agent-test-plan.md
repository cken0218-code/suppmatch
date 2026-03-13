# Multi-Agent 系统测试计划

> **Created**: 2026-03-13 19:15
> **Status**: Testing
> **Priority**: ⭐⭐⭐ High

---

## 🎯 测试目标

验证 14 个 Agents 系统是否可靠运作：
1. Agent 之间 handoff 是否顺畅
2. 品控机制是否有效
3. 错误恢复是否正常
4. 任务分配是否合理

---

## 📊 测试场景

### 测试 1: 简单 Handoff（YouTube → Affiliate）

**场景**：
- YouTube Agent 完成 YouTube 腚本
- 交给 Affiliate Agent 加 affiliate links
- Integration Agent 验证 handoff

**测试步骤**：
1. 创建测试 YouTube 腚本
2. 触发 handoff 到 Affiliate Agent
3. 验证 affiliate links 是否正确插入
4. 检查 handoff 格式是否符合标准

**预期结果**：
- ✅ Handoff 文件创建成功
- ✅ 格式符合 `memory/handoff-template.md`
- ✅ Affiliate links 正确插入
- ✅ 状态更新为 "completed"

**文件位置**：
- Handoff: `memory/handoffs/youtube-to-affiliate-test-20260313.md`

---

### 测试 2: 品控机制（QA Agent）

**场景**：
- 模拟一个有错误的输出
- QA Agent 检测错误
- 给出评分和改进建议

**测试步骤**：
1. 创建一个故意有错误的测试文件
2. 触发 QA Agent 审阅
3. 检查是否检测到错误
4. 验证评分是否合理

**预期结果**：
- ✅ 错误被检测
- ✅ 评分 < C
- ✅ 改进建议提供
- ✅ 记录到 `memory/reports/qa-test-*.md`

---

### 测试 3: 错误恢复（Integration Agent）

**场景**：
- 模拟 handoff 失败
- Integration Agent 检测失败
- 自动重试或通知

**测试步骤**：
1. 创建一个格式错误的 handoff 文件
2. 触发 Integration Agent 验证
3. 检查是否检测到格式错误
4. 验证是否自动重试或通知

**预期结果**：
- ✅ 格式错误被检测
- ✅ 返回错误信息
- ✅ 建议修正方法

---

### 测试 4: 任务分配（Ken Main）

**场景**：
- 用户给出复杂任务
- Ken (Main) 分配给多个 Agents
- 协调执行

**测试步骤**：
1. 给出测试任务："分析 Tesla 股票并发布到 Discord"
2. Ken 分配任务：
   - Stock Agent: 分析股票
   - Discord Agent: 发布消息
3. 检查任务分配是否合理

**预期结果**：
- ✅ 任务正确分解
- ✅ 分配给合适的 Agents
- ✅ 执行顺序合理

---

## 🧪 测试执行

### 测试 1: YouTube → Affiliate Handoff

**创建测试腚本**：