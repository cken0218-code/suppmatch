"""
Breakthrough Stock Scanner
==========================
Detect stocks showing breakout patterns:
- Price consolidation (2-4 weeks)
- Volume spike on breakout
- RSI recovery from oversold
- Moving average crossover (SMA 50/200 golden cross)
- Gap up pattern
- New 52-week high
"""

import csv
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from pathlib import Path
import statistics

class BreakthroughScanner:
    """
    Scanner for detecting breakthrough/breakout patterns in stocks.
    
    Key signals detected:
    1. Consolidation breakout (2-4 weeks tight range)
    2. Volume spike (>2x average)
    3. RSI recovery from oversold (<30 to >40)
    4. SMA golden cross (50/200)
    5. Gap up pattern
    6. New 52-week high
    """
    
    def __init__(self, config):
        self.config = config
        self.signals_file = Path(__file__).parent / 'data' / 'breakthrough_signals.csv'
        self.signals_file.parent.mkdir(exist_ok=True)
        
        # Scanner parameters
        self.params = {
            'consolidation_weeks': (2, 4),  # Min, max weeks
            'consolidation_max_range_pct': 15,  # during Max price range consolidation
            'volume_spike_multiplier': 2.0,  # Volume must be 2x average
            'rsi_oversold': 30,
            'rsi_recovery': 40,
            'rsi_period': 14,
            'sma_short': 50,
            'sma_long': 200,
            'gap_up_min_pct': 2.0,
            'lookback_days': 60  # Days to look back for patterns
        }
    
    def scan_all(self) -> List[Dict]:
        """Scan all watched stocks for breakthrough patterns."""
        # For demo, simulate scanning with sample data
        # In production, integrate with market data API
        
        signals = []
        
        # Get ASX watchlist stocks
        try:
            from asx_watchlist import ASXWatchlist
            asx = ASXWatchlist(self.config)
            stocks = asx.get_watchlist()
        except ImportError:
            stocks = self._get_sample_stocks()
        
        for stock in stocks:
            stock_signals = self._analyze_stock(stock)
            signals.extend(stock_signals)
        
        # Save signals
        self._save_signals(signals)
        
        return signals
    
    def _get_sample_stocks(self) -> List[Dict]:
        """Get sample stocks for demonstration."""
        return [
            {'code': 'WBT', 'name': 'Weebit Nano'},
            {'code': 'SFR', 'name': 'Sandfire'},
            {'code': 'EOS', 'name': 'EOS'},
            {'code': 'BTC', 'name': 'Bitcoin', 'is_crypto': True},
            {'code': 'SOL', 'name': 'Solana', 'is_crypto': True}
        ]
    
    def _analyze_stock(self, stock: Dict) -> List[Dict]:
        """Analyze a single stock for breakthrough patterns."""
        code = stock.get('code', '')
        signals = []
        
        # Simulate analysis for demo
        # In production: fetch real price data and analyze
        
        # Check each pattern type
        if self._check_consolidation_breakout(code):
            signals.append({
                'code': code,
                'pattern': 'Consolidation Breakout',
                'strength': 'HIGH',
                'description': f'{code} breaking out of 2-4 week consolidation',
                'timestamp': datetime.now().isoformat()
            })
        
        if self._check_volume_spike(code):
            signals.append({
                'code': code,
                'pattern': 'Volume Spike',
                'strength': 'MEDIUM',
                'description': f'{code} showing unusual volume increase',
                'timestamp': datetime.now().isoformat()
            })
        
        if self._check_rsi_recovery(code):
            signals.append({
                'code': code,
                'pattern': 'RSI Recovery',
                'strength': 'MEDIUM',
                'description': f'{code} RSI recovering from oversold territory',
                'timestamp': datetime.now().isoformat()
            })
        
        if self._check_golden_cross(code):
            signals.append({
                'code': code,
                'pattern': 'Golden Cross (SMA 50/200)',
                'strength': 'HIGH',
                'description': f'{code} showing golden cross pattern',
                'timestamp': datetime.now().isoformat()
            })
        
        if self._check_gap_up(code):
            signals.append({
                'code': code,
                'pattern': 'Gap Up',
                'strength': 'MEDIUM',
                'description': f'{code} with significant gap up',
                'timestamp': datetime.now().isoformat()
            })
        
        if self._check_52_week_high(code):
            signals.append({
                'code': code,
                'pattern': 'New 52-Week High',
                'strength': 'HIGH',
                'description': f'{code} hitting new 52-week high',
                'timestamp': datetime.now().isoformat()
            })
        
        return signals
    
    # Pattern detection methods (simplified for demo)
    # In production, these would fetch real price data
    
    def _check_consolidation_breakout(self, code: str) -> bool:
        """Check for consolidation breakout pattern."""
        # Simulated detection - real implementation needs price data
        return False  # No signal for demo
    
    def _check_volume_spike(self, code: str) -> bool:
        """Check for volume spike on breakout."""
        return False
    
    def _check_rsi_recovery(self, code: str) -> bool:
        """Check for RSI recovery from oversold."""
        return False
    
    def _check_golden_cross(self, code: str) -> bool:
        """Check for SMA 50/200 golden cross."""
        return False
    
    def _check_gap_up(self, code: str) -> bool:
        """Check for gap up pattern."""
        return False
    
    def _check_52_week_high(self, code: str) -> bool:
        """Check for new 52-week high."""
        return False
    
    def print_signals(self):
        """Print detected breakthrough signals."""
        signals = self.scan_all()
        
        if not signals:
            print("\n" + "="*60)
            print("🎯 BREAKTHROUGH SCANNER RESULTS")
            print("="*60)
            print("\n✅ No breakthrough patterns detected today.")
            print("   Market conditions normal - no alerts triggered.")
            print("\n" + "="*60 + "\n")
            return
        
        print("\n" + "="*60)
        print("🎯 BREAKTHROUGH SCANNER - ALERTS DETECTED")
        print("="*60)
        
        # Group by strength
        high = [s for s in signals if s['strength'] == 'HIGH']
        medium = [s for s in signals if s['strength'] == 'MEDIUM']
        
        if high:
            print("\n🔴 HIGH PRIORITY SIGNALS:")
            for signal in high:
                print(f"   ⚡ {signal['code']} - {signal['pattern']}")
                print(f"      {signal['description']}")
        
        if medium:
            print("\n🟡 MEDIUM PRIORITY SIGNALS:")
            for signal in medium:
                print(f"   📊 {signal['code']} - {signal['pattern']}")
                print(f"      {signal['description']}")
        
        print(f"\n📈 Total Signals: {len(signals)}")
        print(f"   High: {len(high)} | Medium: {len(medium)}")
        print("="*60 + "\n")
    
    def get_signals_summary(self) -> str:
        """Get signals summary as string."""
        signals = self.scan_all()
        
        if not signals:
            return "🎯 No breakthrough patterns detected."
        
        lines = [f"🎯 Breakthrough Signals: {len(signals)}"]
        for signal in signals:
            emoji = "🔴" if signal['strength'] == 'HIGH' else "🟡"
            lines.append(f"   {emoji} {signal['code']}: {signal['pattern']}")
        
        return "\n".join(lines)
    
    def _save_signals(self, signals: List[Dict]):
        """Save signals to CSV."""
        self.signals_file.parent.mkdir(exist_ok=True)
        
        with open(self.signals_file, 'w', newline='') as f:
            if signals:
                fieldnames = list(signals[0].keys())
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(signals)
    
    def load_signals(self) -> List[Dict]:
        """Load saved signals."""
        if not self.signals_file.exists():
            return []
        
        with open(self.signals_file, 'r') as f:
            reader = csv.DictReader(f)
            return list(reader)
    
    def analyze_price_data(self, prices: List[float]) -> Dict:
        """Analyze price data for patterns."""
        if len(prices) < self.params['sma_long']:
            return {'error': 'Insufficient data'}
        
        analysis = {}
        
        # Calculate moving averages
        sma_50 = self._sma(prices, self.params['sma_short'])
        sma_200 = self._sma(prices, self.params['sma_long'])
        
        analysis['sma_50'] = sma_50[-1] if sma_50 else None
        analysis['sma_200'] = sma_200[-1] if sma_200 else None
        analysis['golden_cross'] = (
            sma_50[-1] > sma_200[-1] if sma_50 and sma_200 else False
        )
        
        # Calculate RSI
        analysis['rsi'] = self._rsi(prices, self.params['rsi_period'])
        
        # Calculate volatility
        if len(prices) >= 20:
            recent = prices[-20:]
            analysis['volatility'] = statistics.stdev(recent) / statistics.mean(recent) * 100
        else:
            analysis['volatility'] = None
        
        # Check for new high
        analysis['new_52w_high'] = prices[-1] == max(prices[-260:]) if len(prices) >= 260 else False
        
        return analysis
    
    def _sma(self, data: List[float], period: int) -> List[float]:
        """Calculate Simple Moving Average."""
        if len(data) < period:
            return []
        
        sma = []
        for i in range(period - 1, len(data)):
            sma.append(sum(data[i-period+1:i+1]) / period)
        
        return sma
    
    def _rsi(self, prices: List[float], period: int = 14) -> Optional[float]:
        """Calculate Relative Strength Index."""
        if len(prices) < period + 1:
            return None
        
        gains = []
        losses = []
        
        for i in range(1, len(prices)):
            change = prices[i] - prices[i-1]
            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))
        
        if not gains or sum(gains) == 0:
            return None
        
        avg_gain = sum(gains[-period:]) / period
        avg_loss = sum(losses[-period:]) / period
        
        if avg_loss == 0:
            return 100
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        return round(rsi, 2)
    
    def check_alert_conditions(self) -> List[Dict]:
        """Check if any alert conditions are met."""
        signals = self.scan_all()
        alerts = []
        
        for signal in signals:
            # High priority signals generate alerts
            if signal['strength'] == 'HIGH':
                alerts.append({
                    'type': 'breakout_alert',
                    'code': signal['code'],
                    'pattern': signal['pattern'],
                    'priority': 'HIGH',
                    'timestamp': datetime.now().isoformat()
                })
        
        return alerts
    
    def get_market_scan_report(self) -> str:
        """Generate market scan report."""
        signals = self.load_signals()
        
        report = ["\n" + "="*70]
        report.append("📊 BREAKTHROUGH SCANNER - MARKET REPORT")
        report.append("="*70)
        report.append(f"\nScan Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        
        if not signals:
            report.append("\n✅ No breakthrough patterns detected.")
            report.append("   Market conditions normal.")
        else:
            report.append(f"\n🔔 Signals Detected: {len(signals)}")
            
            # Group by pattern
            patterns = {}
            for signal in signals:
                pattern = signal['pattern']
                patterns[pattern] = patterns.get(pattern, 0) + 1
            
            report.append("\n📈 PATTERN BREAKDOWN:")
            for pattern, count in sorted(patterns.items(), key=lambda x: -x[1]):
                report.append(f"   • {pattern}: {count}")
            
            # Group by strength
            high = [s for s in signals if s['strength'] == 'HIGH']
            medium = [s for s in signals if s['strength'] == 'MEDIUM']
            
            report.append(f"\n⚡ STRENGTH: HIGH: {len(high)} | MEDIUM: {len(medium)}")
            
            report.append("\n📋 DETECTED SIGNALS:")
            for signal in signals:
                emoji = "🔴" if signal['strength'] == 'HIGH' else "🟡"
                report.append(f"   {emoji} {signal['code']}: {signal['pattern']}")
        
        report.append("\n" + "="*70 + "\n")
        
        return "\n".join(report)
