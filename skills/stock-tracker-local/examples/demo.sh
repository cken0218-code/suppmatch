#!/bin/bash
# Stock Tracker 演示腳本

set -e

# 顏色
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

echo "╔═══════════════════════════════════════════════════════════════════╗"
echo "║              📈 STOCK TRACKER LOCAL DEMO                          ║"
echo "║                   本土化股票追蹤演示                             ║"
echo "╚═══════════════════════════════════════════════════════════════════╝"
echo ""

# 檢查依賴
echo -e "${CYAN}1. 檢查依賴...${NC}"
python3 -c "import yfinance; import pandas; import numpy" 2>/dev/null
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ 所有依賴已安裝${NC}"
else
    echo -e "${YELLOW}⚠️ 正在安裝依賴...${NC}"
    pip install -r requirements.txt
fi

echo ""
echo "──────────────────────────────────────────────────────────────────────"
echo ""

# 演示 1: 單一股票分析
echo -e "${CYAN}2. 演示: 單一股票分析 (AAPL)${NC}"
echo "──────────────────────────────────────────────────────────────────────"
python3 tracker.py --symbol=AAPL --report

echo ""
echo "──────────────────────────────────────────────────────────────────────"
echo ""

# 演示 2: 觀察名單
echo -e "${CYAN}3. 演示: 觀察名單${NC}"
echo "──────────────────────────────────────────────────────────────────────"
python3 tracker.py --import=watchlist.csv

echo ""
echo "──────────────────────────────────────────────────────────────────────"
echo ""

# 演示 3: 多支股票
echo -e "${CYAN}4. 演示: 多支股票 (GOOGL, MSFT)${NC}"
echo "──────────────────────────────────────────────────────────────────────"
python3 tracker.py --watchlist="GOOGL,MSFT"

echo ""
echo "╔═══════════════════════════════════════════════════════════════════╗"
echo "║                      🎉 演示完成                                  ║"
echo "╚═══════════════════════════════════════════════════════════════════╝"
echo ""
echo -e "${GREEN}下一步:${NC}"
echo "  • 修改 watchlist.csv 添加你追蹤的股票"
echo "  • 使用 --import 匯入你的觀察名單"
echo "  • 結合 cron-manager 設定定時檢查"
echo ""
