# HEARTBEAT.md - 每日自動維護系統

## 🔁 每日例行檢查（一至五）

### 📊 項目監控（Morning ~09:00）
- [ ] 檢查所有 git repo 狀態（branch, uncommitted changes）
- [ ] 檢查 GitHub notifications / issues / PRs
- [ ] 有異常就 alert shikiouo

### 🔍 Trending Content（每日2次：朝早9點 + 晏晝6點）
- [ ] X (Twitter) trending（keywords: AI, automation, YouTube, agent, workflow, 網上賺錢）
- [ ] 有發現就記錄 + alert（filter過濾垃圾資訊）

### 🧠 知識更新（Afternoon ~15:00）
- [ ] 爬 AI 新聞 / 更新（OpenAI, Anthropic, 開源項目）
- [ ] 有重要更新就整理 + alert
- [ ] 來源：Twitter AI 圈、GitHub trending、ProductHunt

### 📝 錯誤追蹤（Evening ~20:00）
- [ ] 回顧今日 session 做錯嘅嘢
- [ ] 記錄落 `memory/errors/YYYY-MM-DD.md`
- [ ] 更新 MEMORY.md 長期記憶（如果需要）

### 🧹 記憶整理（每週五）
- [ ] Archive 超過7日既 L1-daily 檔案
- [ ] Archive 超過30日既 L2-weekly 檔案
- [ ] 更新 `memory-cleanup-log.md`

### 🔧 工作流程優化（Friday Afternoon）
- [ ] 檢視本週 HEARTBEAT 執行情況
- [ ] 更新 SKILL.md / TOOLS.md（如有改善空間）
- [ ] 整理 `memory/` folder

### 💬 自動提醒
- [ ] 重要會議 / 截止日期（需整合 calendar）
- [ ] 定期任務到期提醒

## ⏰ 執行時間表（Asia/Taipei）
```
09:00 - 項目監控
12:00 - Trending + 知識更新（合併）
18:00 - Trending + 錯誤追蹤（合併）
```

**⚠️ 優化後規則**：
- **每 3 小時執行一次**（唔係 30 分鐘）
- 深夜時段（23:00-08:00）完全停止
- Brave API quota 監控：>15% 就停止搜尋
- 如遇 API 失敗，改為記憶整理模式

## 💓 帶屬性Heartbeat（每次觸發時報告）

### 報告格式
每次heartbeat觸發時，report以下資訊：

```
🐱 Heartbeat 報告
━━━━━━━━━━━━━━━━
狀態：正常運作中 ✅
模型：MiniMax-M2.5
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
- 每次heartbeat trigger都要report（除非深夜）
- 有job完成要主動通知
- 發現有趣嘢要alert

### ⚠️ 注意事項
- 深夜 23:00-08:00 唔好打擾，除非 urgent
- 週末（六日）淨做緊急任務
- 所有 alert 經 Discord DM（ken000ken）
- 新學到嘅重要嘢要更新落 MEMORY.md

## 🎯 追蹤目標
- YouTube Automation 項目進度
- 網賺工具開發狀態
- AI 流程自動化學習
- 錯誤唔重犯

---
*Last updated: 2025-01-16*
