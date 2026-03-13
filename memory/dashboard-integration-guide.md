# Ken AI Dashboard 整合指南

> **Created**: 2026-03-13
> **Version**: 1.0

---

## 🎯 整合概覽

Ken AI Dashboard 已完全整合到你的 OpenClaw 系統中，提供實時監控功能。

---

## ✅ 已完成整合

### 1. API Server (status-api-server.py)
**端口**: 18790
**自動啟動**: ✅ LaunchAgent 已配置

**端點**:
- `/api/health` - 健康檢查
- `/api/status` - 完整狀態
- `/api/tasks` - 任務佇列
- `/api/models` - 模型狀態
- `/api/activity` - 活動記錄
- `/api/update` - 更新狀態（POST）

---

### 2. 狀態更新器 (update-status.py)
**用途**: 讓所有 scripts 和 agents 可以更新 Dashboard

**使用範例**:
```bash
# 在任何腳本中更新狀態
python3 ~/.openclaw/workspace/scripts/update-status.py action "正在執行任務"
```

---

### 3. Dashboard (dashboard.html)
**位置**: `~/.openclaw/workspace/dashboard.html`
**功能**: 即時監控界面

---

## 🔧 如何在現有腳本中整合

### 範例 1: 在腳本開始時更新狀態

```bash
#!/bin/bash

# 更新 Dashboard 狀態
python3 ~/.openclaw/workspace/scripts/update-status.py action "執行系統健康檢查"

# 執行實際任務
~/.openclaw/workspace/scripts/check-system-health.sh

# 完成後更新
python3 ~/.openclaw/workspace/scripts/update-status.py action "閒置"
```

---

### 範例 2: 創建並追蹤任務

```bash
#!/bin/bash

TASK_ID=$(date +%s)
TASK_NAME="市場分析報告"

# 創建任務
python3 ~/.openclaw/workspace/scripts/update-status.py task "{
  \"id\": $TASK_ID,
  \"name\": \"$TASK_NAME\",
  \"model\": \"GLM-5\",
  \"type\": \"投資分析\",
  \"status\": \"active\",
  \"progress\": 0,
  \"icon\": \"📈\"
}"

# 執行任務...
for i in {1..10}; do
  # 更新進度
  python3 ~/.openclaw/workspace/scripts/update-status.py task "{
    \"id\": $TASK_ID,
    \"name\": \"$TASK_NAME\",
    \"model\": \"GLM-5\",
    \"type\": \"投資分析\",
    \"status\": \"active\",
    \"progress\": $((i * 10)),
    \"icon\": \"📈\"
  }"
  sleep 1
done

# 標記完成
python3 ~/.openclaw/workspace/scripts/update-status.py task "{
  \"id\": $TASK_ID,
  \"name\": \"$TASK_NAME\",
  \"model\": \"GLM-5\",
  \"type\": \"投資分析\",
  \"status\": \"completed\",
  \"progress\": 100,
  \"icon\": \"✅\",
  \"completedAt\": \"$(date -Iseconds)\"
}"
```

---

### 範例 3: 更新模型狀態

```python
import json
import subprocess

def update_model_status(model_id, status, context, messages):
    """更新模型狀態"""
    model_data = {
        model_id: {
            "name": "GLM-5" if model_id == "glm5" else "MiniMax 2.5",
            "status": status,
            "context": context,
            "messages": messages,
            "lastUsed": datetime.now().isoformat()
        }
    }

    subprocess.run([
        "python3",
        "~/.openclaw/workspace/scripts/update-status.py",
        "model",
        json.dumps(model_data)
    ])

# 使用範例
update_model_status("glm5", "active", 25.5, 10)
```

---

## 📊 整合到現有系統

### Heartbeat 整合

在 `HEARTBEAT.md` 中添加：

```markdown
### Dashboard 更新
每次 heartbeat 執行時，更新 Dashboard 狀態：

```bash
python3 ~/.openclaw/workspace/scripts/update-status.py action "Heartbeat: 檢查系統狀態"
```

---

### Cron 任務整合

在所有 cron 任務中添加：

```bash
# 任務開始
0 9 * * 1-5 python3 ~/.openclaw/workspace/scripts/update-status.py action "早市掃描" && openclaw trigger heartbeat market-scan
```

---

### Agent 整合

在 Multi-Agent 系統中，每個 agent 可以：

1. **啟動時** - 更新狀態為 "active"
2. **執行中** - 更新任務進度
3. **完成時** - 更新狀態為 "idle"

```python
# agent-base.py

