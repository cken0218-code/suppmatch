#!/bin/bash
# Ken AI Auto-Start Configuration
# Created: 2026-03-13
# Purpose: Auto-start Dashboard API on login

# Get current user
USER=$(whoami)
WORKSPACE="/Users/$USER/.openclaw/workspace"

# Create LaunchAgent for API Server
cat > ~/Library/LaunchAgents/com.kenai.status-api.plist <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.kenai.status-api</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>$WORKSPACE/scripts/status-api-server.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardOutPath</key>
    <string>/tmp/kenai-status-api.log</string>
    <key>StandardErrorPath</key>
    <string>/tmp/kenai-status-api.err</string>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
    </dict>
</dict>
</plist>
EOF

echo "✅ LaunchAgent 已創建"
echo ""
echo "📁 位置: ~/Library/LaunchAgents/com.kenai.status-api.plist"
echo ""
echo "🚀 啟動方式:"
echo "   1. 登出後重新登入（自動啟動）"
echo "   2. 或者立即載入："
echo "      launchctl load ~/Library/LaunchAgents/com.kenai.status-api.plist"
echo ""
echo "📊 Dashboard 訪問:"
echo "   - 本地文件: file://$WORKSPACE/dashboard.html"
echo "   - API 端點: http://127.0.0.1:18790/api/status"
echo ""
echo "🛑 停止服務:"
echo "   launchctl unload ~/Library/LaunchAgents/com.kenai.status-api.plist"
echo ""
echo "📝 日誌位置:"
echo "   - /tmp/kenai-status-api.log"
echo "   - /tmp/kenai-status-api.err"
