# HEARTBEAT.md - 每日自動維護系統

> **Last Updated**: 2026-03-11
> **Version**: 3.0

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

### 💹 早市掃描（08:30，每日）
- [ ] BTC、SOL 24h 變化 + 主要方向（用 coingecko skill）
- [ ] Fear & Greed Index（市場情緒）
- [ ] 澳股昨日收市狀況（用 aus-stock-tracker）
- [ ] 有無重大新聞影響市場（搜 "crypto news today" + "ASX news today"）
- [ ] 結果寫入 `memory/L1-daily/今日.md` 嘅「市場摘要」部分
- [ ] 如有異常走勢（>5% 單日波動）立即 Telegram DM 通知

#### ⚠️ 觸發規則：高風險警報
**如果 BTC 單日跌幅 > 8%**：
- 🚨 立即通知（Telegram DM）
- 標籤：⚠️ **高風險警報**
- 內容包括：
  - 當前跌幅
  - 可能原因（新聞/事件）
  - 建議行動（唔係投資建議，係提醒）

**Cron 設置**：
```bash
# 每日早市掃描（08:30，平日）
30 8 * * 1-5 openclaw trigger heartbeat market-scan
```

---

### 📊 項目監控（09:00）
- [ ] 檢查所有 git repo 狀態
- [ ] 檢查 GitHub notifications / issues / PRs
- [ ] 有異常就 alert shikiouo

### 🔍 Trending Content（12:00 + 18:00）
- [ ] X (Twitter) trending（搜索 + 文字分析）
- [ ] GitHub trending（API + README 分析）
- [ ] **YouTube trending**（搜索 + 元数据分析，**⚠️ 不能看视频内容**）
- [ ] **小紅書 trending**（RPA + 文字爬取，**⚠️ 需要 cookie，不能看图片/视频**）
- [ ] 有發現就記錄 + alert

**⚠️ 技術限制說明**：
- **YouTube**：只能爬取標題、描述、標籤、字幕（如果有），**不能真正"看"視頻**
- **小紅書**：只能爬取文字內容，**不能看圖片/視頻**，需要 cookie 登入
- **實際做法**：基於文字元數據識別趨勢，而非視覺內容分析

**小紅書 Trending 監控**：
```bash
# 每日 10:00 執行（需要 cookie）
0 10 * * * cd ~/.openclaw/workspace && python3 skills/xiaohongshu/scripts/trending_monitor.py
```

**YouTube Trending 監控**（實際可行）：
```bash
# 使用 YouTube Data API 或搜索
# 只讀取元數據（標題、描述、標籤）
# 不能分析視頻內容
```

### 🧠 知識更新（15:00）
- [ ] **定期学习搜索**（每次 heartbeat）：
  - "YouTube automation 2026"
  - "affiliate marketing trends 2026"
  - "AI passive income tools 2026"
- [ ] AI 新聞 / 更新（OpenAI, Anthropic, 開源項目）
- [ ] 有重要更新就整理 + alert
- [ ] 学习笔记保存到 `memory/learning/YYYY-MM-DD-heartbeat-learning.md`

### 📝 錯誤追蹤（20:00）
- [ ] 回顧今日 session 做錯嘅嘢
- [ ] 記錄落 `memory/errors/YYYY-MM-DD.md`

---

## 🧹 記憶整理（每週五）

### 自動壓縮
- [ ] L1-daily 超過 7 日 → 壓縮到 L2-weekly
- [ ] L2-weekly 超過 30 日 → 壓縮到 L3-monthly
- [ ] 更新 `memory/memory-cleanup-log.md`

### 執行腳本
```bash
python3 scripts/compress-memory.py
```

**腳本功能**：
- 自動掃描 `L1-daily/` 目錄
- 移動超過7天嘅檔案到 `L2-weekly/`
- 移動超過30天嘅檔案到 `L3-monthly/`
- 更新 `memory-cleanup-log.md`
- 顯示壓縮統計

**Cron 設置**：
```bash
# 每週五晚上8點執行
0 20 * * 5 cd ~/.openclaw/workspace && python3 scripts/compress-memory.py
```

---

## 💰 Quota 監控

### 每次 Heartbeat 檢查

```json
// memory/quota-state.json
{
  "brave": {"used": 303, "total": 2000, "percent": 15},
  "lastCheck": "2026-02-23T14:00:00Z"
}
```

### 規則
- **< 80%**：正常執行搜尋任務
- **≥ 80%**：停止搜尋，改為記憶整理模式
- **API 失敗**：自動切換到另一個 provider

---

## 💓 帶屬性 Heartbeat 報告

### 報告格式
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
你有咩想我做？
```

### 狀態選項
- ✅ 正常運作中
- ⚡ 忙碌緊（處理緊job）
- 🔄 初始化緊
- ❌ 有問題（需要你睇）

### 匯報時機
- 每次 heartbeat trigger 都要 report（除非深夜）
- 有 job 完成要主動通知
- 發現有趣嘢要 alert

---

## ⚠️ 注意事項

- **深夜 23:00-08:00**：唔好打擾，除非 urgent
- **週末（六日）**：淨做緊急任務
- **所有 alert**：經 Telegram DM（主要聯絡渠道）
- **新學到嘅重要嘢**：更新落 MEMORY.md

---

## 🎯 追蹤目標

- YouTube Automation 項目進度
- 網賺工具開發狀態
- AI 流程自動化學習
- 錯誤唔重犯

---
*Last updated: 2026-03-11*
