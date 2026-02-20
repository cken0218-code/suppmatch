# MEMORY.md - shikiouo 嘅長期記憶

## 基本信息
- **名**: shikiouo
- **時區**: Asia/Taipei
- **語言偏好**: 繁體中文
- **習慣**: 夜瞓（晏啲先搵佢）

## 主要項目

### YouTube Automation
- 做緊 YouTube 自動化相關項目
- 需要定期關注 trending content
- ✅ 740% 增長（2026-02-16 驗證）
- 高潛力 niches：Tech/AI ($35-45 CPM), Celebrity Gossip, Space/Science

### 網賺
- 網賺相關工作
- 自動化工具開發
- 💰 **Local Business Automation**: $300-500/month/client（最易入門）

## 技術偏好
- 用 Mac mini (lau的Mac mini) 做主要機器
- OpenClaw 作為 personal assistant
- 主要 model: GLM-5, fallback MiniMax-M2.5

## 待辦 / 目標
- [ ] Xiaohongshu trending 監控
- [ ] Threads trending 監控
- [ ] 定期自動學習新內容

## 💡 核心學習 - AI 流程執行時代

### 三大趨勢
1. **內容生成 → 流程執行** - AI 執行完整工作流程
2. **自動化普及** - 能力普及到每一個上班族
3. **組織資產轉移** - 「流程設計能力」成為核心資產

### 關鍵洞察
> 未來的效率差距，不會來自誰比較會寫 Prompt，
> 而在誰比較會把工作拆解成流程，交給 AI 執行。

### 五層架構框架
1. **Goal Definition** - 清晰可量化目標
2. **Planning Engine** - AI 拆解任務、優先排序
3. **Tool Integration** - 連接 CMS、Email、社群、Analytics
4. **Execution** - 自動執行
5. **Feedback Loop** - 持續監測與優化

## 重要決定

### 澳洲股票分析工具 (2026-02-20)
- **工具位置**: `~/.openclaw/workspace/skills/aus-stock-tracker/`
- **追蹤股票**: CBA, BHP, CSL, ANZ, NAB, WBC, 4DX, AD8, ARU, BGL, ELD, KMD, VR1 (13隻)
- **每日自動 report**: 09:00 (禮拜一至五)
- **新增技術指標 (5個)**:
  - RSI (相對強弱指標)
  - MACD (動量+趨勢)
  - EMA (12/26，敏感移動平均)
  - ADX (趨勢強度，過濾假突破)
  - ATR (波幅，set stop loss)
- **Signal 邏輯**: ADX > 25 + RSI < 30 + MACD golden cross = BUY
- **歷史記錄功能**:
  - `history/YYYY-MM-DD.json` - 每日數據
  - `--history N` - 睇最近N日
  - `--verify N` - 驗證信號準確度
- **Cron 設定**:
  - 每日 09:00 自動 save history
  - Discord DM 通知完成
- **Signal 驗證結果 (2026-02-20)**:
  - 100% accuracy (4/4 signals correct)
  - Avg price change: +1.30%

### 2026-02-20 新增功能
- 新增 7 隻 ASX 股票: 4DX, AD8, ARU, BGL, ELD, KMD, VR1
- 新增 ADX + ATR 指標
- 新增 history save 功能
- 新增 verify signals 功能
- 2026-02-15: 轉用 GLM-5 做主要思考模型
- 2026-02-16: YouTube Automation 項目方向驗證成功（740% 增長）
- 2026-02-17: Microsoft AI CEO 預測 12-18 個月內白領工作自動化
- 2026-02-18: 安装 9 个安全 Skills，建立自动扫描系统（每 3 小时）
- 2026-02-18: 学习 AI automation trends 2026（多代理系统成为主流）
- 2026-02-18: 设计 multi-agent-orchestrator-local skill

## 🦞 Skills 生態系統

