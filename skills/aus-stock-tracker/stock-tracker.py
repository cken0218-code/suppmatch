#!/usr/bin/env python3
"""
Australian Stock Tracker - Enhanced with Technical Analysis
Usage: stock-tracker --aus --report [--signals]
"""

import argparse
import sys
from datetime import datetime, timedelta
import json

try:
    import yfinance as yf
    import pandas as pd
except ImportError:
    print("❌ yfinance or pandas not installed. Run: pip install yfinance pandas")
    sys.exit(1)

# Default ASX stocks
DEFAULT_ASX_STOCKS = ["CBA", "BHP", "CSL", "ANZ", "NAB", "WBC", "4DX", "AD8", "ARU", "BGL", "ELD", "KMD", "VR1"]

def get_stock_data(ticker, period="6mo"):
    """Get stock data from yfinance"""
    try:
        ticker_ax = ticker if ticker.endswith(".AX") else f"{ticker}.AX"
        stock = yf.Ticker(ticker_ax)
        
        # Get info
        info = stock.info
        
        # Get historical data for technical analysis
        hist = stock.history(period=period)
        
        return {
            "info": info,
            "history": hist,
            "error": None
        }
    except Exception as e:
        return {"info": {}, "history": None, "error": str(e)}

def calculate_rsi(prices, period=14):
    """Calculate RSI indicator"""
    if len(prices) < period:
        return None
    
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1] if len(rsi) > 0 else None

def calculate_sma(prices, period=20):
    """Calculate Simple Moving Average"""
    return prices.rolling(window=period).mean().iloc[-1] if len(prices) >= period else None

def calculate_ema(prices, period=20):
    """Calculate Exponential Moving Average"""
    return prices.ewm(span=period, adjust=False).mean().iloc[-1] if len(prices) >= period else None

def calculate_macd(prices):
    """Calculate MACD"""
    if len(prices) < 26:
        return None, None, None
    
    ema12 = prices.ewm(span=12, adjust=False).mean()
    ema26 = prices.ewm(span=26, adjust=False).mean()
    macd = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()
    histogram = macd - signal
    
    return macd.iloc[-1], signal.iloc[-1], histogram.iloc[-1]

def calculate_adx(hist, period=14):
    """Calculate ADX (Average Directional Index)"""
    if len(hist) < period + 1:
        return None
    
    high = hist['High']
    low = hist['Low']
    close = hist['Close']
    
    # True Range
    tr1 = high - low
    tr2 = abs(high - close.shift(1))
    tr3 = abs(low - close.shift(1))
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    
    # Directional Movement
    plus_dm = high.diff()
    minus_dm = -low.diff()
    
    plus_dm[plus_dm < 0] = 0
    minus_dm[minus_dm < 0] = 0
    
    # Smoothed values
    atr = tr.rolling(window=period).mean()
    plus_di = (plus_dm.rolling(window=period).mean() / atr) * 100
    minus_di = (minus_dm.rolling(window=period).mean() / atr) * 100
    
    dx = (abs(plus_di - minus_di) / (plus_di + minus_di)) * 100
    adx = dx.rolling(window=period).mean()
    
    return adx.iloc[-1] if len(adx) > 0 else None

def calculate_atr(hist, period=14):
    """Calculate ATR (Average True Range)"""
    if len(hist) < period + 1:
        return None
    
    high = hist['High']
    low = hist['Low']
    close = hist['Close']
    
    tr1 = high - low
    tr2 = abs(high - close.shift(1))
    tr3 = abs(low - close.shift(1))
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    
    atr = tr.rolling(window=period).mean()
    return atr.iloc[-1] if len(atr) > 0 else None

def get_signal(rsi, price, sma20, sma50, ema20, macd, macd_signal, macd_hist, adx):
    """Determine buy/hold/sell signal based on technical indicators"""
    score = 0
    
    # ADX Trend Strength filter (ADX > 25 = trending, ADX < 20 = weak/no trend)
    if adx:
        if adx < 20:
            score -= 1  # Weak trend - be cautious
        elif adx > 25:
            score += 1  # Strong trend - good for momentum strategies
    
    # RSI analysis (oversold = buy, overbought = sell)
    if rsi:
        if rsi < 30:
            score += 2  # Oversold - strong buy
        elif rsi < 40:
            score += 1  # Slightly oversold
        elif rsi > 70:
            score -= 2  # Overbought - strong sell
        elif rsi > 60:
            score -= 1  # Slightly overbought
    
    # Price vs SMA analysis
    if sma20 and price:
        if price < sma20:
            score += 1  # Price below SMA - potentially undervalued
        elif price > sma20 * 1.1:
            score -= 1  # Price significantly above SMA - potentially overvalued
    
    # SMA crossover (SMA20 above SMA50 = bullish)
    if sma20 and sma50:
        if sma20 > sma50:
            score += 1
        else:
            score -= 1
    
    # MACD analysis
    if macd and macd_signal:
        if macd > macd_signal and macd_hist > 0:
            score += 1  # Bullish MACD
        elif macd < macd_signal and macd_hist < 0:
            score -= 1  # Bearish MACD
    
    # Determine signal
    if score >= 3:
        return "🟢 BUY"
    elif score <= -3:
        return "🔴 SELL"
    else:
        return "🟡 HOLD"

