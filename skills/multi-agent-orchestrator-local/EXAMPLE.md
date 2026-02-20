# 使用範例集

## 基礎範例

### 範例 1: YouTube 數據分析

**用戶輸入**：
```
"分析我的 YouTube 頻道表現"
```

**路由過程**：
```
1. Intent: "youtube" + "分析" → PLANNER
2. Complexity: 分析類任務 → COMPLEX → GLM-5
3. Skill Match: "youtube-analysis" → youtube-analytics-local
4. Execution: SINGLE → THE PLANNER

執行結果：
📊 YouTube 頻道月度報告
期間：2026-02-01 至 2026-02-28

📈 總體表現
- 觀看次數：12,345 (+15%)
- 新訂閱：234 (+8%)
- 觀看時長：1,234小時 (+12%)
- 收入：$567 (+20%)
```

---

### 範例 2: 內容創作

**用戶輸入**：
```
"幫我為 AI tools 教程生成標題和描述"
```

**路由過程**：
```
1. Intent: "標題" + "描述" + "教程" → PLANNER
2. Complexity: 生成類任務 → SIMPLE → MiniMax
3. Skill Match: "content-creation" → content-creator-local
4. Execution: SINGLE → THE PLANNER

執行結果：
標題選項：
1. "10個 AI Tools 完整指南（2026）- 新手必看"
2. "我用這5個 AI Tools 效率提升 10 倍"
3. "AI Tools 2026：從新手到專家的完整攻略"

描述：
[SEO 優化的描述內容...]
```

---

### 範例 3: 安全審計

**用戶輸入**：
```
"檢查系統安全狀態"
```

**路由過程**：
```
1. Intent: "安全" + "檢查" → INQUISITOR
2. Complexity: 審計類任務 → COMPLEX → GLM-5
3. Skill Match: "security-audit" → security-audit
4. Execution: SINGLE → THE INQUISITOR

執行結果：
🔒 安全審計報告

✅ 通過項目：
- API 權限配置正確
- 無異常登錄記錄
- 密鑰未洩露

⚠️ 警告項目：
- 3個服務器需要更新安全補丁
- 1個 API endpoint 權限過寬

❌ 需修復項目：
- [列出需要立即修復的問題]
```

---

## 複雜範例

### 範例 4: 流水線任務

**用戶輸入**：
```
"用流水線模式創建一個新的 YouTube 視頻：
1. 研究 AI trends
2. 創作內容
3. 生成標題描述
4. 準備發布"
```

**路由過程**：
```
1. Intent: "流水線" → PIPELINE 模式
2. 步驟分解：

Step 1: THE SCOUT (GLM-5)
   Task: "研究 AI trends 2026"
   Result: AI trends 研究報告
   
Step 2: THE PLANNER (MiniMax)
   Task: "基於研究創作視頻內容"
   Result: 視頻腳本和大綱
   
Step 3: THE PLANNER (MiniMax)
   Task: "生成標題和描述"
   Result: 標題+描述+標籤
   
Step 4: THE ARTIFICER (GLM-5)
   Task: "準備發布流程"
   Result: 發布腳本和自動化配置

最終交付：完整 YouTube 視頻方案 + 發布腳本
```

---

### 範例 5: 並行研究

**用戶輸入**：
```
"並行研究以下三個方向：
1. YouTube automation 最新工具
2. AI 寫作工具市場趨勢
3. 網賺新模式 2026"
```

**路由過程**：
```
1. Intent: "並行" → PARALLEL 模式
2. 同時啟動 3 個 THE SCOUT：

┌─────────────────────────────────────────┐
│ Agent 1: THE SCOUT (GLM-5)              │
│ Task: "研究 YouTube automation 工具"    │
│ Status: ✅ 完成                         │
│ Result: [研究報告]                       │
├─────────────────────────────────────────┤
│ Agent 2: THE SCOUT (GLM-5)             │
│ Task: "研究 AI 寫作工具市場"            │
│ Status: ✅ 完成                         │
│ Result: [研究報告]                       │
├─────────────────────────────────────────┤
│ Agent 3: THE SCOUT (GLM-5)              │
│ Task: "研究網賺新模式 2026"             │
│ Status: ✅ 完成                         │
│ Result: [研究報告]                       │
└─────────────────────────────────────────┘
         │
         ▼
   Result Aggregator
         │
         ▼
  合併報告：三個方向的綜合分析
```

