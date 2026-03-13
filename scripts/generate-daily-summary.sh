#!/bin/bash
# Daily Summary Generator Script
# Created: 2026-03-13
# Purpose: Generate daily summary from L1-daily log

TODAY=$(date +%Y-%m-%d)
LOG_FILE="$HOME/.openclaw/workspace/memory/L1-daily/$TODAY.md"

echo "📊 Daily Summary - $TODAY"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ ! -f "$LOG_FILE" ]; then
  echo "❌ No log file found for today"
  exit 1
fi

# Extract completed tasks
echo ""
echo "✅ Completed Tasks:"
grep -E "^- \[x\]" "$LOG_FILE" | head -10 || echo "None"

# Extract important findings
echo ""
echo "💡 Important Findings:"
grep -E "^### |^#### " "$LOG_FILE" | head -5 || echo "None"

# Extract errors
echo ""
echo "❌ Errors:"
ERROR_COUNT=$(grep -c "ERROR\|❌" "$LOG_FILE" || echo 0)
echo "Count: $ERROR_COUNT"
if [ "$ERROR_COUNT" -gt 0 ]; then
  grep "ERROR\|❌" "$LOG_FILE" | head -5
fi

# Extract next steps
echo ""
echo "🎯 Next Steps:"
grep -E "^- \[ \]" "$LOG_FILE" | head -10 || echo "None"

# Git stats
echo ""
echo "📝 Git Statistics:"
cd ~/.openclaw/workspace
COMMIT_COUNT=$(git log --oneline --since="$TODAY 00:00:00" --until="$TODAY 23:59:59" | wc -l | awk '{print $1}')
echo "Commits today: $COMMIT_COUNT"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Summary generated"