### 已安装 Skills（共 13 个）
- **安全类**（3）：clawsec-suite, security-audit, api-security-check
- **本地自动化**（1）：automation-workflows ⭐ NEW
- **系统管理**（2）：system-monitor, backup-manager
- **开发工具**（2）：github, git-automation
- **数据处理**（1）：data-analyzer-local
- **任务管理**（1）：cron-manager
- **自动扫描**（1）：skill-scanner
- **历史查询**（1）：skill-history
- **工作流**（1）：workflow-trigger-local
- **应用开发**（1）：app-scaffold-local
- **多代理编排**（1）：multi-agent-orchestrator-local
- **内容创作**（3）：content-creator-local, thumbnail-generator-local, video-script-writer-local
- **分析工具**（2）：youtube-analytics-local, income-tracker-local

### 安全策略
- ✅ 所有 skills 都经过 VirusTotal 检查
- ✅ 可疑 skills 不安装，只学习概念
- ✅ 自行开发安全替代版本（-local 后缀）
- ✅ ClawSec 安全套件提供实时保护

### 自动化监控（优化版 v2.0）
- **白天轻量扫描**: 09:00, 12:00, 15:00, 18:00, 21:00（节省 Token）
- **深夜深度分析**: 23:00, 02:00, 05:00（完整审查）
- **安全审查**: VirusTotal + 代码审查
- **概念记录**: 有趣但不安全的 skills 概念
- **自行开发**: 根据需求开发安全替代品
- **完整记录**: 所有发现永久保存，绝不遗漏

### 记录系统
- **安全列表**: `memory/skills-safe-to-install.md`（随时更新）
- **概念记录**: `memory/skills-concepts-to-develop.md`（随时更新）
- **扫描历史**: `memory/skill-scans/YYYY-MM-DD-*.md`（永久保存）
- **自开发 skills**: `workspace/skills/*-local/`
- **查询工具**: skill-history skill（随时查询历史）

### 查询方式
- "有冇新嘅 skills？" → 显示最新安全 skills
- "上次发现咩？" → 显示扫描总结
- "帮我睇下 X 月 X 日嘅记录" → 显示历史记录
- "点解唔记得？" → **不可能忘记**，所有记录永久保存

## 🎯 策略建議
- **短期（1-3個月）**：YouTube Automation（high-CPM niche）+ Local Business Automation 試水溫
- **中期（3-6個月）**：專注流程設計能力 + Niche 專精
- **長期（6-12個月）**：跟隨 AI 發展，持續學習新工具

## 📊 2026-02-20 安全扫描

### 修复完成 ✅
- automation-workflows 命令注入漏洞已修复
- autonomous-runner 路径验证已添加

### 今日扫描 (2026-02-20)
- 新发现 20+ skills
- 深度分析 6 个
- 风险标记 3 个
- 概念记录 4 个
- 安全新增 0 个（保持严格标准）

### 不建议安装
- perplexity-research, clawpost-2, tmp, telegram-history, x-post-automation

---
*Last updated: 2026-02-20*
- Brave API quota: ~303/2000 (15.15%)，rate limit 1 req/sec
- 深夜時段（23:00-08:00）唔執行外部搜尋
- Generic AI consultant 已死，需專精特定領域

## 📊 2026-02-18 学习总结

### AI Automation Trends
- **多代理系统**：单代理已过时，多代理协作成为主流
- **行业特定应用**：垂直领域解决方案（酒店业、专业服务、保险）
- **预测决策**：AI 系统可适应动态环境
- **治理即代码**：确保代理系统对齐、安全、合规
- **78% 高管**：需要重塑运营模式以充分利用代理式 AI

### 关键洞察
> Agentic AI is no longer the new frontier, it's the new foundation

### 应用方向
1. **YouTube Automation**：设计多代理工作流（研究 → 创作 → 优化 → 发布 → 监控）
2. **Local Business Automation**：开发行业特定自动化工具
3. **Skills 开发**：专注于垂直领域和多代理协作

## 🤖 自動 Model 切換

### 模型特性對比

| 特性 | GLM-5 | MiniMax 2.1 |
|------|-------|-------------|
| **速度** | 較慢 | 快好多 |
| **分析能力** | 強，深度推理 | 一般，適合簡單任務 |
| **成本** | 較高 | 較低 |
| **適用場景** | 複雜決策、Debug、規劃 | 日常對話、簡單整理、搜尋 |

