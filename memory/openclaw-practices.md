# OpenClaw 最佳實踐

> **Last Updated**: 2026-02-19
> **Source**: 小红书「openclaw踩坑指南」实战经验

---

## 升級流程

- **升級前**：`systemctl stop clawdbot-gateway`
- **原因**：唔stop舊service → 兩個process撐18789 port → restart死循環

---

## 穩定性 (Stability)

- **Watchdog**：寫script每15分鐘ping /health端點，冇response自動重啟
- **一鍵修復**：`openclaw doctor --fix` → 自動修權限/目錄/過期配置
- **唔好死盯住佢**，用自動化

---

## 安全 (Security)

- **gateway.bind**：設loopback只監聽本地
- **外部訪問**：用Tailscale或Cloudflare Tunnel
- **公網暴露**：幾個鐘內必被掃，絕對避免

---

## Agent 行為規範

- **AGENTS.md寫死規則**：說done必須附repo+branch+commit hash
- **驗證方式**：必須跑命令驗證，不能只說"I checked"
- **Message Queue**：`messages.queue.mode`設collect，防止忙時丟消息

---

## 多Agent分工

| Role | Model | 職責 |
|------|-------|------|
| CEO | Opus | 對外通信、統一對接外部渠道 |
| CTO | Codex | 代碼、Technical決策 |
| COO | Haiku | 日常任務、內部協調 |

### 规则
- **外部渠道只接CEO**
- **Subagent不能再派subagent**，保持一層delegation

---

## Memory 分層管理

- **MEMORY.md**：淨係做索引（會被70/20/10截斷，中間內容靜默丟失無提示）
- **詳細內容分層**：
  - `memory/active-tasks.md` → 進行中任務
  - `memory/projects.md` → 項目細節
  - `memory/lessons.md` → 學習教訓
- **共享狀態**：用`ln -s`建立連結，唔好複製文件

---

## Cron vs Heartbeat

| 類型 | 用途 | 特點 |
|------|------|------|
| **Heartbeat** | 主session定期巡檢 | 省token（保持<20行），發現問題先用 |
| **Cron** | 隔離session精確執行 | 獨立上下文，唔加載歷史 |

- **唔好混用**

---

## Crash Recovery

- **active-tasks.md**：記錄進行中任務 + session key
- **Boot.md**：啟動時讀取自動恢復
- **compaction.memoryFlush.enabled: true** → 壓縮前先存盤
- **contextPruning**：用`cache-ttl/30m`自動裁剪過期工具輸出

---

## Debug 鐵律

- **出事先睇**：`gateway.err.log`
- **唔好估估吓**

---
*Last updated: 2026-02-19*
