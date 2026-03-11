# Union Search Skill 记录

> **安装时间**: 2026-03-08 01:09
> **来源**: https://github.com/runningZ1/union-search-skill
> **状态**: ⏸️ 备用（有需要先配置 TikHub）

---

## 📊 功能概览

### 支持平台（23 个）

| 分类 | 平台 | 需要 API Key |
|------|------|--------------|
| **搜索引擎** | DuckDuckGo, Brave, Yahoo, Wikipedia | ❌ 免费 |
| **搜索引擎** | Google, Bing, Yandex, Baidu | ✅ 需要 |
| **AI 搜索** | Tavily, 秘塔, 火山引擎, Jina | ✅ 需要 |
| **开发者** | GitHub, Reddit | ⚠️ GitHub 可选 |
| **社交媒体** | 抖音, B站, Twitter, 知乎, 微博, 小宇宙FM | ✅ 需要 TikHub |
| **工具** | Defuddle（网页提取） | ❌ 免费 |

### 图片搜索（16 个平台）
百度、Bing、Google、360、Yandex、搜狗、Yahoo、Pixabay、Unsplash、Gelbooru、Safebooru、Danbooru、Pexels、花瓣网、Foodiesfeed、火山引擎

---

## 🚀 使用方法

### 基础搜索（免费平台）
```bash
cd ~/.openclaw/workspace/skills/union-search-skill
python3 union_search_cli.py search "关键词" --platforms duckduckgo brave yahoo --limit 5 --pretty
```

### 开发者搜索
```bash
python3 union_search_cli.py search "AI agent" --group dev --limit 3 --pretty
```

### 社交媒体搜索（需要 TikHub）
```bash
python3 union_search_cli.py search "小红书关键词" --platforms xiaohongshu --limit 5 --pretty
```

### 视频下载
```bash
python3 union_search_cli.py download "https://www.youtube.com/watch?v=xxx" --output-dir ./downloads
```

### 图片搜索
```bash
python3 union_search_cli.py image "cute cats" --platforms google bing pixabay --limit 20 --output-dir ./images
```

---

## 🔧 配置

### 环境变量文件
位置：`~/.openclaw/workspace/skills/union-search-skill/.env`

### 已配置的免费平台
- ✅ DuckDuckGo
- ✅ Brave
- ✅ Yahoo
- ✅ Wikipedia
- ✅ GitHub（基础搜索）
- ✅ Defuddle

### 需要配置的平台
| 平台 | 环境变量 | 获取方式 |
|------|----------|----------|
| 小红书/抖音/B站/Twitter | TIKHUB_TOKEN | https://tikhub.io ($5/5000次) |
| Google | GOOGLE_API_KEY + GOOGLE_SEARCH_ENGINE_ID | Google Cloud Console |
| Bing/Yandex | SERPAPI_API_KEY | https://serpapi.com (免费250次/月) |
| YouTube | YOUTUBE_API_KEY | Google Cloud Console |
| Tavily | TAVILY_API_KEY | https://tavily.com (免费1000积分/月) |

---

## 📝 测试记录

### 2026-03-08 01:10
```bash
python3 union_search_cli.py search "AI agent" --platforms duckduckgo --limit 3 --pretty
```
- **结果**: ✅ 成功
- **耗时**: 3.4s
- **返回**: 2 条结果

---

## 🎯 推荐用法

### 日常搜索（免费）
```bash
# 快速搜索
python3 union_search_cli.py search "关键词" --platforms duckduckgo brave yahoo --limit 5

# 深度搜索
python3 union_search_cli.py search "关键词" --platforms duckduckgo brave yahoo wikipedia --preset large
```

### 内容研究（需要 TikHub）
```bash
# 小红书 trending
python3 union_search_cli.py search "香港美食" --platforms xiaohongshu --limit 10

# 抖音 trending
python3 union_search_cli.py search "AI工具" --platforms douyin --limit 10
```

### 开发者研究
```bash
# GitHub trending
python3 union_search_cli.py search "openclaw" --platforms github --limit 10

# Reddit 讨论
python3 union_search_cli.py search "AI agent" --platforms reddit --limit 5
```

---

## ⚠️ 注意事项

1. **小红书暂时禁用** - union orchestrator 中暂时禁用
2. **微博需要 Cookie** - 需要手动获取
3. **Reddit 可能 403** - 取决于 IP 和 endpoint
4. **火山引擎不稳定** - 响应解析偶发问题

---

## 🔗 相关链接

- GitHub: https://github.com/runningZ1/union-search-skill
- TikHub: https://tikhub.io
- SerpAPI: https://serpapi.com
- Tavily: https://tavily.com

---

*最后更新: 2026-03-08*
