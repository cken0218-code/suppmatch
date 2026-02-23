#!/usr/bin/env python3
"""
Breakthrough Stock Scanner - Identifies Breakout Patterns
Scans for stocks showing:
- Price consolidating 2-4 weeks then breaking out
- Volume spike on breakout
- RSI recovering from oversold
- SMA 50/200 golden cross
- Gap up pattern
- New 52-week high

Uses Yahoo Finance (yfinance) for data - free API
"""

import json
import sys
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Tuple
import os

try:
    import yfinance as yf
except ImportError:
    print("Installing yfinance...")
    os.system("pip install yfinance -q")
    import yfinance as yf

# Configuration
SCAN_RESULTS_FILE = os.path.expanduser("~/.openclaw/workspace/skills/market-scanner/scan_results.json")
ALERT_LOG_FILE = os.path.expanduser("~/.openclaw/workspace/skills/market-scanner/alert_log.txt")

# Sample stocks to scan (can be expanded)
DEFAULT_SCAN_TICKERS = [
    # Technology
    "WTC", "XRO", "ABB", "OCL", "WBT", "APT", "MP1", "WSP", "XST", "NXT",
    # Mining
    "BHP", "RIO", "FMG", "SFR", "NST", "EVN", "IGO", "MIN", "LKE", "PLS",
    # Healthcare
    "CSL", "EBR", "BB1", "RHC", "SHL", "COH", "MSB", "FPH", "VHT", "AXP",
    # Energy & Financials
    "CBA", "WBC", "ANZ", "NAB", "MQG", "EOS", "STO", "WDS", "AGL", "ORG"
]


