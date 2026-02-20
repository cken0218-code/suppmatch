#!/bin/bash
# Autonomous Runner - 任務狀態檢查與通知
# 由 Cron 調用，檢查任務是否完成，完成後通知

set -e

# 顏色
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

# 配置
DISCORD_TARGET="ken000ken"

usage() {
    cat << EOF
用法: check-task-status <選項>

選項:
    --task-id, -i     任務 ID              (必填)
    --session, -s     session 類型         (openclaw/local)
    --session-key, -k  session key         (可選)
    --pid, -p         進程 PID             (local 模式用)
    --log, -l         日誌檔案              (可選)
    --notify, -n      完成後通知           (預設: true)
    --help, -h        顯示幫助

範例:
    # Local 模式
    check-task-status -i 1234567890 -s local -p 8315 -l /tmp/build.log

    # OpenClaw Session 模式
    check-task-status -i 1234567890 -s openclaw -k abc123

EOF
    exit 1
}

# 解析參數
TASK_ID=""
SESSION_TYPE=""
SESSION_KEY=""
PID=""
LOG_FILE=""
NOTIFY=true

while [[ $# -gt 0 ]]; do
    case $1 in
        --task-id|-i)
            TASK_ID="$2"
            shift 2
            ;;
        --session|-s)
            SESSION_TYPE="$2"
            shift 2
            ;;
        --session-key|-k)
            SESSION_KEY="$2"
            shift 2
            ;;
        --pid|-p)
            PID="$2"
            shift 2
            ;;
        --log|-l)
            LOG_FILE="$2"
            shift 2
            ;;
        --notify|-n)
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
if [ -z "$TASK_ID" ] || [ -z "$SESSION_TYPE" ]; then
    echo -e "${RED}❌ 錯誤: --task-id 和 --session 係必填${NC}"
    usage
fi

# 讀取任務資訊
TASK_INFO_FILE="/tmp/autonomous-runner-${TASK_ID}.json"
if [ -f "$TASK_INFO_FILE" ]; then
    source <(cat "$TASK_INFO_FILE" | sed 's/": "/="/g' | sed 's/[[:space:]]*,[[:space:]]*/ /g' | tr -d '{}"')
    LABEL=${label:-"unknown"}
    TASK=${task:-"unknown"}
    COMMAND=${command:-"unknown"}
else
    echo -e "${YELLOW}⚠️  未找到任務資訊檔案: $TASK_INFO_FILE${NC}"
    LABEL="unknown"
    TASK="unknown"
fi

# 檢查任務狀態
check_status() {
    case "$SESSION_TYPE" in
        openclaw)
            # 檢查 OpenClaw Session
            if [ -n "$SESSION_KEY" ]; then
                STATUS=$(openclaw sessions status "$SESSION_KEY" 2>/dev/null || echo "unknown")
                echo "$STATUS"
            else
                echo "unknown"
            fi
            ;;
        local)
            # 檢查本地進程
            if [ -n "$PID" ]; then
                if kill -0 "$PID" 2>/dev/null; then
                    echo "running"
                else
                    # 檢查退出碼
                    wait "$PID" 2>/dev/null
                    EXIT_CODE=$?
                    if [ $EXIT_CODE -eq 0 ]; then
                        echo "completed"
                    else
                        echo "failed:$EXIT_CODE"
                    fi
                fi
            elif [ -n "$LOG_FILE" ] && [ -f "$LOG_FILE" ]; then
                # 檢查日誌檔案
                if grep -q "✅\|完成\|success\|DONE" "$LOG_FILE" 2>/dev/null; then
                    echo "completed"
                elif grep -q "❌\|失敗\|error\|FAILED" "$LOG_FILE" 2>/dev/null; then
                    echo "failed"
                else
                    echo "running"
                fi
            else
                echo "unknown"
            fi
            ;;
        *)
            echo "unknown"
            ;;
    esac
}

# 獲取狀態
STATUS=$(check_status)

echo "╔═══════════════════════════════════════════════════════════════════╗"
echo "║              📊 任務狀態檢查                                        ║"
echo "╚═══════════════════════════════════════════════════════════════════╝"
echo ""
echo -e "${CYAN}📋 任務: $TASK${NC}"
echo -e "${CYAN}🏷️  標籤: $LABEL${NC}"
echo -e "${CYAN}🆔  ID: $TASK_ID${NC}"
echo ""
echo "📈 狀態: $STATUS"
echo ""

case "$STATUS" in
    completed)
        echo -e "${GREEN}✅ 任務已完成！${NC}"
        
        # 清理 Cron
        CRON_NAME="check-${LABEL}-${TASK_ID}"
        openclaw cron remove "$CRON_NAME" 2>/dev/null || true
        echo -e "${GREEN}🧹 Cron 已清理: $CRON_NAME${NC}"
        
        # Discord 通知
        if [ "$NOTIFY" = "true" ]; then
            echo ""
            echo -e "${YELLOW}📨 發送 Discord 通知...${NC}"
            
            # 構建通知訊息
            NOTIFICATION=$(cat << EOF
🎉 任務完成！

📋 任務: $TASK
🏷️  標籤: $LABEL
🆔  ID: $TASK_ID

⚙️  指令: $COMMAND

✅ 狀態: 完成
EOF
)
            # 發送 Discord DM
            message send \
                --channel="discord" \
                --target="$DISCORD_TARGET" \
                --message="$NOTIFICATION" 2>/dev/null || \
            echo -e "${YELLOW}⚠️  Discord 通知發送失敗（可能未配置）${NC}"
            
            echo -e "${GREEN}✅ Discord 通知已發送${NC}"
        fi
        
        # 更新任務資訊
        NOTIFIED=${notified:-false}
        if [ "$NOTIFIED" = "false" ]; then
            sed -i '' "s/\"notified\": false/\"notified\": true/" "$TASK_INFO_FILE" 2>/dev/null || true
        fi
        
        # 清理任務資訊（可選，保留一段時間）
        # rm -f "$TASK_INFO_FILE" 2>/dev/null || true
        
        ;;
        
    failed:*)
        EXIT_CODE=${STATUS#failed:}
        echo -e "${RED}❌ 任務失敗！退出碼: $EXIT_CODE${NC}"
        
        # 清理 Cron
        CRON_NAME="check-${LABEL}-${TASK_ID}"
        openclaw cron remove "$CRON_NAME" 2>/dev/null || true
        
        # Discord 通知（失敗）
        if [ "$NOTIFY" = "true" ]; then
            NOTIFICATION=$(cat << EOF
❌ 任務失敗！

📋 任務: $TASK
🏷️  標籤: $LABEL
🆔  ID: $TASK_ID

⚙️  指令: $COMMAND

❌ 狀態: 失敗 (退出碼: $EXIT_CODE)
EOF
)
            message send \
                --channel="discord" \
                --target="$DISCORD_TARGET" \
                --message="$NOTIFICATION" 2>/dev/null || true
        fi
        ;;
        
    running|unknown)
        echo -e "${YELLOW}⏳ 任務仍在運行中...${NC}"
        echo "下次檢查: $(date -v+${INTERVAL:-5}M '+%H:%M:%S' 2>/dev/null || date -d "+${INTERVAL:-5} minutes" '+%H:%M:%S')"
        ;;
        
    *)
        echo -e "${YELLOW}⚠️  未知狀態: $STATUS${NC}"
        ;;
esac

echo ""
