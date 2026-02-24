---
name: threads-automation
description: Automates fetching trending topics from Threads, analyzing content, and storing insights into the knowledge base. Use when asked to check Threads trends, collect Threads content, or run Threads knowledge patrol.
---

# Threads Automation Skill

This skill provides structured workflow for collecting and analyzing trending content from Threads (Meta's text-based social platform).

## Workflow

### 1. Trend Collection
- Use `browser(profile="chrome")` to visit `https://www.threads.net/`
- Scroll to load trending content
- Extract top posts with high engagement

### 2. Content Analysis
- Filter posts by keywords: AI, automation, productivity, side hustle
- Extract: author, content, likes, replies, reposts
- Identify actionable insights

### 3. Knowledge Storage
- Save to `memory/knowledge/threads/` with timestamp
- Tag: trending, ai-tools, efficiency, side-hustles
- Format: Markdown with metadata

### 4. Weekly Summary (Sunday 8 PM)
- Pull top 10 insights from the week
- Generate summary report
- Notify user via Discord

## Scripts

### fetch-threads-trending.py
Main script for fetching trending content.

```bash
python3 scripts/fetch-threads-trending.py --output memory/knowledge/threads/
```

### analyze-content.py
Analyze collected content and extract insights.

```bash
python3 scripts/analyze-content.py --input memory/knowledge/threads/ --model glm-5
```

## Directory Structure

```
threads-automation/
├── SKILL.md           # This file
├── scripts/
│   ├── fetch-threads-trending.py
│   └── analyze-content.py
├── templates/
│   └── summary.md
└── output/            # Collected content
```

## Usage

**Daily Patrol:**
```
User: 執行知識庫巡邏
AI: [Runs x-automation + xiaohongshu + threads-automation]
```

**Manual Trigger:**
```
User: Check Threads trending
AI: [Runs fetch-threads-trending.py]
```

## Notes

- Threads requires browser automation (no public API)
- Use Chrome profile for logged-in access
- Rate limiting: Don't scrape more than 50 posts per session
- Respect Threads TOS

## Troubleshooting

- **Login required**: Ensure Chrome profile is logged into Threads
- **Rate limited**: Wait 30 minutes before retrying
- **No content**: Check if profile has correct language settings
