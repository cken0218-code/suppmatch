#!/usr/bin/env python3
"""
YouTube Content Generator
根據 trending 題材生成標題、描述、標籤
"""

import json
from datetime import datetime
from pathlib import Path

WORKSPACE = Path.home() / ".openclaw" / "workspace"
MEMORY_DIR = WORKSPACE / "memory" / "youtube"
TEMPLATES_DIR = WORKSPACE / "skills" / "youtube-agent" / "templates"

# 標題模板
TITLE_TEMPLATES = {
    "tutorial": [
        "如何在 {year} {action}（{benefit}）",
        "{year} {topic} 完整教學 | {benefit}",
        "{topic} 入門指南：{action} {time}",
        "【{year}最新】{topic} {action} 教學",
    ],
    "trend": [
        "{year} {topic} 趨勢分析 | {insight}",
        "{topic} 崛起：為何 {reason}？",
        "為什麼 {topic} 在 {year} 爆紅？",
        "{topic} vs {competitor}：{year} 誰贏？",
    ],
    "news": [
        "突發！{event} - {impact}",
        "{company} 剛剛宣布 {announcement}",
        "【{year}重要】{topic} 重大更新",
        "{topic} 震撼消息：{headline}",
    ]
}

# 描述模板
DESCRIPTION_TEMPLATE = """
🎯 在這部影片中，你會學到：
{learning_points}

📺 時間軸：
{timestamps}

🔗 相關連結：
{links}

💬 問題？留言問我！

🔔 訂閱更多 {topic} 內容！

#YouTube #AI #Automation #ContentCreation
"""

def generate_title(topic, category="tutorial", year=2026):
    """生成標題建議"""
    import random
    
    templates = TITLE_TEMPLATES.get(category, TITLE_TEMPLATES["tutorial"])
    
    suggestions = []
    for template in templates[:3]:
        title = template.format(
            year=year,
            topic=topic,
            action="開始使用",
            benefit="慳時間又慳錢",
            time="10分鐘",
            insight="必知趨勢",
            reason="市場需求大增",
            competitor="傳統方法",
            event="重大消息",
            impact="影響深遠",
            company="OpenAI",
            announcement="新功能",
            headline="你一定要知"
        )
        suggestions.append(title)
    
    return suggestions

def generate_tags(topic, category="tutorial"):
    """生成標籤"""
    base_tags = [
        "YouTube",
        "AI",
        "Automation",
        "Tutorial",
        "How to",
        topic.replace(" ", ""),
    ]
    
    category_tags = {
        "tutorial": ["教學", "指南", "入門", "Step by step"],
        "trend": ["趨勢", "2026", "分析", "預測"],
        "news": ["新聞", "最新", "更新", "Breaking"],
    }
    
    tags = base_tags + category_tags.get(category, [])
    return tags[:10]  # 最多 10 個標籤

def generate_description(topic, category="tutorial"):
    """生成描述"""
    learning_points = f"""
• 什麼是 {topic}
• 如何開始使用 {topic}
• {topic} 的實際應用
• 常見問題解答
"""
    
    timestamps = """
0:00 開始
1:00 簡介
3:00 主要內容
8:00 實際操作
10:00 總結
"""
    
    links = f"""
• {topic} 官網
• 相關資源
• 代碼示例
"""
    
    description = DESCRIPTION_TEMPLATE.format(
        learning_points=learning_points,
        timestamps=timestamps,
        links=links,
        topic=topic
    )
    
    return description.strip()

def generate_content(topic, category="tutorial"):
    """生成完整內容"""
    titles = generate_title(topic, category)
    tags = generate_tags(topic, category)
    description = generate_description(topic, category)
    
    content = {
        "topic": topic,
        "category": category,
        "generated_at": datetime.now().isoformat(),
        "titles": titles,
        "tags": tags,
        "description": description,
        "thumbnail_text_suggestions": [
            f"{topic} 教學",
            f"2026 {topic}",
            f"如何 {topic}",
        ]
    }
    
    return content

if __name__ == "__main__":
    # 測試
    topic = "Multi-Agent Orchestration"
    content = generate_content(topic, "tutorial")
    
    print(f"📝 內容生成：{topic}\n")
    print("📌 標題建議：")
    for i, title in enumerate(content['titles'], 1):
        print(f"  {i}. {title}")
    
    print("\n🏷️ 標籤：")
    print(f"  {', '.join(content['tags'])}")
    
    print("\n📄 描述：")
    print(content['description'][:200] + "...")
