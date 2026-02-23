"""
Discord Notifier Module
=======================
Send notifications to Discord when breakout patterns are detected.
"""

import json
import requests
from datetime import datetime
from typing import List, Dict, Optional

class DiscordNotifier:
    """Send market scanner alerts to Discord."""
    
    def __init__(self, config):
        self.config = config
        self.webhook_url = config.discord_webhook
        self.enabled = config.discord_enabled
    
    def send_message(self, content: str, embed: Optional[Dict] = None) -> bool:
        """Send message to Discord channel."""
        if not self.enabled or not self.webhook_url:
            print("Discord not enabled or webhook URL not set")
            return False
        
        payload = {}
        
        if content:
            payload['content'] = content
        
        if embed:
            payload['embeds'] = [embed]
        
        try:
            response = requests.post(
                self.webhook_url,
                json=payload,
                timeout=10
            )
            response.raise_for_status()
            return True
        except requests.RequestException as e:
            print(f"Error sending Discord message: {e}")
            return False
    
    def send_daily_report(self, results: Dict) -> bool:
        """Send daily market report to Discord."""
        embed = {
            'title': '📊 Market Scanner - Daily Report',
            'description': f'Scan performed at {datetime.now().strftime("%Y-%m-%d %H:%M")}',
            'color': 0x3498db,
            'footer': {
                'text': 'Market Scanner v1.0'
            },
            'fields': []
        }
        
        # Add crypto summary
        if 'crypto' in results and results['crypto']:
            embed['fields'].append({
                'name': '💰 Crypto',
                'value': 'Updated',
                'inline': True
            })
        
        # Add ASX summary
        if 'asx_watchlist' in results and results['asx_watchlist']:
            embed['fields'].append({
                'name': '📋 ASX Watchlist',
                'value': 'Updated',
                'inline': True
            })
        
        # Add breakthrough signals
        if 'breakthrough_signals' in results:
            signals = results['breakthrough_signals']
            signal_count = len(signals)
            high_count = len([s for s in signals if s.get('strength') == 'HIGH'])
            
            signal_text = f"{signal_count} signals"
            if high_count > 0:
                signal_text += f" ({high_count} high priority)"
            
            embed['fields'].append({
                'name': '🎯 Breakthrough',
                'value': signal_text,
                'inline': True
            })
        
        return self.send_message('📈 **Daily Market Scan Complete**', embed)
    
    def send_breakout_alert(self, signals: List[Dict]) -> bool:
        """Send breakout alert when patterns are detected."""
        if not signals:
            return False
        
        high_priority = [s for s in signals if s.get('strength') == 'HIGH']
        medium_priority = [s for s in signals if s.get('strength') == 'MEDIUM']
        
        # Build alert message
        alert_text = "🚨 **BREAKTHROUGH ALERT DETECTED** 🚨\n"
        
        if high_priority:
            alert_text += f"\n🔴 **HIGH PRIORITY ({len(high_priority)})**\n"
            for signal in high_priority:
                alert_text += f"⚡ **{signal['code']}** - {signal['pattern']}\n"
        
        if medium_priority:
            alert_text += f"\n🟡 **MEDIUM PRIORITY ({len(medium_priority)})**\n"
            for signal in medium_priority:
                alert_text += f"📊 **{signal['code']}** - {signal['pattern']}\n"
        
        embed = {
            'title': '🎯 Breakthrough Pattern Detected',
            'description': alert_text,
            'color': 0xe74c3c if high_priority else 0xf39c12,
            'timestamp': datetime.now().isoformat(),
            'footer': {
                'text': 'Market Scanner - Breakout Alert'
            }
        }
        
        return self.send_message(None, embed)
    
    def send_crypto_alert(self, symbol: str, change_24h: float, price: float) -> bool:
        """Send crypto price alert."""
        emoji = "🚀" if change_24h > 0 else "📉"
        direction = "surge" if change_24h > 0 else "drop"
        
        embed = {
            'title': f'{emoji} Crypto Alert - {symbol}',
            'description': f'{symbol} has {direction} **{change_24h:+.2f}%** in the last 24 hours',
            'color': 0xe74c3c if change_24h < -5 else (0x2ecc71 if change_24h > 5 else 0x3498db),
            'fields': [
                {
                    'name': 'Current Price',
                    'value': f'${price:,.2f}',
                    'inline': True
                },
                {
                    'name': '24h Change',
                    'value': f'{change_24h:+.2f}%',
                    'inline': True
                }
            ],
            'timestamp': datetime.now().isoformat()
        }
        
        return self.send_message(f'📢 **{symbol}** crypto alert!', embed)
    
    def send_error_alert(self, error_message: str) -> bool:
        """Send error notification."""
        embed = {
            'title': '❌ Scanner Error',
            'description': error_message,
            'color': 0xe74c3c,
            'timestamp': datetime.now().isoformat()
        }
        
        return self.send_message('⚠️ **Scanner Error Occurred**', embed)
    
    def test_connection(self) -> bool:
        """Test Discord webhook connection."""
        test_embed = {
            'title': '✅ Connection Test',
            'description': 'Market Scanner Discord integration is working!',
            'color': 0x2ecc71,
            'timestamp': datetime.now().isoformat()
        }
        
        return self.send_message('🧪 **Discord Connection Test**', test_embed)
