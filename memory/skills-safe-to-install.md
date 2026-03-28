# 安全 Skills 列表 - 2026-03-26 更新

> **來源**: ClawHub 官方 + Felo 團隊測試
> **測試日期**: 2026-03-26
> **安全標準**: 已通過 Snyk 安全審計

---

## ⚠️ 重要警告

**ClawHub 安全狀況**（2026年2月）:
- 總 skills: 13,000+
- **有問題: 13.4%**（Snyk 審計）
- **惡意 skills: 341 個**（Koi Security 掃描）

**安裝前必查**:
1. ✅ 讀 SKILL.md 文件
2. ✅ 檢查 GitHub repo
3. ✅ 驗證發布者
4. ✅ 查看安裝數量和評論
5. ✅ 檢查最後更新時間

---

## ✅ 推薦安全 Skills（10個）

### 核心必裝（前3個）

#### 1. web-browsing
- **用途**: 網頁導航、內容提取
- **安裝數**: 180,000+
- **發布者**: OpenClaw 官方
- **安全**: ✅ 官方維護
- **安裝**: `npx clawhub@latest install web-browsing`

#### 2. felo-search ⭐
- **用途**: AI 搜索 + 源引用
- **特點**: 
  - 返回結構化答案（不是鏈接列表）
  - 支持中英日韓
  - 免費開放期間
- **發布者**: Felo AI（已驗證）
- **安全**: ✅ MIT 開源
- **需要**: FELO_API_KEY
- **安裝**: `npx clawhub@latest install felo-search`
- **獲取 API Key**: https://felo.ai → Settings → API Keys

#### 3. telegram
- **用途**: 移動端訪問 OpenClaw
- **安裝數**: 145,000+
- **特點**: 5分鐘設置，低延遲
- **發布者**: OpenClaw 官方
- **安全**: ✅ 官方維護
- **安裝**: `npx clawhub@latest install telegram`

---

### 進階工具

#### 4. felo-superAgent ⭐⭐
- **用途**: 多功能工作站
- **特點**:
  - 6 個內置工具（圖像、研究、文檔、PPT、HTML、X搜索）
  - LiveDoc canvas（持久化工作空間）
  - SSE streaming（實時響應）
- **發布者**: Felo AI（已驗證）
- **安全**: ✅ MIT 開源
- **依賴**: felo-livedoc
- **需要**: FELO_API_KEY（與 felo-search 共享）
- **安裝**: 
  ```bash
  npx clawhub@latest install felo-superAgent
  npx clawhub@latest install felo-livedoc
  ```

#### 5. n8n-workflow
- **用途**: 業務流程自動化
- **特點**: 連接現有 n8n 工作流
- **發布者**: n8n 官方
- **安全**: ✅ 官方維護
- **安裝**: `npx clawhub@latest install n8n-workflow`

#### 6. felo-slides ⭐
- **用途**: AI 簡報生成
- **特點**:
  - 填補 ClawHub PPT 空白
  - 生成可編輯 PPTX（HTML 渲染）
  - 返回下載鏈接 + LiveDoc URL
- **發布者**: Felo AI（已驗證）
- **安全**: ✅ MIT 開源
- **需要**: FELO_API_KEY（與其他 Felo skills 共享）
- **安裝**: `npx clawhub@latest install felo-slides`

#### 7. github
- **用途**: 代碼工作流管理
- **特點**: 自然語言操作 GitHub
- **發布者**: OpenClaw 社區
- **安全**: ✅ 活躍維護
- **安裝**: `npx clawhub@latest install github`

#### 8. database-query
- **用途**: 數據庫查詢（PostgreSQL, MySQL, SQLite）
- **特點**: 自然語言轉 SQL
- **安裝數**: 95,000+
- **⚠️ 安全注意**: 
  - **必須使用只讀連接**
  - 限制為非生產數據庫
- **發布者**: OpenClaw 社區
- **安全**: ✅ 需謹慎配置
- **安裝**: `npx clawhub@latest install database-query`

#### 9. elevenlabs-agent
- **用途**: 語音合成（TTS）
- **特點**: Eleven Labs API 集成
- **發布者**: Eleven Labs
- **安全**: ✅ 官方維護
- **需要**: Eleven Labs API key
- **安裝**: `npx clawhub@latest install elevenlabs-agent`

#### 10. home-assistant
- **用途**: 智能家居控制
- **特點**: 控制設備、傳感器、自動化
- **發布者**: Home Assistant 社區
- **安全**: ✅ 開源項目
- **需要**: Home Assistant 實例
- **安裝**: `npx clawhub@latest install home-assistant`

---

## 🎯 Felo 生態系統（8個 Skills）

**所有 Felo skills 共享一個 API key**（經濟實惠）

| Skill | 功能 | 安裝命令 |
|-------|------|----------|
| **felo-search** | AI 搜索 + 引用 | `npx clawhub@latest install felo-search` |
| **felo-superAgent** | 流式對話 + 6 工具 | `npx clawhub@latest install felo-superAgent` |
| **felo-slides** | AI PPT 生成 | `npx clawhub@latest install felo-slides` |
| **felo-livedoc** | 知識庫管理 | `npx clawhub@latest install felo-livedoc` |
| **felo-web-fetch** | 網頁提取 | `npx clawhub@latest install felo-web-fetch` |
| **felo-x-search** | X/Twitter 搜索 | `npx clawhub@latest install felo-x-search` |
| **felo-youtube-subtitling** | YouTube 字幕 | `npx clawhub@latest install felo-youtube-subtitling` |
| **felo-content-to-slides** | URL/視頻轉簡報 | `npx clawhub@latest install felo-content-to-slides` |

