#!/bin/bash
# YouTube Workflow Cron Setup
# 设置每週一、三、五 10:00 自動執行

PROJECT_DIR="/Users/cken0218/.openclaw/workspace"
SCRIPT_PATH="$PROJECT_DIR/skills/youtube-workflow-local/run.py"
LOG_DIR="$PROJECT_DIR/logs"
CRON_JOB="0 10 * * 1,3,5 cd $PROJECT_DIR && /usr/bin/python3 $SCRIPT_PATH >> $LOG_DIR/youtube-workflow.log 2>&1"

echo "🎬 YouTube Workflow Cron Setup"
echo "================================"
echo ""
echo "Project Directory: $PROJECT_DIR"
echo "Script Path: $SCRIPT_PATH"
echo "Log Directory: $LOG_DIR"
echo ""

# 創建 log 目錄
mkdir -p "$LOG_DIR"

# 檢查當前 cron
echo "📋 當前 cron jobs:"
echo "----------------------------------------"
crontab -l 2>/dev/null | grep -i youtube || echo "無 YouTube 相關 cron job"
echo ""

# 添加 cron job
echo "⚙️  添加 cron job..."
echo ""

# 獲取當前 cron
CURRENT_CRON=$(crontab -l 2>/dev/null)

# 檢查是否已存在
if echo "$CURRENT_CRON" | grep -q "youtube-workflow"; then
    echo "⚠️  YouTube Workflow cron job 已存在"
    echo ""
    echo "現有 job:"
    echo "$CURRENT_CRON" | grep "youtube-workflow"
    echo ""
    read -p "是否要更新？(y/n): " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ 取消操作"
        exit 0
    fi
    # 移除舊的
    CURRENT_CRON=$(echo "$CURRENT_CRON" | grep -v "youtube-workflow")
fi

# 添加新的 cron job
(echo "$CURRENT_CRON"; echo "$CRON_JOB") | crontab -

echo "✅ Cron job 已添加"
echo ""
echo "📋 新的 cron job:"
echo "----------------------------------------"
crontab -l | grep "youtube-workflow"
echo ""

echo "📝 日誌文件: $LOG_DIR/youtube-workflow.log"
echo ""
echo "🔍 查看日誌命令:"
echo "   tail -f $LOG_DIR/youtube-workflow.log"
echo ""
echo "✅ 設置完成！"