### 自動切換邏輯

| 任務類型 | Model | 原因 |
|----------|-------|------|
| 思考決策、策略分析 | GLM-5 | 需要深度推理 |
| Multi-step 規劃 | GLM-5 | 任務拆解需要邏輯 |
| Code/Debug、Refactor | GLM-5 | 程式推理 |
| 整合多文件分析 | GLM-5 | 複雜理解 |
| 日常對話、簡單搜尋 | MiniMax | 快速響應 |
| 寫作/整理、記錄 | MiniMax | 不需要深度 |
| 例行 heartbeat 檢查 | MiniMax | 慳成本 |

**運作方式：**
- 平時用 MiniMax（快、平）
- 遇到複雜嘢 → 自動 call `session_status(model="glm-5")`
- 完成後切返 MiniMax

**原則**：90% MiniMax，10% GLM-5

**詳細規則**：見 AGENTS.md

## 📋 OpenClaw 最佳實踐（2026-02-19 整合）

### 升級流程
- **升級前**：`systemctl stop clawdbot-gateway`
- **原因**：唔stop舊service → 兩個process撐18789 port → restart死循環

### 穩定性 (Stability)
- **Watchdog**：寫script每15分鐘ping /health端點，冇response自動重啟
- **一鍵修復**：`openclaw doctor --fix` → 自動修權限/目錄/過期配置
- **唔好死盯住佢**，用自動化

### 安全 (Security)
- **gateway.bind**：設loopback只監聽本地
- **外部訪問**：用Tailscale或Cloudflare Tunnel
- **公網暴露**：幾個鐘內必被掃，絕對避免

### Agent 行為規範
- **AGENTS.md寫死規則**：說done必須附repo+branch+commit hash
- **驗證方式**：必須跑命令驗證，不能只說"I checked"
- **Message Queue**：`messages.queue.mode`設collect，防止忙時丟消息

### 多Agent分工
| Role | Model | 職責 |
|------|-------|------|
| CEO | Opus | 對外通信、統一對接外部渠道 |
| CTO | Codex | 代碼、Technical決策 |
| COO | Haiku | 日常任務、內部協調 |

- **外部渠道只接CEO**
- **Subagent不能再派subagent**，保持一層delegation

### Memory 分層管理
- **MEMORY.md**：淨係做索引（會被70/20/10截斷，中間內容靜默丟失無提示）
- **詳細內容分層**：
  - `memory/active-tasks.md` → 進行中任務
  - `memory/projects.md` → 項目細節
  - `memory/lessons.md` → 學習教訓
- **共享狀態**：用`ln -s`建立連結，唔好複製文件

### Cron vs Heartbeat
| 類型 | 用途 | 特點 |
|------|------|------|
| **Heartbeat** | 主session定期巡檢 | 省token（保持<20行），發現問題先用 |
| **Cron** | 隔離session精確執行 | 獨立上下文，唔加載歷史 |

- **唔好混用**

### Crash Recovery
- **active-tasks.md**：記錄進行中任務 + session key
- **Boot.md**：啟動時讀取自動恢復
- **compaction.memoryFlush.enabled: true** → 壓縮前先存盤
- **contextPruning**：用`cache-ttl/30m`自動裁剪過期工具輸出

### Debug 鐵律
- **出事先睇**：`gateway.err.log`
- **唔好估估吓**

### 參考來源
- 2026-02-19：小紅書「openclaw踩坑指南」實戰經驗整合

### High Priority
1. **x-post-automation** - Twitter/X API
2. **xiaohongshu** - 小紅書 API (needs security review first)
3. **grok-ai-video** - Grok API (emerging tool from 2026-02-19)

### Medium Priority
4. **seo-content-writer** - SEO APIs
5. **ai-automation-workflows** - AI provider APIs
6. **afrexai-business-automation** - Business APIs

---
*Last updated: 2026-02-20*
*詳細記錄：`memory/skills-pending-api.md`*

---

## 📅 每週報告索引

### 2026-W8 (2月14日-20日)
**報告位置**: `memory/weekly-summary-2026-W8.md`

