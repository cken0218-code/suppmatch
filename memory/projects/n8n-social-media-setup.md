# N8n 社交媒體內容製作工廠 - 設置指南

> 創建日期：2026-03-19

---

## 1. N8n 基礎設置

### 點樣安裝？

| 方法 | 難度 | 費用 |
|------|------|------|
| **Cloud** (n8n.io) | 易 | $0-20/月 |
| **Self-hosted** (Docker/VPS) | 中 | $5-10/月 |

### 建議
如果淨係自己用，**Cloud free tier** 已經夠：
- 每月 100 workflow runs
- 基本 nodes 都有

---

## 2. 你需要既 API Keys

### 必須既

| API | 用途 | 点樣拎 |
|-----|------|--------|
| **YouTube Data API** | 上傳影片、獲取數據 | Google Cloud Console |
| **Twitter/X API** | 發布post | developer.twitter.com |
| **OpenAI / MiniMax** | AI 生成內容 | OpenAI.com / MiniMax |

### 可選既

| API | 用途 |
|-----|------|
| **Google Sheets** | 儲存數據 |
| **Telegram Bot** | 通知你 |
| **Discord Webhook** | 發送通知 |
| **Pinterest API** | Pinterest 自動發布 |

---

## 3. 常用 Workflow 模板

### A. AI 內容生成 → 發布到多平台

```
[Google Trends] → [AI 生成內容] → [YouTube] → [Twitter] → [Telegram 通知]
```

**N8n Template**: [AI-powered multi-social media automation](https://n8n.io/workflows/4352-ai-powered-multi-social-media-post-automation-google-trends-and-perplexity-ai/)

### B. 影片自動上傳 YouTube

```
[AI 生成影片] → [YouTube Upload] → [Database] → [Telegram 通知]
```

### C. 熱門話題 → 內容生成

```
[Reddit/Twitter Trending] → [AI 分析] → [生成標題] → [Google Sheets]
```

---

## 4. 設置步驟

### Step 1: 註冊 N8n Cloud
1. 去 [n8n.io](https://n8n.io)
2. Sign up (可以用 Google account)
3. 選擇 free plan

### Step 2: 連接 API

#### YouTube API
1. 去 [Google Cloud Console](https://console.cloud.google.com)
2. Create Project
3. Enable "YouTube Data API v3"
4. Credentials → Create API Key

#### Twitter/X API
1. 去 [developer.twitter.com](https://developer.twitter.com)
2. Create App
3. 拎 API Key + API Secret + Bearer Token

#### OpenAI / MiniMax
- **OpenAI**: 去 [platform.openai.com](https://platform.openai.com)
- **MiniMax**: 去 [platform.minimax.io](https://platform.minimax.io)

### Step 3: 建立第一個 Workflow

1. Click "Workflows" → "New"
2. 添加 Trigger (例如：Schedule / Webhook)
3. 添加 Action Nodes (例如：HTTP Request / AI)
4. 測試 → Activate

---

## 5. 推薦既 N8n Templates

| Template | 用途 | 連結 |
|----------|------|------|
| AI Social Media Poster | AI 生成 → 多平台發布 | [Link](https://n8n.io/workflows/4352-ai-powered-multi-social-media-post-automation-google-trends-and-perplexity-ai/) |
| YouTube Auto Upload | 自動上傳 YouTube | [Link](https://n8n.io/workflows/5035-generate-and-auto-post-ai-videos-to-social-media-with-veo3-and-blotato/) |
| Content Repurposing | 一個內容 → 多平台 | [Link](https://n8n.io/workflows/categories/social-media/) |

---

## 6. 常見問題

### Q: N8n 同 Make/Zapier 既分別？

| Feature | N8n | Make | Zapier |
|---------|-----|------|--------|
| 免費版 | ✅ 100 runs | ✅ 1000 ops | ✅ 100 tasks |
| 自托管 | ✅ | ❌ | ❌ |
| AI Nodes | ✅ | ✅ | ✅ |
| 學習曲線 | 中等 | 易 | 易 |

### Q: API 要錢嗎？

| API | 免費額度 |
|-----|----------|
| YouTube | 10,000 quota units/日 |
| Twitter | App-only: 500,000/月 |
| OpenAI | $5 credit |
| MiniMax | 免費註冊有 credit |

---

## 7. 下一步

1. ✅ 註冊 N8n Cloud
2. ✅ 拎 YouTube API Key
3. ✅ 拎 MiniMax / OpenAI API Key
4. ✅ 導入第一個 Template
5. ✅ 測試

---

有唔明既地方可以問我！
