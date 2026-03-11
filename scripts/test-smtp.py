#!/usr/bin/env python3
"""
SMTP Test Script - 測試 Gmail SMTP 連線
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import sys
from pathlib import Path

# 讀取配置
config_path = Path.home() / ".openclaw" / "openclaw.json"
with open(config_path) as f:
    config = json.load(f)

smtp_config = config.get("email", {}).get("smtp", {})

# SMTP 配置
SMTP_HOST = smtp_config.get("host", "smtp.gmail.com")
SMTP_PORT = smtp_config.get("port", 587)
SMTP_USER = smtp_config.get("user", "")
SMTP_PASSWORD = smtp_config.get("password", "")

if not SMTP_USER or not SMTP_PASSWORD:
    print("❌ 錯誤：SMTP 配置缺失")
    sys.exit(1)

def test_smtp_connection():
    """測試 SMTP 連線"""
    print(f"🔍 測試 SMTP 連線...")
    print(f"   Host: {SMTP_HOST}")
    print(f"   Port: {SMTP_PORT}")
    print(f"   User: {SMTP_USER}")
    print()
    
    try:
        # 建立連線
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.set_debuglevel(0)  # 1 = 顯示詳細日誌
        
        # 啟用 TLS
        server.starttls()
        
        # 登入
        server.login(SMTP_USER, SMTP_PASSWORD)
        print("✅ SMTP 連線成功！")
        print()
        
        # 關閉連線
        server.quit()
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ 認證失敗：{e}")
        print()
        print("可能原因：")
        print("  1. App Password 錯誤")
        print("  2. Google 帳號安全設定阻擋")
        print("  3. 2FA 未啟用")
        return False
        
    except Exception as e:
        print(f"❌ 連線失敗：{e}")
        return False

def send_test_email(to_email=None):
    """發送測試郵件"""
    if not to_email:
        to_email = SMTP_USER  # 發送給自己
    
    print(f"📧 發送測試郵件到 {to_email}...")
    print()
    
    try:
        # 建立郵件
        msg = MIMEMultipart()
        msg['From'] = SMTP_USER
        msg['To'] = to_email
        msg['Subject'] = '🧪 OpenClaw SMTP 測試成功！'
        
        body = """
喵~ 🐱

這是一封測試郵件，來自 OpenClaw SMTP 配置。

如果你收到這封郵件，表示 SMTP 配置成功！

---
發送時間：{time}
配置文件：~/.openclaw/openclaw.json
        """.format(time=__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # 發送
        server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        print("✅ 測試郵件發送成功！")
        print(f"   收件人：{to_email}")
        print()
        print("📧 請檢查收件匣（可能在垃圾郵件）")
        return True
        
    except Exception as e:
        print(f"❌ 發送失敗：{e}")
        return False

if __name__ == "__main__":
    print("━━━━━━━━━━━━━━━━━━━━")
    print("🧪 OpenClaw SMTP 測試")
    print("━━━━━━━━━━━━━━━━━━━━")
    print()
    
    # 測試連線
    if test_smtp_connection():
        print()
        # 詢問是否發送測試郵件
        if len(sys.argv) > 1 and sys.argv[1] == "--send":
            send_test_email()
        else:
            print("💡 如要發送測試郵件，運行：")
            print(f"   python3 {sys.argv[0]} --send")
    else:
        print()
        print("❌ SMTP 配置失敗，請檢查：")
        print("   1. App Password 是否正確")
        print("   2. Google 帳號是否啟用 2FA")
        print("   3. 是否允許低安全性應用程式存取")
