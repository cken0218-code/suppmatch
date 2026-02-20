#!/usr/bin/env python3
"""
Portfolio Optimizer - Modern Portfolio Theory + Technical Signals
Usage: portfolio-optimizer.py --weights 0.3,0.2,0.15,0.15,0.1,0.1 --rebalance

Features:
- Modern Portfolio Theory optimization
- Risk-adjusted returns (Sharpe, Sortino, Calmar)
- Technical signal aggregation
- Sector diversification scoring
"""

import argparse
import json
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Optional

try:
    import yfinance as yf
    import pandas as pd
    import numpy as np
except ImportError:
    print("❌ Required: pip install yfinance pandas numpy")
    sys.exit(1)

# ASX stocks with sector info
ASX_PORTFOLIO = {
    "CBA": {"sector": "Financial", "weight": 0.15},
    "BHP": {"sector": "Materials", "weight": 0.12},
    "CSL": {"sector": "Healthcare", "weight": 0.12},
    "ANZ": {"sector": "Financial", "weight": 0.10},
    "NAB": {"sector": "Financial", "weight": 0.10},
    "WBC": {"sector": "Financial", "weight": 0.08},
    "4DX": {"sector": "Healthcare", "weight": 0.05},
    "AD8": {"sector": "Technology", "weight": 0.05},
    "ARU": {"sector": "Real Estate", "weight": 0.05},
    "BGL": {"sector": "Real Estate", "weight": 0.05},
    "ELD": {"sector": "Consumer", "weight": 0.05},
    "KMD": {"sector": "Consumer", "weight": 0.04},
    "VR1": {"sector": "Technology", "weight": 0.04},
}

def fetch_all_data(tickers: List[str], period="1y") -> Dict:
    """Fetch data for all tickers"""
    results = {}
    for ticker in tickers:
        try:
            ticker_ax = f"{ticker}.AX"
            stock = yf.Ticker(ticker_ax)
            hist = stock.history(period=period)
            info = stock.info
            results[ticker] = {"history": hist, "info": info, "error": None}
        except Exception as e:
            results[ticker] = {"history": None, "info": {}, "error": str(e)}
    return results

def calculate_returns(data: pd.Series) -> pd.Series:
    """Calculate daily returns"""
    return data.pct_change().dropna()

def calculate_sharpe(returns: pd.Series, risk_free_rate: float = 0.045) -> float:
    """Calculate Sharpe Ratio (annualized)"""
    if len(returns) < 30:
        return 0.0
    excess = returns.mean() * 252 - risk_free_rate
    return excess / (returns.std() * np.sqrt(252)) if returns.std() > 0 else 0.0

def calculate_sortino(returns: pd.Series, risk_free_rate: float = 0.045) -> float:
    """Calculate Sortino Ratio (downside deviation)"""
    if len(returns) < 30:
        return 0.0
    excess = returns.mean() * 252 - risk_free_rate
    downside = returns[returns < 0].std() * np.sqrt(252)
    return excess / downside if downside > 0 else 0.0

def calculate_max_drawdown(cumulative: pd.Series) -> float:
    """Calculate maximum drawdown"""
    if len(cumulative) < 2:
        return 0.0
    peak = cumulative.expanding(min_periods=1).max()
    drawdown = (cumulative - peak) / peak
    return drawdown.min() * 100

def calculate_calmar(returns: pd.Series, max_dd: float) -> float:
    """Calculate Calmar Ratio (annualized return / max drawdown)"""
    if max_dd == 0:
        return 0.0
    annual_return = returns.mean() * 252
    return abs(annual_return / (max_dd / 100))

def calculate_volatility(returns: pd.Series) -> float:
    """Calculate annualized volatility"""
    return returns.std() * np.sqrt(252) * 100

def calculate_var(returns: pd.Series, confidence: float = 0.95) -> float:
    """Calculate Value at Risk"""
    return np.percentile(returns, (1 - confidence) * 100) * 100

def calculate_cvar(returns: pd.Series, confidence: float = 0.95) -> float:
    """Calculate Conditional Value at Risk (Expected Shortfall)"""
    var = np.percentile(returns, (1 - confidence) * 100)
    return returns[returns <= var].mean() * 100

