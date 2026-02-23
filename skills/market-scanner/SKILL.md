# SKILL.md - Market Scanner Skill

## Overview
A comprehensive stock & crypto scanner system that tracks:
- **Crypto Tracker**: SOL and BTC prices using CoinGecko API
- **ASX Watchlist**: Curated list of high-potential Australian stocks
- **Breakout Scanner**: Identifies stocks with breakthrough patterns

## Components

### 1. Crypto Tracker (`crypto_tracker.py`)
Tracks Solana (SOL) and Bitcoin (BTC) with:
- Real-time price data from CoinGecko
- 24h and 7d change percentages
- Volume and market cap
- Daily summary report

**Usage:**
```bash
python3 crypto_tracker.py
```

**Output:** `~/.openclaw/workspace/skills/market-scanner/crypto_report.md`

### 2. ASX Watchlist (`asx_watchlist.py`)
Curated database of 13 high-potential Australian stocks across:
- Technology (WBT, WTC, XRO, ABB, OCL)
- Mining (SFR, IPD, FMG, NST)
- Healthcare (CSL, EBR, BB1)
- Energy (EOS)

**Usage:**
```python
from asx_watchlist import ASX_WATCHLIST, get_watchlist_summary
print(get_watchlist_summary())
```

### 3. Breakout Scanner (`breakout_scanner.py`)
Identifies stocks showing breakthrough patterns:
- Price consolidating 2-4 weeks then breaking out
- Volume spike on breakout (>2x average)
- RSI recovering from oversold (<40)
- SMA 50/200 golden cross
- Gap up pattern (>2%)
- New 52-week high

**Usage:**
```bash
python3 breakout_scanner.py
```

**Output:** 
- `~/.openclaw/workspace/skills/market-scanner/scan_results.json`
- `~/.openclaw/workspace/skills/market-scanner/breakout_report.md`

### 4. Main Orchestrator (`market_scanner.py`)
Combines all components:
- Runs complete daily scan
- Generates combined report
- Sends Discord notifications

**Usage:**
```bash
# Interactive mode
python3 market_scanner.py

# Cron mode (silent)
python3 market_scanner.py --cron
```

## Dependencies
```bash
pip install yfinance
```

## API Sources
- **Crypto**: CoinGecko API (free, no key required)
- **Stocks**: Yahoo Finance via yfinance (free)

## Output Files
| File | Description |
|------|-------------|
| `crypto_report.md` | Daily crypto summary |
| `scan_results.json` | Breakout scan results (JSON) |
| `breakout_report.md` | Human-readable breakout report |
| `daily_report.md` | Combined daily report |
| `cron_log.txt` | Cron execution logs |

## Discord Integration
To enable Discord notifications:
1. Create a Discord webhook URL
2. Set environment variable: `export DISCORD_WEBHOOK_URL="your_webhook_url"`
3. Alerts sent when breakout score >= 50

## Cron Setup
```bash
# Add to crontab for daily 9:00 AM scan:
crontab -e
# Add line:
0 9 * * * cd /Users/cken0218/.openclaw/workspace/skills/market-scanner && python3 market_scanner.py --cron >> cron_log.txt 2>&1
```

## Scanner Tickers
Default scan list includes 40+ ASX stocks:
- Technology: WTC, XRO, ABB, OCL, WBT, APT, MP1, WSP, XST, NXT
- Mining: BHP, RIO, FMG, SFR, NST, EVN, IGO, MIN, LKE, PLS
- Healthcare: CSL, EBR, BB1, RHC, SHL, COH, MSB, FPH, VHT, AXP
- Energy/Financials: CBA, WBC, ANZ, NAB, MQG, EOS, STO, WDS, AGL, ORG

To customize, edit `DEFAULT_SCAN_TICKERS` in `breakout_scanner.py`.

## Breakout Score
Stocks scored 0-100 based on pattern detection:
- Consolidation breakout: 25 pts
- Volume spike: 20 pts
- RSI recovery: 15 pts
- Golden cross: 25 pts
- Gap up: 10 pts
- 52-week high: 20 pts

Score >= 40 =值得关注 (值得关注)
Score >= 60 = Strong breakout candidate
Score >= 80 = Very strong signal
