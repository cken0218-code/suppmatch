# Agent Routing Logic - 路由邏輯詳解

## 路由決策流程

### Step 1: 任務意圖識別

```python
INTENT_PATTERNS = {
    "planner": [
        "youtube", "頻道", "訂閱", "觀看",
        "收入", "賺錢", "roi", "利潤",
        "內容", "標題", "描述", "標籤",
        "策略", "增長", "推廣", "cpm"
    ],
    "artificer": [
        "代碼", "開發", "編程", "bug",
        "git", "github", "pr", "commit",
        "項目", "構建", "部署", "發布",
        "自動化", "腳本", "workflow"
    ],
    "scout": [
        "研究", "分析", "趨勢",
        "搜索", "查詢", "找尋",
        "數據", "報告", "統計",
        "市場", "競爭", "機會"
    ],
    "inquisitor": [
        "安全", "審計", "漏洞",
        "監控", "健康", "狀態",
        "性能", "優化", "問題",
        "日誌", "錯誤", "bug"
    ],
    "logistics": [
        "備份", "恢復", "保存",
        "觸發", "自動化", "定時",
        "token", "成本", "優化"
    ]
}
```

### Step 2: 複雜度評估

```python
COMPLEXITY_THRESHOLDS = {
    "simple": {
        "max_tokens": 500,
        "models": ["minimax/m2.1"],
        "tasks": [
            "簡單搜索",
            "數據整理",
            "基礎生成",
            "狀態查詢"
        ]
    },
    "complex": {
        "min_tokens": 500,
        "models": ["zai/glm-5"],
        "tasks": [
            "代碼開發",
            "策略規劃",
            "安全審計",
            "趨勢分析",
            "架構設計"
        ]
    }
}
```

### Step 3: 技能匹配

```python
SKILL_MAPPING = {
    "youtube-analysis": {
        "skill": "youtube-analytics-local",
        "agent": "planner",
        "models": ["zai/glm-5"]  # 需要深度分析
    },
    "content-creation": {
        "skill": "content-creator-local",
        "agent": "planner", 
        "models": ["minimax/m2.1"]  # 基礎生成即可
    },
    "code-development": {
        "skill": "app-scaffold-local",
        "agent": "artificer",
        "models": ["zai/glm-5"]  # 需要複雜邏輯
    },
    "github-ops": {
        "skill": "github",
        "agent": "artificer",
        "models": ["minimax/m2.1"]  # CLI 操作
    },
    "web-search": {
        "skill": "ddg-web-search",
        "agent": "scout",
        "models": ["minimax/m2.1"]  # 基礎搜索
    },
    "market-research": {
        "skill": "ddg-web-search + data-analyzer-local",
        "agent": "scout",
        "models": ["zai/glm-5"]  # 需要分析整合
    },
    "security-audit": {
        "skill": "security-audit",
        "agent": "inquisitor",
        "models": ["zai/glm-5"]  # 需要深度分析
    },
    "system-monitor": {
        "skill": "system-monitor",
        "agent": "inquisitor",
        "models": ["minimax/m2.1"]  # 基礎監控
    },
    "backup": {
        "skill": "backup-manager",
        "agent": "logistics",
        "models": ["minimax/m2.1"]  # 基礎操作
    },
    "token-optimize": {
        "skill": "token-maximizer",
        "agent": "logistics",
        "models": ["zai/glm-5"]  # 需要優化策略
    }
}
```

### Step 4: 執行模式選擇

```python
EXECUTION_MODES = {
    "pipeline": {
        "trigger": ["流水線", "pipeline", "步驟", "順序"],
        "example": "用流水線：研究 → 創作 → 發布",
        "agents": ["scout", "planner", "artificer"]
    },
    "parallel": {
        "trigger": ["並行", "parallel", "同時", "一起"],
        "example": "並行：搜索 A、搜索 B、搜索 C",
        "agents": ["scout"]  # 多個 scout 同時執行
    },
    "debate": {
        "trigger": ["辯論", "debate", "討論", "對比"],
        "example": "辯論：YouTube vs B站",
        "agents": ["planner", "scout", "planner"]  # 交替觀點
    },
    "single": {
        "trigger": [],  # 默認
        "example": "分析 YouTube 數據",
        "agents": ["planner"]
    }
}
```

---

## 實際路由範例

### 範例 1: "分析我的 YouTube 頻道"

```
1. 意圖識別: "youtube" + "分析" → planner
2. 複雜度評估: "分析" → complex → GLM-5
3. 技能匹配: "youtube-analysis" → youtube-analytics-local
4. 執行模式: 默認 single
5. 執行: THE PLANNER → youtube-analytics-local (GLM-5)
```

### 範例 2: "創建一個新的 skill"

```
1. 意圖識別: "創建" + "skill" → artificer
2. 複雜度評估: "創建" → complex → GLM-5
3. 技能匹配: "code-development" → app-scaffold-local
4. 執行模式: 默認 single
5. 執行: THE ARTIFICER → app-scaffold-local (GLM-5)
```

### 範例 3: "並行研究 AI 工具和網賺趨勢"

```
1. 意圖識別: "研究" → scout
2. 複雜度評估: "研究" → complex → GLM-5
3. 技能匹配: "market-research" → ddg-web-search + data-analyzer
4. 執行模式: "並行" → parallel
5. 執行:
   - Agent 1: THE SCOUT → 研究 AI 工具 (GLM-5)
   - Agent 2: THE SCOUT → 研究網賺趨勢 (GLM-5)
   ↓
   合併結果
```

### 範例 4: "用流水線：研究趨勢 → 創作內容 → 發布"

```
1. 意圖識別: "流水線" → 複雜任務
2. 執行模式: pipeline
3. 步驟:
   - Step 1: THE SCOUT → 研究趨勢 (GLM-5)
   - Step 2: THE PLANNER → 創作內容 (MiniMax)
   - Step 3: THE ARTIFICER → 發布 (GLM-5)
4. 結果傳遞: Step 1 → Step 2 → Step 3
```

---

## 成本控制策略

### Token 分配

| 任務類型 | 預估 Token | 建議 Model | 優先級 |
|----------|-----------|------------|--------|
| 基礎搜索 | 100-500 | MiniMax | 高 |
| 數據分析 | 500-2000 | MiniMax | 高 |
| 內容創作 | 500-1500 | MiniMax | 高 |
| 代碼開發 | 2000+ | GLM-5 | 低 |
| 策略規劃 | 2000+ | GLM-5 | 低 |
| 安全審計 | 2000+ | GLM-5 | 低 |

### 自動降級

```python
def auto_downgrade(task, original_model):
    # 如果任務失敗，降級到更便宜的模型
    if original_model == "zai/glm-5":
        return "minimax/m2.1"
    return original_model
```

---

## 路由準確率優化

### 學習歷史

```python
ROUTING_HISTORY = {
    "2026-02-19": {
        "total_tasks": 100,
        "correct_routes": 95,
        "accuracy": 95%
    }
}
```

### 持續優化

1. 記錄每次路由決策
2. 追蹤任務完成質量
3. 調整關鍵詞權重
4. 更新複雜度評估