def calculate_beta(returns: pd.Series, market_returns: pd.Series) -> float:
    """Calculate beta relative to market"""
    if len(returns) < 30 or len(market_returns) < 30:
        return 1.0
    covariance = np.cov(returns, market_returns)[0][1]
    market_variance = np.var(market_returns)
    return covariance / market_variance if market_variance > 0 else 1.0

def technical_signals(data: pd.DataFrame) -> Dict:
    """Calculate comprehensive technical indicators"""
    if data is None or len(data) < 50:
        return {"overall": "NEUTRAL", "signals": {}}
    
    close = data['Close']
    signals = {}
    
    # RSI
    delta = close.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    signals['rsi'] = rsi.iloc[-1]
    
    # MACD
    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()
    macd = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()
    signals['macd'] = macd.iloc[-1]
    signals['macd_signal'] = signal.iloc[-1]
    signals['macd_histogram'] = macd.iloc[-1] - signal.iloc[-1]
    
    # Moving Averages
    signals['sma_20'] = close.rolling(20).mean().iloc[-1]
    signals['sma_50'] = close.rolling(50).mean().iloc[-1]
    signals['sma_200'] = close.rolling(200).mean().iloc[-1] if len(close) >= 200 else None
    signals['ema_12'] = close.ewm(span=12).mean().iloc[-1]
    signals['ema_26'] = close.ewm(span=26).mean().iloc[-1]
    
    # Price position
    current_price = close.iloc[-1]
    signals['price'] = current_price
    signals['above_sma20'] = current_price > signals['sma_20']
    signals['above_sma50'] = current_price > signals['sma_50']
    
    # ADX (trend strength)
    high = data['High']
    low = data['Low']
    tr1 = high - low
    tr2 = abs(high - close.shift(1))
    tr3 = abs(low - close.shift(1))
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    atr = tr.rolling(14).mean()
    
    plus_dm = high.diff()
    minus_dm = -low.diff()
    plus_dm[plus_dm < 0] = 0
    minus_dm[minus_dm < 0] = 0
    
    plus_di = (plus_dm.rolling(14).mean() / atr) * 100
    minus_di = (minus_dm.rolling(14).mean() / atr) * 100
    
    dx = abs(plus_di - minus_di) / (plus_di + minus_di) * 100
    adx = dx.rolling(14).mean()
    signals['adx'] = adx.iloc[-1]
    signals['trend_strength'] = "STRONG" if adx.iloc[-1] > 25 else "WEAK"
    
    # Overall signal
    score = 0
    if signals['rsi'] < 30:
        score += 1  # Oversold - potential buy
    elif signals['rsi'] > 70:
        score -= 1  # Overbought - potential sell
    
    if signals['macd_histogram'] > 0:
        score += 1  # Bullish momentum
    else:
        score -= 1
    
    if signals['above_sma50']:
        score += 1
    
    if adx.iloc[-1] > 25:
        score += 1  # Strong trend
    
    if score >= 2:
        overall = "BULLISH"
    elif score <= -2:
        overall = "BEARISH"
    else:
        overall = "NEUTRAL"
    
    signals['overall'] = overall
    signals['score'] = score
    
    return signals

def analyze_stock(ticker: str, data: Dict) -> Dict:
    """Full analysis of a single stock"""
    hist = data.get('history')
    info = data.get('info', {})
    
    if hist is None or len(hist) < 30:
        return {"ticker": ticker, "error": data.get('error', "Insufficient data")}
    
    close = hist['Close']
    returns = calculate_returns(close)
    cumulative = (1 + returns).cumprod()
    
    analysis = {
        "ticker": ticker,
        "name": info.get('shortName', ticker),
        "sector": ASX_PORTFOLIO.get(ticker, {}).get('sector', 'Unknown'),
        "current_price": round(close.iloc[-1], 2),
        "previous_close": round(close.iloc[-2], 2) if len(close) > 1 else None,
        "change_pct": round(((close.iloc[-1] - close.iloc[-2]) / close.iloc[-2]) * 100, 2) if len(close) > 1 else 0,
        
        # Risk metrics
        "sharpe_ratio": round(calculate_sharpe(returns), 3),
        "sortino_ratio": round(calculate_sortino(returns), 3),
        "volatility": round(calculate_volatility(returns), 2),
        "max_drawdown": round(calculate_max_drawdown(cumulative), 2),
        "calmar_ratio": round(calculate_calmar(returns, calculate_max_drawdown(cumulative)), 3),
        "var_95": round(calculate_var(returns), 2),
        "cvar_95": round(calculate_cvar(returns), 2),
        
        # Technical
        "technical": technical_signals(hist),
        
        # Performance
        "1m_return": round((close.iloc[-1] / close.iloc[-21] - 1) * 100, 2) if len(close) > 21 else None,
        "3m_return": round((close.iloc[-1] / close.iloc[-63] - 1) * 100, 2) if len(close) > 63 else None,
        "6m_return": round((close.iloc[-1] / close.iloc[-126] - 1) * 100, 2) if len(close) > 126 else None,
        "ytd_return": round((close.iloc[-1] / close.iloc[0] - 1) * 100, 2),
    }
    
    return analysis

