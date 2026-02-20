#!/usr/bin/env python3
"""
Stock Tracker Local - 本土化股票追蹤程式
基於技術指標的買賣信號分析
"""

import argparse
import sys
import json
import csv
import os
from datetime import datetime, timedelta
from pathlib import Path

try:
    import yfinance as yf
    import pandas as pd
    import numpy as np
except ImportError:
    print("❌ 錯誤: 缺少必要依賴")
    print("請執行: pip install yfinance pandas numpy")
    sys.exit(1)


# ==================== 配置 ====================
DEFAULT_PERIOD = "6mo"
DEFAULT_INTERVAL = "1d"

# 技術指標參數
CCI_PERIOD = 14
MACD_FAST = 8
MACD_SLOW = 12
MACD_SIGNAL = 26
MA_SHORT = 5
MA_LONG = 20

# 風險管理
DEFAULT_STOP_LOSS = 8.0
DEFAULT_TAKE_PROFIT = 15.0
MAX_POSITION_SIZE = 25.0

# 顏色
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
CYAN = '\033[0;36m'
NC = '\033[0m'

# ==================== 澳洲股票列表 ====================
AUS_STOCKS = {
    # 四大銀行
    'CBA': 'Commonwealth Bank of Australia',
    'ANZ': 'Australia and New Zealand Banking Group',
    'NAB': 'National Australia Bank',
    'WBC': 'Westpac Banking Corp',
    
    # 礦業巨頭
    'BHP': 'BHP Group Limited',
    'RIO': 'Rio Tinto',
    'FMG': 'Fortescue Metals Group',
    'S32': 'South32',
    
    # 能源
    'WDS': 'Woodside Energy',
    'STO': 'Santos',
    'OSH': 'Oil Search',
    
    # 科技/生技
    'CSL': 'CSL Limited',
    'MQG': 'Macquarie Group',
    'GMG': 'Goodman Group',
    'QBE': 'QBE Insurance',
    'IAG': 'Insurance Australia Group',
    'SUN': 'Suncorp Group',
    'TLS': 'Telstra Corporation',
    
    # ASX 200 熱門
    'COL': 'Coles Group',
    'WES': 'Wesfarmers',
    'WOW': 'Woolworths Group',
    'TCL': 'Transurban',
    'CTD': 'Computershare',
    'RMD': 'ResMed Inc.',
    'REA': 'REA Group',
    'SEK': 'SEEK Limited',
    'XJO': 'ASX 200 Index',
}

# 交易所後綴
EXCHANGE_SUFFIX = {
    'AUS': '.AX',      # Australian Securities Exchange
    'US': '',          # US Stocks
    'HK': '.HK',       # Hong Kong Stock Exchange
    'JP': '.T',        # Tokyo Stock Exchange
    'UK': '.L',        # London Stock Exchange
}


def normalize_symbol(symbol, market='US'):
    """標準化股票代號"""
    symbol = symbol.upper().strip()
    
    # 如果已有後綴，直接返回
    if '.' in symbol:
        return symbol
    
    # 澳洲股票
    if market.upper() == 'AUS' or market.upper() == 'AUSTRALIA':
        return symbol + '.AX'
    
    return symbol


# ==================== 指標計算 ====================
def calculate_cci(data, period=14):
    """計算 CCI (Commodity Channel Index)"""
    typical_price = (data['High'] + data['Low'] + data['Close']) / 3
    sma = typical_price.rolling(window=period).mean()
    mean_deviation = typical_price.rolling(window=period).apply(
        lambda x: np.abs(x - x.mean()).mean(), raw=True
    )
    cci = (typical_price - sma) / (0.015 * mean_deviation)
    return cci


def calculate_macd(data, fast=8, slow=12, signal=26):
    """計算 MACD"""
    ema_fast = data['Close'].ewm(span=fast, adjust=False).mean()
    ema_slow = data['Close'].ewm(span=slow, adjust=False).mean()
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()
    histogram = macd_line - signal_line
    return macd_line, signal_line, histogram