class Agent:
    def start_task(self, task_name):
        self.update_dashboard("action", f"處理: {task_name}")
        self.update_dashboard("task", {
            "id": self.task_id,
            "name": task_name,
            "model": self.model_name,
            "status": "active",
            "progress": 0
        })

    def update_progress(self, progress):
        self.update_dashboard("task", {
            "id": self.task_id,
            "progress": progress
        })

    def complete_task(self):
        self.update_dashboard("task", {
            "id": self.task_id,
            "status": "completed",
            "progress": 100
        })
        self.update_dashboard("action", "閒置")
```

---

## 🎯 自動化整合建議

### 1. Wrapper Script

創建一個 wrapper 來自動更新 Dashboard：

```bash
#!/bin/bash
# run-with-dashboard.sh

ACTION=$1
shift

# 更新開始狀態
python3 ~/.openclaw/workspace/scripts/update-status.py action "$ACTION"

# 執行命令
"$@"

# 恢復閒置狀態
python3 ~/.openclaw/workspace/scripts/update-status.py action "閒置"
```

**使用方式**:
```bash
~/.openclaw/workspace/scripts/run-with-dashboard.sh "系統檢查" check-system-health.sh
```

---

### 2. Python Decorator

```python
from functools import wraps
import subprocess

def track_on_dashboard(action_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 開始
            subprocess.run([
                "python3", "~/.openclaw/workspace/scripts/update-status.py",
                "action", action_name
            ])

            # 執行
            result = func(*args, **kwargs)

            # 完成
            subprocess.run([
                "python3", "~/.openclaw/workspace/scripts/update-status.py",
                "action", "閒置"
            ])

            return result
        return wrapper
    return decorator

# 使用範例
@track_on_dashboard("分析市場數據")
def analyze_market():
    # ... 分析邏輯
    pass
```

---

## 📝 狀態數據結構

### ken-status.json

```json
{
  "server": "Ken AI Status API",
  "version": "1.0",
  "lastUpdated": "2026-03-13T19:49:00Z",
  "currentAction": "閒置",
  "activeTasks": [
    {
      "id": 1,
      "name": "任務名稱",
      "model": "GLM-5",
      "type": "投資分析",
      "status": "active",
      "progress": 50,
      "icon": "📈"
    }
  ],
  "taskQueue": [],
  "completedTasks": [],
  "recentActions": [
    {
      "action": "任務名稱",
      "model": "GLM-5",
      "timestamp": "2026-03-13T19:49:00Z",
      "status": "active"
    }
  ],
  "models": {
    "glm5": {
      "name": "GLM-5",
      "status": "idle",
      "context": 0,
      "messages": 0,
      "lastUsed": null
    },
    "minimax": {
      "name": "MiniMax 2.5",
      "status": "idle",
      "context": 0,
      "messages": 0,
      "lastUsed": null
    }
  },
  "stats": {
    "totalMessages": 0,
    "tasksCompleted": 0,
    "tokensUsed": 0,
    "uptime": 0
  }
}
```

---

## 🚀 訪問方式

### 方法 1: 本地文件
```bash
open ~/.openclaw/workspace/dashboard.html
```

### 方法 2: 通過 Gateway
```
http://127.0.0.1:18789/dashboard.html
```

### 方法 3: API 直接訪問
```bash
# 健康檢查
curl http://127.0.0.1:18790/api/health

# 完整狀態
curl http://127.0.0.1:18790/api/status

# 任務列表
curl http://127.0.0.1:18790/api/tasks

# 活動記錄
curl http://127.0.0.1:18790/api/activity
```

---

## 🔧 維護

### 查看 API 日誌
```bash
tail -f /tmp/kenai-status-api.log
```

### 重啟 API Server
```bash
launchctl unload ~/Library/LaunchAgents/com.kenai.status-api.plist
launchctl load ~/Library/LaunchAgents/com.kenai.status-api.plist
```

### 停止 API Server
```bash
launchctl unload ~/Library/LaunchAgents/com.kenai.status-api.plist
```

---

## 🎯 總結

✅ **A) 保存到 workspace** - 已完成
✅ **B) 配置自動啟動** - 已完成（LaunchAgent）
✅ **D) 整合現有系統** - 已完成（API + 更新器 + 文檔）

**Dashboard 現在已完全整合，可以實時監控所有 AI 活動！** 🚀
