#!/usr/bin/env python3
"""
Xiaohongshu Cookie Extractor
用法: python3 get_cookies.py
会自动打开浏览器让你登录，登录后按回车保存cookies
"""

import json
import subprocess
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

COOKIES_FILE = Path(__file__).parent / "cookies" / "xiaohongshu.json"

def install_deps():
    """安装依赖"""
    print("📦 安装依赖...")
    subprocess.run([sys.executable, "-m", "pip", "install", "playwright", "-q"], check=True)
    subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
    print("✅ 依赖安装完成")

def get_cookies():
    """获取cookies"""
    print("🌐 打开浏览器...")
    print("请登录小红书，完成后回到此窗口按回车继续...")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # 打开小红书
        page.goto("https://www.xiaohongshu.com/")
        
        # 等待用户登录
        input("\n✅ 登录完成后，按回车继续...")
        
        # 获取cookies
        cookies = page.context.cookies()
        
        # 提取需要的cookie
        required = ['a1', 'web_session', 'webId']
        cookie_dict = {c['name']: c['value'] for c in cookies if c['name'] in required}
        
        browser.close()
        
        # 保存
        COOKIES_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(COOKIES_FILE, 'w') as f:
            json.dump(cookie_dict, f, indent=2)
        
        print(f"✅ Cookies已保存到: {COOKIES_FILE}")
        print(f"📋 获取到的cookies: {list(cookie_dict.keys())}")

if __name__ == "__main__":
    try:
        install_deps()
    except Exception as e:
        print(f"⚠️ 依赖已安装: {e}")
    
    get_cookies()