def portfolio_metrics(analyses: List[Dict], weights: Dict) -> Dict:
    """Calculate portfolio-level metrics"""
    # Filter successful analyses
    valid = [a for a in analyses if 'error' not in a]
    if not valid:
        return {"error": "No valid analyses"}
    
    # Aggregate returns
    tickers = [a['ticker'] for a in valid]
    returns_data = {}
    
    for a in valid:
        ticker = a['ticker']
        # Fetch fresh data for returns calculation
        try:
            stock = yf.Ticker(f"{ticker}.AX")
            hist = stock.history(period="1y")
            if hist is not None and len(hist) > 30:
                returns_data[ticker] = calculate_returns(hist['Close'])
        except:
            pass
    
    if not returns_data:
        return {"error": "Could not calculate portfolio returns"}
    
    # Weighted portfolio returns
    portfolio_returns = pd.Series(dtype=float)
    for ticker, ret in returns_data.items():
        weight = weights.get(ticker, 0)
        if weight > 0:
            portfolio_returns = portfolio_returns.add(ret * weight, fill_value=0)
    
    if len(portfolio_returns) < 30:
        return {"error": "Insufficient portfolio data"}
    
    # Portfolio metrics
    cum_portfolio = (1 + portfolio_returns).cumprod()
    
    metrics = {
        "portfolio_return": round(portfolio_returns.mean() * 252 * 100, 2),
        "portfolio_volatility": round(calculate_volatility(portfolio_returns), 2),
        "portfolio_sharpe": round(calculate_sharpe(portfolio_returns), 3),
        "portfolio_sortino": round(calculate_sortino(portfolio_returns), 3),
        "portfolio_max_dd": round(calculate_max_drawdown(cum_portfolio), 2),
        "portfolio_calmar": round(calculate_calmar(portfolio_returns, calculate_max_drawdown(cum_portfolio)), 3),
        "portfolio_var_95": round(calculate_var(portfolio_returns), 2),
        "portfolio_cvar_95": round(calculate_cvar(portfolio_returns), 2),
    }
    
    # Sector allocation
    sector_alloc = {}
    for a in valid:
        sector = a.get('sector', 'Unknown')
        sector_alloc[sector] = sector_alloc.get(sector, 0) + weights.get(a['ticker'], 0)
    metrics['sector_allocation'] = {k: round(v * 100, 1) for k, v in sector_alloc.items()}
    
    return metrics

def generate_signals_summary(analyses: List[Dict]) -> str:
    """Generate trading signals summary"""
    bullish = [a for a in analyses if a.get('technical', {}).get('overall') == 'BULLISH']
    bearish = [a for a in analyses if a.get('technical', {}).get('overall') == 'BEARISH']
    neutral = [a for a in analyses if a.get('technical', {}).get('overall') == 'NEUTRAL']
    
    # Sort by score
    bullish.sort(key=lambda x: x.get('technical', {}).get('score', 0), reverse=True)
    bearish.sort(key=lambda x: x.get('technical', {}).get('score', 0))
    
    summary = f"""
📊 Technical Signals Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🟢 BULLISH ({len(bullish)}): {', '.join([a['ticker'] for a in bullish[:5]])}
🔴 BEARISH ({len(bearish)}): {', '.join([a['ticker'] for a in bearish[:5]])}
⚪ NEUTRAL ({len(neutral)}): {', '.join([a['ticker'] for a in neutral[:5]])}

🏆 Top Picks (by technical score):
"""
    for a in bullish[:3]:
        tech = a.get('technical', {})
        summary += f"  • {a['ticker']}: {a.get('name', '')} — RSI: {tech.get('rsi', 'N/A'):.1f}, ADX: {tech.get('adx', 'N/A'):.1f}\n"
    
    return summary

