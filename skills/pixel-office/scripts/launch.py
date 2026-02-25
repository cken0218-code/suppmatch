#!/usr/bin/env python3
"""
OpenClaw Pixel Office Launcher
啟動 Pixel Office 儀表板
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

def main():
    # 獲取 webview 目錄
    script_dir = Path(__file__).parent
    webview_dir = script_dir / "webview"
    
    if not webview_dir.exists():
        print(f"❌ 找不到 webview 目錄: {webview_dir}")
        sys.exit(1)
    
    # 切換到 webview 目錄
    os.chdir(webview_dir)
    
    PORT = 8888
    
    # 創建 HTTP 伺服器
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            url = f"http://localhost:{PORT}"
            print(f"🦞 OpenClaw Pixel Office")
            print(f"=" * 40)
            print(f"📍 URL: {url}")
            print(f"📂 目錄: {webview_dir}")
            print(f"")
            print(f"💡 按 Ctrl+C 停止伺服器")
            print(f"=" * 40)
            
            # 自動打開瀏覽器
            webbrowser.open(url)
            
            # 啟動伺服器
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 Pixel Office 已關閉")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {PORT} 已被使用")
            print(f"💡 嘗試其他 port 或關閉佔用嘅程序")
        else:
            raise

if __name__ == "__main__":
    main()