def calculate_ma(data, short=5, long=20):
    """計算 MA 交叉"""
    ma_short = data['Close'].rolling(window=short).mean()
    ma_long = data['Close'].rolling(window=long).mean()
    return ma_short, ma_long


def calculate_all_indicators(data):
    """計算所有指標"""
    result = data.copy()
    result['CCI'] = calculate_cci(result, CCI_PERIOD)
    result['MACD'], result['Signal'], result['Histogram'] = calculate_macd(
        result, MACD_FAST, MACD_SLOW, MACD_SIGNAL
    )
    result['MA5'], result['MA20'] = calculate_ma(result, MA_SHORT, MA_LONG)
    return result


# ==================== 信號分析 ====================
def analyze_signal(df, period_name):
    """分析單一週期的信號"""
    if df.empty or len(df) < 30:
        return {
            'period': period_name,
            'error': '數據不足',
            'status': 'unknown'
        }
    
    latest = df.iloc[-1]
    prev = df.iloc[-2] if len(df) > 1 else latest
    
    # CCI 分析
    cci_current = latest['CCI']
    cci_prev = prev['CCI']
    cci_cross_zero = (cci_prev < 0 and cci_current >= 0)
    cci_below_zero = (cci_prev < 0 and cci_current < 0)
    
    # MACD 分析
    macd_current = latest['MACD']
    macd_prev = prev['MACD']
    signal_current = latest['Signal']
    signal_prev = prev['Signal']
    
    macd_cross_zero = (macd_prev < 0 and macd_current >= 0)
    macd_death_cross = (macd_prev > 0 and macd_current <= 0)
    macd_golden_cross = (macd_prev < signal_prev and macd_current >= signal_current)
    macd_below_zero = macd_current < 0
    
    # MA 交叉分析
    ma5_current = latest['MA5']
    ma20_current = latest['MA20']
    ma5_prev = prev['MA5']
    ma20_prev = prev['MA20']
    
    ma_golden_cross = (ma5_prev < ma20_prev and ma5_current >= ma20_current)
    ma_death_cross = (ma5_prev > ma20_prev and ma5_current <= ma20_current)
    ma_bullish = ma5_current > ma20_current
    ma_bearish = ma5_current < ma20_current
    
    # 總結信號
    bullish_count = 0
    bearish_count = 0
    signals = []
    
    # CCI 信號
    if cci_cross_zero:
        bullish_count += 1
        signals.append("CCI 穿越 0 線向上")
    elif cci_below_zero:
        bearish_count += 1
        signals.append("CCI < 0")
    elif cci_current > 0:
        bullish_count += 0.5
        signals.append("CCI > 0 (偏多)")
    
    # MACD 信號
    if macd_cross_zero:
        bullish_count += 1
        signals.append("MACD 穿越 0 線向上")
    elif macd_death_cross:
        bearish_count += 1
        signals.append("MACD 穿越 0 線向下")
    elif macd_golden_cross:
        bullish_count += 1
        signals.append("MACD 金叉")
    elif macd_below_zero:
        bearish_count += 0.5
        signals.append("MACD < 0")
    
    # MA 信號
    if ma_golden_cross:
        bullish_count += 1
        signals.append("MA 金叉")
    elif ma_death_cross:
        bearish_count += 1
        signals.append("MA 死叉")
    elif ma_bullish:
        bullish_count += 0.5
        signals.append("MA5 > MA20 (偏多)")
    elif ma_bearish:
        bearish_count += 0.5
        signals.append("MA5 < MA20 (偏空)")
    
    # 判定狀態
    if bullish_count >= 2.5:
        status = "偏多"
        emoji = "🟢"
    elif bearish_count >= 2.5:
        status = "偏空"
        emoji = "🔴"
    else:
        status = "中性"
        emoji = "🟡"
    
    return {
        'period': period_name,
        'cci': round(cci_current, 2),
        'macd': round(macd_current, 4),
        'signal': round(signal_current, 4),
        'ma5': round(ma5_current, 2),
        'ma20': round(ma20_current, 2),
        'bullish_count': bullish_count,
        'bearish_count': bearish_count,
        'signals': signals,
        'status': status,
        'emoji': emoji
    }


