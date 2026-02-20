#!/bin/bash
#===============================================================================
# AI Trends Research - Cron/Launchd Setup Script
#===============================================================================
# Purpose: Install the AI Trends Research automation schedule
# Usage: ./setup-schedule.sh [cron|launchd|both]
#===============================================================================

set -euo pipefail

SCRIPT_DIR="${HOME}/.openclaw/workspace/scripts"
CONFIG_DIR="${HOME}/.openclaw/workspace/config"
PLIST_FILE="${CONFIG_DIR}/com.openclaw.ai-trends-research.plist"

install_cron() {
    echo "Setting up cron job..."
    local cron_entry="0 2 * * * ${SCRIPT_DIR}/ai-trends-research.sh full >> ${HOME}/.openclaw/workspace/memory/learning/ai-trends/cron.log 2>&1"
    
    # Add to crontab
    (crontab -l 2>/dev/null | grep -v "ai-trends-research"; echo "$cron_entry") | crontab -
    
    echo "✅ Cron job installed"
    echo "   Schedule: 每天 02:00 (01:00-09:00 窗口內)"
    echo "   Command: ${SCRIPT_DIR}/ai-trends-research.sh full"
}

install_launchd() {
    echo "Setting up launchd (macOS)..."
    
    # Copy plist to LaunchAgents
    mkdir -p "${HOME}/Library/LaunchAgents"
    cp "${PLIST_FILE}" "${HOME}/Library/LaunchAgents/"
    
    # Load the daemon
    launchctl unload "${HOME}/Library/LaunchAgents/com.openclaw.ai-trends-research.plist" 2>/dev/null || true
    launchctl load "${HOME}/Library/LaunchAgents/com.openclaw.ai-trends-research.plist"
    
    echo "✅ Launchd daemon installed"
    echo "   Schedule: 每天 02:00"
    echo "   Label: com.openclaw.ai-trends-research"
}

show_status() {
    echo ""
    echo "========================================"
    echo "AI Trends Research Schedule Status"
    echo "========================================"
    
    echo ""
    echo "📅 Cron Jobs:"
    crontab -l 2>/dev/null | grep -E "ai-trends|研究" || echo "   No cron jobs found"
    
    echo ""
    echo "🚀 Launchd Agents:"
    launchctl list 2>/dev/null | grep -E "ai-trends|研究" || echo "   No launchd agents found"
    
    echo ""
    echo "📁 Configuration:"
    echo "   Script: ${SCRIPT_DIR}/ai-trends-research.sh"
    echo "   Plist: ${PLIST_FILE}"
    echo "   Topics: ${CONFIG_DIR}/research-topics.txt"
    
    echo ""
    echo "📊 Next Run:"
    echo "   Daily at 02:00 (within 01:00-09:00 window)"
}

case "${1:-both}" in
    cron)
        install_cron
        ;;
    launchd)
        install_launchd
        ;;
    both)
        install_cron
        # install_launchd  # Uncomment for macOS launchd
        ;;
    status)
        show_status
        ;;
    *)
        echo "Usage: $0 [cron|launchd|both|status]"
        exit 1
        ;;
esac
