#!/usr/bin/env python3
"""
Market Scanner - Main Orchestrator
Combines:
1. Crypto Tracker (SOL + BTC)
2. ASX Watchlist
3. Breakthrough Stock Scanner

Features:
- Daily automated scanning
- Discord notifications
- Report generation
"""

import os
import sys
import json
import subprocess
from datetime import datetime
from typing import Optional

# Paths
SKILL_DIR = os.path.expanduser("~/.openclaw/workspace/skills/market-scanner")
CRON_LOG_FILE = os.path.join(SKILL_DIR, "cron_log.txt")
LATEST_REPORT_FILE = os.path.join(SKILL_DIR, "daily_report.md")


def log_message(message: str, level: str = "INFO"):
    """Log message to file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}] {message}\n"
    
    try:
        with open(CRON_LOG_FILE, 'a') as f:
            f.write(log_entry)
    except IOError:
        pass
    
    print(log_entry.strip())


def run_crypto_tracker():
    """Run crypto tracker and return summary"""
    log_message("Running crypto tracker...")
    
    try:
        result = subprocess.run(
            [sys.executable, os.path.join(SKILL_DIR, "crypto_tracker.py")],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode == 0:
            log_message("Crypto tracker completed successfully")
            return True
        else:
            log_message(f"Crypto tracker failed: {result.stderr}", "ERROR")
            return False
    except subprocess.TimeoutExpired:
        log_message("Crypto tracker timed out", "ERROR")
        return False
    except Exception as e:
        log_message(f"Crypto tracker error: {e}", "ERROR")
        return False


def run_breakout_scanner():
    """Run breakout scanner and return results"""
    log_message("Running breakout scanner...")
    
    try:
        result = subprocess.run(
            [sys.executable, os.path.join(SKILL_DIR, "breakout_scanner.py")],
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        if result.returncode == 0:
            log_message("Breakout scanner completed successfully")
            # Parse results
            results_file = os.path.join(SKILL_DIR, "scan_results.json")
            if os.path.exists(results_file):
                with open(results_file, 'r') as f:
                    data = json.load(f)
                    return data.get("results", [])
            return []
        else:
            log_message(f"Breakout scanner failed: {result.stderr}", "ERROR")
            return []
    except subprocess.TimeoutExpired:
        log_message("Breakout scanner timed out", "ERROR")
        return []
    except Exception as e:
        log_message(f"Breakout scanner error: {e}", "ERROR")
        return []


def generate_combined_report(crypto_success: bool, breakouts: list):
    """Generate combined daily report"""
    
    report_lines = []
    report_lines.append("# Market Scanner Daily Report")
    report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S %Z')}")
    report_lines.append("")
    
    # Crypto Section
    report_lines.append("## Crypto Summary")
    report_lines.append("-" * 40)
    
    crypto_report = os.path.join(SKILL_DIR, "crypto_report.md")
    if os.path.exists(crypto_report) and crypto_success:
        with open(crypto_report, 'r') as f:
            crypto_content = f.read()
        # Extract relevant part (skip header if needed)
        report_lines.append(crypto_content)
    else:
        report_lines.append("Crypto data unavailable")
    report_lines.append("")
    
    # ASX Watchlist Section
    report_lines.append("## ASX Watchlist")
    report_lines.append("-" * 40)
    
    try:
        sys.path.insert(0, SKILL_DIR)
        from asx_watchlist import get_watchlist_summary
        report_lines.append(get_watchlist_summary())
    except Exception as e:
        report_lines.append(f"Error loading watchlist: {e}")
    report_lines.append("")
    
    # Breakout Scanner Section
    report_lines.append("## Breakout Scanner Results")
    report_lines.append("-" * 40)
    report_lines.append(f"Found {len(breakouts)} potential breakouts:")
    report_lines.append("")
    
    for i, breakout in enumerate(breakouts[:10], 1):  # Top 10
        report_lines.append(f"**{i}. {breakout['ticker']}** - {breakout['name']}")
        report_lines.append(f"   Price: ${breakout['current_price']:.2f}")
        report_lines.append(f"   Score: {breakout['breakout_score']}/100")
        report_lines.append(f"   Signals: {', '.join(breakout['breakout_signals'])}")
        report_lines.append("")
    
    # Actions
    report_lines.append("## Recommended Actions")
    report_lines.append("-" * 40)
    
    if breakouts:
        top_breakout = breakouts[0]
        report_lines.append(f"⭐ **Top Pick**: {top_breakout['ticker']} ({top_breakout['name']})")
        report_lines.append(f"   Price: ${top_breakout['current_price']:.2f}")
        report_lines.append(f"   Score: {top_breakout['breakout_score']}/100")
        report_lines.append(f"   Why: {', '.join(top_breakout['breakout_signals'])}")
    else:
        report_lines.append("No strong breakout signals at this time.")
    
    report_lines.append("")
    report_lines.append("---\n")
    report_lines.append("Report generated by Market Scanner System")
    report_lines.append(f"Next scan: {datetime.now().strftime('%Y-%m-%d')}")
    
    # Save report
    with open(LATEST_REPORT_FILE, 'w') as f:
        f.write("\n".join(report_lines))
    
    return "\n".join(report_lines)


def send_discord_notification(breakouts: list):
    """Send Discord notification for alerts"""
    if not breakouts:
        return
    
    # Check for Discord configuration
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        log_message("No Discord webhook URL configured")
        return
    
    # Prepare notification
    top_breakout = breakouts[0]
    message = {
        "content": "🚨 **Market Scanner Alert** 🚨",
        "embeds": [
            {
                "title": f"Breakout Signal: {top_breakout['ticker']}",
                "description": f"**{top_breakout['name']}** is showing breakout patterns",
                "color": 0x00FF00,
                "fields": [
                    {"name": "Price", "value": f"${top_breakout['current_price']:.2f}", "inline": True},
                    {"name": "Score", "value": f"{top_breakout['breakout_score']}/100", "inline": True},
                    {"name": "Signals", "value": ", ".join(top_breakout['breakout_signals']), "inline": False}
                ],
                "footer": {"text": "Market Scanner System"},
                "timestamp": datetime.now().isoformat()
            }
        ]
    }
    
    try:
        import urllib.request
        import json as json_lib
        
        data = json_lib.dumps(message).encode('utf-8')
        request = urllib.request.Request(
            webhook_url,
            data=data,
            headers={'Content-Type': 'application/json'},
            method='POST'
        )
        
        with urllib.request.urlopen(request, timeout=10) as response:
            if response.status == 204:
                log_message("Discord notification sent successfully")
            else:
                log_message(f"Discord notification failed: {response.status}", "WARNING")
    except Exception as e:
        log_message(f"Discord notification error: {e}", "WARNING")


def run_daily_scan(notify_discord: bool = True):
    """Run complete daily market scan"""
    log_message("Starting daily market scan...")
    
    start_time = datetime.now()
    
    # Run components
    crypto_success = run_crypto_tracker()
    breakouts = run_breakout_scanner()
    
    # Generate report
    report = generate_combined_report(crypto_success, breakouts)
    
    # Send notification if significant breakouts found
    if notify_discord and breakouts and breakouts[0]['breakout_score'] >= 50:
        send_discord_notification(breakouts)
    
    elapsed = (datetime.now() - start_time).total_seconds()
    log_message(f"Daily scan complete in {elapsed:.1f}s")
    
    return {
        "crypto_success": crypto_success,
        "breakouts_found": len(breakouts),
        "report_file": LATEST_REPORT_FILE
    }


def show_menu():
    """Show interactive menu"""
    print("\n" + "=" * 50)
    print("MARKET SCANNER - Main Menu")
    print("=" * 50)
    print("1. Run Daily Scan (all components)")
    print("2. Run Crypto Tracker Only")
    print("3. Run Breakout Scanner Only")
    print("4. View ASX Watchlist")
    print("5. View Latest Report")
    print("6. Setup Cron Job")
    print("0. Exit")
    print("=" * 50)
    
    choice = input("Enter choice: ").strip()
    
    if choice == "1":
        run_daily_scan()
    elif choice == "2":
        run_crypto_tracker()
    elif choice == "3":
        run_breakout_scanner()
    elif choice == "4":
        sys.path.insert(0, SKILL_DIR)
        from asx_watchlist import get_watchlist_summary
        print(get_watchlist_summary())
    elif choice == "5":
        if os.path.exists(LATEST_REPORT_FILE):
            with open(LATEST_REPORT_FILE, 'r') as f:
                print(f.read())
        else:
            print("No report found. Run a scan first.")
    elif choice == "6":
        setup_cron()
    elif choice == "0":
        sys.exit(0)
    else:
        print("Invalid choice")


def setup_cron():
    """Setup cron job for daily scanning"""
    script_path = os.path.join(SKILL_DIR, "market_scanner.py")
    
    cron_entry = f"# Market Scanner - Daily at 9:00 AM\n0 9 * * * cd {SKILL_DIR} && python3 market_scanner.py --cron >> {CRON_LOG_FILE} 2>&1"
    
    print("\nTo setup daily scanning at 9:00 AM:")
    print("-" * 50)
    print("Run this command:")
    print(f'  echo "{cron_entry}" >> ~/.crontab && crontab ~/.crontab')
    print("\nOr manually add to crontab:")
    print(f"  crontab -e")
    print(f"  # Add line:")
    print(f"  {cron_entry}")
    print("-" * 50)


def main():
    """Main entry point"""
    if len(sys.argv) > 1 and sys.argv[1] == "--cron":
        # Run in cron mode (silent except for errors)
        run_daily_scan(notify_discord=True)
    else:
        # Interactive mode
        show_menu()


if __name__ == "__main__":
    main()
