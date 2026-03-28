# AI Video Hub v2 - 使用指南

> **Last Updated**: 2026-03-18
> **Version**: 2.0

---

## 📋 目錄

1. [快速開始](#快速開始)
2. [功能介紹](#功能介紹)
3. [API 設定](#api-設定)
4. [字幕生成](#字幕生成)
5. [雲端同步](#雲端同步)
6. [多語言切換](#多語言切換)
7. [常見問題](#常見問題)

---

## 🚀 快速開始

### Step 1: 打開程式

1. 去呢個位置：
   ```
   /Users/cken0218/.openclaw/media/inbound/
   ```
2. 搵 `ai_video_hub---f3ff42ab-204d-428d-8c60-6de06d742295`
3. Double-click 用 Safari/Chrome 打開

### Step 2: 設定 API Keys

去「API 設定」page，輸入：

| API | 點樣拎 | 必需？ |
|-----|--------|--------|
| MiniMax API Key | [minimaxi.com](https://www.minimaxi.com) | ✅ 必需 |
| YouTube API Key | Google Cloud Console | ✅ 必需（上傳片用）|
| N8n Webhook | N8n 自建 | ❌ 可選 |
| Google Drive API | Google Cloud Console | ❌ 可選（雲端sync）|

### Step 3: 開始生成影片

1. 選擇頻道
2. 輸入影片主題
3. 揀語言（廣東話/普通話/English）
4. Click 「開始生成影片」

---

## 🎯 功能介紹

### 1. 一鍵生成影片
- 輸入主題 → AI 自動寫脚本 → 配音 → 生成影片 → 上傳 YouTube

### 2. 腳本生成器
- 獨立生成脚本
- 支援風格：教育/娛樂/新聞/放鬆
- 支援語言：廣東話/普通話

### 3. AI 配音
- TTS 語音合成
- 多種聲線選擇

### 4. 字幕生成器 🆕
- 輸入文字 → 自動生成 SRT/VTT 字幕
- 支援語言：廣東話/普通話/English

### 5. 排程發佈
- 預約時間發佈 YouTube

### 6. 雲端同步 🆕
- Google Drive API 連接
- 多部電腦共享數據

---

## 🔑 API 設定

### MiniMax API Key（必需）

1. 去 [minimaxi.com](https://www.minimaxi.com)
2. Register/Login
3. 去 API Keys 頁面
4. Copy Key，貼去 setting

### YouTube API Key

1. 去 [Google Cloud Console](https://console.cloud.google.com)
2. Create Project
3. Enable YouTube Data API v3
4. Create Credentials → API Key
5. Copy Key，貼去 setting

### Google Drive API（可選）

1. 去 [Google Cloud Console](https://console.cloud.google.com)
2. Enable Google Drive API
3. Create OAuth 2.0 Client ID
4. Get Client ID + Client Secret
5. 貼去 setting，click 「連接 Google Drive」

---

## 📝 字幕生成

### 使用方法

1. 去「字幕生成器」page
2. 選擇輸入方式：
   - **輸入文字**：直接貼脚本
   - **上傳影片**：語音轉文字（需要 N8n/Whisper）
3. 揀字幕語言
4. Click 「生成字幕」
5. Download SRT/VTT

### 下載格式

| 格式 | 用途 |
|------|------|
| SRT | 大部分影片編輯軟件 |
| VTT | 網頁字幕、YouTube |

---

## ☁️ 雲端同步

### 設定 Google Drive

1. 去 API 設定
2. 輸入 Client ID + Secret
3. Click 「連接 Google Drive」
4. 授權比你既 Google Account

### 同步範圍

- ✅ 頻道設定
- ✅ 發佈歷史
- ✅ API Keys（加密）
- ❌ 影片檔案（需要自己備份）

### 多部電腦使用

1. 每部電腦都設定同一個 Google Account
2. Click 頂部雲朵 icon 一鍵同步
3. 數據會自動同步

---

## 🌐 多語言切換

### 使用方法

Click 頂部 🌐 icon 可以切換：
- 中文（預設）
- English

---

## ❓ 常見問題

### Q: 點解生成唔到片？

A: 檢查：
1. MiniMax API Key 啱唔啱？
2. N8n Webhook 有冇設定？
3. 網絡有冇問題？

### Q: 字幕生成係咪即時既？

A: 目前既字幕係基於你既文字輸入生成既 時間軸如果要從影片自動生成字幕，需要設定 N8n + Whisper API

### Q: 可以用幾多部電腦？

A: 無上限！只要連接同一個 Google Account 就得

### Q: 啱啱既 AI Video Hub 檔案喺邊？

A: 
```
/Users/cken0218/.openclaw/media/inbound/ai_video_hub---f3ff42ab-204d-428d-8c60-6de06d742295
```

---

## 📞 支援

有問題既話，可以問 Ken (我)！

---

*Last updated: 2026-03-18*
