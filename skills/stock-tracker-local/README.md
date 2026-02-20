# 📈 Stock Tracker Local - 快速開始

## 5 分鐘上手

### 1️⃣ 安裝依賴

```bash
cd /Users/cken0218/.openclaw/workspace/skills/stock-tracker-local
pip install -r requirements.txt
```

### 2️⃣ 試用演示

```bash
# 運行演示
./examples/demo.sh

# 或者直接運行
python3 tracker.py --symbol=AAPL --report
```

### 3️⃣ 添加你的股票

```bash
# 方法 1: 直接指定
python3 tracker.py --watchlist="AAPL,GOOGL,MSFT"

# 方法 2: 修改 watchlist.csv
vim watchlist.csv

# 方法 3: CSV 匯入
python3 tracker.py --import=my_stocks.csv
```

## 常見用法

| 用法 | 命令 |
|------|------|
| 追蹤單支股票 | `python3 tracker.py --symbol=AAPL` |
| 詳細報告 | `python3 tracker.py --symbol=AAPL --report` |
| 多支股票 | `python3 tracker.py --watchlist="AAPL,GOOGL"` |
| CSV 匯入 | `python3 tracker.py --import=watchlist.csv` |
| 設定止損止盈 | `python3 tracker.py --symbol=AAPL --stop-loss=10 --take-profit=20` |

## 技術指標說明

| 指標 | 參數 | 信號 |
|------|------|------|
| CCI | 14 | +100 超買 / -100 超賣 |
| MACD | 8, 12, 26 | 金叉/死叉 / 0線穿越 |
| MA | 5, 20 | 交叉方向 |

## 配合其他 Skills

```bash
# 使用 orchestrator
orchestrator stock-tracker --symbol=AAPL --report

# 設定 cron 任務
openclaw cron add --name "Daily Stock Check" \
  --cron "0 9 * * 1-5" \
  --message "python3 /path/to/tracker.py --watchlist=\"AAPL,GOOGL\""
```

## 注意事項

⚠️ 風險提示：
- 技術分析僅供參考，不構成投資建議
- 過往表現不代表未來結果
- 請做好資金管理，設定止損
