#!/usr/bin/env python3
"""
Crypto Tracker - Daily Summary Report
Tracks SOL and BTC using CoinGecko free API
"""

import json
import sys
from datetime import datetime
from typing import Optional
import os

try:
    from urllib.request import urlopen, Request
    from urllib.error import URLError, HTTPError
except ImportError:
    from urllib2 import urlopen, Request, URLError, HTTPError

# Configuration
COINGECKO_API = "https://api.coingecko.com/api/v3"
REPORT_FILE = os.path.expanduser("~/.openclaw/workspace/skills/market-scanner/crypto_report.md")

def fetch_crypto_data(coin_id: str) -> Optional[dict]:
    """Fetch current price data from CoinGecko"""
    url = f"{COINGECKO_API}/simple/price"
    params = {
        "ids": coin_id,
        "vs_currencies": "usd",
        "include_24hr_change": "true",
        "include_24hr_vol": "true",
        "include_market_cap": "true"
    }
    
    query_string = "&".join([f"{k}={v}" for k, v in params.items()])
    full_url = f"{url}?{query_string}"
    
    try:
        request = Request(full_url)
        request.add_header('Accept', 'application/json')
        
        with urlopen(request, timeout=15) as response:
            data = json.loads(response.read().decode())
            return data.get(coin_id)
    except (URLError, HTTPError, json.JSONDecodeError, TimeoutError) as e:
        print(f"Error fetching {coin_id}: {e}")
        return None

def fetch_historical_7d(coin_id: str) -> Optional[float]:
    """Fetch 7-day historical data to calculate 7d change"""
    url = f"{COINGECKO_API}/coins/{coin_id}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": "7",
        "interval": "daily"
    }
    
    query_string = "&".join([f"{k}={v}" for k, v in params.items()])
    full_url = f"{url}?{query_string}"
    
    try:
        request = Request(full_url)
        request.add_header('Accept', 'application/json')
        
        with urlopen(request, timeout=15) as response:
            data = json.loads(response.read().decode())
            
            prices = data.get("prices", [])
            if len(prices) >= 2:
                current_price = prices[-1][1]
                week_ago_price = prices[0][1]
                if week_ago_price > 0:
                    return ((current_price - week_ago_price) / week_ago_price) * 100
            return None
    except (URLError, HTTPError, json.JSONDecodeError, TimeoutError) as e:
        print(f"Error fetching 7d history for {coin_id}: {e}")
        return None

def format_currency(value: float) -> str:
    """Format currency with appropriate symbols"""
    return f"${value:,.2f}"

def format_percentage(value: float) -> str:
    """Format percentage with sign"""
    sign = "+" if value > 0 else ""
    return f"{sign}{value:.2f}%"

def generate_crypto_report():
    """Generate daily crypto summary report"""
    coins = ["solana", "bitcoin"]
    coin_info = {
        "solana": {"name": "Solana", "symbol": "SOL"},
        "bitcoin": {"name": "Bitcoin", "symbol": "BTC"}
    }
    
    report_lines = []
    report_lines.append("=" * 60)
    report_lines.append("CRYPTO DAILY SUMMARY REPORT")
    report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S %Z')}")
    report_lines.append("=" * 60)
    report_lines.append("")
    
    data_collected = []
    
    for coin_id in coins:
        info = coin_info[coin_id]
        current_data = fetch_crypto_data(coin_id)
        seven_day_change = fetch_historical_7d(coin_id)
        
        if current_data:
            data_collected.append({
                "coin_id": coin_id,
                "name": info["name"],
                "symbol": info["symbol"],
                "price": current_data.get("usd", 0),
                "change_24h": current_data.get("usd_24h_change", 0),
                "change_7d": seven_day_change or 0,
                "volume_24h": current_data.get("usd_24h_vol", 0),
                "market_cap": current_data.get("usd_market_cap", 0)
            })
        else:
            print(f"Warning: Could not fetch data for {info['name']}")
    
    # Generate report
    for item in data_collected:
        report_lines.append(f"## {item['name']} ({item['symbol']})")
        report_lines.append("-" * 40)
        report_lines.append(f"  Price:      {format_currency(item['price'])}")
        report_lines.append(f"  24h Change: {format_percentage(item['change_24h'])}")
        report_lines.append(f"  7d Change:  {format_percentage(item['change_7d'])}")
        report_lines.append(f"  Volume:     {format_currency(item['volume_24h'])}")
        report_lines.append(f"  Market Cap: {format_currency(item['market_cap'])}")
        report_lines.append("")
    
    # Summary section
    report_lines.append("## Market Summary")
    report_lines.append("-" * 40)
    
    if data_collected:
        total_mcap = sum(d["market_cap"] for d in data_collected)
        avg_24h_change = sum(d["change_24h"] for d in data_collected) / len(data_collected)
        avg_7d_change = sum(d["change_7d"] for d in data_collected) / len(data_collected)
        
        report_lines.append(f"  Total Market Cap: {format_currency(total_mcap)}")
        report_lines.append(f"  Avg 24h Change:   {format_percentage(avg_24h_change)}")
        report_lines.append(f"  Avg 7d Change:    {format_percentage(avg_7d_change)}")
        report_lines.append("")
        
        # Performance summary
        report_lines.append("## Performance Summary")
        report_lines.append("-" * 40)
        best_performer = max(data_collected, key=lambda x: x["change_24h"])
        worst_performer = min(data_collected, key=lambda x: x["change_24h"])
        
        report_lines.append(f"  Best 24h: {best_performer['symbol']} ({format_percentage(best_performer['change_24h'])})")
        report_lines.append(f"  Worst 24h: {worst_performer['symbol']} ({format_percentage(worst_performer['change_24h'])})")
        report_lines.append("")
    
    report_lines.append("=" * 60)
    report_lines.append("Data provided by CoinGecko API")
    report_lines.append("Report generated by Market Scanner System")
    report_lines.append("=" * 60)
    
    report_content = "\n".join(report_lines)
    
    # Save report
    try:
        with open(REPORT_FILE, 'w') as f:
            f.write(report_content)
        print(f"Report saved to: {REPORT_FILE}")
    except IOError as e:
        print(f"Error saving report: {e}")
    
    return report_content

if __name__ == "__main__":
    try:
        report = generate_crypto_report()
        print("\n" + report)
    except Exception as e:
        print(f"Error generating report: {e}")
        sys.exit(1)
