# Stock Tracker Local

本土化股票追蹤程式 - 基於技術指標的買賣信號分析

## 簡介

參考 spoutnik rebirth h1v1.0 顺势交易概念，改編為：
- **適用標的**：股票（而非外汇）
- **周期**：H4 (4小時) + 日線 雙重確認
- **數據源**：Yahoo Finance（免費）
- **風格**：技術分析 + 多周期驗證

## 架構

```
╔═══════════════════════════════════════════════════════════════════════╗
║                    📈 STOCK TRACKER LOCAL v1.0.0                      ║
║                   本土化股票追蹤與技術分析系統                        ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                       ║
║   ┌─────────────────┐     ┌─────────────────┐                         ║
║   │   數據獲取層    │     │   指標計算層    │                         ║
║   │  yfinance       │ ──▶ │  CCI           │                         ║
║   │  CSV匯入        │     │  MACD          │                         ║
║   │  實時報價       │     │  MA Cross      │                         ║
║   └─────────────────┘     └─────────────────┘                         ║
║            │                       │                                    ║
║            ▼                       ▼                                    ║
║   ┌─────────────────┐     ┌─────────────────┐                         ║
║   │   信號生成層    │     │   風險管理層    │                         ║
║   │  多周期確認     │ ──▶ │  止盈止損計算   │                         ║
║   │  買賣信號       │     │  倉位管理       │                         ║
║   └─────────────────┘     └─────────────────┘                         ║
║            │                                                    ║
║            ▼                                                    ║
║   ┌─────────────────────────────────────────────────────────┐     ║
║   │                      輸出層                               │     ║
║   │   信號報告 / 追蹤歷史 / CSV匯出 / Discord 通知           │     ║
║   └─────────────────────────────────────────────────────────┘     ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
```

## 技術指標

### 1. CCI (Commodity Channel Index) - 商品通道指數
- **參數**：14 周期
- **用途**：識別超買超賣
- **閾值**：+100 (超買) / -100 (超賣)

### 2. MACD - 移動平均匯聚發散
- **參數**：8, 12, 26（快速/慢速/信號）
- **用途**：趨勢方向
- **信號**：金叉/死叉、0線穿越

### 3. MA Cross - 均線交叉
- **參數**：5 / 20（短期/長期）
- **用途**：確認趨勢

## 交易信號邏輯

### 🟢 買入信號（需全部滿足）
```
H4 週期:
  ✓ CCI 穿越 0 線向上
  ✓ MACD 穿越 0 線向上
  ✓ MA5 在 MA20 之上
  ✓ Flat Trend = 綠色

日線 週期:
  ✓ CCI > 0
  ✓ MACD > 0 或 金叉
  ✓ MA5 > MA20
```

### 🔴 賣出信號（需全部滿足）
```
H4 週期:
  ✓ CCI 穿越 0 線向下
  ✓ MACD 穿越 0 線向下
  ✓ MA5 在 MA20 之下
  ✓ Flat Trend = 紅色

日線 週期:
  ✓ CCI < 0
  ✓ MACD < 0 或 死叉
  ✓ MA5 < MA20
```

### 🟡 持有信號
- 條件未完全滿足
- 顯示為「觀望」狀態

## 安裝

### 前置需求
```bash
# Python 3.8+
python3 --version

# 安裝依賴
pip install -r requirements.txt
```

### requirements.txt
```
yfinance>=0.2.36
pandas>=2.0.0
numpy>=1.24.0
requests>=2.31.0
```

## 使用方式

### 基本命令

```bash
# 追蹤單支股票
python tracker.py --symbol=AAPL

# 追蹤單支股票（指定週期）
python tracker.py --symbol=AAPL --period=6m

# 追蹤多支股票
python tracker.py --watchlist="AAPL,GOOGL,MSFT"

# 產生詳細報告
python tracker.py --symbol=AAPL --report

# CSV 匯入
python tracker.py --import=my_stocks.csv

# 設定提醒閾值
python tracker.py --symbol=AAPL --alert=cci:80
```

### 參數說明

| 參數 | 說明 | 預設值 |
|------|------|--------|
| `--symbol` | 股票代號 | 必填 |
| `--period` | 數據週期 | 6m |
| `--interval` | K線週期間隔 | 1d |
| `--report` | 產生詳細報告 | False |
| `--watchlist` | 股票清單 | None |
| `--import` | CSV 匯入檔案 | None |
| `--output` | 輸出檔案 | stdout |
| `--alert` | 價格提醒閾值 | None |

### 輸出範例

