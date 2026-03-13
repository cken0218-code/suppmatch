#!/bin/bash
# API Health Monitoring Script
# Created: 2026-03-13
# Purpose: Monitor API health status and detect failures

LOG_FILE="$HOME/.openclaw/workspace/memory/api-health-log.json"
ALERT_THRESHOLD=3  # Alert after 3 consecutive failures

echo "🔍 API Health Monitoring"
echo "━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Timestamp: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# Initialize log file if not exists
if [ ! -f "$LOG_FILE" ]; then
  echo '{"apis": {}, "last_check": "", "alerts": []}' > "$LOG_FILE"
fi

# Function to check API
check_api() {
  local api_name=$1
  local test_url=$2

  echo "Testing $api_name..."

  # Measure response time
  START_TIME=$(python3 -c "import time; print(time.time())")
  HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$test_url" 2>/dev/null || echo "000")
  END_TIME=$(python3 -c "import time; print(time.time())")

  RESPONSE_TIME=$(python3 -c "print(f'{$END_TIME - $START_TIME:.2f}')")

  # Determine status
  if [ "$HTTP_CODE" = "200" ] || [ "$HTTP_CODE" = "401" ]; then
    STATUS="✅ OK"
    FAILURE_COUNT=0
  else
    STATUS="❌ FAIL"
    # Increment failure count (simplified)
    FAILURE_COUNT=1
  fi

  echo "  Status: $STATUS"
  echo "  HTTP Code: $HTTP_CODE"
  echo "  Response Time: ${RESPONSE_TIME}s"
  echo ""

  # Update log
  python3 -c "
import json
import sys
from datetime import datetime

log_file = '$LOG_FILE'
api_name = '$api_name'
status = '$STATUS'
http_code = '$HTTP_CODE'
response_time = float('$RESPONSE_TIME')
failure_count = $FAILURE_COUNT

try:
    with open(log_file, 'r') as f:
        data = json.load(f)
except:
    data = {'apis': {}, 'last_check': '', 'alerts': []}

# Update API status
if api_name not in data['apis']:
    data['apis'][api_name] = {'failures': 0, 'last_success': ''}

if 'FAIL' in status:
    data['apis'][api_name]['failures'] += failure_count
else:
    data['apis'][api_name]['failures'] = 0
    data['apis'][api_name]['last_success'] = datetime.now().isoformat()

data['apis'][api_name]['last_check'] = {
    'status': status,
    'http_code': http_code,
    'response_time': response_time,
    'timestamp': datetime.now().isoformat()
}

# Check for alerts
if data['apis'][api_name]['failures'] >= 3:
    alert = {
        'api': api_name,
        'message': f'{api_name} has failed {data[\"apis\"][api_name][\"failures\"]} times',
        'timestamp': datetime.now().isoformat()
    }
    data['alerts'].append(alert)
    print(f'⚠️ ALERT: {alert[\"message\"]}')

data['last_check'] = datetime.now().isoformat()

with open(log_file, 'w') as f:
    json.dump(data, f, indent=2)
"
}

# Check GLM-5 (ZAI)
check_api "GLM-5 (ZAI)" "https://api.z.ai/v1/models"

# Check MiniMax
check_api "MiniMax" "https://api.minimaxi.com/anthropic/v1/models"

# Check Brave Search
check_api "Brave Search" "https://api.search.brave.com/res/v1/web/search"

# Check CoinGecko
check_api "CoinGecko" "https://api.coingecko.com/api/v3/ping"

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 Summary"
python3 -c "
import json
try:
    with open('$LOG_FILE', 'r') as f:
        data = json.load(f)

    total = len(data['apis'])
    ok = sum(1 for api in data['apis'].values() if 'OK' in api.get('last_check', {}).get('status', ''))
    fail = total - ok

    print(f'Total APIs: {total}')
    print(f'✅ OK: {ok}')
    print(f'❌ FAIL: {fail}')

    if data['alerts']:
        print(f'⚠️ Alerts: {len(data[\"alerts\"])}')
        for alert in data['alerts'][-3:]:  # Show last 3 alerts
            print(f'  - {alert[\"message\"]}')
except Exception as e:
    print(f'Error reading log: {e}')
"

echo ""
echo "✅ Health monitoring complete"
echo "Log saved to: $LOG_FILE"
