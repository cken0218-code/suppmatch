#!/bin/bash
# Dashboard Wrapper Script
# Created: 2026-03-13
# Purpose: Run any command with automatic Dashboard updates

SCRIPTS_DIR=~/.openclaw/workspace/scripts

if [ $# -lt 2 ]; then
  echo "Usage: $0 <action_name> <command> [args...]"
  echo ""
  echo "Example:"
  echo "  $0 '系統健康檢查' check-system-health.sh"
  echo "  $0 '市場分析' python3 analyze-market.py"
  exit 1
fi

ACTION_NAME=$1
shift
COMMAND=$@

# Update Dashboard - Start
python3 "$SCRIPTS_DIR/update-status.py" action "$ACTION_NAME" 2>/dev/null

# Execute command
eval "$COMMAND"
EXIT_CODE=$?

# Update Dashboard - Complete
python3 "$SCRIPTS_DIR/update-status.py" action "閒置" 2>/dev/null

exit $EXIT_CODE
