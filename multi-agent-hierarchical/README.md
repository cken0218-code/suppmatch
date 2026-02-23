# Hierarchical Multi-Agent System

## 結構

```
┌─────────────────────────────────────┐
│        SUPERVISOR (GLM-5)           │
│   收到任務 → 分析 → 分俾子Agent     │
└──────────────┬──────────────────────┘
               │
    ┌──────────┼──────────┐
    ↓          ↓          ↓
┌────────┐ ┌────────┐ ┌────────┐
│Research│ │Engineer│ │Reviewer│
│ MiniMax│ │  GLM-5 │ │ MiniMax│
└────────┘ └────────┘ └────────┘
    ↑          ↑          ↑
    └──────────┴──────────┘
               │
        匯報俾 Supervisor
```

## Agent 設定

### Supervisor (總指揮)
- **Model**: GLM-5
- **功能**: 
  - 接收用戶任務
  - 分析任務類型
  - 決定邊個 sub-agent 做
  - 整合結果
- **System Prompt**: `supervisor-prompt.md`

### Researcher (研究員)
- **Model**: MiniMax
- **功能**:
  - 搜尋資料
  - 讀取文件
  - 整理資訊
- **System Prompt**: `researcher-prompt.md`

### Engineer (工程師)
- **Model**: GLM-5
- **功能**:
  - 寫Code
  - Debug
  - 建立項目
- **System Prompt**: `engineer-prompt.md`

### Reviewer (審查員)
- **Model**: MiniMax
- **功能**:
  - 檢查輸出
  - 捉蟲
  - 提建議
- **System Prompt**: `reviewer-prompt.md`

## 使用方法

### 方法1: 直接叫 sub-agent

```
你: 我想整一個天氣App

Supervisor分析:
→ 需要Researcher搵天氣API
→ 需要Engineer寫Code
→ 需要Reviewer檢查
```

### 方法2: 經常使用既Prompt

```
/research [問題] - 叫 Researcher 做
/build [項目] - 叫 Engineer 做  
/review [野] - 叫 Reviewer 做
```

## 示例對話

**User**: 幫我整一個BMI計算機

**Supervisor (GLM-5)**:
```
分析: 需要寫一個簡單既網頁應用
→ Engineer: 寫HTML+JS既BMI計算機
→ Reviewer: 檢查代碼
```

---

## 慳錢Tips

| Agent | Model | 幾時用 |
|-------|-------|--------|
| Researcher | MiniMax | 搜野、睇資料 |
| Engineer | GLM-5 | 寫Code |
| Reviewer | MiniMax | 簡單檢查 |
| Supervisor | GLM-5 | 淨係分析同決定 |

**預算**: $3-10/月 (主要係GLM-5)