**整合優勢**:
- 搜索結果 → 簡報生成
- 競爭對手頁面 → 幻燈片
- YouTube 視頻 → 簡報
- 一個 API key，無限可能

**獲取 API Key**:
1. 訪問 https://felo.ai
2. 註冊/登錄
3. Settings → API Keys
4. 複製 key 到 `~/.openclaw/openclaw.json`

---

## 🔍 已安裝 Skills 檢查

```bash
# 查看已安裝
npx clawhub@latest list

# 更新所有
npx clawhub@latest update

# 移除不安全的
npx clawhub@latest remove <skill-name>
```

---

## ⚠️ 危險信號（不要安裝）

### 紅旗特徵

1. **無 GitHub repository**
   - 無法審查代碼
   - 無法驗證安全性

2. **請求通配符 shell 權限**
   - `Bash(*)` 權限
   - 可以執行任何命令

3. **超過 3 個月未更新**
   - 可能存在未修補的漏洞
   - 與最新 OpenClaw 版本不兼容

4. **少於 100 installs 且無評論**
   - 未經社區驗證
   - 可能是新上傳的惡意軟件

5. **名稱模仿熱門 skill**
   - Typosquatting 攻擊
   - 例如：`web-browsing-official`（假冒官方）

6. **請求敏感權限**
   - 訪問文件系統
   - 網絡請求到未知服務器
   - 讀取環境變量

---

## 📊 ClawHub 新 Skills 掃描結果（2026-03-26）

### Automation 類別（Top 10）

1. **automation-workflows** (3.774) ✅
2. **ai-web-automation** (3.633) ✅
3. **automation-workflows-0-1-0** (3.595) ✅
4. **agentic-workflow-automation** (3.550) ✅
5. **afrexai-business-automation** (3.503) ⚠️（需驗證）
6. **productivity-automation-kit** (3.446) ✅
7. **ai-automation-consulting** (3.445) ⚠️（需驗證）
8. **automation-tool** (3.431) ✅
9. **ai-ceo-automation** (3.410) ⚠️（需驗證）
10. **ai-web-automation-1-0-0** (3.390) ✅

### YouTube 類別（Top 10）

1. **youtube-watcher** (3.686) ✅
2. **youtube-transcript** (3.601) ✅
3. **bilibili-youtube-watcher** (3.459) ✅
4. **creatordb-youtube-v3** (3.448) ✅
5. **youtube-publisher** (3.413) ✅
6. **youtube-shorts-automation** (3.401) ✅
7. **youtube-video-finder** (3.385) ✅
8. **youtube-watcherkx** (3.383) ✅
9. **openclaw-aisa-youtube-search** (3.356) ✅
10. **aisa-youtube-skill** (3.352) ✅

### Multi-Agent 類別（Top 10）

1. **multi-agent-cn** (3.648) ⚠️（中文，需驗證）
2. **multi-agent-collaboration** (3.598) ✅ **（已安裝）**
3. **multi-agent-roles** (3.579) ✅
4. **multi-agent-coordinator** (3.557) ✅
5. **naruto-multi-agent-cn** (3.551) ⚠️（中文，需驗證）
6. **sdw-multi-agent-orchestration** (3.449) ✅
7. **multi-agent-chat** (3.443) ✅
8. **friday-multi-agent-orchestrator** (3.334) ✅
9. **agent-team-orchestration** (1.274) ⚠️（低分，需驗證）
10. **agent-orchestrator** (1.270) ⚠️（低分，需驗證）

---

## 🎯 推薦安裝順序

### 第一步：基礎（今天）
```bash
# 1. 官方基礎
npx clawhub@latest install web-browsing

# 2. AI 搜索
npx clawhub@latest install felo-search

# 3. 移動端訪問
npx clawhub@latest install telegram
```

### 第二步：Felo 生態系統（本週）
```bash
# 4. 多功能工作站
npx clawhub@latest install felo-superAgent
npx clawhub@latest install felo-livedoc

# 5. 簡報生成
npx clawhub@latest install felo-slides
```

### 第三步：根據需求（需要時）
```bash
# 6. 代碼工作流
npx clawhub@latest install github

# 7. 業務自動化
npx clawhub@latest install n8n-workflow

# 8. 數據查詢（⚠️ 謹慎）
npx clawhub@latest install database-query

# 9. 語音合成
npx clawhub@latest install elevenlabs-agent

# 10. 智能家居
npx clawhub@latest install home-assistant
```

---

## 📝 安全檢查清單（每次安裝前）

- [ ] 讀取 SKILL.md 文件
- [ ] 檢查 GitHub repository
- [ ] 驗證發布者身份
- [ ] 查看安裝數量（>100）
- [ ] 檢查最後更新時間（<3 個月）
- [ ] 查看評論和評分
- [ ] 檢查請求的權限
- [ ] 運行 VirusTotal 掃描（可選）

---

## 🔄 更新記錄

- **2026-03-26**: 初始版本，基於 Felo 團隊測試
- **下次更新**: 每週掃描新 skills

---

**重要**: 這個列表會持續更新。定期回來查看最新安全建議。

**最後更新**: 2026-03-26 18:15 (Asia/Taipei)
