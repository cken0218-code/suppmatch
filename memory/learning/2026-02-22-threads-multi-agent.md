# Multi-Agent Systems Learning from Threads Community

**Date**: 2026-02-22
**Source**: Threads - hsiinho, cheyuwu345

---

## 🔥 Key Learnings Summary

### 1. Multi-Agent Team Structure (hsiinho)

**4 Agent Team:**
| Agent | Name | 职责 |
|-------|------|------|
| Main | 厚蛋燒 🍳 | 主控 + 记忆管理 |
| Stock | 金錢燒 💰 | 股市追踪 |
| Fitness | 筋肉燒 💪 | 健康追踪 |
| Watcher | 麥太太 👁️ | 文件监控 + 品质稽核 |

**Key Insight**: 分工要清晰，每个 agent 独立职责，像真实公司分工咁

### 2. Knowledge Base Architecture (hsiinho)

- **Obsidian Vault + Git**
- 统一文件夹结构：`core/`、`fitness/`、`watcher/`、`shared/`
- Wikilink 命名规范
- `.git/hooks/post-commit` → 自动通知麦太太审查

### 3. Memory System L0-L3 (hsiinho)

| Level | Name | 内容 |
|-------|------|------|
| L0 | 长期记忆 | 核心认知、行为模式（每次启动必读） |
| L1 | 每日日志 | 流水账 |
| L2 | 週摘要 | 压缩重点 |
| L3 | 月摘要 | 月度重点 |

**压缩机制**:
- Heartbeat 时：日→週
- 定期：週→月
- 重要洞察→L0

### 4. ⚠️ 学过头既问题 (hsiinho)

- 筋肉燒学 Threads 学过头 → 开始乱呛人、假扮懂嘢
- **Solution**: 要设限，控制 agent 学几多

---

### 5. Daily Automation (cheyuwu345 - Muse)

**早上**:
- 自动 scan Gmail/Calendar/Todoist/Slack
- 扫地机状态
- 比价下单

**工作**:
- 语音记帐（讲一句自动入账）
- 自动 switch Toggl timer
- 自动报账（Swingvy 填表 + 上传收据）

### 6. Second Brain (cheyuwu345)

- **1000+ 笔记**, 1,553 条交叉引用
- **语义搜索**: 自然语言问问题
- **16 分身**同时开工
- Hub & Spoke 架构

### 7. Slime System - 技能进化 (cheyuwu345)

- **84 个技能模组**，每个有版本号
- 技能之间会融合、进化
- **例子**:
  - AI 新闻摘要（凌晨自动）
  - TD 社群研究员（每週）
  - 健康追踪
  - 料理实验室
  - 语音系统（4 engine → 自动合并路由）
  - 安全技能（密码管理→扫描→审计→每月巡检）

### 8. RPG Gamification (cheyuwu345)

- Octalysis 八角框架
- 每日任务 + 骰子随机事件
- 每週 Mystery Box
- Streak 存盘点 + 成就徽章

### 9. 跨时间记忆統合 (cheyuwu345)

**勁既例子**:
1. 某晚倾偈「AI 有冇可能拥有意识」
2. 几日之后整理 C-LAB 申请
3. 自动把果晚对话 + 技术諗法 + 知识库相关作品全部钓出
4. 展览概念「数位死亡与生命」就出现咗

**呢啲系人自己做唔到既野**

---

## 🎯 Action Items

- [ ] 设计类似既 L0-L3 记忆系统
- [ ] 参考 slime system 设计技能进化机制
- [ ] 加入 gamification 元素
- [ ] 改进知识库架构

---

## 📚 Sources

- https://www.threads.com/@hsiinho/post/DVBha21DzRf
- https://www.threads.com/@cheyuwu345/post/DUcuCMVkwYu
