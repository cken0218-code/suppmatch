# 技术限制说明 — YouTube / 小红书 Trending 监控

> **Created**: 2026-03-13 13:20
> **Purpose**: 澄清技术能力边界

---

## ⚠️ 技术限制

### YouTube

**可以做到**：
- ✅ 爬取 trending 标题和描述
- ✅ 读取视频元数据（views, likes, 发布时间）
- ✅ 读取字幕文件（如果有 .srt API）
- ✅ 搜索 trending 话题

**不能做到**：
- ❌ 真正"看"视频（无视觉理解能力）
- ❌ 分析视频内容（画面、动作、表情）
- ❌ 理解视频中的视觉元素

**最实际做法**：
```
定期搜索 YouTube trending
    ↓
读取标题 + 描述 + 标签
    ↓
（如果有字幕）读取字幕文本
    ↓
基于文字内容分析趋势
```

---

### 小红书

**可以做到**：
- ✅ 爬取文字内容（笔记正文）
- ✅ 读取标题、标签、互动数据
- ✅ RPA 自动化（已实现）

**不能做到**：
- ❌ 无 cookie 无法访问
- ❌ 需要登录才能看完整内容
- ❌ 图片/视频内容无法"看"

**最实际做法**：
```
使用 RPA + cookie 登录
    ↓
爬取热门笔记的文字内容
    ↓
分析标题 + 正文 + 标签
    ↓
基于文字数据识别趋势
```

---

## 📋 修正后的 Trending 监控方案

### YouTube Trending 监控（实际可行）

**方法 1：YouTube Data API**（推荐）
```python
# 使用官方 API
import googleapiclient.discovery

youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)

# 获取 trending videos
request = youtube.videos().list(
    part='snippet,statistics',
    chart='mostPopular',
    regionCode='US',
    maxResults=50
)

response = request.execute()

# 提取数据
for video in response['items']:
    title = video['snippet']['title']
    description = video['snippet']['description']
    tags = video['snippet'].get('tags', [])
    views = video['statistics']['viewCount']
```

**优点**：
- ✅ 官方支持，稳定
- ✅ 可以获取元数据
- ✅ 有字幕 API（部分视频）

**缺点**：
- ❌ 需要 API key
- ❌ 有配额限制

---

**方法 2：Web Scraping**（备选）
```python
# 使用 BeautifulSoup 或 Selenium
import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/feed/trending'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 提取 trending videos
videos = soup.find_all('a', class_='yt-simple-endpoint')
```

**优点**：
- ✅ 不需要 API key
- ✅ 无配额限制

**缺点**：
- ❌ 可能被 block
- ❌ 结构变化需要维护

---

### 小红书 Trending 监控（实际可行）

**方法：RPA + Cookie**（已实现）
```python
# 已有 xiaohongshu skill
# 使用 Playwright + cookie

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    
    # 加载 cookie
    context.add_cookies([cookie_data])
    
    page = context.new_page()
    page.goto('https://www.xiaohongshu.com/explore')
    
    # 爬取热门笔记
    notes = page.query_selector_all('.note-item')
    
    for note in notes:
        title = note.query_selector('.title').text_content()
        content = note.query_selector('.content').text_content()
        likes = note.query_selector('.likes').text_content()
```

**优点**：
- ✅ 可以访问完整内容
- ✅ 可以获取互动数据

**缺点**：
- ❌ 需要维护 cookie
- ❌ 可能触发反爬

---

## 🎯 修正后的 Heartbeat Trending Check

### YouTube Trending（每次 heartbeat）

**实际可行**：
```
1. 搜索 "AI automation trending"（用 web_search）
2. 读取搜索结果的标题 + 描述
3. 提取关键词
4. 记录到 trending report
```

**不能做**：
- ❌ "看"视频内容
- ❌ 分析视频画面

---

### 小红书 Trending（每次 heartbeat）

**实际可行**：
```
1. 使用 RPA 访问 explore page
2. 爬取热门笔记的文字内容
3. 提取关键词
4. 记录到 trending report
```

**不能做**：
- ❌ "看"图片/视频内容
- ❌ 无 cookie 访问

---

## 📝 更新 HEARTBEAT.md

### 修正前（错误）
```markdown
- [ ] X (Twitter) trending
- [ ] GitHub trending
- [ ] 小紅書 trending
```

### 修正后（正确）
```markdown
- [ ] X (Twitter) trending（搜索 + 文字分析）
- [ ] GitHub trending（API + 文字分析）
- [ ] YouTube trending（搜索 + 元数据分析，**不能看视频**）
- [ ] 小红书 trending（RPA + 文字爬取，**需要 cookie**）
```

---

## 💡 实际可行的 Trending 监控

### 每日 Trending Check（实际可行）

**YouTube**：
1. 用 web_search 搜索 "AI tools trending 2026"
2. 读取搜索结果的标题 + 描述
3. 提取关键词
4. 生成 trending report

**小红书**：
1. 用 RPA 访问 explore page
2. 爬取文字内容
3. 提取关键词
4. 生成 trending report

**GitHub**：
1. 用 GitHub API 获取 trending repos
2. 读取 README + 描述
3. 提取关键词
4. 生成 trending report

---

## 🔧 需要实现的工具

### 1. YouTube Trending API Wrapper
```python
# skills/youtube-agent/youtube-trending-api.py

def get_trending_videos(category='AI', max_results=50):
    """
    获取 YouTube trending videos（只读取元数据）
    """
    # 使用 YouTube Data API
    pass

def get_video_captions(video_id):
    """
    获取视频字幕（如果有）
    """
    # 使用 YouTube Captions API
    pass
```

### 2. 小红书 RPA Trending
```python
# skills/xiaohongshu/scripts/trending-rpa.py

def get_trending_notes(category='科技', max_notes=50):
    """
    用 RPA 爬取小红书热门笔记（文字内容）
    需要 cookie
    """
    # 使用 Playwright
    pass
```

---

## 📊 总结

| 平台 | 可以做 | 不能做 | 最实际方法 |
|------|--------|--------|------------|
| YouTube | 爬标题/描述/字幕 | 看视频内容 | API + 文字分析 |
| 小红书 | 爬文字内容 | 看图片/视频 | RPA + cookie |
| GitHub | 爬代码/README | - | API + 文字分析 |
| Twitter | 爬推文内容 | - | API + 文字分析 |

**关键点**：
- ✅ 基于文字内容的分析是可行的
- ❌ 视觉理解（看视频/图片）做不到
- ✅ 元数据（标题、描述、标签）足够识别趋势

---

**Created by**: Ken AI Assistant
**Date**: 2026-03-13
**Status**: 技术限制已澄清
**Next Action**: 更新 HEARTBEAT.md + 实现 API wrapper
