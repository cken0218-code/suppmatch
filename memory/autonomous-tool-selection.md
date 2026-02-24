# 自主調動策略 (Autonomous Tool Selection)

> **Last Updated**: 2026-02-24
> **Goal**: 讓 AI 更自主選擇工具，唔只係執行 workflow

---

## 🎯 核心理念

**Level 1 Agent**: 執行指令
**Level 2 Agent**: 工具 + 知識 + 記憶
**Level 3 Agent**: 自主調動 + 自我修正

---

## 📋 Step 1: 清晰目標 + 工具文檔

### 工具優先級矩陣

| 任務 | 首選工具 | 備選方案 | 觸發條件 |
|------|----------|----------|----------|
| X Trending | Chrome browser | OpenClaw browser | Chrome 未 attach |
| Web Search | Brave API | DuckDuckGo | API quota 用盡 |
| 知識收集 | browser automation | web_fetch | 需要登入 |
| 圖片生成 | 外部 API | 本地模型 | API fail |

### Fallback Prompt 範本

```markdown
## Tool Selection Strategy

When executing tasks, follow this priority:

1. **Primary Tool**: [Tool A]
   - When to use: [conditions]
   - Example: [use case]

2. **Fallback Tool**: [Tool B]
   - Trigger: [Tool A] fails with [error type]
   - Example: [use case]

3. **Last Resort**: [Tool C]
   - Trigger: Both A and B fail
   - Action: Notify user or skip
```

---

## 🧠 Step 2: 記憶 + 知識層

### 錯誤記憶庫

**位置**: `memory/errors/`

**格式**:
```json
{
  "date": "2026-02-24",
  "task": "X trending crawl",
  "tool_used": "chrome browser",
  "error": "Tab not attached",
  "solution": "Switched to openclaw browser",
  "success": true
}
```

### 自動查詢記憶

每次執行任務前：
1. 搜尋 `memory/errors/` 睇有冇類似錯誤
2. 如果有，直接用上次成功嘅方案
3. 記錄新錯誤同解決方案

---

## 🔨 Step 3: 目標分解

### 大任務 → 細步驟

**Example: 爬 X Trending**

```
大任務: 收集 AI trending 內容
    ↓
分解:
1. 檢查 browser 狀態 → Chrome attached?
   └─ No → 切換到 OpenClaw browser
2. 導航到 X explore
3. 提取 trending keywords
4. 儲存到知識庫
    ↓
每步檢查:
- 成功 → 下一步
- 失敗 → 嘗試備選方案
- 再失敗 → 記錄錯誤 + 通知用戶
```

---

## 🔄 Step 4: 反饋循環

### 自我檢查機制

**位置**: 每個 skill 加入 feedback check

```python
def execute_with_feedback(task, max_retries=3):
    for attempt in range(max_retries):
        result = execute(task)

        if result.success:
            log_success(task, result)
            return result
        else:
            error = result.error
            solution = check_memory_for_solution(error)

            if solution:
                apply_solution(solution)
            else:
                try_alternative_tool()

    # All attempts failed
    log_error(task, error)
    notify_user(task, error)
```

### 遞歸改善

- 每週 review 錯誤記錄
- 更新工具優先級
- 改進 fallback 策略

---

## 🚀 Step 5: 框架應用

### OpenClaw 已有功能

✅ Multi-tool access (browser, exec, web_fetch)
✅ Memory system (L0-L3)
✅ Subagents for complex tasks
✅ Skills for specialized workflows

### 建議增強

| 功能 | 現狀 | 建議 |
|------|------|------|
| 工具選擇 | 手動 | 加入 priority matrix |
| 錯誤記憶 | 手動記錄 | 自動搜尋 + 應用 |
| Fallback | 臨場判斷 | 預設策略 |
| 反饋循環 | 無 | 每步 self-check |

---

## 💻 實作範例

### Updated HEARTBEAT.md 指令

```markdown
## 🔧 自主調動規則

當執行任務時，遵循以下策略：

1. **優先檢查**: 睇下 memory/errors/ 有冇同類任務嘅解決方案
2. **工具選擇**: 根據 Task-Tool Matrix 選擇最合適工具
3. **Fallback**: 如果首選失敗，自動切換到備選
4. **記錄**: 無論成功定失敗，都記錄落 memory/errors/
5. **通知**: 只有當所有方法都失敗時先通知用戶
```

### 實際 Prompt 加入 AGENTS.md

```markdown
## 🤖 自主調動系統

**Tool Selection Priority:**
1. Check memory/errors/ for similar tasks
2. Use Task-Tool Matrix to select primary tool
3. If primary fails → switch to fallback
4. Record result (success/failure) to memory
5. Only notify user if all methods exhausted

**Example - Web Crawling:**
- Primary: Chrome browser (if tab attached)
- Fallback: OpenClaw browser (always available)
- Last resort: web_fetch (no login required content)
```

---

## 📊 成功指標

| 指標 | 目標 |
|------|------|
| 首次成功率 | > 70% |
| Fallback 成功率 | > 90% |
| 用戶介入率 | < 10% |
| 錯誤重複率 | < 5% |

---

## 🎯 下一步行動

1. [ ] 更新 AGENTS.md 加入自主調動規則
2. [ ] 建立 Task-Tool Matrix 文檔
3. [ ] 設置 memory/errors/ 自動搜尋
4. [ ] 為每個 skill 加入 fallback 機制
5. [ ] 每週 review 錯誤率 + 改進策略

---

*Version: 1.0*
*Created: 2026-02-24*