def generate_trade_signal(h4_analysis, daily_analysis):
    """生成綜合交易信號"""
    
    # 買入條件
    buy_conditions = [
        h4_analysis['cci_cross_zero'] if 'cci_cross_zero' in h4_analysis else False,
        h4_analysis['macd_cross_zero'] if 'macd_cross_zero' in h4_analysis else False,
        daily_analysis['cci'] > 0,
        daily_analysis['macd'] > 0,
    ]
    
    # 賣出條件
    sell_conditions = [
        h4_analysis['cci_below_zero'] if 'cci_below_zero' in h4_analysis else False,
        h4_analysis['macd_death_cross'] if 'macd_death_cross' in h4_analysis else False,
        daily_analysis['cci'] < 0,
        daily_analysis['macd'] < 0,
    ]
    
    if all(buy_conditions):
        return 'BUY', '🟢 強烈買入', buy_conditions
    elif all(sell_conditions):
        return 'SELL', '🔴 強烈賣出', sell_conditions
    elif h4_analysis['bullish_count'] >= 2 and daily_analysis['bullish_count'] >= 2:
        return 'BUY', '🟢 潛在買入', buy_conditions
    elif h4_analysis['bearish_count'] >= 2 and daily_analysis['bearish_count'] >= 2:
        return 'SELL', '🔴 潛在賣出', sell_conditions
    else:
        return 'HOLD', '🟡 觀望', []


# ==================== 數據獲取 ====================
def fetch_stock_data(symbol, period="6mo", interval="1d"):
    """從 Yahoo Finance 獲取股票數據"""
    try:
        stock = yf.Ticker(symbol)
        df = stock.history(period=period, interval=interval)
        return df
    except Exception as e:
        print(f"❌ 獲取 {symbol} 數據失敗: {e}")
        return None


def import_from_csv(filepath):
    """從 CSV 匯入股票清單"""
    stocks = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                stocks.append(row)
        return stocks
    except Exception as e:
        print(f"❌ 匯入失敗: {e}")
        return []


# ==================== 輸出 ====================
def print_analysis(symbol, price, h4_result, daily_result, signal, signal_text, stop_loss, take_profit):
    """打印分析結果"""
    
    print(f"\n{'='*70}")
    print(f"📈 股票追蹤報告 - {symbol}")
    print(f"{'='*70}")
    
    # 基本資訊
    print(f"\n📊 基本資訊")
    print(f"─{'─'*60}")
    print(f"當前價格: ${price:.2f}")
    print(f"H4 週期: {h4_result['status']} {h4_result['emoji']}")
    print(f"日線週期: {daily_result['status']} {daily_result['emoji']}")
    
    # H4 詳細
    print(f"\n📈 H4 週期分析")
    print(f"─{'─'*60}")
    print(f"CCI ({CCI_PERIOD}):    {h4_result['cci']:+.1f}  │ 狀態: {h4_result['status']}")
    print(f"MACD:         {h4_result['macd']:+.4f} │ 狀態: {'偏多' if h4_result['bullish_count'] > h4_result['bearish_count'] else '偏空'}")
    print(f"MA 交叉:      {'▲ 上升' if h4_result['ma5'] > h4_result['ma20'] else '▼ 下降'} │ 狀態: {h4_result['status']}")
    if h4_result['signals']:
        print(f"信號: {' │ '.join(h4_result['signals'][-3:])}")
    
    # 日線詳細
    print(f"\n📊 日線分析")
    print(f"─{'─'*60}")
    print(f"CCI ({CCI_PERIOD}):    {daily_result['cci']:+.1f} │ 狀態: {daily_result['status']}")
    print(f"MACD:         {daily_result['macd']:+.4f} │ 狀態: {'偏多' if daily_result['bullish_count'] > daily_result['bearish_count'] else '偏空'}")
    print(f"MA 交叉:      {'▲ 上升' if daily_result['ma5'] > daily_result['ma20'] else '▼ 下降'} │ 狀態: {daily_result['status']}")
    if daily_result['signals']:
        print(f"信號: {' │ '.join(daily_result['signals'][-3:])}")
    
    # 綜合信號
    print(f"\n{'─'*60}")
    print(f"\n🎯 綜合信號")
    print(f"─{'─'*60}")
    print(f"信號狀態: {signal_text}")
    if signal == 'HOLD':
        print("等待更明確的信號")
    
    # 風險管理
    print(f"\n💰 風險管理")
    print(f"─{'─'*60}")
    print(f"建議止損: -{stop_loss:.1f}%  (${price * (1 - stop_loss/100):.2f})")
    print(f"建議止盈: +{take_profit:.1f}%  (${price * (1 + take_profit/100):.2f})")
    
    # 風險報酬比
    rr = take_profit / stop_loss
    print(f"風險報酬比: 1:{rr:.2f}")
    
    print(f"\n{'='*70}\n")


