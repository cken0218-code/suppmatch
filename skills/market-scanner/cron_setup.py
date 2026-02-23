#!/usr/bin/env python3
"""
CRON Job Setup Script
=====================
Automated daily scanning with Discord notifications.
"""

import os
import sys
from pathlib import Path

# Add market-scanner to path
sys.path.insert(0, str(Path(__file__).parent))

def get_cron_script_path():
    """Get path to the cron runner script."""
    return Path(__file__).parent / 'cron_runner.py'

def get_cron_command() -> str:
    """Generate the cron command."""
    script_path = get_cron_script_path()
    return f"python3 {script_path} >> ~/.openclaw/logs/market_scanner.log 2>&1"

def generate_cron_content() -> str:
    """Generate the cron runner script content."""
    return '''#!/usr/bin/env python3
"""
CRON Runner Script
==================
This script is executed by cron for daily automated scanning.
"""

import sys
import logging
from pathlib import Path

# Setup logging
log_dir = Path.home() / '.openclaw' / 'logs'
log_dir.mkdir(exist_ok=True)
logging.basicConfig(
    filename=log_dir / 'market_scanner.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Add market-scanner to path
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from main import MarketScanner
    
    logger = logging.getLogger(__name__)
    logger.info("="*60)
    logger.info("Starting daily market scan...")
    
    scanner = MarketScanner()
    results = scanner.run_daily_scan()
    
    # Send to Discord if configured
    if results:
        from discord_notifier import DiscordNotifier
        DiscordNotifier(scanner.config).send_daily_report(results)
        
        # Check for breakout alerts
        breakthrough_signals = results.get('breakthrough_signals', [])
        if breakthrough_signals:
            DiscordNotifier(scanner.config).send_breakout_alert(breakthrough_signals)
    
    logger.info("Daily scan completed successfully!")
    logger.info("="*60)

except Exception as e:
    logging.error(f"Error during daily scan: {e}", exc_info=True)
    
    try:
        from discord_notifier import DiscordNotifier
        from config import Config
        DiscordNotifier(Config()).send_error_alert(str(e))
    except:
        pass

    sys.exit(1)
'''

def setup_cron(schedule: str = '0 8 * * 1-5'):
    """Setup cron job for daily scanning."""
    print("\n" + "="*60)
    print("⏰ CRON JOB SETUP")
    print("="*60)
    
    # Create cron runner script
    cron_script = Path(__file__).parent / 'cron_runner.py'
    cron_script.write_text(generate_cron_content())
    cron_script.chmod(0o755)
    print(f"\n✅ Created cron runner script: {cron_script}")
    
    # Generate cron entry
    cron_command = get_cron_command()
    cron_entry = f"{schedule} {cron_command}"
    
    print(f"\n📝 Cron Entry:")
    print(f"   {cron_entry}")
    
    # Create crontab backup
    print("\n💾 Backing up existing crontab...")
    os.system('crontab -l > ~/.openclaw/backup_crontab.txt 2>/dev/null || true')
    
    # Add new cron entry
    print("\n📅 Adding new cron job...")
    os.system(f'(crontab -l 2>/dev/null | grep -v "market-scanner"; echo "{cron_entry}") | crontab -')
    
    print("\n✅ Cron job installed!")
    print(f"\n📋 Current crontab:")
    os.system('crontab -l')
    
    print("\n" + "-"*60)
    print("💡 Manual Commands:")
    print("-"*60)
    print("   View crontab:    crontab -l")
    print("   Edit crontab:    crontab -e")
    print("   Remove cron:     crontab -r")
    print("   Run now:        python3 ~/.openclaw/workspace/skills/market-scanner/main.py --mode daily")
    print("-"*60)

def remove_cron():
    """Remove the market scanner cron job."""
    print("\n🗑️  Removing market scanner cron job...")
    os.system("crontab -l | grep -v 'market-scanner' | crontab -")
    print("✅ Cron job removed!")

def test_cron():
    """Test the cron runner script."""
    print("\n🧪 Testing cron runner script...")
    
    script_path = get_cron_script_path()
    if not script_path.exists():
        print("❌ Cron runner script not found. Run setup first.")
        return False
    
    import subprocess
    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
        timeout=120
    )
    
    if result.returncode == 0:
        print("✅ Cron runner script executed successfully!")
        print(result.stdout)
        return True
    else:
        print("❌ Cron runner script failed!")
        print("STDERR:", result.stderr)
        return False

def get_status():
    """Check cron job status."""
    print("\n📊 Cron Job Status")
    print("="*40)
    
    result = os.popen('crontab -l').read()
    
    if 'market-scanner' in result:
        print("✅ Market Scanner cron job is INSTALLED")
        print("\n📅 Scheduled Time:")
        for line in result.split('\n'):
            if 'market-scanner' in line:
                print(f"   {line}")
    else:
        print("❌ Market Scanner cron job is NOT installed")
    
    print("\n💡 To setup: python3 main.py --setup")

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='CRON setup for Market Scanner')
    parser.add_argument('--setup', action='store_true', help='Setup cron job')
    parser.add_argument('--remove', action='store_true', help='Remove cron job')
    parser.add_argument('--test', action='store_true', help='Test cron script')
    parser.add_argument('--status', action='store_true', help='Check status')
    parser.add_argument('--schedule', default='0 8 * * 1-5', 
                       help='Cron schedule (default: 0 8 * * 1-5 = 8AM weekdays)')
    
    args = parser.parse_args()
    
    if args.setup:
        setup_cron(args.schedule)
    elif args.remove:
        remove_cron()
    elif args.test:
        test_cron()
    elif args.status:
        get_status()
    else:
        get_status()