#### 本週掃描統計
- **掃描 Skills**: 24+ 個
- **深度分析**: 9+ 個
- **安全安裝**: 1 個 (automation-workflows)
- **風險標記**: 14+ 個

#### 風險分類
- 🔴 高風險: 10+ 個 (VirusTotal 標記)
- 🟡 中風險: 4+ 個 (概念記錄)
- 🟢 已安裝: 1 個

#### 重點發現
- ⚠️ **ClawHavoc 攻擊**: 341 個惡意 Clawed skills 被發現
- ✅ **安全策略**: 繼續使用 ClawSec，拒絕高風險 skills
- 📚 **學習成果**: AI Trends 2026, Multi-agent Architecture
- 🎯 **項目進展**: YouTube Automation Suite 設計中

#### 下週重點
1. 繼續安全掃描（輕量 + 深度）
2. 優先檢查待處理 skills (ai-automation-workflows 等)
3. 開發 content-creator-local

---

## 📊 2026-02-20 深度學習 - AI Trends 全面分析

### 核心發現

**1. Agentic AI 元年降临**
- Gartner 預測：40% 企業應用將嵌入 AI agents（2026年底）
- 市場規模：$7.8B → $52B（2030）
- MCP 標準化：Anthropic → OpenAI/Microsoft/Google/Linux Foundation

**2. 從 Scaling 到 Efficiency 轉向**
- Fine-tuned SLMs 取代通用 LLM（AT&T、IBM 確認）
- 邊緣運算主流化
- 硬件多元化：ASIC, chiplet, analog, quantum

**3. Super Agents 時代**
- 跨功能、跨環境協作
- Agent Control Planes 成為新介面
- 統一 Dashboard 管理多 agents

**4. YouTube Automation 2026 變革**
- AI 內建工具：auto-dubbing, Dream Screen, automated editing
- Analytics 轉向「有意義觀眾」
- Shopping 成為核心收入層
- Courses 成熟為完整學習平台

**5. 數據品質瓶頸**
- Unstructured data 噪音問題嚴重
- 缺乏上下文導致 autonomous agents 風險
- Metadata 與治理投資增加

**6. Physical AI 主流化**
- 機器人、AVs、drones、wearables 進入主流
- 雲端模擬 (Opex) 取代 Capex
- World Models 遊戲市場 $276B（2030）

**7. 人類增強而非取代**
- Katanforoosh: "2026 will be the year of the humans"
- AI 未能如預期自主 → 對話轉向 augment
- 新職位：AI 治理、透明、安全、數據管理

### 關鍵引述

> "It's a buyer's market... The model itself is not going to be the main differentiator."
> — Gabe Goodhart, IBM

> "Physical AI will hit the mainstream in 2026 as new categories of AI-powered devices... start to enter the market."
> — Vikram Taneja, AT&T Ventures

> "Fine-tuned SLMs will be the big trend and become a staple used by mature AI enterprises in 2026"
> — Andy Markus, AT&T

### 行動建議

**YouTube Automation 方向** ✅ 已驗證
- Niche 選擇：Tech/AI ($35-45 CPM)
- AI 工具整合：auto-dubbing, editing
- 多代理工作流：Research → Creation → Optimization → Publishing → Monitoring

**Multi-agent 技能** ✅ 已有 skill
- Multi-agent-orchestrator-local
- 學習 MCP 標準化
- 實踐 agent evaluation frameworks

**持續監控**
- AI automation trends（季度）
- YouTube platform changes（每月）
- Agentic AI developments（每月）
- Hardware breakthroughs（半年）

### 與現有項目關聯

| 項目 | 2026 趨勢 | 行動 |
|------|-----------|------|
| YouTube Automation | AI 內建工具、Shoppping 成核心 | 整合 YouTube API + AI tools |
| multi-agent-orchestrator | Super Agents 趨勢 | 持續優化 |
| Local Business Automation | 垂直領域解決方案 | 擴展 niche 覆蓋 |

### 筆記位置
- 完整分析：`memory/learning/2026-02-20-ai-trends.md`
- 來源：IBM, TechCrunch, InformationWeek, PwC, Primescroll, Ping Network
