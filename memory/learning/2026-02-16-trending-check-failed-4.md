# Trending Check 失敗記錄 #4

**時間**: 2026-02-16 16:29 (4:29 PM)
**原因**: Brave API 問題

## 失敗詳情

### 嘗試 1: YouTube automation 小紅書
- **錯誤**: 參數驗證失敗 (422)
- **原因**: search_lang 應該用 "zh-hans" 而唔係 "zh"
- **修正**: 下次用 "zh-hans" (簡體中文) 或 "zh-hant" (繁體中文)

### 嘗試 2: AI automation 網賺 Threads
- **錯誤**: Rate limit exceeded (429)
- **數據**: quota_current: 269/2000
- **Rate limit**: 1 req/sec
- **分析**: 雖然 quota 未爆，但短時間內發送多個 request 觸發 rate limit

## 建議改善

### 1. API 參數優化
```javascript
// 錯誤寫法
search_lang: "zh"

// 正確寫法
search_lang: "zh-hans"  // 簡體中文
search_lang: "zh-hant"  // 繁體中文
```

### 2. Rate Limit 策略
- **當前問題**: 多個 concurrent requests 觸發 rate limit
- **解決方案**: 
  - Sequential requests（一個接一個）
  - 加入 delay（至少 1 秒間隔）
  - 或者用 browser fallback

### 3. Fallback 機制
根據 MEMORY.md 之前嘅建議：
- 降低 cron 頻率至 2-3 小時
- 加入 browser fallback
- 考慮 Brave API paid plan

## 統計

### Brave API 使用情況
- **上次記錄** (14:29): 260/2000
- **今次記錄** (16:29): 269/2000
- **2 小時增量**: +9 requests
- **剩餘 quota**: 1731

### 今日失敗次數
1. 2026-02-16 14:29 - 第一次失敗（Brave API rate limit）
2. 2026-02-16 16:29 - 第二次失敗（參數錯誤 + rate limit）

## 下步行動

1. **修正 search_lang 參數**（立即）
2. **加入 request delay**（需要修改 cron job）
3. **考慮 browser fallback**（需要配置）
4. **檢討 cron 頻率**（目前每 30 分鐘一次，可能太密）

---
*這個失敗記錄有助於優化自動學習系統*
