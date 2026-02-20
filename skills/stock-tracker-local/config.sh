#!/bin/bash
# Stock Tracker 配置
# 本土化股票追蹤程式

# 🎯 數據來源配置
DATA_SOURCE="yfinance"  # yfinance, csv, api
CACHE_ENABLED=true
CACHE_DIR="$HOME/.cache/stock-tracker"

# 📈 技術指標參數
CCI_PERIOD=14
MACD_FAST=8
MACD_SLOW=12
MACD_SIGNAL=26
MA_SHORT=5
MA_LONG=20

# 💰 風險管理
DEFAULT_STOP_LOSS=8.0
DEFAULT_TAKE_PROFIT=15.0
MAX_POSITION_SIZE=25.0

# 📊 預設參數
DEFAULT_PERIOD="6mo"
DEFAULT_INTERVAL="1d"

# 📤 輸出格式
OUTPUT_FORMAT="terminal"  # terminal, json, csv, discord
DISCORD_WEBHOOK=""

# 🔄 更新頻率
REFRESH_INTERVAL=300  # 秒
AUTO_REFRESH=false