def print_watchlist_report(stocks):
    """打印觀察名單報告"""
    print(f"\n{'='*70}")
    print(f"📋 股票觀察名單")
    print(f"{'='*70}")
    
    for stock in stocks:
        symbol = stock.get('symbol', stock.get('Symbol', '?'))
        name = stock.get('name', stock.get('Name', ''))
        signal = stock.get('signal', '?')
        price = stock.get('price', 0)
        
        emoji = {
            'BUY': '🟢',
            'SELL': '🔴',
            'HOLD': '🟡',
        }.get(signal, '⚪')
        
        print(f"{emoji} {symbol:8s} │ ${price:8.2f} │ {signal:4s} │ {name[:20]}")
    
    print(f"{'='*70}\n")


def scan_trending_stocks(market='AUS', limit=20):
    """自動掃描並排名股票"""
    
    # 選擇股票清單
    if market.upper() == 'AUS':
        stock_list = list(AUS_STOCKS.items())
    else:
        # 預設美國熱門股票
        stock_list = [
            ('AAPL', 'Apple Inc.'), ('GOOGL', 'Alphabet'), ('MSFT', 'Microsoft'),
            ('AMZN', 'Amazon'), ('NVDA', 'NVIDIA'), ('META', 'Meta'),
            ('TSLA', 'Tesla'), ('AMD', 'AMD'), ('NFLX', 'Netflix'),
            ('JPM', 'JPMorgan'), ('V', 'Visa'), ('WMT', 'Walmart'),
        ]
    
    print(f"\n{'='*70}")
    print(f"🔍 自動掃描: {market.upper()} 市場")
    print(f"{'='*70}")
    print(f"正在掃描 {len(stock_list)} 支股票...\n")
    
    results = []
    
    for i, (code, name) in enumerate(stock_list):
        symbol = normalize_symbol(code, market)
        print(f"[{i+1}/{len(stock_list)}] 掃描 {symbol}...", end=" ")
        
        try:
            data = fetch_stock_data(symbol, period="6mo", interval="1d")
            if data is None or data.empty or len(data) < 20:
                print("❌ 數據不足")
                continue
            
            # 計算指標
            data = calculate_all_indicators(data)
            analysis = analyze_signal(data, "日線")
            
            # 計算得分 (bullish_count - bearish_count)
            score = analysis['bullish_count'] - analysis['bearish_count']
            price = data['Close'].iloc[-1]
            
            results.append({
                'symbol': symbol,
                'name': name,
                'price': price,
                'signal': analysis['status'],
                'emoji': analysis['emoji'],
                'score': score,
                'cci': analysis['cci'],
                'macd': analysis['macd'],
            })
            
            print(f"{analysis['emoji']} {analysis['status']}")
            
        except Exception as e:
            print(f"❌ {e}")
    
    if not results:
        print("❌ 沒有找到有效數據")
        return
    
    # 按分數排序
    results.sort(key=lambda x: x['score'], reverse=True)
    
    print(f"\n{'='*70}")
    print(f"📈 掃描結果排名")
    print(f"{'='*70}")
    
    # Top 5 買入
    buys = [r for r in results if r['score'] >= 1]
    if buys[:5]:
        print(f"\n🟢 **Top 買入 ({len(buys)}支)**")
        print(f"{'代號':<10s} │ {'價格':<10s} │ {'CCI':<10s} │ {'MACD':<10s}")
        print("-" * 50)
        for r in buys[:5]:
            print(f"{r['symbol']:<10s} │ ${r['price']:<9.2f} │ {r['cci']:>+8.1f} │ {r['macd']:>+8.4f}")
    
    # Top 5 賣出
    sells = [r for r in results if r['score'] <= -1]
    if sells[:5]:
        print(f"\n🔴 **Top 賣出 ({len(sells)}支)**")
        print(f"{'代號':<10s} │ {'價格':<10s} │ {'CCI':<10s} │ {'MACD':<10s}")
        print("-" * 50)
        for r in sells[:5]:
            print(f"{r['symbol']:<10s} │ ${r['price']:<9.2f} │ {r['cci']:>+8.1f} │ {r['macd']:>+8.4f}")
    
    # 中性
    neutrals = [r for r in results if -1 < r['score'] < 1]
    if neutrals[:5]:
        print(f"\n🟡 **觀望 ({len(neutrals)}支)**")
        print(f"{'代號':<10s} │ {'價格':<10s} │ {'CCI':<10s} │ {'MACD':<10s}")
        print("-" * 50)
        for r in neutrals[:5]:
            print(f"{r['symbol']:<10s} │ ${r['price']:<9.2f} │ {r['cci']:>+8.1f} │ {r['macd']:>+8.4f}")
    
    print(f"\n{'='*70}\n")