---

### 範例 6: 辯論模式

**用戶輸入**：
```
"辯論：應該專注 YouTube automation 還是 Local Business Automation？"
```

**路由過程**：
```
1. Intent: "辯論" → DEBATE 模式
2. 參與方設定：

Agent A: THE PLANNER (支持 YouTube)
   "作為 YouTube automation 專家，列出優勢、數據、案例"

Agent B: THE PLANNER (支持 Local Business)  
   "作為 Local Business 專家，列出優勢、數據、案例"

Agent C: THE SCOUT (中立分析)
   "作為中立分析師，對比兩者，提出綜合建議"

         │
         ▼
   Result Aggregator + 主 Agent 總結
         │
         ▼
最終建議：
根據你的情況（資金、技術、時間），建議：
- 如果 X 條件 → 選擇 YouTube
- 如果 Y 條件 → 選擇 Local Business
- 混合策略建議
```

---

## 系統管理範例

### 範例 7: 完整系統檢查

**用戶輸入**：
```
"進行全面的系統健康檢查"
```

**路由過程**：
```
1. Intent: "系統" + "檢查" → INQUISITOR
2. 並行執行多個檢查：

┌─────────────────────────────────────────┐
│ security-audit      → ✅ 通過           │
│ system-monitor      → 正常              │
│ api-security-check  → ✅ 通過           │
│ cron-manager        → 3個任務待執行     │
│ agent-audit         → 分析中...         │
└─────────────────────────────────────────┘
         │
         ▼
   合併結果
         │
         ▼
🔍 系統健康報告

系統狀態：🟢 良好

📊 資源使用：
- CPU: 45%
- Memory: 62%
- Disk: 78%

✅ 安全狀態：
- 所有安全檢查通過

⚠️ 注意事項：
- 磁碟空間接近 80%

📅 待處理：
- 3個定時任務等待執行
```

---

## 成本優化範例

### 範例 8: Token 節省策略

**用戶輸入**：
```
"優化我的 token 使用"
```

**路由過程**：
```
1. Intent: "token" + "優化" → LOGISTICS
2. Complexity: 優化類 → COMPLEX → GLM-5
3. Skill Match: "token-optimize" → token-maximizer
4. Execution: SINGLE → LOGISTICS

執行結果：
💰 Token 優化報告

當前使用：
- MiniMax: 85% (90% 目標) ✅
- GLM-5: 15% (10% 目標) ⚠️

優化建議：
1. 將 5 個複雜查詢改為 MiniMax
2. 啟用結果快取
3. 批量處理小任務
4. 使用壓縮輸出

預估節省：
- 每日: ~50,000 tokens
- 每月: ~1.5M tokens
```

---

## 常見錯誤處理

### 範例 9: Skill 不可用

**用戶輸入**：
```
"使用某個不存在的 skill"
```

**路由過程**：
```
1. Intent: 識別成功 → PLANNER
2. Skill Match: 嘗試匹配 "xyz-skill"
3. 錯誤: SKILL_NOT_FOUND
4. 錯誤處理:
   - 嘗試通用路由
   - 返回友好錯誤
   - 建議替代方案

執行結果：
❌ 找不到指定的 skill

建議：
1. 檢查 skill 名稱是否正確
2. 使用通用任務描述
3. 查看可用 skills：skill-list
```

---

## 組合範例

### 範例 10: 完整內容生產流程

**用戶輸入**：
```
"幫我完成一個完整的 YouTube 內容生產流程：
1. 研究本週 AI 趨勢
2. 找出熱門話題
3. 創作 3 個視頻方案
4. 評估 ROI"
```

**路由過程**：
```
Phase 1: 研究 (THE SCOUT)
  - 搜索 AI 趨勢新聞
  - 分析熱門話題
  - 生成研究報告

Phase 2: 創作 (THE PLANNER)
  - 基於研究創作 3 個視頻方案
  - 生成標題、描述、標籤
  - 評估點擊率預測

Phase 3: 分析 (THE INQUISITOR)
  - 計算時間投入
  - 預估收益
  - ROI 分析

最終交付：
📋 完整內容生產方案
- 3 個視頻創意
- 預估 ROI: 150%
- 執行時間表
```
