#!/bin/bash
# 澳股买入信号自动扫描器
# 每日运行，发现买入信号时通知用户

WORKSPACE="/Users/cken0218/.openclaw/workspace/skills/aus-stock-tracker"
LOG_FILE="/tmp/stock-alert.log"

echo "================================" >> "$LOG_FILE"
echo "$(date '+%Y-%m-%d %H:%M:%S') - 开始扫描" >> "$LOG_FILE"

# 运行扫描
cd "$WORKSPACE"
python3 stock-alert.py >> "$LOG_FILE" 2>&1

# 检查是否有通知文件
NOTIFICATION_FILE="/tmp/stock-alert.json"

if [ -f "$NOTIFICATION_FILE" ]; then
    echo "✅ 发现买入信号，准备通知用户" >> "$LOG_FILE"
    
    # 读取通知内容
    MESSAGE=$(python3 -c "import json; print(json.load(open('$NOTIFICATION_FILE'))['message'])")
    
    # 通过 OpenClaw 发送 Discord 通知
    # 注意：这里需要 OpenClaw 的 message tool
    echo "$MESSAGE"
    
    # 清理通知文件
    rm "$NOTIFICATION_FILE"
else
    echo "😴 今日没有买入信号" >> "$LOG_FILE"
fi

echo "$(date '+%Y-%m-%d %H:%M:%S') - 扫描完成" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"
