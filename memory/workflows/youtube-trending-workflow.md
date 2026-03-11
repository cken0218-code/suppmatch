# Workflow 1: YouTube Trending 监控

## 🎯 目标
每日自动扫描 YouTube trending，找出适合拍摄的内容主题，发送通知

---

## 📊 流程图

```
┌─────────────────────────────────────────────────┐
│          每日自动化流程 (09:00 + 18:00)            │
└─────────────────────────────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   n8n 触发器 (Schedule)   │
        │   时间: 09:00 & 18:00    │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   MCP Server: Fetch     │
        │   动作: 抓取 YouTube API  │
        │   URL: trending endpoint │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   数据处理 (JavaScript)  │
        │   • 提取 top 20 videos  │
        │   • 过滤: views > 100K  │
        │   • 分类: by category   │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   AI 分析 (OpenClaw)     │
        │   Prompt:               │
        │   "分析呢 20 条片，边条   │
        │    值得拍？点解？"        │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   MCP Server: Filesystem │
        │   保存到文件:            │
        │   ~/youtube-trending/    │
        │   YYYY-MM-DD.json        │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   生成报告 (Markdown)    │
        │   • Top 5 推荐主题       │
        │   • 拍摄建议             │
        │   • 预计流量             │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   通知 (Discord/Telegram)│
        │   发送:                  │
        │   📺 今日 YouTube 建议   │
        │   + 报告摘要             │
        └─────────────────────────┘
                      ↓
                  [完成 ✅]
```

---

## 🔧 详细步骤

### Step 1: n8n 触发器
**工具**: n8n Schedule Trigger
**配置**:
```json
{
  "trigger": "schedule",
  "cron": "0 9,18 * * *",
  "timezone": "Asia/Taipei"
}
```
**说明**: 每日 09:00 和 18:00 自动触发

---

### Step 2: MCP Fetch 抓取数据
**工具**: MCP Server - fetch
**配置**:
```json
{
  "server": "fetch",
  "url": "https://www.googleapis.com/youtube/v3/videos",
  "params": {
    "part": "snippet,statistics",
    "chart": "mostPopular",
    "regionCode": "AU",
    "maxResults": 20,
    "key": "YOUR_API_KEY"
  }
}
```
**输出**: JSON 格式的 trending 数据

---

### Step 3: 数据处理
**工具**: n8n Function Node (JavaScript)
**代码**:
```javascript
// 过滤和处理数据
const items = $input.all();

const processed = items[0].json.items
  .filter(item => item.statistics.viewCount > 100000)
  .map(item => ({
    title: item.snippet.title,
    views: parseInt(item.statistics.viewCount),
    likes: parseInt(item.statistics.likeCount),
    category: item.snippet.categoryId,
    publishedAt: item.snippet.publishedAt,
    videoId: item.id
  }))
  .sort((a, b) => b.views - a.views)
  .slice(0, 10);

return { json: { videos: processed } };
```
**输出**: 排序后的 top 10 视频

---

### Step 4: AI 分析
**工具**: OpenClaw (通过 HTTP Request)
**Prompt**:
```
你是 YouTube 内容策略专家。

分析以下 10 条 trending 视频：
{{videos}}

任务：
1. 识别适合翻拍的题材（不侵权）
2. 评估竞争程度
3. 建议拍摄角度
4. 预计流量潜力

输出格式：
- Top 5 推荐
- 每个推荐包含：
  • 主题
  • 原因
  • 拍摄建议
  • 预计流量
```
**输出**: Markdown 格式的分析报告

---

### Step 5: 保存文件
**工具**: MCP Server - filesystem
**配置**:
```json
{
  "server": "filesystem",
  "action": "write",
  "path": "~/youtube-trending/{{YYYY-MM-DD}}.json",
  "content": "{{all_data}}"
}
```
**输出**: 文件保存成功

---

### Step 6: 生成报告
**工具**: n8n Template Node
**模板**:
```markdown
# 📺 YouTube Trending 报告
**日期**: {{date}}

## 🔥 Top 5 推荐

{{#each recommendations}}
### {{rank}}. {{title}}
- **原因**: {{reason}}
- **建议**: {{suggestion}}
- **预计流量**: {{traffic}}
{{/each}}

---
⏰ 分析时间: {{timestamp}}
```

---

### Step 7: 发送通知
**工具**: Discord Webhook / Telegram Bot
**配置**:
```json
{
  "method": "POST",
  "url": "DISCORD_WEBHOOK_URL",
  "body": {
    "content": "📺 今日 YouTube Trending 建议已生成！",
    "embeds": [{
      "title": "Top 5 推荐",
      "description": "{{summary}}",
      "color": 15158332
    }]
  }
}
```

---

## 📊 数据流

```
输入: 无（自动触发）
  ↓
处理: 
  - YouTube API: 20 条 trending
  - 过滤: views > 100K
  - 排序: Top 10
  - AI 分析: Top 5 推荐
  ↓
输出:
  - 文件: JSON + Markdown
  - 通知: Discord/Telegram
  - 日志: n8n execution log
```

---

## 💰 成本

**API 调用**:
- YouTube Data API: 免费（每日 quota）
- OpenClaw AI: ~$0.01-0.05/次
- Discord Webhook: 免费

**总计**: **< $0.10/日** （约 $3/月）

---

## ⏱️ 执行时间

- 抓取数据: ~2秒
- 数据处理: ~1秒
- AI 分析: ~5-10秒
- 保存文件: ~1秒
- 发送通知: ~1秒

**总计**: **~10-15秒**

---

## 🔄 变体

### 变体 A: 实时监控
- 触发: Webhook（手动）
- 用途: 即时查看 trending
- 输出: 即时通知

### 变体 B: 周报
- 触发: 每周一 09:00
- 用途: 整理上周 trending
- 输出: 详细 PDF 报告

### 变体 C: 多地区
- 触发: 每日 09:00
- 地区: AU, US, UK, HK
- 输出: 对比报告

---

## 🎯 成功指标

- ✅ 每日自动运行 2 次
- ✅ 发现 3-5 个值得拍的主题
- ✅ 通知准时送达
- ✅ 数据完整保存

---

## 🐛 故障排除

### 问题 1: YouTube API quota 用完
**解决**: 
- 减少 maxResults 到 10
- 减少触发频率到 1 次/日
- 或申请更高 quota

### 问题 2: AI 分析太慢
**解决**:
- 减少 prompt 长度
- 用更快的模型（MiniMax）
- 缓存常用分析

### 问题 3: Discord 通知失败
**解决**:
- 检查 webhook URL
- 添加重试机制
- 备用: Email 通知

---

## 🚀 扩展方向

1. **加入竞争对手分析**
   - 监控指定频道
   - 分析他们的 trending 视频

2. **自动生成标题/描述**
   - AI 生成优化标题
   - 生成 SEO 描述

3. **整合到 Content Calendar**
   - 自动排程拍摄
   - 整合 Google Calendar

4. **加入 A/B 测试**
   - 生成多个标题版本
   - 追踪哪个效果好

---

**下一步**: 
- ✅ 理解这个 workflow
- ⚠️ 准备 Option 3（快速试用）
- 🎯 然后 Option 1（完整实施）
