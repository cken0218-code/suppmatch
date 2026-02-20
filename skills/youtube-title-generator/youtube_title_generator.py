#!/usr/bin/env python3
"""
YouTube Title Generator - 為 YouTube 影片生成吸引人的標題

使用方法:
    python3 youtube_title_generator.py --topic "教學影片" --style "吸引點擊" --keywords "Python,程式設計"
    
互動模式:
    python3 youtube_title_generator.py
"""

import argparse
import random
import re
from datetime import datetime
from typing import List, Dict, Optional


class YouTubeTitleGenerator:
    """YouTube 標題生成器類別"""
    
    # 標題模板
    TEMPLATES = {
        "教學": [
            "{keywords}入門教學 | {level}分鐘學會",
            "初學者必看 | {keywords}完整教學",
            "{keywords}速成班 | {time}分鐘精通",
            "學會{keywords}的{count}個技巧 | 新手教學",
            "{keywords}從零到高手 | 完整攻略",
        ],
        "吸引點擊": [
            "你絕對想不到的{keywords}方法！",
            "{keywords}背後的秘密 | 看完才懂",
            "{keywords}讓我{result}！| 經驗分享",
            "{keywords}注意事項 | 90%人都做錯",
            "為什麼{keywords}這麼有效？",
        ],
        "問答": [
            "{keywords}到底好不好？| 優缺點分析",
            "{keywords}值得學嗎？| 真實評測",
            "{keywords}常見問題解答 | FAQ",
            "{keywords}疑問一次解決 | 完整指南",
            "如何選擇{keywords}？| 專家建議",
        ],
        "趨勢": [
            "2026年{keywords}新趨勢搶先看",
            "{keywords}最新技巧 | 必須知道",
            "跟上{keywords}熱潮 | {year}必學",
            "{keywords}改變了！| 新功能教學",
            "2026 {keywords}完整攻略",
        ],
        "挑戰": [
            "{keywords}挑戰賽 | {count}天後成果公開",
            "挑戰連續{keywords}{count}天 | Day 1",
            "{keywords}30天改變計劃 | 成果對比",
            "新手VS老手 | {keywords}差異有多大？",
            "{keywords}極限挑戰 | 結果出乎意料",
        ]
    }
    
    # 情緒詞彙
    EMOTIONAL_WORDS = [
        "驚人", "震撼", "必看", "必學", "獨家", "秘密", "完整",
        "專業", "進階", "新手", "專家", "高效", "快速", "簡易",
        "終極", "終極指南", "終極攻略", "大公開", "首度公開"
    ]
    
    # 數字模式
    NUMBER_PATTERNS = [
        "{count}個技巧", "{count}分鐘", "{count}天學會", 
        "{count}個步驟", "{count}個重點", "{count}個常見錯誤"
    ]
    
    def __init__(self):
        self.history: List[Dict] = []
    
    def generate(
        self, 
        topic: str, 
        style: str = "吸引點擊", 
        keywords: Optional[List[str]] = None,
        count: int = 5
    ) -> List[str]:
        """
        生成標題
        
        Args:
            topic: 主題
            style: 風格 (教學/吸引點擊/問答/趨勢/挑戰)
            keywords: 關鍵詞列表
            count: 生成數量
            
        Returns:
            生成的標題列表
        """
        if keywords is None:
            keywords = [topic]
        
        # 隨機選擇模板
        templates = self.TEMPLATES.get(style, self.TEMPLATES["吸引點擊"])
        results = []
        
        for _ in range(count):
            template = random.choice(templates)
            title = self._fill_template(template, topic, keywords)
            results.append(title)
        
        # 記錄到歷史
        self.history.append({
            "timestamp": datetime.now().isoformat(),
            "topic": topic,
            "style": style,
            "titles": results
        })
        
        return results
    
    def _fill_template(self, template: str, topic: str, keywords: List[str]) -> str:
        """填充模板"""
        keyword = random.choice(keywords)
        
        # 隨機數字
        numbers = [3, 5, 7, 10, 15, 20, 30]
        num = random.choice(numbers)
        
        # 隨機結果詞
        results = ["成功了", "賺到錢", "變強了", "突破了", "翻身了", "開心了"]
        result = random.choice(results)
        
        # 年份
        year = datetime.now().year
        
        # 填充
        title = template.format(
            keywords=keyword,
            topic=topic,
            level=f"{num}",
            time=f"{random.randint(5, 60)}",
            count=num,
            result=result,
            year=year
        )
        
        # 隨機添加情緒詞
        if random.random() < 0.3:
            emotional = random.choice(self.EMOTIONAL_WORDS)
            title = f"{emotional} | {title}"
        
        return title
    
    def add_emotional_hook(self, title: str) -> str:
        """為標題添加情緒鉤子"""
        hooks = [
            "你一定要知道...",
            "千萬別錯過...",
            "這個秘密...",
            "令人震驚...",
            "不敢相信...",
            "後果自負...",
            "趕快收藏..."
        ]
        hook = random.choice(hooks)
        return f"{hook} {title}"
    
    def analyze_title(self, title: str) -> Dict:
        """分析標題"""
        analysis = {
            "title": title,
            "length": len(title),
            "has_numbers": bool(re.search(r'\d+', title)),
            "has_emotion": any(word in title for word in self.EMOTIONAL_WORDS),
            "word_count": len(title.split()),
            "recommendation": ""
        }
        
        # 給出建議
        if analysis["length"] > 60:
            analysis["recommendation"] = "⚠️ 標題過長，可能被截斷"
        elif analysis["length"] < 30:
            analysis["recommendation"] = "⚠️ 標題過短，建議增加關鍵詞"
        else:
            analysis["recommendation"] = "✅ 標題長度適中"
        
        if not analysis["has_numbers"]:
            analysis["recommendation"] += " | 建議加入數字增加點擊率"
        
        if not analysis["has_emotion"]:
            analysis["recommendation"] += " | 建議加入情緒詞"
        
        return analysis
    
    def save_history(self, filepath: str = "title_history.json"):
        """保存歷史記錄"""
        import json
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)
        print(f"✅ 歷史已保存到 {filepath}")


