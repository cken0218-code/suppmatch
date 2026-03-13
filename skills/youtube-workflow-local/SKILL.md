# YouTube Workflow - 自動產出系統

> **Created**: 2026-03-13
> **Version**: 1.0.0
> **Purpose**: 每週自動產出 2-3 條 YouTube 腳本

---

## 用途

自動化 YouTube 內容產出流程，從 trending 搜尋到腳本生成。

## 觸發條件

- Heartbeat（每週一、三、五）
- 手動觸發：`/youtube-workflow`
- Cron 定時（每週二、四、六 10:00）

## 工作流程

### Phase 1: Trending 搜尋（自動）
```
搜尋 trending 話題
    ↓
過濾相關主題（AI, tech, productivity）
    ↓
提取 3-5 個候選題目
    ↓
評估潛力（views, competition, monetization）
    ↓
選擇 1 個最佳題目
```

### Phase 2: 腳本生成（自動）
```
讀取 content-persona.md
    ↓
生成標題（3 個選項）
    ↓
生成腳本（5 段式結構）
    ↓
整合 affiliate 連結
    ↓
生成描述欄 + tags
    ↓
保存到 youtube-scripts/
```

### Phase 3: 通知（自動）
```
Send Telegram 通知
    ↓
包含：標題、預計收入、affiliate、檔案路徑
    ↓
等待用戶拍攝
```

---

## 配置

### 內容人設
**位置**: `memory/projects/content-persona.md`

**主題**:
- 健康資訊
- AI tools review
- Productivity tips
- 補充品推介

**風格**:
- 親切、溫暖
- 唔硬銷
- 專業但親民

### Affiliate 整合

**主要**:
- CustomGPT (20% recurring) - AI niche
- Shopify ($150-$3000) - 電商
- ClickBank - 數位產品

**次要**:
- Amazon Associates
- 其他健康補充品

### 發布頻率

| 星期 | 任務 | 時間 |
|------|------|------|
| 一 | Trending 搜尋 + 腳本生成 | 10:00 |
| 二 | - | - |
| 三 | Trending 搜尋 + 腳本生成 | 10:00 |
| 四 | - | - |
| 五 | Trending 搜尋 + 腳本生成 | 10:00 |
| 六 | - | - |
| 日 | - | - |

**目標**: 每週 3 條腳本 → 每月 12-13 條

---

## 自動化腳本

### 1. trending-search.py

```python
#!/usr/bin/env python3
"""
搜尋 trending 話題
"""
import json
from datetime import datetime

def search_trending():
    topics = [
        "AI tools trending",
        "productivity hacks 2026",
        "health supplements research",
        "tech news today"
    ]

    # TODO: 用 web_search API
    # TODO: 過濾相關主題
    # TODO: 評估潛力

    return {
        "date": datetime.now().isoformat(),
        "topics": topics
    }

if __name__ == "__main__":
    result = search_trending()
    print(json.dumps(result, indent=2))
```

### 2. script-generator.py

```python
#!/usr/bin/env python3
"""
生成 YouTube 腳本
"""
import json
from datetime import datetime

def generate_script(topic, persona_path):
    # TODO: 讀取 persona
    # TODO: 生成標題
    # TODO: 生成腳本
    # TODO: 整合 affiliate

    return {
        "title": f"Generated: {topic}",
        "script": "...",
        "monetization": "CustomGPT affiliate"
    }

if __name__ == "__main__":
    # TODO: 實現
    pass
```

---

## Cron 設置

```bash
# 每週一、三、五 10:00 執行
0 10 * * 1,3,5 cd ~/.openclaw/workspace && python3 skills/youtube-workflow-local/run.py

# 或者用 OpenClaw trigger
0 10 * * 1,3,5 openclaw trigger heartbeat youtube-workflow
```

---

## 預計效果

### 每月產出
- 腳本數量：12-13 條
- 假設拍攝率：50%（6-7 條影片）
- 假設發布率：80%（5-6 條發布）

### 收入預測（保守）

| 來源 | 每條片 | 每月（6條） |
|------|--------|-------------|
| AdSense | $100-200 | $600-1200 |
| Affiliate | $50-500 | $300-3000 |
| **總計** | $150-700 | **$900-4200** |

---

## 監控指標

- [ ] 腳本產出數量
- [ ] 拍攝轉化率
- [ ] 發布轉化率
- [ ] Views per video
- [ ] Affiliate clicks
- [ ] Affiliate conversions
- [ ] 總收入

---

## 下一步

1. [ ] 實現 trending-search.py
2. [ ] 實現 script-generator.py
3. [ ] 設置 cron job
4. [ ] 測試第一次自動產出
5. [ ] 優化 workflow

---

**Created by**: Ken AI Assistant
**Date**: 2026-03-13
**Status**: Ready for implementation
