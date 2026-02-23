# Market Scanner - User Guide

A comprehensive stock & crypto scanner system for Australian and global markets.

## Quick Start

```bash
# 1. Navigate to skill directory
cd ~/.openclaw/workspace/skills/market-scanner

# 2. Install dependencies
pip install yfinance

# 3. Run daily scan
python3 market_scanner.py
```

## What It Does

### 1. Crypto Tracker
Monitors **Solana (SOL)** and **Bitcoin (BTC)**:
- Current price
- 24-hour change
- 7-day change
- Trading volume
- Market capitalization

**Run:** `python3 crypto_tracker.py`

### 2. ASX Watchlist
Curated list of **13 high-potential Australian stocks**:

| Sector | Stocks | Key Picks |
|--------|--------|-----------|
| Technology | WBT, WTC, XRO, ABB, OCL | WBT (semiconductors), ABB (telco growth) |
| Mining | SFR, IPD, FMG, NST | SFR (copper), NST (gold) |
| Healthcare | CSL, EBR, BB1 | EBR (FDA approved), CSL (biopharma) |
| Energy | EOS | EOS (defense tech, laser weapons) |

### 3. Breakout Scanner
Identifies stocks breaking out with technical patterns:
- 📈 Price consolidating 2-4 weeks then breaking out
- 📊 Volume spike (>2x average)
- 🔄 RSI recovering from oversold (<40)
- ✝️ SMA 50/200 golden cross
- 🚀 Gap up pattern (>2%)
- 🏆 New 52-week high

## Usage Modes

### Interactive Mode
```bash
python3 market_scanner.py
```
Shows a menu with options to run individual components.

### Cron Mode (Automated Daily Scan)
```bash
python3 market_scanner.py --cron
```
Runs silently and sends Discord notifications if breakouts detected.

### Individual Components
```bash
# Crypto only
python3 crypto_tracker.py

# Breakout scanner only
python3 breakout_scanner.py

# View ASX watchlist
python3 -c "from asx_watchlist import get_watchlist_summary; print(get_watchlist_summary())"
```

## Output Files

| File | Description |
|------|-------------|
| `crypto_report.md` | Daily crypto prices and changes |
| `breakout_report.md` | Technical analysis of breakouts |
| `scan_results.json` | Machine-readable scan results |
| `daily_report.md` | Combined report (all-in-one) |
| `cron_log.txt` | Execution logs |

## Setting Up Daily Automation

### Step 1: Open crontab editor
```bash
crontab -e
```

### Step 2: Add this line (for 9:00 AM daily)
```
0 9 * * * cd ~/.openclaw/workspace/skills/market-scanner && python3 market_scanner.py --cron >> cron_log.txt 2>&1
```

### Step 3: Verify
```bash
crontab -l  # Should show your entry
tail -f ~/.openclaw/workspace/skills/market-scanner/cron_log.txt  # Check logs
```

## Discord Notifications

To receive alerts when breakouts are found:

1. **Get a webhook URL:**
   - Go to Discord Server Settings > Integrations
   - Create a webhook
   - Copy the URL

2. **Set environment variable:**
   ```bash
   # Add to ~/.zshrc or ~/.bashrc
   export DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..."
   ```

3. **Test notification:**
   ```bash
   # Run a scan to trigger alert if breakout score >= 50
   python3 market_scanner.py
   ```

## Customizing Scan Tickers

Edit `breakout_scanner.py` and modify `DEFAULT_SCAN_TICKERS`:

```python
DEFAULT_SCAN_TICKERS = [
    "WTC", "XRO", "ABB",  # Add your tech picks
    "BHP", "RIO", "SFR",  # Add mining stocks
    # ... etc
]
```

## Understanding Breakout Scores

| Score | Interpretation | Action |
|-------|----------------|--------|
| 0-20 | No clear signal | Monitor only |
| 20-40 | Weak signal | Research further |
| 40-60 | Moderate breakout | Consider entry |
| 60-80 | Strong breakout | Good candidate |
| 80+ | Very strong | High confidence |

## Example Output

```
# BREAKTHROUGH STOCK SCANNER REPORT
Generated: 2026-02-20 22:30:00
Scanned: 40 tickers

## #1 WBT - Weebit Nano
----------------------------------------
  Current Price:  $4.52
  Breakout Score: 75/100
  Sector:         Technology
  Signals:        consolidation_breakout, volume_spike, golden_cross

  ✓ Consolidation Breakout:
    Range: $4.10 - $4.38 | Breakout: 3.2%
  ✓ Volume Spike:
    2.5x average volume
  ✓ Golden Cross:
    Signal: bullish_alignment | SMA50: $4.35 | SMA200: $4.20

========================================
Total breakouts found: 5
========================================
```

## Troubleshooting

### "Module not found: yfinance"
```bash
pip install yfinance
```

### "No data for ticker"
- Check internet connection
- Verify ticker is listed on ASX (add .AX suffix in yfinance)
- Try a different ticker

### Cron not running
```bash
# Check cron status
ps aux | grep cron

# Test manually
cd ~/.openclaw/workspace/skills/market-scanner && python3 market_scanner.py --cron
```

### Discord not receiving alerts
- Verify webhook URL is correct
- Check Discord server permissions
- Ensure environment variable is set in the same shell as cron

## API Sources

| Data | Source | Cost |
|------|--------|------|
| Crypto prices | CoinGecko API | Free |
| Stock prices | Yahoo Finance (yfinance) | Free |
| Stock info | Yahoo Finance | Free |

No API keys required!

## Support

- Check logs: `cat ~/.openclaw/workspace/skills/market-scanner/cron_log.txt`
- View latest report: `cat ~/.openclaw/workspace/skills/market-scanner/daily_report.md`
- View raw results: `cat ~/.openclaw/workspace/skills/market-scanner/scan_results.json`
