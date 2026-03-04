#!/bin/bash
# OpenClaw Config Validator
# 每次改 config 前自動驗證

CONFIG_FILE=~/.openclaw/openclaw.json

echo "🔍 Validating OpenClaw config..."

# 檢查 config 是否有效
if openclaw config validate --json 2>&1 | grep -q "error"; then
    echo "❌ Config 有錯誤！唔會重啟 gateway"
    echo ""
    echo "錯誤詳情："
    openclaw config validate
    exit 1
else
    echo "✅ Config 正確"
    exit 0
fi
