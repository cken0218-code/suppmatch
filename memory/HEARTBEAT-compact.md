# HEARTBEAT-compact - 心跳规则精简版

> **Last Updated**: 2026-03-13
> **Version**: 2.0
> **Purpose**: 启动时必读（核心规则，50 行以内）

---

## ⏰ 執行時間表（Asia/Taipei）

### Cron 格式
```
# 項目監控（平日朝早）
0 9 * * 1-5

# Trending + 知識更新（每日兩次）
0 12,18 * * *

# 記憶壓縮（每週五）
0 20 * * 5
```

### 執行規則
- **每 3 小時執行一次**（唔係 30 分鐘）
- **深夜停止**：23:00-08:00 完全停止
- **週末減量**：六日淨做緊急任務

---

## 🔁 每日例行檢查（一至五）

### 💹 早市掃描（08:30）
- BTC、SOL 24h 變化
- Fear & Greed Index
- 澳股昨日收市
- **異常警報**：單日波動 > 5% → Telegram DM

### 📊 項目監控（09:00）
- Git repo 狀態
- GitHub notifications / issues / PRs

### 🔍 Trending Content（12:00 + 18:00）
- X (Twitter) trending
- GitHub trending
- YouTube trending（只讀元數據，不能看视频）

### 🧠 知識更新（15:00）
- 學習搜索：
  - YouTube automation 2026
  - Affiliate marketing trends 2026
  - AI passive income tools 2026
  - **Multi-agent orchestration 2026** ⭐ 新增
  - **MCP protocol integration** ⭐ 新增
  - **AI company architecture** ⭐ 新增
- AI 新聞 / 更新

---

## 📅 每週任務

### 週五（重點日）
- 🎯 **機會掃描**（13:00）- Reddit + YouTube
- 📧 **Newsletter 發布**（10:00）
- 🔍 **ClawHub Skills 掃描**（13:50）
- 📊 **投資機會清單**（13:35）
- 🧹 **記憶壓縮**（20:00）

### 週日
- 📝 **L2-Weekly 摘要**（晚上）
- 翻閱過去 7 日 L1-daily
- 發現跨日鏈接 → 通知用戶

---

## 💓 Heartbeat 報告格式

```
🐱 Heartbeat 報告
━━━━━━━━━━━━━━━━
狀態：[狀態] [emoji]
模型：[當前模型]
今次做咗：
- [具體事項1]
- [具體事項2]
有咩要你知：
- [有趣發現/問題/建議]
```

### 狀態選項
- ✅ 正常運作中
- ⚡ 忙碌緊
- 🔄 初始化緊
- ❌ 有問題

---

## 💰 Quota 監控

### 每次 Heartbeat 檢查
```json
{
  "brave": {"used": 303, "total": 2000, "percent": 15},
  "lastCheck": "2026-02-23T14:00:00Z"
}
```

### 規則
- **< 80%**：正常執行搜尋
- **≥ 80%**：停止搜尋，記憶整理模式
- **API 失敗**：自動切換 provider

---

**详细版本**：见 `HEARTBEAT.md`（211 行）
**详细任务清单**：见 `memory/heartbeat-tasks.md`
**Created**: 2026-03-13
**Status**: Active
