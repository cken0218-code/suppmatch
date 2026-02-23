"""
Configuration Module
====================
Load and manage scanner configuration.
"""

import yaml
from pathlib import Path
from datetime import datetime

class Config:
    """Configuration management for the market scanner."""
    
    def __init__(self):
        self.config_file = Path(__file__).parent / 'config.yaml'
        self._config = self._load_config()
    
    def _load_config(self) -> dict:
        """Load configuration from YAML file."""
        default_config = self._get_default_config()
        
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    user_config = yaml.safe_load(f) or {}
                
                # Merge user config with defaults
                return {**default_config, **user_config}
            except Exception as e:
                print(f"Error loading config: {e}")
                return default_config
        else:
            return default_config
    
    def _get_default_config(self) -> dict:
        """Get default configuration."""
        return {
            'scanner': {
                'name': 'Market Scanner',
                'version': '1.0.0',
                'created': datetime.now().isoformat(),
                'timezone': 'Australia/Sydney'
            },
            'crypto': {
                'tracked_coins': ['bitcoin', 'solana'],
                'default_currency': 'usd',
                'price_alert_threshold_pct': 5,
                'trend_alert_threshold_pct': 10
            },
            'asx': {
                'watchlist_file': 'data/asx_watchlist.csv',
                'default_sectors': [
                    'Technology',
                    'Healthcare',
                    'Materials',
                    'Energy',
                    'Financials'
                ],
                'min_market_cap_millions': 100
            },
            'breakthrough': {
                'consolidation_weeks_min': 2,
                'consolidation_weeks_max': 4,
                'consolidation_range_max_pct': 15,
                'volume_spike_multiplier': 2.0,
                'rsi_oversold': 30,
                'rsi_recovery': 40,
                'sma_short': 50,
                'sma_long': 200,
                'gap_up_min_pct': 2.0,
                'lookback_days': 60
            },
            'discord': {
                'enabled': False,
                'webhook_url': '',
                'channel': '',
                'mention_role': ''
            },
            'cron': {
                'enabled': True,
                'schedule': '0 8 * * 1-5',  # 8 AM weekdays
                'daily_report': True,
                'breakout_alerts': True
            },
            'notifications': {
                'email': {
                    'enabled': False,
                    'smtp_server': '',
                    'smtp_port': 587,
                    'from_address': '',
                    'to_addresses': []
                },
                'discord': {
                    'enabled': False,
                    'webhook_url': ''
                }
            }
        }
    
    def save(self):
        """Save current configuration to file."""
        self.config_file.parent.mkdir(exist_ok=True)
        
        with open(self.config_file, 'w') as f:
            yaml.dump(self._config, f, default_flow_style=False, indent=2)
    
    def setup(self):
        """Interactive setup wizard."""
        print("\n" + "="*50)
        print("🔧 MARKET SCANNER SETUP")
        print("="*50)
        
        # Discord setup
        discord_enabled = input("\nEnable Discord notifications? (y/n): ").lower() == 'y'
        self._config['discord']['enabled'] = discord_enabled
        
        if discord_enabled:
            webhook = input("Enter Discord webhook URL: ").strip()
            self._config['discord']['webhook_url'] = webhook
        
        # Cron setup
        cron_enabled = input("\nEnable automated daily scanning? (y/n): ").lower() == 'y'
        self._config['cron']['enabled'] = cron_enabled
        
        if cron_enabled:
            schedule = input("Enter cron schedule (default: 0 8 * * 1-5): ").strip()
            if schedule:
                self._config['cron']['schedule'] = schedule
        
        # Save configuration
        self.save()
        
        print("\n✅ Setup complete! Configuration saved to config.yaml")
        print("\nTo configure CRON job, run:")
        print(f"   echo '0 8 * * 1-5 python3 {Path(__file__).parent}/main.py --mode daily --discord' >> /etc/crontab")
    
    def get(self, key: str, default=None):
        """Get configuration value using dot notation."""
        keys = key.split('.')
        value = self._config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value):
        """Set configuration value using dot notation."""
        keys = key.split('.')
        config = self._config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
        self.save()
    
    @property
    def discord_webhook(self) -> str:
        """Get Discord webhook URL."""
        return self._config.get('discord', {}).get('webhook_url', '')
    
    @property
    def discord_enabled(self) -> bool:
        """Check if Discord notifications are enabled."""
        return self._config.get('discord', {}).get('enabled', False)
    
    @property
    def cron_enabled(self) -> bool:
        """Check if CRON scheduling is enabled."""
        return self._config.get('cron', {}).get('enabled', False)
    
    @property
    def cron_schedule(self) -> str:
        """Get CRON schedule."""
        return self._config.get('cron', {}).get('schedule', '0 8 * * 1-5')