```
╔═══════════════════════════════════════════════════════════════════╗
║                    📈 股票追蹤報告                               ║
║                      AAPL - 蘋果公司                            ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║   📊 基本資訊                                                   ║
║   ─────────────────────────────────────────────────────────────  ║
║   當前價格: $185.92                                              ║
║   數據週期: 6 個月                                               ║
║   更新時間: 2024-02-19 15:30:00                                 ║
║                                                                   ║
║   📈 H4 週期分析                                                ║
║   ─────────────────────────────────────────────────────────────  ║
║   CCI (14):    +23.5  │ 狀態: 中性                              ║
║   MACD:        ▲ 金叉 │ 狀態: 偏多                              ║
║   MA 交叉:     ▲ 上升 │ 狀態: 偏多                              ║
║                                                                   ║
║   📊 日線分析                                                   ║
║   ─────────────────────────────────────────────────────────────  ║
║   CCI (14):    +67.2  │ 狀態: 偏多                              ║
║   MACD:        ▲ 上升 │ 狀態: 偏多                              ║
║   MA 交叉:     ▲ 上升 │ 狀態: 偏多                              ║
║                                                                   ║
╠═══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║   🎯 綜合信號                                                   ║
║   ─────────────────────────────────────────────────────────────  ║
║                                                                   ║
║   信號狀態: 🟢 潛在買入                                          ║
║                                                                   ║
║   📌 信號依據:                                                   ║
║   • H4: MACD 金叉 + MA 交叉向上                                  ║
║   • 日線: CCI > 0 + MACD 偏多                                    ║
║                                                                   ║
║   💰 風險管理                                                    ║
║   ─────────────────────────────────────────────────────────────  ║
║   建議止損: -8.0%  ($171.05)                                     ║
║   建議止盈: +15.0% ($213.81)                                     ║
║   風險報酬比: 1:1.88                                             ║
║                                                                   ║
║   📝 備註                                                       ║
║   ─────────────────────────────────────────────────────────────  ║
║   多周期確認中，建議等待 H4 CCI 穿越 0 線後入場                   ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
```

## CSV 格式

### 匯入格式
```csv
symbol,name,exchange,alert_price,alert_indicator
AAPL,Apple Inc.,NASDAQ,180,CCI
GOOGL,Alphabet Inc.,NASDAQ,140,MACD
MSFT,Microsoft Corporation,NASDAQ,400,RSI
```

### 匯出格式
```csv
timestamp,symbol,price,signal,confidence,indicators,notes
2024-02-19,AAPL,185.92,BUY,75,CCI:+23.5/MACD:金叉,多周期確認
```

## 配置

### config.sh
```bash
# 數據獲取
DATA_SOURCE="yfinance"  # yfinance, csv, api
CACHE_ENABLED=true
CACHE_DIR="$HOME/.cache/stock-tracker"

# 技術指標
CCI_PERIOD=14
MACD_FAST=8
MACD_SLOW=12
MACD_SIGNAL=26
MA_SHORT=5
MA_LONG=20

# 風險管理
DEFAULT_STOP_LOSS=8.0
DEFAULT_TAKE_PROFIT=15.0
MAX_POSITION_SIZE=25.0

# 輸出格式
OUTPUT_FORMAT="terminal"  # terminal, json, csv, discord
DISCORD_WEBHOOK=""
```

## 工作流程整合

### 配合 multi-agent-orchestrator

```bash
# 使用 orchestrator 調用
orchestrator stock-tracker --symbol=AAPL --report

# 在 workflow 中使用
workflow-trigger --workflow=stock-check --symbols="AAPL,GOOGL"
```

### 定時監控
```bash
# Cron 任務 - 每日檢查
0 9 * * 1-5 /path/to/tracker.py --watchlist="AAPL,GOOGL" --report
```

## 風險提示 ⚠️

1. **技術分析有局限性**：過去表現不代表未來
2. **市場風險**：任何策略都可能虧損
3. **建議分散投資**：不要把資金放在單一策略
4. **回測驗證**：使用歷史數據驗證策略有效性
5. **資金管理**：設定合理的倉位和止損

## 擴展功能

### 添加新指標
```python
def calculate_rsi(data, period=14):
    """相對強弱指數"""
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))
```

### 自定義篩選器
```python
def custom_filter(stocks):
    """自定義股票篩選"""
    return [s for s in stocks if s['pe_ratio'] < 25 and s['dividend_yield'] > 2]
```

## 常見問題

### Q: 數據獲取失敗？
A: 檢查網絡連線，或使用 `--import` 匯入本地 CSV

### Q: 指標顯示錯誤？
A: 確保數據足夠長度（至少 100 根 K 線）

### Q: 如何添加新股票？
A: 使用 `--import` 或直接編輯 `watchlist.csv`

## 項目結構

```
stock-tracker-local/
├── SKILL.md              # 完整文檔
├── tracker.py            # 主程式
├── config.sh             # 配置
├── requirements.txt      # Python 依賴
├── README.md            # 快速開始
├── watchlist.csv        # 追蹤清單
└── examples/
    └── demo.sh          # 演示腳本
```

## 版本歷史

- **v1.0.0** (2026-02-19): 初始版本，基於 spoutnik 概念的股票追蹤系統

## 授權

MIT License - 完全本地化，無外部依賴
