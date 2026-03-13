#!/usr/bin/env python3
"""
YouTube Trending Search
搜尋 trending 話題並評估潛力
"""

import json
import sys
from datetime import datetime

# 熱門主題關鍵詞
TOPIC_KEYWORDS = [
    "AI tools",
    "productivity",
    "health supplements",
    "tech review",
    "automation",
    "ChatGPT",
    "Claude",
    "Gemini"
]

def assess_topic_potential(topic, description=""):
    """
    評估話題潛力（0-100分）

    評分標準：
    - 相關性（40分）：是否符合 content persona
    - 時效性（30分）：是否 trending
    - 變現潛力（30分）：能否整合 affiliate
    """
    score = 0

    # 相關性評分
    relevant_keywords = ["AI", "tools", "productivity", "health", "tech", "automation"]
    for keyword in relevant_keywords:
        if keyword.lower() in topic.lower():
            score += 7

    # 時效性評分
    trending_keywords = ["2026", "trending", "new", "latest", "March"]
    for keyword in trending_keywords:
        if keyword.lower() in topic.lower():
            score += 6

    # 變現潛力評分
    monetization_keywords = ["review", "comparison", "best", "top"]
    for keyword in monetization_keywords:
        if keyword.lower() in topic.lower():
            score += 8

    return min(score, 100)

def search_trending_topics():
    """
    搜尋 trending 話題
    注意：這是一個框架，實際需要整合 web_search API
    """
    # 模擬搜尋結果（實際應該用 web_search API）
    mock_results = [
        {
            "topic": "15 AI Tools Trending March 2026",
            "description": "Explore trending AI tools including ChatGPT, Claude, Gemini",
            "potential_score": 95
        },
        {
            "topic": "Productivity Hacks Using AI in 2026",
            "description": "How AI can boost your productivity",
            "potential_score": 85
        },
        {
            "topic": "Best Health Supplements for Sleep 2026",
            "description": "Science-backed supplements for better sleep",
            "potential_score": 80
        },
        {
            "topic": "AI Automation for Small Business",
            "description": "How to automate your business with AI",
            "potential_score": 88
        }
    ]

    # 評分排序
    for result in mock_results:
        result["potential_score"] = assess_topic_potential(
            result["topic"],
            result["description"]
        )

    # 按分數排序
    sorted_results = sorted(
        mock_results,
        key=lambda x: x["potential_score"],
        reverse=True
    )

    return sorted_results

def select_best_topic(topics):
    """
    選擇最佳題目
    """
    if not topics:
        return None

    best = topics[0]
    return {
        "topic": best["topic"],
        "description": best["description"],
        "potential_score": best["potential_score"],
        "reason": f"最高潛力分數：{best['potential_score']}/100"
    }

def main():
    """主流程"""
    print("🔍 搜尋 Trending 話題...")
    print("=" * 50)

    # 搜尋 trending
    topics = search_trending_topics()

    # 顯示結果
    print("\n📊 候選題目：")
    for i, topic in enumerate(topics, 1):
        print(f"{i}. {topic['topic']}")
        print(f"   潛力分數：{topic['potential_score']}/100")
        print()

    # 選擇最佳
    best = select_best_topic(topics)

    print("=" * 50)
    print("🎯 最佳題目：")
    print(f"   {best['topic']}")
    print(f"   {best['reason']}")
    print()

    # 保存結果
    output = {
        "timestamp": datetime.now().isoformat(),
        "topics": topics,
        "selected": best
    }

    output_file = f"youtube-scripts/trending-{datetime.now().strftime('%Y-%m-%d')}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"✅ 結果已保存到：{output_file}")

    return best

if __name__ == "__main__":
    try:
        best_topic = main()
        sys.exit(0)
    except Exception as e:
        print(f"❌ 錯誤：{e}")
        sys.exit(1)