class BreakoutScanner:
    """Scanner for identifying breakthrough/breakout stock patterns"""
    
    def __init__(self, tickers: List[str] = None, lookback_days: int = 90):
        self.tickers = tickers or DEFAULT_SCAN_TICKERS
        self.lookback_days = lookback_days
        self.results = []
    
    def calculate_sma(self, prices: List[float], period: int) -> List[float]:
        """Calculate Simple Moving Average"""
        if len(prices) < period:
            return prices
        sma = []
        for i in range(len(prices)):
            if i < period - 1:
                sma.append(prices[i])
            else:
                sma.append(sum(prices[i-period+1:i+1]) / period)
        return sma
    
    def calculate_rsi(self, prices: List[float], period: int = 14) -> List[float]:
        """Calculate Relative Strength Index"""
        if len(prices) < period + 1:
            return [50.0] * len(prices)
        
        deltas = [prices[i+1] - prices[i] for i in range(len(prices)-1)]
        gains = [d if d > 0 else 0 for d in deltas]
        losses = [-d if d < 0 else 0 for d in deltas]
        
        avg_gain = sum(gains[:period]) / period
        avg_loss = sum(losses[:period]) / period
        
        rsi = [50.0]  # First point is neutral
        
        for i in range(period, len(gains)):
            avg_gain = (avg_gain * (period - 1) + gains[i]) / period
            avg_loss = (avg_loss * (period - 1) + losses[i]) / period
            
            if avg_loss == 0:
                rsi.append(100)
            else:
                rs = avg_gain / avg_loss
                rsi.append(100 - (100 / (1 + rs)))
        
        return rsi
    
    def calculate_volume_sma(self, volumes: List[int], period: int = 20) -> List[float]:
        """Calculate Volume SMA"""
        if len(volumes) < period:
            return [float(v) for v in volumes]
        
        sma = []
        for i in range(len(volumes)):
            if i < period - 1:
                sma.append(float(volumes[i]))
            else:
                sma.append(sum(volumes[i-period+1:i+1]) / period)
        return sma
    
    def detect_consolidation_breakout(self, prices: List[float], window: int = 20) -> Dict:
        """Detect if price is breaking out of consolidation"""
        if len(prices) < window + 10:
            return {"detected": False, "breakout_price": None, "consolidation_range": None}
        
        recent_prices = prices[-window:]
        min_price = min(recent_prices)
        max_price = max(recent_prices)
        current_price = prices[-1]
        
        # Consolidation: price range is narrow (less than 15% range)
        price_range_pct = (max_price - min_price) / min_price * 100
        is_consolidating = price_range_pct < 15
        
        # Breakout: current price above recent high
        breakout_threshold = max_price * 1.02  # 2% above consolidation high
        is_breakout = current_price >= breakout_threshold
        
        return {
            "detected": is_consolidating and is_breakout,
            "breakout_price": current_price,
            "consolidation_range": f"{min_price:.2f} - {max_price:.2f}",
            "range_pct": price_range_pct,
            "breakout_strength": (current_price - max_price) / max_price * 100 if is_breakout else 0
        }
    
    def detect_volume_spike(self, volumes: List[int], sma_period: int = 20, threshold: float = 2.0) -> Dict:
        """Detect volume spike on breakout"""
        if len(volumes) < sma_period + 5:
            return {"detected": False, "volume_ratio": None}
        
        recent_volumes = volumes[-10:]
        current_volume = volumes[-1]
        avg_volume = sum(recent_volumes) / len(recent_volumes)
        
        volume_ratio = current_volume / avg_volume if avg_volume > 0 else 0
        
        return {
            "detected": volume_ratio >= threshold,
            "volume_ratio": round(volume_ratio, 2),
            "current_volume": current_volume,
            "avg_volume": int(avg_volume)
        }
    
    def detect_rsi_recovery(self, prices: List[float], period: int = 14, oversold: float = 40) -> Dict:
        """Detect RSI recovering from oversold"""
        rsi = self.calculate_rsi(prices, period)
        
        if len(rsi) < 10:
            return {"detected": False, "current_rsi": 50, "direction": "unknown"}
        
        recent_rsi = rsi[-10:]
        current_rsi = rsi[-1]
        
        # Check if RSI was oversold recently and is recovering
        was_oversold = any(r < oversold for r in recent_rsi[:-2])
        is_recovering = current_rsi > oversold and current_rsi > recent_rsi[0]
        
        return {
            "detected": was_oversold and is_recovering,
            "current_rsi": round(current_rsi, 2),
            "direction": "recovering" if is_recovering else "weakening",
            "was_oversold": was_oversold
        }
    
    def detect_golden_cross(self, prices: List[float], short_period: int = 50, long_period: int = 200) -> Dict:
        """Detect SMA 50/200 golden cross (or bullish alignment)"""
        if len(prices) < long_period + 5:
            return {"detected": False, "signal": "insufficient_data"}
        
        sma_50 = self.calculate_sma(prices, short_period)[-10:]
        sma_200 = self.calculate_sma(prices, long_period)[-10:]
        
        current_price = prices[-1]
        current_sma50 = sma_50[-1]
        current_sma200 = sma_200[-1]
        
        # Golden cross: SMA50 crosses above SMA200
        prev_sma50 = sma_50[-5]
        prev_sma200 = sma_200[-5]
        
        golden_cross = prev_sma50 < prev_sma200 and current_sma50 > current_sma200
        bullish_alignment = current_sma50 > current_sma200  # Price above both SMAs
        
        return {
            "detected": golden_cross or bullish_alignment,
            "signal": "golden_cross" if golden_cross else "bullish_alignment" if bullish_alignment else "neutral",
            "sma_50": round(current_sma50, 2),
            "sma_200": round(current_sma200, 2),
            "price_vs_sma50": (current_price - current_sma50) / current_sma50 * 100,
            "price_vs_sma200": (current_price - current_sma200) / current_sma200 * 100
        }
    
    def detect_gap_up(self, prices: List[float], gap_threshold: float = 2.0) -> Dict:
        """Detect gap up pattern"""
        if len(prices) < 2:
            return {"detected": False, "gap_pct": None}
        
        current_price = prices[-1]
        prev_close = prices[-2]
        
        # Check for gap up (current open significantly above previous close)
        gap_pct = (current_price - prev_close) / prev_close * 100
        
        return {
            "detected": gap_pct >= gap_threshold,
            "gap_pct": round(gap_pct, 2),
            "prev_close": prev_close,
            "current_price": current_price
        }
    
    def detect_52week_high(self, prices: List[float], current_price: float) -> Dict:
        """Detect if stock is at new 52-week high"""
        if len(prices) < 252:
            # Use available data if less than 252 days
            period = len(prices)
        else:
            period = 252
        
        recent_prices = prices[-period:]
        week_high = max(recent_prices)
        
        # New high if within 1% of 52-week high
        is_new_high = current_price >= week_high * 0.99
        
        return {
            "detected": is_new_high,
            "current_price": current_price,
            "week_52_high": week_high,
            "distance_from_high": (current_price - week_high) / week_high * 100
        }
    
    def calculate_breakout_score(self, patterns: Dict) -> int:
        """Calculate overall breakout score (0-100)"""
        score = 0
        
        if patterns.get("consolidation_breakout", {}).get("detected"):
            score += 25
        if patterns.get("volume_spike", {}).get("detected"):
            score += 20
        if patterns.get("rsi_recovery", {}).get("detected"):
            score += 15
        if patterns.get("golden_cross", {}).get("detected"):
            score += 25
        if patterns.get("gap_up", {}).get("detected"):
            score += 10
        if patterns.get("week_high", {}).get("detected"):
            score += 20
        
        return score
    
    def scan_ticker(self, ticker: str) -> Optional[Dict]:
        """Scan a single ticker for breakout patterns"""
        try:
            stock = yf.Ticker(f"{ticker}.AX")
            hist = stock.history(period=f"{self.lookback_days}d")
            
            if hist.empty or len(hist) < 50:
                return None
            
            prices = hist['Close'].tolist()
            volumes = hist['Volume'].tolist()
            current_price = prices[-1]
            
            patterns = {
                "consolidation_breakout": self.detect_consolidation_breakout(prices, window=20),
                "volume_spike": self.detect_volume_spike(volumes),
                "rsi_recovery": self.detect_rsi_recovery(prices),
                "golden_cross": self.detect_golden_cross(prices),
                "gap_up": self.detect_gap_up(prices),
                "week_high": self.detect_52week_high(prices, current_price)
            }
            
            breakout_score = self.calculate_breakout_score(patterns)
            
            # Get company info
            info = stock.info
            company_name = info.get('longName', info.get('shortName', ticker))
            sector = info.get('sector', 'Unknown')
            
            return {
                "ticker": ticker,
                "name": company_name,
                "sector": sector,
                "current_price": current_price,
                "breakout_score": breakout_score,
                "patterns": patterns,
                "breakout_signals": [k for k, v in patterns.items() if v.get("detected")],
                "scan_time": datetime.now().isoformat()
            }
            
        except Exception as e:
            print(f"Error scanning {ticker}: {e}")
            return None
    
    def run_scan(self, min_score: int = 40) -> List[Dict]:
        """Run breakout scan on all tickers"""
        print(f"Scanning {len(self.tickers)} tickers for breakout patterns...")
        
        results = []
        for ticker in self.tickers:
            result = self.scan_ticker(ticker)
            if result and result["breakout_score"] >= min_score:
                results.append(result)
        
        # Sort by breakout score
        results.sort(key=lambda x: x["breakout_score"], reverse=True)
        
        self.results = results
        return results
    
    def generate_report(self) -> str:
        """Generate scan report"""
        report_lines = []
        report_lines.append("=" * 70)
        report_lines.append("BREAKTHROUGH STOCK SCANNER REPORT")
        report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S %Z')}")
        report_lines.append(f"Scanned: {len(self.tickers)} tickers")
        report_lines.append("=" * 70)
        report_lines.append("")
        
        if not self.results:
            report_lines.append("No breakout signals detected above threshold.")
            return "\n".join(report_lines)
        
        for i, result in enumerate(self.results, 1):
            report_lines.append(f"## #{i} {result['ticker']} - {result['name']}")
            report_lines.append("-" * 60)
            report_lines.append(f"  Current Price:  ${result['current_price']:.2f}")
            report_lines.append(f"  Breakout Score: {result['breakout_score']}/100")
            report_lines.append(f"  Sector:         {result['sector']}")
            report_lines.append(f"  Signals:        {', '.join(result['breakout_signals']) if result['breakout_signals'] else 'None'}")
            report_lines.append("")
            
            # Pattern details
            patterns = result["patterns"]
            if patterns["consolidation_breakout"]["detected"]:
                pb = patterns["consolidation_breakout"]
                report_lines.append(f"  ✓ Consolidation Breakout:")
                report_lines.append(f"    Range: {pb['consolidation_range']} | Breakout: {pb['breakout_strength']:.2f}%")
            
            if patterns["volume_spike"]["detected"]:
                vs = patterns["volume_spike"]
                report_lines.append(f"  ✓ Volume Spike:")
                report_lines.append(f"    {vs['volume_ratio']}x average volume")
            
            if patterns["rsi_recovery"]["detected"]:
                rr = patterns["rsi_recovery"]
                report_lines.append(f"  ✓ RSI Recovery:")
                report_lines.append(f"    RSI: {rr['current_rsi']} (recovering from oversold)")
            
            if patterns["golden_cross"]["detected"]:
                gc = patterns["golden_cross"]
                report_lines.append(f"  ✓ Golden Cross:")
                report_lines.append(f"    Signal: {gc['signal']} | SMA50: ${gc['sma_50']:.2f} | SMA200: ${gc['sma_200']:.2f}")
            
            if patterns["gap_up"]["detected"]:
                gu = patterns["gap_up"]
                report_lines.append(f"  ✓ Gap Up:")
                report_lines.append(f"    Gap: {gu['gap_pct']:.2f}%")
            
            if patterns["week_high"]["detected"]:
                wh = patterns["week_high"]
                report_lines.append(f"  ✓ 52-Week High:")
                report_lines.append(f"    New high: ${wh['current_price']:.2f} (52w: ${wh['week_52_high']:.2f})")
            
            report_lines.append("")
        
        # Summary
        report_lines.append("=" * 70)
        report_lines.append("SCAN SUMMARY")
        report_lines.append("=" * 70)
        report_lines.append(f"Total breakouts found: {len(self.results)}")
        report_lines.append(f"Average breakout score: {sum(r['breakout_score'] for r in self.results) / len(self.results):.1f}")
        report_lines.append("")
        report_lines.append("Pattern Legend:")
        report_lines.append("  - consolidation_breakout: Price breaking out of 2-4 week range")
        report_lines.append("  - volume_spike: 2x+ average volume on breakout")
        report_lines.append("  - rsi_recovery: RSI recovering from oversold (<40)")
        report_lines.append("  - golden_cross: SMA50 crossing above SMA200")
        report_lines.append("  - gap_up: Gap up pattern (>2%)")
        report_lines.append("  - week_high: New 52-week high")
        report_lines.append("")
        report_lines.append("=" * 70)
        
        return "\n".join(report_lines)
    
    def save_results(self):
        """Save scan results to JSON"""
        results_data = {
            "scan_time": datetime.now().isoformat(),
            "tickers_scanned": len(self.tickers),
            "results_count": len(self.results),
            "results": self.results
        }
        
        with open(SCAN_RESULTS_FILE, 'w') as f:
            json.dump(results_data, f, indent=2, default=str)
        
        print(f"Results saved to: {SCAN_RESULTS_FILE}")


def main():
    """Main entry point"""
    print("Starting Breakthrough Stock Scanner...")
    
    scanner = BreakoutScanner()
    results = scanner.run_scan(min_score=30)
    scanner.save_results()
    
    report = scanner.generate_report()
    print("\n" + report)
    
    # Save report
    report_file = os.path.expanduser("~/.openclaw/workspace/skills/market-scanner/breakout_report.md")
    with open(report_file, 'w') as f:
        f.write(report)
    print(f"\nReport saved to: {report_file}")
    
    return results


if __name__ == "__main__":
    try:
        results = main()
        print(f"\nScan complete. Found {len(results)} potential breakouts.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
