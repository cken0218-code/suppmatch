#!/usr/bin/env python3
"""
小红书 Trending 监控脚本
功能：爬取小红书热门话题和笔记
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# 输出目录
OUTPUT_DIR = Path(__file__).parent.parent / "output" / "trending"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def get_trending_mock():
    """
    模拟获取 trending 数据
    实际应该用 Playwright RPA 爬取
    """
    # 模拟数据（实际应该从网页爬取）
    trending_data = {
        "timestamp": datetime.now().isoformat(),
        "source": "xiaohongshu",
        "categories": {
            "美妆": [
                {"title": "春季必买口红推荐", "likes": 12500, "views": 89000},
                {"title": "敏感肌护肤攻略", "likes": 9800, "views": 65000},
                {"title": "平价粉底液测评", "likes": 8200, "views": 52000}
            ],
            "穿搭": [
                {"title": "春季穿搭灵感", "likes": 15600, "views": 102000},
                {"title": "小个子显高穿搭", "likes": 11300, "views": 78000},
                {"title": "通勤穿搭公式", "likes": 8900, "views": 61000}
            ],
            "美食": [
                {"title": "减脂餐食谱分享", "likes": 18900, "views": 125000},
                {"title": "早餐打卡30天", "likes": 14200, "views": 95000},
                {"title": "懒人料理合集", "likes": 10600, "views": 72000}
            ],
            "健康": [
                {"title": "改善睡眠质量", "likes": 22100, "views": 145000},
                {"title": "办公室拉伸", "likes": 13400, "views": 88000},
                {"title": "提高免疫力方法", "likes": 9700, "views": 63000}
            ]
        }
    }

    return trending_data

def analyze_trending(data):
    """
    分析 trending 数据
    """
    analysis = {
        "timestamp": data["timestamp"],
        "total_posts": 0,
        "avg_likes": 0,
        "avg_views": 0,
        "top_categories": [],
        "recommendations": []
    }

    all_likes = []
    all_views = []

    for category, posts in data["categories"].items():
        category_likes = sum(p["likes"] for p in posts)
        category_views = sum(p["views"] for p in posts)

        analysis["top_categories"].append({
            "category": category,
            "total_likes": category_likes,
            "total_views": category_views,
            "post_count": len(posts)
        })

        all_likes.extend([p["likes"] for p in posts])
        all_views.extend([p["views"] for p in posts])

    analysis["total_posts"] = len(all_likes)
    analysis["avg_likes"] = sum(all_likes) / len(all_likes) if all_likes else 0
    analysis["avg_views"] = sum(all_views) / len(all_views) if all_views else 0

    # 排序
    analysis["top_categories"].sort(key=lambda x: x["total_likes"], reverse=True)

    # 生成推荐
    top_category = analysis["top_categories"][0] if analysis["top_categories"] else None
    if top_category:
        analysis["recommendations"] = [
            f"🔥 最热门分类：{top_category['category']}（{top_category['total_likes']:,} likes）",
            f"📊 平均互动：{analysis['avg_likes']:,.0f} likes, {analysis['avg_views']:,.0f} views",
            f"💡 建议：创作 {top_category['category']} 相关内容"
        ]

    return analysis

def save_trending(data, analysis):
    """
    保存 trending 数据
    """
    date_str = datetime.now().strftime("%Y-%m-%d")
    time_str = datetime.now().strftime("%H%M%S")

    # 保存原始数据
    raw_file = OUTPUT_DIR / f"trending-{date_str}-{time_str}.json"
    with open(raw_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # 保存分析报告
    analysis_file = OUTPUT_DIR / f"analysis-{date_str}-{time_str}.json"
    with open(analysis_file, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, indent=2, ensure_ascii=False)

    return raw_file, analysis_file

def generate_report(analysis):
    """
    生成可读报告
    """
    report_lines = [
        "📊 小红书 Trending 监控报告",
        "=" * 50,
        f"📅 时间：{analysis['timestamp']}",
        f"📝 总帖子数：{analysis['total_posts']}",
        f"❤️ 平均点赞：{analysis['avg_likes']:,.0f}",
        f"👁️ 平均浏览：{analysis['avg_views']:,.0f}",
        "",
        "🔥 热门分类排行："
    ]

    for i, cat in enumerate(analysis["top_categories"], 1):
        report_lines.append(
            f"{i}. {cat['category']} - {cat['total_likes']:,} likes, {cat['total_views']:,} views"
        )

    report_lines.extend([
        "",
        "💡 推荐行动："
    ])

    for rec in analysis["recommendations"]:
        report_lines.append(f"  {rec}")

    return "\n".join(report_lines)

def main():
    """主流程"""
    print("🔍 小红书 Trending 监控启动...")
    print("=" * 50)

    # 获取 trending 数据
    print("📥 获取 trending 数据...")
    trending_data = get_trending_mock()

    # 分析数据
    print("📊 分析数据...")
    analysis = analyze_trending(trending_data)

    # 保存数据
    print("💾 保存数据...")
    raw_file, analysis_file = save_trending(trending_data, analysis)

    # 生成报告
    print("\n" + "=" * 50)
    report = generate_report(analysis)
    print(report)

    print("\n" + "=" * 50)
    print(f"✅ 原始数据：{raw_file}")
    print(f"✅ 分析报告：{analysis_file}")
    print("\n🎉 Trending 监控完成！")

    return analysis

if __name__ == "__main__":
    try:
        analysis = main()
        sys.exit(0)
    except Exception as e:
        print(f"❌ 错误：{e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
