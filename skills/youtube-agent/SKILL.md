---
name: youtube-agent
description: YouTube Agent - 内容创作、Trending监控、发布排程
version: 1.0.0
author: local
license: MIT
---

# YouTube Agent 📺

> 专门负责 YouTube 自动化相关内容

## 职责

1. **Trending 监控** - 追踪 YouTube trending 内容
2. **内容创作** - 标题、描述、标签生成
3. **发布排程** - 自动排程发布
4. **数据分析** - 频道表现分析

---

## 可用工具

### 1. YouTube Data API
- Trending videos
- Search
- Video details

### 2. Content Generation
- 标题生成
- 描述生成
- 标签建议

### 3. Analytics
- 频道统计
- 视频表现
- 增长趋势

---

## 使用方式

### 监控 Trending
```bash
python3 skills/youtube-agent/trending-scanner.py
```

### 生成内容
```bash
python3 skills/youtube-agent/content-generator.py
```

### 分析频道
```
"analyze channel performance last 30 days"
```

### 快速指令
```bash
# 每日 trending 掃描
openclaw cron add --name="youtube-trending-am" --schedule="0 12 * * *" -- python3 skills/youtube-agent/trending-scanner.py

openclaw cron add --name="youtube-trending-pm" --schedule="0 18 * * *" -- python3 skills/youtube-agent/trending-scanner.py
```

---

## Cron Jobs

- **Trending Scan**: 每日 12:00, 18:00
- **Weekly Report**: 每週一 09:00

---

## 输出格式

### Trending Report
```
📺 YouTube Trending Report
Niche: [niche]
Date: [date]

🔥 Top Videos:
1. [title] - [views] views
2. [title] - [views] views
...

💡 Insights:
- [insight 1]
- [insight 2]
```

### Content Suggestion
```
📝 Content Suggestion
Topic: [topic]

📌 Title Options:
1. [title 1]
2. [title 2]
3. [title 3]

🏷️ Tags: [tags]

📄 Description:
[description]
```

---

## 注意事项

- 使用 YouTube Data API v3
- 遵守 YouTube API Terms of Service
- 定期检查 API quota
- 记录所有 API 调用

---

**目标**: 实现 YouTube 内容自动化！
