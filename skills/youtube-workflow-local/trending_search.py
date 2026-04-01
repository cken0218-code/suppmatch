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
    使用 web_search API（通過 OpenClaw）或降級到本地模擬
    """
    import subprocess
    import json
    
    # 嘗試用 OpenClaw web_search
    search_queries = [
        "AI tools trending 2026",
        "productivity hacks AI March 2026",
        "health supplements research 2026",
        "YouTube automation tools 2026"
    ]
    
    results = []
    
    for query in search_queries:
        try:
            # 使用 OpenClaw web_search（通過 subprocess）
            # 注意：這需要 OpenClaw 支持 CLI 調用
            cmd = f'openclaw search "{query}" --count 3 --format json'
            process = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if process.returncode == 0:
                search_results = json.loads(process.stdout)
                for item in search_results.get('results', []):
                    results.append({
                        "topic": item.get('title', query),
                        "description": item.get('description', ''),
                        "url": item.get('url', ''),
                        "source": "web_search"
                    })
        except (subprocess.TimeoutExpired, json.JSONDecodeError, FileNotFoundError):
            # 降級：使用模擬數據
            pass
    
    # 如果沒有真實結果，使用本地模擬
    if not results:
        print("⚠️  使用本地模擬數據（web_search 不可用）")
        mock_results = [
            {
                "topic": "15 AI Tools Trending March 2026",
                "description": "Explore trending AI tools including ChatGPT, Claude, Gemini, and productivity boosters",
                "source": "mock"
            },
            {
                "topic": "Productivity Hacks Using AI in 2026",
                "description": "How AI can boost your productivity with automation workflows",
                "source": "mock"
            },
            {
                "topic": "Best Health Supplements for Sleep 2026",
                "description": "Science-backed supplements for better sleep: Magnesium, Melatonin, Ashwagandha",
                "source": "mock"
            },
            {
                "topic": "AI Automation for Small Business",
                "description": "How to automate your business with AI tools and workflows",
                "source": "mock"
            },
            {
                "topic": "YouTube Automation Tools 2026",
                "description": "Best tools for YouTube content automation: vidIQ, Descript, Canva AI",
                "source": "mock"
            }
        ]
        results = mock_results
    
    # 評分排序
    for result in results:
        result["potential_score"] = assess_topic_potential(
            result["topic"],
            result.get("description", "")
        )
    
    # 按分數排序
    sorted_results = sorted(
        results,
        key=lambda x: x["potential_score"],
        reverse=True
    )
    
    return sorted_results[:5]  # 返回前 5 個

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