# ==================== 主程式 ====================
def main():
    parser = argparse.ArgumentParser(
        description="Stock Tracker Local - 本土化股票追蹤程式"
    )
    parser.add_argument(
        '--symbol', '-s',
        help='股票代號 (例如: AAPL)'
    )
    parser.add_argument(
        '--watchlist', '-w',
        help='股票清單，用逗號分隔 (例如: AAPL,GOOGL,MSFT)'
    )
    parser.add_argument(
        '--period', '-p',
        default=DEFAULT_PERIOD,
        help=f'數據週期 (預設: {DEFAULT_PERIOD})'
    )
    parser.add_argument(
        '--interval', '-i',
        default=DEFAULT_INTERVAL,
        help=f'K線週期間隔 (預設: {DEFAULT_INTERVAL})'
    )
    parser.add_argument(
        '--report', '-r',
        action='store_true',
        help='產生詳細報告'
    )
    parser.add_argument(
        '--import', '-m',
        dest='import_file',
        help='從 CSV 匯入股票清單'
    )
    parser.add_argument(
        '--stop-loss',
        type=float,
        default=DEFAULT_STOP_LOSS,
        help=f'止損百分比 (預設: {DEFAULT_STOP_LOSS}%)'
    )
    parser.add_argument(
        '--take-profit',
        type=float,
        default=DEFAULT_TAKE_PROFIT,
        help=f'止盈百分比 (預設: {DEFAULT_TAKE_PROFIT}%)'
    )
    parser.add_argument(
        '--output', '-o',
        help='輸出到檔案'
    )
    parser.add_argument(
        '--aus', '-a',
        action='store_true',
        help='澳洲股票 (自動添加 .AX 後綴)'
    )
    parser.add_argument(
        '--list-aus',
        action='store_true',
        help='列出常用澳洲股票'
    )
    parser.add_argument(
        '--trending', '-t',
        action='store_true',
        help='自動掃描並排名所有股票'
    )
    
    args = parser.parse_args()
    
    # 列出澳洲股票
    if args.list_aus:
        print("\n🇦🇺 常用澳洲股票 (ASX)")
        print("=" * 60)
        print(f"{'代號':<8s} │ {'名稱':<40s}")
        print("-" * 60)
        for code, name in AUS_STOCKS.items():
            print(f"{code:<8s} │ {name:<40s}")
        print("=" * 60)
        print("\n使用方法:")
        print("  python3 tracker.py --aus CBA      # 分析 CBA")
        print("  python3 tracker.py --aus BHP,RIO  # 分析 BHP 和 RIO")
        return
    
    # 重新導向輸出
    if args.output:
        print(f"💾 輸出將保存到: {args.output}")
        # TODO: 實現檔案輸出
    
    # 處理觀察名單
    if args.import_file:
        stocks = import_from_csv(args.import_file)
        if stocks:
            print_watchlist_report(stocks)
        return
    
    # 處理 watchlist 參數
    if args.watchlist:
        symbols = [s.strip() for s in args.watchlist.split(',')]
        for symbol in symbols:
            # 如果是澳洲模式
            if args.aus:
                symbol = normalize_symbol(symbol, 'AUS')
            analyze_stock(symbol, args.period, args.interval, args.report, args.stop_loss, args.take_profit)
        return
    
    # 自動 Trending 掃描
    if args.trending:
        scan_trending_stocks(market='AUS' if args.aus else 'US', limit=20)
        return
    
    # 處理單一股票
    if args.symbol:
        # 如果是澳洲模式
        if args.aus:
            symbol = normalize_symbol(args.symbol, 'AUS')
        else:
            symbol = args.symbol
        analyze_stock(symbol, args.period, args.interval, args.report, args.stop_loss, args.take_profit)
    else:
        parser.print_help()


