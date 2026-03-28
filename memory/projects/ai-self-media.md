# AI 自媒体自动化系统

> 完全自动化：研究 → 规划 → 创作 → 发布 → 分析

---

## 架构

```
AI CEO (Commander)
       ↓
┌──────────────────┐
│  Content Team    │
├──────────────────┤
│ Research Agent   │ → 研究趋势
│ Planner Agent    │ → 规划内容
│ Builder Agent    │ → 技术实现
│ Content Agent    │ → 创作内容
│ Review Agent     │ → 质量审核
└──────────────────┘
       ↓
   发布平台
   ├─→ YouTube
   ├─→ 小红书
   └─→ Instagram
       ↓
   数据分析
   └─→ 反馈 → 优化
```

---

## 流程

### 1. Research (Research Agent)
- 扫描 trending topics
- 分析竞争对手
- 搵高潜力 niche

### 2. Planning (Planner Agent)
- 选题策划
- 制定内容策略
- 安排发布时间

### 3. Script (Content Agent)
- 写 YouTube script
- 写小红书笔记
- SEO 优化

### 4. 生成 (Builder + 外部工具)
- AI 影片生成 (Runway/Pika)
- 图片生成 (Midjourney)
- 剪辑 (自动化)

### 5. 发布 (Builder Agent)
- YouTube upload
- 小红书发布
- IG post

### 6. 分析 (Research Agent)
- 观看/点赞/评论分析
- 趋势分析
- 优化建议

---

## Cron 自动运行

```
# 每日 research (6:00)
0 6 * * * → 扫描趋势

# 每日 content gen (12:00)
0 12 * * * → 生成内容

# 每日 publish (18:00)
0 18 * * * → 自动发布

# 每日 analytics (22:00)
0 22 * * * → 数据分析
```

---

## 所需工具

| 环节 | 工具 |
|------|------|
| Trending 扫描 | YouTube API, 小红书爬虫 |
| Script 生成 | MiniMax |
| 影片生成 | Runway, Pika, HeyGen |
| 图片生成 | Midjourney API |
| 发布 | YouTube API, 小红书 API |
| 数据分析 | 内部工具 |
