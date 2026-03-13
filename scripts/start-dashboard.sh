#!/bin/bash
# Ken AI Dashboard Launcher
# Created: 2026-03-13
# Purpose: Start Ken AI monitoring system

echo "🚀 Ken AI Dashboard Launcher"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

WORKSPACE=~/.openclaw/workspace

# Check if API server is already running
if pgrep -f "status-api-server.py" > /dev/null; then
  echo "✅ API Server 已在運行"
else
  echo "🔄 啟動 API Server..."
  python3 "$WORKSPACE/scripts/status-api-server.py" &
  sleep 2
  echo "✅ API Server 已啟動 (http://127.0.0.1:18790)"
fi

echo ""
echo "📊 Dashboard 地址:"
echo "   - 本地文件: file://$WORKSPACE/dashboard.html"
echo "   - Gateway: http://127.0.0.1:18789/dashboard.html"
echo ""
echo "🔌 API 端點:"
echo "   - http://127.0.0.1:18790/api/status"
echo "   - http://127.0.0.1:18790/api/tasks"
echo "   - http://127.0.0.1:18790/api/activity"
echo "   - http://127.0.0.1:18790/api/models"
echo ""
echo "📝 狀態文件: $WORKSPACE/memory/ken-status.json"
echo ""
echo "🛑 停止 API Server: pkill -f status-api-server.py"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Open dashboard in browser
if command -v open > /dev/null; then
  echo ""
  read -p "是否在瀏覽器中打開 Dashboard？(y/n) " -n 1 -r
  echo
  if [[ $REPLY =~ ^[Yy]$ ]]; then
    open "$WORKSPACE/dashboard.html"
  fi
fi