def main():
    parser = argparse.ArgumentParser(description="ASX Portfolio Optimizer")
    parser.add_argument("--tickers", nargs="+", default=list(ASX_PORTFOLIO.keys()),
                        help="Tickers to analyze")
    parser.add_argument("--weights", type=str,
                        help="Comma-separated weights (must sum to 1)")
    parser.add_argument("--rebalance", action="store_true",
                        help="Show rebalancing suggestions")
    parser.add_argument("--signals", action="store_true",
                        help="Show technical signals")
    parser.add_argument("--json", action="store_true",
                        help="Output JSON")
    parser.add_argument("--top", type=int, default=5,
                        help="Number of top stocks to show")
    
    args = parser.parse_args()
    
    print(f"🔄 Fetching data for {len(args.tickers)} stocks...")
    data = fetch_all_data(args.tickers)
    
    # Analyze each stock
    analyses = []
    for ticker in args.tickers:
        if ticker in data:
            analysis = analyze_stock(ticker, data[ticker])
            analyses.append(analysis)
    
    # Parse weights
    weights = {}
    if args.weights:
        try:
            w_list = [float(w) for w in args.weights.split(',')]
            if len(w_list) == len(args.tickers):
                weights = dict(zip(args.tickers, w_list))
            else:
                print("⚠️ Weight count mismatch, using equal weights")
                weights = {t: 1/len(args.tickers) for t in args.tickers}
        except:
            weights = {t: 1/len(args.tickers) for t in args.tickers}
    else:
        weights = {t: ASX_PORTFOLIO.get(t, {}).get('weight', 1/len(args.tickers)) for t in args.tickers}
    
    if args.json:
        result = {
            "timestamp": datetime.now().isoformat(),
            "analyses": analyses,
            "portfolio": portfolio_metrics(analyses, weights)
        }
        print(json.dumps(result, indent=2))
        return
    
    # Display results
    print(f"\n📈 Portfolio Analysis — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)
    
    # Portfolio metrics
    pm = portfolio_metrics(analyses, weights)
    if 'error' not in pm:
        print(f"""
💼 Portfolio Metrics:
   Return:     {pm['portfolio_return']:.1f}% (annualized)
   Volatility: {pm['portfolio_volatility']:.1f}%
   Sharpe:     {pm['portfolio_sharpe']:.2f}
   Sortino:    {pm['portfolio_sortino']:.2f}
   Max DD:     {pm['portfolio_max_dd']:.1f}%
   Calmar:     {pm['portfolio_calmar']:.2f}
   VaR (95%):  {pm['portfolio_var_95']:.2f}%
   
🏛️ Sector Allocation:""")
        for sector, alloc in pm.get('sector_allocation', {}).items():
            print(f"   {sector}: {alloc:.1f}%")
    
    # Top performers
    print(f"\n📊 Top {args.top} Performers (6M):")
    valid = [a for a in analyses if 'error' not in a and a.get('6m_return') is not None]
    valid.sort(key=lambda x: x.get('6m_return', 0), reverse=True)
    for i, a in enumerate(valid[:args.top], 1):
        tech = a.get('technical', {})
        signal = tech.get('overall', 'N/A')[:3].upper()
        print(f"  {i}. {a['ticker']:4s} {a.get('name', '')[:20]:20s} | +{a.get('6m_return', 0):6.1f}% | {signal} | Sharpe: {a.get('sharpe_ratio', 0):.2f}")
    
    # Technical signals
    if args.signals:
        print(generate_signals_summary(analyses))
    
    # Rebalancing suggestions
    if args.rebalance:
        print("\n⚖️ Rebalancing Suggestions:")
        for a in valid:
            current_w = weights.get(a['ticker'], 0)
            target_w = ASX_PORTFOLIO.get(a['ticker'], {}).get('weight', 1/len(args.tickers))
            diff = target_w - current_w
            if abs(diff) > 0.02:
                action = "BUY" if diff > 0 else "SELL"
                print(f"  {action:4s} {a['ticker']}: {diff*100:+.1f}% ({current_w*100:.1f}% → {target_w*100:.1f}%)")

if __name__ == "__main__":
    main()
