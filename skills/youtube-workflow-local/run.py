#!/usr/bin/env python3
"""
YouTube Workflow - 完整自動化腳本
執行流程：Trending Search → Script Generation → Notification
"""

import sys
import json
import subprocess
from datetime import datetime
from pathlib import Path

# 簡單執行流程
def run_workflow():
    """執行完整工作流"""
    print("🎬 YouTube Workflow 自動產出系統")
    print("=" * 60)
    print(f"📅 執行時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Step 1: Trending Search
    print("🔍 Step 1: 搜尋 Trending 話題...")
    print("-" * 60)
    
    # 執行 trending_search.py
    result = subprocess.run(
        ["python3", "trending_search.py"],
        capture_output=True,
        text=True,
        cwd=str(Path(__file__).parent),
        timeout=30
    )
    
    if result.returncode != 0:
        print("❌ Trending 搜尋失敗")
        print(result.stderr)
        return False
    
    print(result.stdout)
    print()
    
    # Step 2: Script Generation
    print("📝 Step 2: 生成腳本...")
    print("-" * 60)
    
    # 執行 script_generator.py
    result = subprocess.run(
        ["python3", "script_generator.py"],
        capture_output=True,
        text=True,
        cwd=str(Path(__file__).parent),
        timeout=60
    )
    
    if result.returncode != 0:
        print("❌ 腳本生成失敗")
        print(result.stderr)
        return False
    
    print(result.stdout)
    print()
    
    # Step 3: Summary
    print("📊 產出摘要：")
    print("-" * 60)
    print(f"📄 查看產出：youtube-scripts/")
    
    return True

    # Step 3: Send Discord Notification (新增)
    print("\n📢 Step 3: 發送 Discord 通知...")
    print("-" * 60)
    
    try:
        # 執行 Discord 通知
        workspace_root = str(Path(__file__).parent.parent.parent)
        notifier_script = Path(workspace_root) / "scripts" / "youtube-discord-notifier.py"
        
        if notifier_script.exists():
            result = subprocess.run(
                ["python3", str(notifier_script)],
                capture_output=True,
                text=True,
                cwd=workspace_root,
                timeout=30
            )
            
            if result.returncode == 0:
                print("✅ Discord 通知發送成功")
                print(result.stdout)
            else:
                print("⚠️ Discord 通知發送失敗")
                print(result.stderr)
        else:
            print("⚠️ Discord 通知腳本不存在，跳過通知步驟")
    except Exception as e:
        print(f"⚠️ Discord 通知發送出錯：{e}")
    
    return success

if __name__ == "__main__":
    try:
        success = run_workflow()
        print("\n✅ 工作流完成！" if success else "\n❌ 工作流失敗")
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ 執行出錯：{e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