def main():
    parser = argparse.ArgumentParser(
        description="YouTube Title Generator - 生成吸引人的標題",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
範例:
    # 互動模式
    python3 youtube_title_generator.py
    
    # 指定主題生成
    python3 youtube_title_generator.py --topic "Python程式設計"
    
    # 指定風格和關鍵詞
    python3 youtube_title_generator.py --topic "健身" --style "挑戰" --keywords "增肌,減脂"
    
    # 生成多個標題
    python3 youtube_title_generator.py --topic "投資理財" --count 10
        """
    )
    
    parser.add_argument("--topic", "-t", type=str, help="影片主題")
    parser.add_argument("--style", "-s", type=str, default="吸引點擊",
                        choices=["教學", "吸引點擊", "問答", "趨勢", "挑戰"],
                        help="標題風格")
    parser.add_argument("--keywords", "-k", type=str, help="關鍵詞 (逗號分隔)")
    parser.add_argument("--count", "-c", type=int, default=5, help="生成數量 (默認: 5)")
    parser.add_argument("--analyze", "-a", type=str, help="分析現有標題")
    parser.add_argument("--output", "-o", type=str, help="保存歷史到檔案")
    
    args = parser.parse_args()
    
    generator = YouTubeTitleGenerator()
    
    # 分析模式
    if args.analyze:
        result = generator.analyze_title(args.analyze)
        print(f"\n📊 標題分析結果:")
        print(f"   標題: {result['title']}")
        print(f"   字數: {result['length']} | 詞數: {result['word_count']}")
        print(f"   包含數字: {'是' if result['has_numbers'] else '否'}")
        print(f"   包含情緒詞: {'是' if result['has_emotion'] else '否'}")
        print(f"   建議: {result['recommendation']}")
        return
    
    # 互動模式或主題模式
    if not args.topic:
        print("🎬 YouTube 標題生成器")
        print("=" * 40)
        args.topic = input("📝 請輸入影片主題: ").strip()
        
        print("\n🎨 選擇標題風格:")
        print("   1. 教學")
        print("   2. 吸引點擊")
        print("   3. 問答")
        print("   4. 趨勢")
        print("   5. 挑戰")
        choice = input("   請選擇 (1-5, 默認2): ").strip() or "2"
        
        style_map = {"1": "教學", "2": "吸引點擊", "3": "問答", "4": "趨勢", "5": "挑戰"}
        args.style = style_map.get(choice, "吸引點擊")
        
        keywords_input = input("\n🏷️  關鍵詞 (逗號分隔, 可留空): ").strip()
        args.keywords = keywords_input if keywords_input else None
        args.count = int(input("\n📊 生成數量 (默認5): ").strip() or "5")
    
    # 處理關鍵詞
    keywords = None
    if args.keywords:
        keywords = [k.strip() for k in args.keywords.split(",")]
    
    # 生成標題
    print(f"\n🎬 主題: {args.topic}")
    print(f"🎨 風格: {args.style}")
    print(f"🏷️  關鍵詞: {keywords or '使用主題'}")
    print("=" * 50)
    print("✨ 生成的標題:")
    print("-" * 50)
    
    titles = generator.generate(
        topic=args.topic,
        style=args.style,
        keywords=keywords,
        count=args.count
    )
    
    for i, title in enumerate(titles, 1):
        print(f"  {i}. {title}")
    
    # 額外建議
    print("-" * 50)
    print("💡 小提示:")
    print("   • 前30個字符最重要，確保包含核心關鍵詞")
    print("   • 使用數字和問句增加點擊率")
    print("   • 避免過度點擊誘餌 (clickbait)")
    
    # 保存歷史
    if args.output:
        generator.save_history(args.output)
    else:
        generator.save_history()


if __name__ == "__main__":
    main()
