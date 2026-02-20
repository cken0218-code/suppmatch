#!/bin/bash
# Autonomous Runner - 主動回報系統
# 當收到長任務時，自動開 background session、設 cron check、完成後通知

set -e

# 顏色
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

# 配置
CHECK_INTERVAL=300  # 5分鐘檢查一次
SESSION_NAME="autonomous-runner"
DISCORD_CHANNEL="ken000ken"

usage() {
    cat << EOF
用法: autonomous-runner <選項>

選項:
    --task, -t      "任務描述"     (必填)
    --command, -c    "執行指令"     (必填)
    --label, -l      "任務標籤"     (可選，預設: autonomous-task)
    --interval, -i   檢查間隔秒數  (預設: 300)
    --notify         完成後通知     (預設: true)
    --help, -h       顯示幫助

範例:
    autonomous-runner --task "建立 Stock Tracker" \
        --command "python3 /path/to/tracker.py --aus CBA" \
        --label "stock-tracker-build"

EOF
    exit 1
}

# 解析參數
TASK=""
COMMAND=""
LABEL="autonomous-task"
INTERVAL=300
NOTIFY=true

while [[ $# -gt 0 ]]; do
    case $1 in
        --task|-t)
            TASK="$2"
            shift 2
            ;;
        --command|-c)
            COMMAND="$2"
            shift 2
            ;;
        --label|-l)
            LABEL="$2"
            shift 2
            ;;
        --interval|-i)
            INTERVAL="$2"
            shift 2
            ;;
        --notify)
            NOTIFY="$2"
            shift 2
            ;;
        --help|-h)
            usage
            ;;
        *)
            echo -e "${RED}未知參數: $1${NC}"
            usage
            ;;
    esac
done

# 驗證必填參數
if [ -z "$TASK" ] || [ -z "$COMMAND" ]; then
    echo -e "${RED}❌ 錯誤: --task 和 --command 係必填${NC}"
    usage
fi

# 生成任務 ID
TASK_ID=$(date +%s)-$$
echo "🤖 任務 ID: $TASK_ID"

echo ""
echo "╔═══════════════════════════════════════════════════════════════════╗"
echo "║              🚀 AUTONOMOUS RUNNER - 主動回報系統                  ║"
echo "╚═══════════════════════════════════════════════════════════════════╝"
echo ""
echo -e "${CYAN}📋 任務: $TASK${NC}"
echo -e "${CYAN}🏷️  標籤: $LABEL${NC}"
echo -e "${CYAN}⚙️  指令: $COMMAND${NC}"
echo ""

# 步驟 1: 開 Background Session
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${YELLOW}1️⃣ 步驟 1: 開 Background Session${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Validate COMMAND to prevent command injection
if [[ "$COMMAND" =~ [;&|`$(){}[\]\\><#*?!] ]]; then
    echo -e "${RED}❌ 錯誤: 命令包含非法字符${NC}"
    echo "不允許使用: ; & | ` \$ ( ) { } [ ] \\ < > # * ? !"
    exit 1
fi

# Sanitize LABEL and TASK_ID for file paths
SANITIZED_LABEL=$(echo "$LABEL" | tr -cd 'a-zA-Z0-9_-')
SANITIZED_LOG="/tmp/${SANITIZED_LABEL}_${TASK_ID}.log"

SESSION_KEY=$(openclaw sessions spawn \
    --task="$COMMAND" \
    --label="$LABEL" \
    --cleanup=delete 2>/dev/null | grep -o 'sessionKey:[^ ]*' | cut -d: -f2 || echo "")

if [ -z "$SESSION_KEY" ]; then
    # Fallback: 用 nohup (sanitized)
    echo "使用本地 background 模式..."
    nohup bash -c "$COMMAND" > "$SANITIZED_LOG" 2>&1 &
    BACKGROUND_PID=$!
    echo -e "${GREEN}✅ 已啟動 PID: $BACKGROUND_PID${NC}"
    SESSION_TYPE="local"
    LOG_FILE="$SANITIZED_LOG"
else
    echo -e "${GREEN}✅ Session Key: $SESSION_KEY${NC}"
    SESSION_TYPE="openclaw"
    LOG_FILE="$SANITIZED_LOG"
fi

# 步驟 2: 設 Cron 檢查
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${YELLOW}2️⃣ 步驟 2: 設 Cron 檢查 ($INTERVAL 秒)${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

CRON_NAME="check-${LABEL}-${TASK_ID}"
openclaw cron add \
    --name="$CRON_NAME" \
    --everyMs=$((INTERVAL * 1000)) \
    --session=isolated \
    --message="check-task-status --task-id=$TASK_ID --session=$SESSION_TYPE --session-key=$SESSION_KEY --pid=$BACKGROUND_PID --log=$LOG_FILE"

echo -e "${GREEN}✅ Cron 已設定: $CRON_NAME${NC}"

# 步驟 3: 返回任務資訊
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${GREEN}🎉 任務已啟動！${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📝 任務資訊:"
echo "   • 任務 ID: $TASK_ID"
echo "   • 標籤: $LABEL"
echo "   • Session: $SESSION_TYPE"
echo "   • Cron: $CRON_NAME"
echo "   • 檢查間隔: ${INTERVAL}秒"
echo ""
echo "📍 狀態查詢:"
echo "   • 查 log: tail -f $LOG_FILE"
echo "   • 查 cron: openclaw cron list | grep $CRON_NAME"
echo ""
echo "💡 完成後會自動 Discord DM 通知你 🟦"
echo ""

# 儲存任務資訊
TASK_INFO_FILE="/tmp/autonomous-runner-${TASK_ID}.json"
cat > "$TASK_INFO_FILE" << EOF
{
    "task_id": "$TASK_ID",
    "label": "$LABEL",
    "task": "$TASK",
    "command": "$COMMAND",
    "session_type": "$SESSION_TYPE",
    "session_key": "$SESSION_KEY",
    "pid": "$BACKGROUND_PID",
    "cron_name": "$CRON_NAME",
    "log_file": "$LOG_FILE",
    "start_time": "$(date +%s)",
    "notified": false
}
EOF

echo -e "${CYAN}📁 任務資訊已儲存: $TASK_INFO_FILE${NC}"
