#!/bin/bash
# System Health Check Script
# Created: 2026-03-13
# Purpose: Check system health status

echo "🔍 System Health Check - $(date '+%Y-%m-%d %H:%M:%S')"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Gateway status
echo ""
echo "📡 Gateway Status:"
openclaw gateway status 2>&1 | head -10

# Check errors today
echo ""
echo "❌ Today's Errors:"
ERROR_COUNT=$(grep -c "ERROR" /tmp/openclaw/openclaw-$(date +%Y-%m-%d).log 2>/dev/null || echo 0)
echo "Count: $ERROR_COUNT"

if [ "$ERROR_COUNT" -gt 5 ]; then
  echo "⚠️ Warning: High error count!"
  grep "ERROR" /tmp/openclaw/openclaw-$(date +%Y-%m-%d).log | tail -5
fi

# Check disk space
echo ""
echo "💾 Disk Usage:"
df -h / | awk 'NR==1 || NR==2 {print}'

# Check memory
echo ""
echo "🧠 Memory Usage:"
vm_stat | perl -ne '/free.*?(\d+)/ && printf "Free: %.2f GB\n", $1 * 4096 / 1073741824'

# Check Git status
echo ""
echo "📦 Git Status:"
cd ~/.openclaw/workspace
git status --short | head -10

# Check recent commits
echo ""
echo "📝 Recent Commits (last 5):"
git log --oneline -5

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Health check complete"
