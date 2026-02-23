#!/usr/bin/env python3
"""
Market Scanner System - Main Entry Point
=========================================
A comprehensive stock & crypto scanner system with:
1. ASX Watchlist Extension
2. Crypto Tracker (SOL + BTC)
3. Breakthrough Stock Scanner

Author: OpenClaw Agent
Date: 2026-02-20
"""

import sys
import argparse
from datetime import datetime
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from crypto_tracker import CryptoTracker
from asx_watchlist import ASXWatchlist
from breakthrough_scanner import BreakthroughScanner
from config import Config

class MarketScanner:
    """Main orchestrator for the market scanner system."""
    
    def __init__(self):
        self.config = Config()
        self.crypto = CryptoTracker(self.config)
        self.asx = ASXWatchlist(self.config)
        self.breakthrough = BreakthroughScanner(self.config)
    
    def run_daily_scan(self):
        """Run complete daily scan of all components."""
        print(f"\n{'='*60}")
        print(f"📊 MARKET SCANNER - DAILY REPORT")
        print(f"   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}\n")
        
        results = {
            'crypto': None,
            'asx_watchlist': None,
            'breakthrough_signals': None
        }
        
        # 1. Crypto Tracker
        print("🔄 Fetching Crypto Data...")
        results['crypto'] = self.crypto.get_daily_summary()
        print(results['crypto'])
        
        # 2. ASX Watchlist
        print("\n🔄 Updating ASX Watchlist...")
        results['asx_watchlist'] = self.asx.get_watchlist_summary()
        print(results['asx_watchlist'])
        
        # 3. Breakthrough Scanner
        print("\n🔄 Running Breakthrough Scanner...")
        results['breakthrough_signals'] = self.breakthrough.scan_all()
        self.breakthrough.print_signals()
        
        return results

def main():
    parser = argparse.ArgumentParser(
        description='Market Scanner System - ASX, Crypto & Breakout Detection'
    )
    parser.add_argument(
        '--mode',
        choices=['daily', 'crypto', 'asx', 'breakthrough', 'setup'],
        default='daily',
        help='Scanner mode (default: daily)'
    )
    parser.add_argument(
        '--discord',
        action='store_true',
        help='Send results to Discord'
    )
    parser.add_argument(
        '--watchlist',
        action='store_true',
        help='Show current ASX watchlist'
    )
    
    args = parser.parse_args()
    
    scanner = MarketScanner()
    
    if args.mode == 'setup':
        scanner.config.setup()
        print("✅ Setup complete! Edit config.yaml with your preferences.")
        return
    
    if args.mode == 'daily':
        results = scanner.run_daily_scan()
        if args.discord:
            from discord_notifier import DiscordNotifier
            DiscordNotifier(scanner.config).send_daily_report(results)
    
    elif args.mode == 'crypto':
        print(scanner.crypto.get_daily_summary())
    
    elif args.mode == 'asx':
        print(scanner.asx.get_watchlist_summary())
        if args.watchlist:
            scanner.asx.print_watchlist()
    
    elif args.mode == 'breakthrough':
        signals = scanner.breakthrough.scan_all()
        scanner.breakthrough.print_signals()
        if args.discord:
            from discord_notifier import DiscordNotifier
            DiscordNotifier(scanner.config).send_breakout_alert(signals)

if __name__ == '__main__':
    main()
