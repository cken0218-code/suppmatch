#!/bin/bash
# Safe Config Updater
# 自動備份 + 驗證 + 回滾機制

CONFIG_FILE=~/.openclaw/openclaw.json
BACKUP_DIR=~/.openclaw/backups
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo "🛡️ Safe Config Updater"
echo "======================"
echo ""

# 1. 備份現有 config
echo "📦 Step 1: 備份現有 config..."
mkdir -p $BACKUP_DIR
cp $CONFIG_FILE $BACKUP_DIR/openclaw_$TIMESTAMP.json
echo "✅ 已備份到: $BACKUP_DIR/openclaw_$TIMESTAMP.json"
echo ""

# 2. 驗證新 config
echo "🔍 Step 2: 驗證 config..."
if openclaw config validate --json 2>&1 | grep -q "error"; then
    echo "❌ Config 有錯誤！"
    echo ""
    echo "錯誤詳情："
    openclaw config validate
    echo ""
    echo "🔄 回滾到上一個版本..."
    cp $BACKUP_DIR/openclaw_$TIMESTAMP.json $CONFIG_FILE
    echo "✅ 已回滾"
    exit 1
else
    echo "✅ Config 正確"
fi
echo ""

# 3. 測試 gateway 啟動
echo "🚀 Step 3: 測試 gateway 啟動..."
timeout 10 openclaw gateway start 2>&1 | head -20

if [ $? -eq 0 ]; then
    echo "✅ Gateway 啟動成功"
    echo ""
    echo "🎉 Config 更新完成！"
else
    echo "❌ Gateway 啟動失敗"
    echo ""
    echo "🔄 回滾到上一個版本..."
    cp $BACKUP_DIR/openclaw_$TIMESTAMP.json $CONFIG_FILE
    echo "✅ 已回滾"
    exit 1
fi

# 4. 清理舊備份（保留最近 5 個）
echo ""
echo "🧹 清理舊備份..."
ls -t $BACKUP_DIR/openclaw_*.json | tail -n +6 | xargs rm -f
echo "✅ 已清理"