def analyze_stock(symbol, period, interval, report=False, stop_loss=8.0, take_profit=15.0):
    """分析單一股票"""
    
    print(f"\n🔍 正在分析: {symbol}")
    
    # 獲取數據
    # 日線數據
    daily_data = fetch_stock_data(symbol, period=period, interval="1d")
    if daily_data is None or daily_data.empty:
        print(f"❌ 無法獲取 {symbol} 的數據")
        return
    
    # H4 數據（使用 1h 間隔模擬）
    h4_data = fetch_stock_data(symbol, period="3mo", interval="1h")
    
    # 計算指標
    daily_with_indicators = calculate_all_indicators(daily_data)
    
    if h4_data is not None and not h4_data.empty:
        h4_with_indicators = calculate_all_indicators(h4_data)
        h4_result = analyze_signal(h4_with_indicators, "H4")
    else:
        h4_result = {
            'period': 'H4',
            'cci': daily_result['cci'] if 'daily_result' in dir() else 0,
            'macd': 0,
            'ma5': 0,
            'ma20': 0,
            'bullish_count': 0,
            'bearish_count': 0,
            'signals': ['H4 數據不可用'],
            'status': '未知',
            'emoji': '⚪'
        }
    
    daily_result = analyze_signal(daily_with_indicators, "日線")
    
    # 獲取當前價格
    price = daily_data['Close'].iloc[-1] if not daily_data.empty else 0
    
    # 生成信號
    h4_cross = any('穿越 0 線' in s for s in h4_result['signals'])
    daily_bullish = daily_result['cci'] > 0 and daily_result['macd'] > 0
    
    if h4_cross and daily_bullish:
        signal = 'BUY'
        signal_text = '🟢 潛在買入'
    elif any('穿越 0 線向下' in s for s in h4_result['signals']) and daily_result['cci'] < 0:
        signal = 'SELL'
        signal_text = '🔴 潛在賣出'
    else:
        signal = 'HOLD'
        signal_text = '🟡 觀望'
    
    # 輸出
    print_analysis(symbol, price, h4_result, daily_result, signal, signal_text, stop_loss, take_profit)


if __name__ == "__main__":
    main()
