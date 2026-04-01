#!/usr/bin/env python3
"""
YouTube Video Performance Tracker
追踪视频表现和 affiliate 收入
"""

import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

DATA_FILE = "youtube-scripts/performance-data.json"

def init_data():
    """初始化數據文件"""
    if not Path(DATA_FILE).exists():
        data = {
            "created_at": datetime.now().isoformat(),
            "videos": [],
            "affiliate_clicks": [],
            "total_views": 0,
            "total_revenue": 0.0
        }
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return data
    
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def add_video(title, script_file, published_date=None):
    """添加新視頻記錄"""
    data = init_data()
    
    video = {
        "id": len(data["videos"]) + 1,
        "title": title,
        "script_file": script_file,
        "created_at": datetime.now().isoformat(),
        "published_date": published_date,
        "views": 0,
        "likes": 0,
        "comments": 0,
        "affiliate_clicks": 0,
        "revenue": 0.0,
        "status": "script"  # script, filming, editing, published
    }
    
    data["videos"].append(video)
    
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ 視頻記錄已添加：{title}")
    print(f"   ID: {video['id']}")
    print(f"   狀態: {video['status']}")
    
    return video

def update_video(video_id, **kwargs):
    """更新視頻數據"""
    data = init_data()
    
    for video in data["videos"]:
        if video["id"] == video_id:
            for key, value in kwargs.items():
                if key in video:
                    video[key] = value
            
            with open(DATA_FILE, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"✅ 視頻 #{video_id} 已更新")
            return video
    
    print(f"❌ 找不到視頻 #{video_id}")
    return None

def add_affiliate_click(video_id, affiliate_name, click_date=None):
    """記錄 affiliate 點擊"""
    data = init_data()
    
    click = {
        "video_id": video_id,
        "affiliate": affiliate_name,
        "date": click_date or datetime.now().isoformat(),
        "converted": False,
        "revenue": 0.0
    }
    
    data["affiliate_clicks"].append(click)
    
    # 更新視頻的 affiliate 點擊數
    for video in data["videos"]:
        if video["id"] == video_id:
            video["affiliate_clicks"] += 1
            break
    
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Affiliate 點擊已記錄：{affiliate_name}")
    return click

def show_stats():
    """顯示統計數據"""
    data = init_data()
    
    print("\n📊 YouTube 頻道表現統計")
    print("=" * 60)
    print(f"📅 統計時間：{datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()
    
    # 基本統計
    total_videos = len(data["videos"])
    published_videos = sum(1 for v in data["videos"] if v["status"] == "published")
    total_views = sum(v["views"] for v in data["videos"])
    total_affiliate_clicks = len(data["affiliate_clicks"])
    total_revenue = sum(v["revenue"] for v in data["videos"])
    
    print("📈 總體表現：")
    print(f"   腳本生成：{total_videos} 條")
    print(f"   已發布：{published_videos} 條")
    print(f"   總觀看：{total_views:,}")
    print(f"   Affiliate 點擊：{total_affiliate_clicks}")
    print(f"   總收入：${total_revenue:.2f}")
    print()
    
    # 最近視頻
    if data["videos"]:
        print("🎥 最近視頻（前 5 條）：")
        recent = sorted(data["videos"], key=lambda x: x["created_at"], reverse=True)[:5]
        for video in recent:
            status_emoji = {
                "script": "📝",
                "filming": "🎬",
                "editing": "✂️",
                "published": "✅"
            }.get(video["status"], "❓")
            
            print(f"   {status_emoji} #{video['id']} {video['title']}")
            print(f"      Views: {video['views']:,} | Revenue: ${video['revenue']:.2f}")
        print()
    
    # 轉化率
    if total_videos > 0:
        publish_rate = (published_videos / total_videos) * 100
        print(f"📊 轉化率：")
        print(f"   發布率：{publish_rate:.1f}%（{published_videos}/{total_videos}）")
        if total_views > 0:
            ctr = (total_affiliate_clicks / total_views) * 100
            print(f"   CTR：{ctr:.2f}%（{total_affiliate_clicks}/{total_views}）")
        print()
    
    print("=" * 60)

def list_videos(status=None):
    """列出視頻"""
    data = init_data()
    
    videos = data["videos"]
    if status:
        videos = [v for v in videos if v["status"] == status]
    
    print(f"\n🎥 視頻列表（{status or '全部'}）：")
    print("=" * 60)
    
    if not videos:
        print("   無記錄")
        return
    
    for video in videos:
        print(f"   #{video['id']} {video['title']}")
        print(f"   狀態：{video['status']} | Views：{video['views']:,}")
        print()

def main():
    """主程式"""
    if len(sys.argv) < 2:
        print("使用方式：")
        print("  python3 performance_tracker.py stats              # 顯示統計")
        print("  python3 performance_tracker.py add \"標題\" 腳本文件   # 添加視頻")
        print("  python3 performance_tracker.py update ID views=100 # 更新數據")
        print("  python3 performance_tracker.py list               # 列出所有視頻")
        print("  python3 performance_tracker.py list published     # 列出已發布")
        return
    
    command = sys.argv[1]
    
    if command == "stats":
        show_stats()
    elif command == "add":
        if len(sys.argv) < 4:
            print("❌ 缺少參數：python3 performance_tracker.py add \"標題\" 腳本文件")
            return
        title = sys.argv[2]
        script_file = sys.argv[3]
        add_video(title, script_file)
    elif command == "update":
        if len(sys.argv) < 4:
            print("❌ 缺少參數：python3 performance_tracker.py update ID key=value")
            return
        video_id = int(sys.argv[2])
        updates = {}
        for arg in sys.argv[3:]:
            if "=" in arg:
                key, value = arg.split("=", 1)
                # 嘗試轉換為數字
                try:
                    value = int(value)
                except ValueError:
                    try:
                        value = float(value)
                    except ValueError:
                        pass
                updates[key] = value
        update_video(video_id, **updates)
    elif command == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_videos(status)
    else:
        print(f"❌ 未知命令：{command}")

if __name__ == "__main__":
    main()
