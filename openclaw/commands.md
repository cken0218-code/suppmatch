# Telegram Commands

> 完整既 Telegram 指令系统

---

## 📋 任务管理

### /task \<内容\>
创建新任务

```
/task 建立YouTube自動頻道
```

**回复：**
```
✅ Task Created

任务：建立YouTube自動頻道
Priority: HIGH

→ 派发给 Planner...
```

---

### /tasks
列出所有任务

```
/tasks
```

**回复：**
```
📋 Active Tasks

[HIGH]
1. 建立YouTube AI頻道
2. 小紅書自動內容

[MEDIUM]
3. 優化prompt
4. AI影片pipeline

[LOW]
5. workflow整理
```

---

### /work
强制开始执行任务

```
/work
```

**回复：**
```
🚀 开始执行任务

拣选：建立YouTube AI頻道

→ Research: 扫描趋势
→ Planner: 规划内容
→ Content: 生成脚本
...

✅ 完成
```

---

### /report
查看今日进度

```
/report
```

**回复：**
```
🐱 今日進度 Report
━━━━━━━━━━━━━━━━

✅ 完成
- prompt optimisation

🔄 進行中
- YouTube automation (60%)

📋 Tasks: [HIGH] 2 | [MEDIUM] 2 | [LOW] 1
```

---

### /done \<任务\>
标记任务完成

```
/done YouTube automation
```

---

### /priority \<任务\> \<HIGH/MEDIUM/LOW\>
调整优先级

```
/priority Xiaohongshu HIGH
```

---

## 🤖 Model Routing

| 任务类型 | Model |
|----------|-------|
| planning | GLM-5 |
| strategy | GLM-5 |
| debug | GLM-5 |
| content | MiniMax |
| social | MiniMax |
| translation | MiniMax |
