# 用户习惯记录 - User Patterns

> **Created**: 2026-03-13 18:52
> **Last Updated**: 2026-03-13 18:52
> **Purpose**: 记录用户使用模式，持续改进系统

---

## 📊 常用任务（按频率排序）

### 高频任务（每周 3+ 次）
1. **YouTube 内容创作** 📺
   - 腚本生成
   - Trending 分析
   - SEO 优化

2. **投资分析** 📈
   - 澳股每日报告（09:00）
   - BTC/ETH 追踪
   - 买卖信号

### 中频任务（每周 1-2 次）
3. **Newsletter 发布** 📧
   - Beehiiv Issue 生成
   - 每周五发布

4. **Skills 扫描** 🔍
   - ClawHub 新 skills
   - 每周五扫描

### 低频任务（每月 1-2 次）
5. **架构升级** 🏗️
   - Multi-agent 系统
   - MCP 整合

6. **MD 优化** 📝
   - 精简文件
   - 改进规则

---

## 💬 反馈历史

### 2026-03-13（今日）
1. **建议用 GLM-5 做 primary**
   - 用户原话："通常係咪應該用Glm5做主力Mini Max後備會更好更"
   - 采纳：✅ 是
   - 原因：用户认为 GLM-5 推理能力更强
   - 执行：已切换（Primary: GLM-5, Fallback: MiniMax-M2.1）

2. **建议简化 AGENTS.md**
   - 用户原话："我想問根據我咁耐嘅情況，我應該點樣改善你個md會比較好"
   - 采纳：✅ 是
   - 原因：AGENTS.md 太大（966 行），信息重复
   - 执行：Phase 1-3 已完成（减少 68% 内容）

3. **选择全部执行改进建议**
   - 用户原话："C"
   - 采纳：✅ 是
   - 原因：用户想要全面改进系统
   - 执行：正在按优先级执行

---

## 🐛 错误学习

### 2026-03-13
1. **API Fail（16:28）**
   - 错误：GLM-5 timeout + MiniMax-M2.5 HTTP 500
   - 原因：MiniMax-M2.5 当前计划不支持
   - 解决：切换到 MiniMax-M2.1
   - 教训：检查 fallback 是否真的可用

2. **API Fail（再次）**
   - 错误：GLM-5 timeout
   - 原因：API 压力大
   - 解决：切换到 MiniMax-M2.1
   - 教训：需要监控 GLM-5 timeout 频率

---

## 🎯 用户习惯模式

### 沟通习惯
- **语言**：广东话口语 + emoji
- **语气**：直接、唔好废话
- **长度**：简洁有力
- **格式**：Table > Bullet list（Discord/WhatsApp）

### 工作习惯
- **瞓觉时间**：夜瞓（02:00-03:00）
- **起身时间**：晏（10:00-11:00）
- **工作时间**：下午 + 深夜
- **最佳联络时间**：14:00 - 02:00

### 决策习惯
- **快速决策**：A/B/C 选项
- **信任 AI**：允许自主执行内部任务
- **谨慎**：外部行动需要确认

---

## 📈 改进记录

### 2026-03-13
1. ✅ **自主解决原则** - 先自己解决，唔好即刻问用户
2. ✅ **Browser tools checklist** - 执行前检查可用工具
3. ✅ **模型切换优化** - GLM-5 primary + MiniMax-M2.1 fallback
4. ✅ **MD 精简计划** - Phase 1-3 完成（减少 68% 内容）
5. ✅ **安装 self-improving-agent** - ClawHub rate limit，手动从 GitHub clone
6. ✅ **优化 Heartbeat 学习关键词** - 新增 multi-agent / MCP / AI company
7. ✅ **创建自动化脚本库** - check-system-health.sh, generate-daily-summary.sh, track-token-usage.py
5. ✅ **安装 self-improving-agent** - 补充史莱姆系统，自动记录错误

---

## 🎯 下次更新

**触发条件**：
- 用户提供新反馈
- 发现新习惯模式
- 错误学习
- 改进记录

**更新频率**：每次 heartbeat（12:00, 18:00, 20:00）

---

**Created by**: Ken AI Assistant
**Date**: 2026-03-13 18:52
**Status**: Active
