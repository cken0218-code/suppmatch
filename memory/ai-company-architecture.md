# AI 公司架构 — Ken AI Corporation

> **Created**: 2026-03-13
> **Version**: 1.0
> **Status**: Active

---

## 🏢 公司架构总览

**核心理念**：从「一个助理」升级成「一间 AI 公司」，每个 Agent 都有明确职责、触发条件和专属模型。

---

## 📊 组织架构图

```
                    Ken (Main) 🐱
                    CEO / Commander
                         |
        ┌────────────────┼────────────────┐
        |                |                |
   Operations        Content         Research
      Agent           Hub              Hub
                        |
        ┌───────────┬───┴───┬───────────┐
        |           |       |           |
   YouTube      Newsletter  Blog     Affiliate
    Agent        Agent      Agent     Agent
        
        ┌────────────────┼────────────────┐
        |                |                |
     Stock           Crypto          Evolution
     Agent            Agent           Agent
        
        ┌────────────────┼────────────────┐
        |                |                |
      MCP              QA             R&D
     Agent            Agent           Agent
```

---

## 🤖 Agent 清单（共 14 个）

### 🎯 Level 1: Command Layer

#### 1. Ken (Main) - CEO / Commander 🐱
**职责**：
- 对外通信（用户、Telegram、Discord）
- 任务分配和统筹
- 每日审阅 QA 报告
- 战略决策

**触发条件**：
- 用户直接对话
- Agent 任务完成通知
- QA 报告异常

**模型**：GLM-5（战略决策）+ MiniMax（日常对话）

**报告格式**：`memory/reports/daily-summary-YYYY-MM-DD.md`

---

### 🏢 Level 2: Operations Layer

#### 2. Operations Agent - 运营管理 📋
**职责**：
- 日常任务调度（cron jobs）
- Heartbeat 执行
- 系统监控（Gateway、Discord）
- 错误追踪和记录

**触发条件**：
- Cron 定时触发（09:00, 12:00, 15:00, 18:00, 20:00）
- 系统异常
- Gateway 重启

**模型**：MiniMax（简单任务）

**报告格式**：`memory/reports/operations-YYYY-MM-DD.md`

**Skill 位置**：`skills/operations-agent/`

---

### ✍️ Level 3: Content Hub

#### 3. YouTube Agent - 视频内容 📺
**职责**：
- Trending 监控（YouTube、Threads、X）
- 脚本生成
- SEO 优化
- 发布排程

**触发条件**：
- 每日 12:00, 18:00 trending 扫描
- 用户要求「写 YouTube 腚本」
- 新 affiliate 产品发布

**模型**：GLM-5（腚本创作）+ MiniMax（trending 扫描）

**报告格式**：`memory/reports/youtube-YYYY-MM-DD.md`

**Skill 位置**：`skills/youtube-agent/`

---

#### 4. Newsletter Agent - 通讯管理 📧
**职责**：
- Beehiiv 管理
- Issue 内容生成
- Subscriber 追踪
- Open rate / Click rate 分析

**触发条件**：
- 每周五 10:00 发布
- Subscriber 里程碑（100, 500, 1000）
- Open rate < 20% 警报

**模型**：GLM-5（内容创作）

**报告格式**：`memory/reports/newsletter-YYYY-MM-DD.md`

**Skill 位置**：`skills/newsletter-agent/`

---

#### 5. Blog Agent - 博客内容 📝
**职责**：
- WordPress/Ghost 管理
- SEO 优化内容生成
- 关键词研究
- 流量分析

**触发条件**：
- 每周一、三、五发布
- Google Search Console 异常
- 用户要求「写 blog post」

**模型**：GLM-5（内容创作）+ MiniMax（数据分析）

**报告格式**：`memory/reports/blog-YYYY-MM-DD.md`

**Skill 位置**：`skills/blog-agent/`

---

#### 6. Affiliate Agent - 联盟行销 💰
**职责**：
- Affiliate 产品研究
- Landing page 创建
- Conversion rate 追踪
- 佣金收入分析

**触发条件**：
- 新 affiliate program 发布
- Conversion rate < 1% 警报
- 用户要求「整 landing page」

**模型**：GLM-5（策略）+ MiniMax（数据分析）

**报告格式**：`memory/reports/affiliate-YYYY-MM-DD.md`

**Skill 位置**：`skills/affiliate-agent/`

---

### 📊 Level 4: Research & Analysis Hub

#### 7. Stock Agent - 澳股分析 📈
**职责**：
- ASX 股票技术分析
- RSI / MACD / ADX 计算
- 买卖信号生成
- 每日报告（09:00）

**触发条件**：
- 每日 09:00（平日）
- 用户要求「分析 [股票]」
- RSI < 20 或 > 80 异常

**模型**：MiniMax（数据分析）

**报告格式**：`memory/reports/stock-YYYY-MM-DD.md`

**Skill 位置**：`skills/stock-agent/`

---