def calculate_targets(price, signal):
    """Calculate suggested buy/sell prices"""
    if not price:
        return None, None
    
    if signal.startswith("🟢"):  # Buy signal
        # Strong buy - tighter range
        buy_price = round(price * 0.97, 2)  # 3% below current
        sell_price = round(price * 1.10, 2)  # 10% upside target
    elif signal.startswith("🔴"):  # Sell signal
        # Strong sell - exit now
        buy_price = None
        sell_price = round(price * 0.95, 2)  # 5% downside protection
    else:  # Hold
        buy_price = round(price * 0.95, 2)  # 5% below for adding
        sell_price = round(price * 1.08, 2)  # 8% target
    
    return buy_price, sell_price

def get_stock_analysis(ticker):
    """Get complete stock analysis"""
    data = get_stock_data(ticker)
    
    if data["error"]:
        return {"error": data["error"], "ticker": ticker}
    
    info = data["info"]
    hist = data["history"]
    
    if hist is None or len(hist) < 20:
        return {"error": "Insufficient data", "ticker": ticker}
    
    # Current price
    current_price = hist['Close'].iloc[-1]
    
    # Technical indicators
    prices = hist['Close']
    rsi = calculate_rsi(prices)
    sma20 = calculate_sma(prices, 20)
    sma50 = calculate_sma(prices, 50)
    ema20 = calculate_ema(prices, 20)
    macd, macd_signal, macd_hist = calculate_macd(prices)
    adx = calculate_adx(hist)
    atr = calculate_atr(hist)
    
    # Get signal
    signal = get_signal(rsi, current_price, sma20, sma50, ema20, macd, macd_signal, macd_hist, adx)
    
    # Calculate targets
    buy_price, sell_price = calculate_targets(current_price, signal)
    
    # Basic info
    change = info.get("regularMarketChange", 0)
    change_pct = info.get("regularMarketChangePercent", 0)
    market_cap = info.get("marketCap", 0)
    pe_ratio = info.get("trailingPE", 0)
    dividend_yield = info.get("dividendYield", 0)
    
    return {
        "ticker": ticker,
        "name": info.get("longName", ticker),
        "price": current_price,
        "change": change,
        "change_pct": change_pct,
        "market_cap": market_cap,
        "pe_ratio": pe_ratio,
        "dividend_yield": info.get("dividendYield", 0),
        "rsi": round(rsi, 2) if rsi else None,
        "sma20": round(sma20, 2) if sma20 else None,
        "sma50": round(sma50, 2) if sma50 else None,
        "ema20": round(ema20, 2) if ema20 else None,
        "macd": round(macd, 2) if macd else None,
        "macd_signal": round(macd_signal, 2) if macd_signal else None,
        "adx": round(adx, 2) if adx else None,
        "atr": round(atr, 2) if atr else None,
        "signal": signal,
        "buy_price": buy_price,
        "sell_price": sell_price,
    }

def format_market_cap(market_cap):
    """Format market cap to human readable"""
    if market_cap == 0:
        return "N/A"
    if market_cap >= 1e12:
        return f"${market_cap/1e12:.2f}T"
    elif market_cap >= 1e9:
        return f"${market_cap/1e9:.2f}B"
    elif market_cap >= 1e6:
        return f"${market_cap/1e6:.2f}M"
    return f"${market_cap}"

