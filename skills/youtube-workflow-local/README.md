# YouTube Workflow Local - 自動產出系統

> **Version**: 2.0
> **Created**: 2026-03-13
> **Updated**: 2026-03-29
> **Status**: ✅ Production Ready

---

## 🎯 功能

自動化 YouTube 內容產出流程：
1. **Trending 搜尋** - 自動發現熱門話題
2. **腳本生成** - 基於 persona 生成完整腳本
3. **變現整合** - 自動加入 affiliate 連結

---

## 🚀 快速開始

### 第一次使用

```bash
# 1. 進入工作目錄
cd /Users/cken0218/.openclaw/workspace

# 2. 執行完整流程
python3 skills/youtube-workflow-local/run.py

# 3. 查看產出
ls -lht youtube-scripts/
```

### 輸出文件

執行後會生成 3 個文件：
- `trending-2026-03-29.json` - Trending 搜尋結果
- `script-2026-03-29-1250.md` - 完整 YouTube 腳本
- `notification-2026-03-29-1250.txt` - 通知訊息（可發送到 Telegram/Discord）

---

## 📋 腳本結構

每個生成的腳本包含：

### 1️⃣ Hook（15 秒）
- 問問題、數據震驚、痛點共鳴、承諾價值

### 2️⃣ 痛點（30-60 秒）
- 列舉症狀、情景描述、情感連結

### 3️⃣ 解決方案（60-90 秒）
- **AI 類主題**：工具推薦（ChatGPT、vidIQ、Canva AI、ElevenLabs、Descript 等）
- **健康類主題**：生活習慣、營養補充、實用技巧

### 4️⃣ 示範（30-60 秒）
- 親身體驗、用戶見證、數據支持

### 5️⃣ CTA（15-30 秒）
- 訂閱、留言、點擊連結、分享

---

## 💰 變現整合

### 主要 Affiliate
- **CustomGPT** - 20% recurring commission
- **Amazon Associates** - 相關產品推薦

### 整合位置
- 簡介欄連結
- 腳本內提及
- CTA 引導

---

## ⚙️ 自動化設置

### Cron Job（推薦）

```bash
# 編輯 crontab
crontab -e

# 每週一、三、五 10:00 執行
0 10 * * 1,3,5 cd /Users/cken0218/.openclaw/workspace && /usr/bin/python3 skills/youtube-workflow-local/run.py >> logs/youtube-workflow.log 2>&1
```

### 日誌查看

```bash
# 查看最近執行記錄
tail -50 logs/youtube-workflow.log

# 查看今日產出
ls -lht youtube-scripts/ | grep $(date +%Y-%m-%d)
```

---

## 📊 預期效果

### 產出量
- **每週**：3 個腳本
- **每月**：12-13 個腳本
- **拍攝率**：50%（6-7 條影片/月）

### 收入預測（保守）

| 來源 | 每條片 | 每月（6條） |
|------|--------|-------------|
| AdSense | $100-200 | $600-1200 |
| Affiliate | $50-500 | $300-3000 |
| **總計** | $150-700 | **$900-4200** |

---

## 🔧 技術細節

### 依賴
- Python 3.9+
- 無外部依賴（純 Python）

### 架構
```
run.py (主控)
    ├── trending_search.py (搜尋模組)
    └── script_generator.py (生成模組)
```

### 擴展性
- 可加入真實 web_search API（當 OpenClaw 支援時）
- 可加入 Telegram/Discord 通知
- 可整合自動發布系統

---

## 📝 配置

### Content Persona
位置：`memory/projects/content-persona.md`

修改 persona 以調整：
- 主題定位
- 語言風格
- 目標受眾
- CTA 策略

### Affiliate 連結
位置：`script_generator.py` 的 `generate_script()` 函數

---

## 🐛 故障排除

### 找不到 trending 文件
**原因**：路徑問題
**解決**：確保在 workspace 目錄執行

### web_search 不可用
**狀態**：正常，會降級到本地模擬
**影響**：使用預設 trending 話題

### 腳本內容不準確
**解決**：調整 `script_generator.py` 的內容生成邏輯

---

## 🚀 未來發展

- [ ] 整合真實 web_search API
- [ ] 加入 Telegram/Discord 通知
- [ ] 整合自動縮圖生成
- [ ] 加入競爭對手分析
- [ ] 整合自動發布（YouTube API）

---

## 📚 相關資源

- **Content Persona**: `memory/projects/content-persona.md`
- **學習報告**: `memory/learning/2026-03-29-token-maximizer.md`
- **趨勢分析**: `memory/reports/trending-analysis-2026-03-29.md`
- **YouTube Skills**: `skills/youtube-*`

---

**Created by**: Ken AI Assistant 🐱
**GitHub**: (如有)
**License**: MIT