#### 8. Crypto Agent - 加密货币 ₿
**职责**：
- BTC/ETH/SOL 价格追踪
- Fear & Greed Index
- 突破/跌破警报
- 技术分析

**触发条件**：
- 每日 08:30（早市扫描）
- 单日波动 > 8%
- 用户要求「睇下 [币]」

**模型**：MiniMax（数据分析）

**报告格式**：`memory/reports/crypto-YYYY-MM-DD.md`

**Skill 位置**：`skills/crypto-agent/`

---

#### 9. Research Agent - 趋势研究 📚
**职责**：
- ClawHub skills 扫描
- AI 趋势研究
- 学习新技术
- 知识库更新

**触发条件**：
- 每周五 13:50（skills 扫描）
- 每日 15:00（学习）
- 用户要求「研究 [topic]」

**模型**：GLM-5（深度研究）

**报告格式**：`memory/reports/research-YYYY-MM-DD.md`

**Skill 位置**：`skills/research-agent/`

---

### 🔧 Level 5: Infrastructure Hub

#### 10. Evolution Agent - 史莱姆进化 🧬
**职责**：
- Skills 基因管理
- 自动演化触发
- Fusion 机会检测
- XP/成就系统

**触发条件**：
- 每周日 20:00（演化检测）
- Fusion synergy > 90%
- Health < 50 警报

**模型**：GLM-5（演化决策）

**报告格式**：`memory/reports/evolution-YYYY-MM-DD.md`

**Skill 位置**：`skills/slime-evolution/`

---

#### 11. MCP Agent - 协议整合 🔌
**职责**：
- MCP servers 管理（GitHub, Discord, n8n）
- Phase 1-4 整合
- API 连接监控
- 错误处理

**触发条件**：
- MCP server 启动/停止
- API 连接失败
- 用户要求「整合 [tool]」

**模型**：GLM-5（技术整合）

**报告格式**：`memory/reports/mcp-YYYY-MM-DD.md`

**Skill 位置**：`skills/mcp-agent/`

---

### ✅ Level 6: Quality Assurance Hub

#### 12. QA Agent - 品质控制 🔍
**职责**：
- 审阅所有 agent 输出
- 错误检测和修正
- 品质评分（A/B/C/D/F）
- 改进建议

**触发条件**：
- 每个 agent 任务完成后
- 每日 20:00（综合报告）
- 错误率 > 10% 警报

**模型**：GLM-5（品质分析）

**报告格式**：`memory/reports/qa-YYYY-MM-DD.md`

**Skill 位置**：`skills/qa-agent/`

---

#### 13. R&D Agent - 研发创新 💡
**职责**：
- 新工具测试
- 自动化机会识别
- 工具提案系统
- 实验性项目

**触发条件**：
- 发现新工具
- 用户要求「试下 [tool]」
- 效率瓶颈识别

**模型**：GLM-5（研发）

**报告格式**：`memory/reports/rd-YYYY-MM-DD.md`

**Skill 位置**：`skills/rd-agent/`

---

#### 14. Integration Agent - 整合协调 🔗
**职责**：
- Agent 之间沟通协调
- Handoff 格式验证
- 数据流管理
- API 整合

**触发条件**：
- Agent 任务交接
- 数据同步需求
- API 调用失败

**模型**：MiniMax（协调）

**报告格式**：`memory/reports/integration-YYYY-MM-DD.md`

**Skill 位置**：`skills/integration-agent/`

---

## 📊 Agent 统计

| Level | 数量 | 主要职责 |
|-------|------|----------|
| Command | 1 | 战略决策 |
| Operations | 1 | 日常运营 |
| Content | 4 | 内容创作 |
| Research | 3 | 分析研究 |
| Infrastructure | 2 | 技术支持 |
| QA | 3 | 品质保证 |
| **总计** | **14** | - |

---

## 🎯 模型分配

| 模型 | 负责的 Agents | 原因 |
|------|--------------|------|
| **GLM-5** | Ken, Content Hub (4), Research Agent, Evolution, MCP, QA, R&D | 需要深度思考、创作、分析 |
| **MiniMax** | Operations, Stock, Crypto, Integration | 日常任务、数据分析 |
| **混合** | YouTube (GLM-5 + MiniMax), Blog (GLM-5 + MiniMax), Affiliate (GLM-5 + MiniMax) | 创作部分用 GLM-5，数据用 MiniMax |

**成本优化**：
- GLM-5: 30% 任务（复杂）
- MiniMax: 70% 任务（简单）

---

## 📋 下一步行动

1. ✅ 架构设计完成
2. ⏳ 创建新 Agent Skills（Newsletter, Affiliate, Blog, Crypto, MCP, QA, R&D, Integration, Operations）
3. ⏳ 建立品控机制
4. ⏳ 建立 Handoff Template
5. ⏳ 更新 L0-core.md

---

**Created by**: Ken AI Assistant
**Date**: 2026-03-13
**Status**: Architecture Complete, Skills Creation In Progress