def print_report(stocks, show_signals=False):
    """Print formatted stock report"""
    print("\n" + "="*80)
    print(f"🇦🇺 Australian Stock Report - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("="*80)
    
    results = []
    for ticker in stocks:
        analysis = get_stock_analysis(ticker)
        
        if "error" in analysis:
            print(f"{ticker:<8} ❌ Error: {analysis['error']}")
            continue
        
        results.append(analysis)
        
        price = analysis["price"]
        change = analysis["change"]
        change_pct = analysis["change_pct"]
        
        # Change indicator
        if change > 0:
            change_str = f"+{change:.2f} (+{change_pct:.2f}%)"
        elif change < 0:
            change_str = f"{change:.2f} ({change_pct:.2f}%)"
        else:
            change_str = "0.00 (0.00%)"
        
        print(f"\n📊 {ticker} - {analysis['name']}")
        print(f"   💰 Price: ${price:.2f} | Change: {change_str}")
        print(f"   📈 Market Cap: {format_market_cap(analysis['market_cap'])} | PE: {analysis['pe_ratio']:.2f}" if analysis['pe_ratio'] else f"   📈 Market Cap: {format_market_cap(analysis['market_cap'])}")
        
        if analysis['dividend_yield'] > 0:
            print(f"   💵 Dividend Yield: {analysis['dividend_yield']:.2f}%")
        
        if show_signals:
            print(f"   ─────────────────────────────")
            print(f"   📉 RSI: {analysis['rsi']}" if analysis['rsi'] else "   📉 RSI: N/A")
            print(f"   📊 SMA20: {analysis['sma20']} | SMA50: {analysis['sma50']}" if analysis['sma20'] and analysis['sma50'] else "   📊 SMA: N/A")
            print(f"   📊 EMA20: {analysis['ema20']}" if analysis['ema20'] else "   📊 EMA20: N/A")
            print(f"   📊 MACD: {analysis['macd']} | Signal: {analysis['macd_signal']}" if analysis['macd'] else "   📊 MACD: N/A")
            trend_strength = "Strong" if analysis['adx'] and analysis['adx'] > 25 else "Weak" if analysis['adx'] and analysis['adx'] < 20 else "Moderate"
            print(f"   💪 ADX: {analysis['adx']} ({trend_strength})" if analysis['adx'] else "   💪 ADX: N/A")
            print(f"   📐 ATR: ${analysis['atr']}" if analysis['atr'] else "   📐 ATR: N/A")
            print(f"   ─────────────────────────────")
            print(f"   🎯 SIGNAL: {analysis['signal']}")
            
            if analysis['buy_price']:
                print(f"   💚 Suggested BUY:  ${analysis['buy_price']:.2f}")
            if analysis['sell_price']:
                print(f"   ❤️ Suggested SELL: ${analysis['sell_price']:.2f}")
    
    # Summary
    print("\n" + "="*80)
    print("📋 SUMMARY")
    print("="*80)
    
    buy_count = sum(1 for r in results if r['signal'].startswith("🟢"))
    sell_count = sum(1 for r in results if r['signal'].startswith("🔴"))
    hold_count = sum(1 for r in results if r['signal'].startswith("🟡"))
    
    print(f"🟢 BUY signals:  {buy_count}")
    print(f"🟡 HOLD signals: {hold_count}")
    print(f"🔴 SELL signals: {sell_count}")
    print("="*80)
    
    return results

# History functions
HISTORY_DIR = "/Users/cken0218/.openclaw/workspace/skills/aus-stock-tracker/history"

def save_history(results):
    """Save today's analysis to history folder"""
    import os
    os.makedirs(HISTORY_DIR, exist_ok=True)
    
    today = datetime.now().strftime("%Y-%m-%d")
    history_data = {
        "date": today,
        "stocks": {}
    }
    
    for stock in results:
        if "error" not in stock:
            history_data["stocks"][stock["ticker"]] = {
                "price": round(stock["price"], 2),
                "rsi": stock["rsi"],
                "adx": stock["adx"],
                "ema20": stock["ema20"],
                "macd": stock["macd"],
                "signal": stock["signal"]
            }
    
    file_path = os.path.join(HISTORY_DIR, f"{today}.json")
    with open(file_path, 'w') as f:
        json.dump(history_data, f, indent=2)
    
    print(f"✅ Saved history to: {file_path}")
    return file_path

def load_history(days=7):
    """Load recent history records"""
    import os
    import glob
    
    if not os.path.exists(HISTORY_DIR):
        print("❌ History folder not found")
        return []
    
    # Get all json files and sort by date
    pattern = os.path.join(HISTORY_DIR, "*.json")
    files = sorted(glob.glob(pattern), reverse=True)[:days]
    
    history = []
    for file_path in files:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                history.append(data)
        except Exception as e:
            print(f"⚠️ Error loading {file_path}: {e}")
    
    return history

def print_history(days=7):
    """Print historical records"""
    history = load_history(days)
    
    if not history:
        print("❌ No history records found")
        return
    
    print("\n" + "="*80)
    print(f"📜 Stock History - Last {days} Days")
    print("="*80)
    
    for record in history:
        date = record.get("date", "Unknown")
        print(f"\n📅 {date}")
        print("-" * 40)
        
        stocks = record.get("stocks", {})
        for ticker, data in stocks.items():
            signal_emoji = data.get("signal", "N/A")[:4]  # Get emoji
            price = data.get("price", 0)
            rsi = data.get("rsi", "N/A")
            adx = data.get("adx", "N/A")
            print(f"   {ticker:<6} {signal_emoji} ${price:.2f} | RSI:{rsi} | ADX:{adx}")
    
    print("\n" + "="*80)

def verify_signals(days=7):
    """Verify historical signal accuracy"""
    history = load_history(days)
    
    if len(history) < 2:
        print("❌ Need at least 2 days of history to verify signals")
        return
    
    print("\n" + "="*80)
    print(f"🎯 Signal Verification - Last {days} Days")
    print("="*80)
    
    # Sort by date (oldest first for comparison)
    history_sorted = sorted(history, key=lambda x: x.get("date", ""))
    
    stats = {
        "BUY": {"total": 0, "correct": 0, "price_change": []},
        "HOLD": {"total": 0, "correct": 0, "price_change": []},
        "SELL": {"total": 0, "correct": 0, "price_change": []}
    }
    
    detailed_results = []
    
    for i in range(len(history_sorted) - 1):
        old_record = history_sorted[i]
        new_record = history_sorted[i + 1]
        
        old_date = old_record.get("date", "")
        new_date = new_record.get("date", "")
        
        old_stocks = old_record.get("stocks", {})
        new_stocks = new_record.get("stocks", {})
        
        for ticker, old_data in old_stocks.items():
            if ticker not in new_stocks:
                continue
            
            new_data = new_stocks[ticker]
            old_price = old_data.get("price", 0)
            new_price = new_data.get("price", 0)
            old_signal = old_data.get("signal", "")
            
            # Determine signal type
            if old_signal.startswith("🟢"):
                signal_type = "BUY"
            elif old_signal.startswith("🔴"):
                signal_type = "SELL"
            else:
                signal_type = "HOLD"
            
            if old_price > 0 and new_price > 0:
                price_change = ((new_price - old_price) / old_price) * 100
                
                # Determine if signal was correct
                if signal_type == "BUY" and price_change > 0:
                    correct = True
                elif signal_type == "SELL" and price_change < 0:
                    correct = True
                elif signal_type == "HOLD" and -5 < price_change < 5:
                    correct = True  # Hold is correct if price didn't move much
                else:
                    correct = False
                
                stats[signal_type]["total"] += 1
                stats[signal_type]["correct"] += 1 if correct else 0
                stats[signal_type]["price_change"].append(price_change)
                
                detailed_results.append({
                    "ticker": ticker,
                    "date": old_date,
                    "old_signal": old_signal,
                    "old_price": old_price,
                    "new_price": new_price,
                    "change_pct": price_change,
                    "correct": correct
                })
    
    # Print detailed results
    print("\n📊 Detailed Signal Results:")
    print("-" * 80)
    for result in detailed_results:
        status = "✅" if result["correct"] else "❌"
        print(f"{status} {result['ticker']:<6} {result['old_signal']:<8} "
              f"${result['old_price']:.2f} → ${result['new_price']:.2f} "
              f"({result['change_pct']:+.2f}%)")
    
    # Print summary
    print("\n" + "="*80)
    print("📈 Signal Accuracy Summary")
    print("="*80)
    
    for signal_type in ["BUY", "HOLD", "SELL"]:
        total = stats[signal_type]["total"]
        correct = stats[signal_type]["correct"]
        avg_change = stats[signal_type]["price_change"]
        
        if total > 0:
            accuracy = (correct / total) * 100
            avg_pct = sum(avg_change) / len(avg_change) if avg_change else 0
            print(f"\n{signal_type} Signals:")
            print(f"   Total signals: {total}")
            print(f"   Correct: {correct}/{total} ({accuracy:.1f}%)")
            print(f"   Avg price change: {avg_pct:+.2f}%")
    
    # Overall accuracy
    total_all = sum(stats[s]["total"] for s in stats)
    correct_all = sum(stats[s]["correct"] for s in stats)
    
    if total_all > 0:
        overall_accuracy = (correct_all / total_all) * 100
        print(f"\n🎯 Overall Signal Accuracy: {correct_all}/{total_all} ({overall_accuracy:.1f}%)")
    
    print("="*80)

def main():
    parser = argparse.ArgumentParser(description="Australian Stock Tracker - Enhanced")
    parser.add_argument("--aus", action="store_true", help="Track ASX stocks")
    parser.add_argument("--report", action="store_true", help="Generate daily report")
    parser.add_argument("--signals", action="store_true", help="Show buy/sell signals and technical analysis")
    parser.add_argument("--stocks", nargs="+", help="Custom stock list (e.g., CBA BHP CSL)")
    parser.add_argument("--save", action="store_true", help="Save today's analysis to history")
    parser.add_argument("--history", type=int, default=0, metavar="N", help="Show last N days of history")
    parser.add_argument("--verify", type=int, default=0, metavar="N", help="Verify signals for last N days")
    
    args = parser.parse_args()
    
    if args.history > 0:
        print_history(args.history)
    elif args.verify > 0:
        verify_signals(args.verify)
    elif args.aus or args.stocks:
        stocks = args.stocks if args.stocks else DEFAULT_ASX_STOCKS
        results = print_report(stocks, show_signals=args.signals)
        
        if args.save:
            save_history(results)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
