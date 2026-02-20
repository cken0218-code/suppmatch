#!/usr/bin/env python3
"""
Australian Stock Tracker - WhatsApp Friendly Format
Usage: stock-tracker --aus --whatsapp
"""

import argparse
import sys
from datetime import datetime

try:
    import yfinance as yf
    import pandas as pd
except ImportError:
    print("❌ yfinance or pandas not installed.")
    sys.exit(1)

DEFAULT_ASX_STOCKS = ["CBA", "BHP", "CSL", "ANZ", "NAB", "WBC"]

def get_stock_data(ticker):
    try:
        ticker_ax = ticker if ticker.endswith(".AX") else f"{ticker}.AX"
        stock = yf.Ticker(ticker_ax)
        info = stock.info
        hist = stock.history(period="6mo")
        return {"info": info, "history": hist, "error": None}
    except Exception as e:
        return {"info": {}, "history": None, "error": str(e)}

def calculate_rsi(prices, period=14):
    if len(prices) < period:
        return None
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1] if len(rsi) > 0 else None

def calculate_sma(prices, period=20):
    return prices.rolling(window=period).mean().iloc[-1] if len(prices) >= period else None

def get_signal(rsi):
    if rsi and rsi < 30:
        return "BUY", "🟢"
    elif rsi and rsi > 70:
        return "SELL", "🔴"
    return "HOLD", "🟡"

def analyze_stock(ticker):
    data = get_stock_data(ticker)
    if data["error"]:
        return None
    
    hist = data["history"]
    info = data["info"]
    
    if hist is None or len(hist) < 20:
        return None
    
    current_price = hist['Close'].iloc[-1]
    prices = hist['Close']
    rsi = calculate_rsi(prices)
    sma20 = calculate_sma(prices, 20)
    
    signal, emoji = get_signal(rsi)
    
    # Calculate targets
    if signal == "BUY":
        buy_price = round(current_price * 0.97, 2)
        sell_price = round(current_price * 1.10, 2)
    elif signal == "SELL":
        buy_price = None
        sell_price = round(current_price * 0.95, 2)
    else:
        buy_price = round(current_price * 0.95, 2)
        sell_price = round(current_price * 1.08, 2)
    
    change = info.get("regularMarketChange", 0)
    change_pct = info.get("regularMarketChangePercent", 0)
    pe = info.get("trailingPE", 0)
    div_yield = info.get("dividendYield", 0)
    
    return {
        "ticker": ticker,
        "name": info.get("shortName", ticker),
        "price": current_price,
        "change": f"+{change:.2f}" if change >= 0 else f"{change:.2f}",
        "change_pct": f"+{change_pct:.2f}%" if change_pct >= 0 else f"{change_pct:.2f}%",
        "pe": f"{pe:.1f}" if pe else "N/A",
        "div": f"{div_yield:.1f}%" if div_yield else "N/A",
        "rsi": f"{rsi:.0f}" if rsi else "N/A",
        "signal": signal,
        "emoji": emoji,
        "buy": f"${buy_price}" if buy_price else "-",
        "sell": f"${sell_price}" if sell_price else "-",
    }

def print_whatsapp(stocks):
    print("\n" + "="*50)
    print("🇦🇺 澳洲股票每日快報 " + datetime.now().strftime("%Y-%m-%d"))
    print("="*50 + "\n")
    
    results = []
    for ticker in stocks:
        a = analyze_stock(ticker)
        if a:
            results.append(a)
            print(f"{a['emoji']} {a['ticker']} ${a['price']:.2f} ({a['change_pct']})")
            print(f"   RSI:{a['rsi']} | PE:{a['pe']} | 股息:{a['div']}")
            print(f"   建議:{a['signal']} | 買入:{a['buy']} | 目標:{a['sell']}")
            print()
    
    # Summary
    buys = sum(1 for r in results if r['signal'] == "BUY")
    holds = sum(1 for r in results if r['signal'] == "HOLD")
    sells = sum(1 for r in results if r['signal'] == "SELL")
    
    print("-"*50)
    print(f"信號汇总: 🟢買{buys} | 🟡等{holds} | 🔴沽{sells}")
    print("="*50)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--aus", action="store_true")
    parser.add_argument("--whatsapp", action="store_true")
    parser.add_argument("--stocks", nargs="+")
    args = parser.parse_args()
    
    stocks = args.stocks if args.stocks else DEFAULT_ASX_STOCKS
    print_whatsapp(stocks)

if __name__ == "__main__":
    main()
