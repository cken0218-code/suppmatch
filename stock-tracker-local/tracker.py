#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
股票追蹤程式 - Stock Tracker Local
=====================================

基於技術指標的多周期股票追蹤系統
支援 H4 (4小時) 和 日線 雙周期確認

技術指標：
- CCI (Commodity Channel Index) - 順勢指標
- MACD (Moving Average Convergence Divergence) - 指數平滑異同移動平均線
- MA Crossover (Moving Average) - 移動平均線交叉

Author: OpenClaw
Version: 1.0.0
License: MIT
"""

import sys
import argparse
import csv
import json
import logging
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

try:
    import yfinance as yf
    import pandas as pd
    import numpy as np
except ImportError as e:
    print(f"錯誤: 缺少必要依賴，請先執行: pip install -r requirements.txt")
    print(f"具體錯誤: {e}")
    sys.exit(1)

# ==================== 配置常量 ====================

# 技術指標參數
CCI_PERIOD = 14           # CCI 週期
CCI_OVERBOUGHT = 100      # CCI 超買閾值
CCI_OVERSOLD = -100       # CCI 超賣閾值

MACD_FAST = 12            # MACD 快速 EMA 週期
MACD_SLOW = 26            # MACD 慢速 EMA 週期
MACD_SIGNAL = 9           # MACD 訊號線週期

MA_SHORT = 5              # 短期 MA 週期
MA_LONG = 20              # 長期 MA 週期

# 多周期確認權重
H4_WEIGHT = 0.6            # H4 週期權重
DAILY_WEIGHT = 0.4        # 日線週期權重

# 止盈止損參數
TAKE_PROFIT_PERCENT = 5.0     # 止盈百分比
STOP_LOSS_PERCENT = 3.0       # 止損百分比
ATR_MULTIPLIER = 2.0          # ATR 倍數 (用於動態止損)

# 數據週期 (月)
DEFAULT_PERIOD = "6mo"        # 預設數據週期
MAX_PERIOD = "2y"             # 最大數據週期

# 時間框架映射
TIMEFRAMES = {
    "H4": "4h",
    "DAILY": "1d",
    "1D": "1d",
    "4H": "4h"
}

# 日誌配置
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_FILE = "stock_tracker.log"

# 輸出編碼
OUTPUT_ENCODING = "utf-8"


# ==================== 日誌設置 ====================

def setup_logging(log_level: int = logging.INFO) -> logging.Logger:
    """
    配置日誌系統
    
    Args:
        log_level: 日誌級別
        
    Returns:
        配置後的 logger 實例
    """
    logger = logging.getLogger("StockTracker")
    logger.setLevel(log_level)
    
    # 清除現有處理器
    logger.handlers.clear()
    
    # 控制台處理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_formatter = logging.Formatter(LOG_FORMAT)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    # 文件處理器
    try:
        file_handler = logging.FileHandler(LOG_FILE, encoding=OUTPUT_ENCODING)
        file_handler.setLevel(log_level)
        file_formatter = logging.Formatter(LOG_FORMAT)
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
    except (IOError, OSError) as e:
        logger.warning(f"無法創建日誌文件: {e}")
    
    return logger


# ==================== 技術指標計算 ====================

def calculate_ma(data: pd.Series, period: int) -> pd.Series:
    """
    計算移動平均線
    
    Args:
        data: 價格數據
        period: MA 週期
        
    Returns:
        MA 序列
    """
    return data.rolling(window=period).mean()


def calculate_ema(data: pd.Series, period: int) -> pd.Series:
    """
    計算指數移動平均線
    
    Args:
        data: 價格數據
        period: EMA 週期
        
    Returns:
        EMA 序列
    """
    return data.ewm(span=period, adjust=False).mean()


def calculate_macd(
    data: pd.Series, 
    fast_period: int = MACD_FAST, 
    slow_period: int = MACD_SLOW, 
    signal_period: int = MACD_SIGNAL
) -> Tuple[pd.Series, pd.Series, pd.Series]:
    """
    計算 MACD
    
    Args:
        data: 價格數據
        fast_period: 快速 EMA 週期
        slow_period: 慢速 EMA 週期
        signal_period: 訊號線週期
        
    Returns:
        (MACD線, 訊號線, MACD柱狀圖)
    """
    ema_fast = calculate_ema(data, fast_period)
    ema_slow = calculate_ema(data, slow_period)
    
    macd_line = ema_fast - ema_slow
    signal_line = calculate_ema(macd_line, signal_period)
    macd_histogram = macd_line - signal_line
    
    return macd_line, signal_line, macd_histogram


def calculate_cci(
    high: pd.Series, 
    low: pd.Series, 
    close: pd.Series, 
    period: int = CCI_PERIOD
) -> pd.Series:
    """
    計算 CCI (Commodity Channel Index)
    
    Args:
        high: 最高價
        low: 最低價
        close: 收盤價
        period: CCI 週期
        
    Returns:
        CCI 序列
    """
    typical_price = (high + low + close) / 3
    sma = typical_price.rolling(window=period).mean()
    mean_deviation = typical_price.rolling(window=period).apply(
        lambda x: np.abs(x - x.mean()).mean(), 
        raw=True
    )
    
    cci = (typical_price - sma) / (0.015 * mean_deviation)
    return cci


def calculate_atr(
    high: pd.Series, 
    low: pd.Series, 
    close: pd.Series, 
    period: int = 14
) -> pd.Series:
    """
    計算 ATR (Average True Range)
    
    Args:
        high: 最高價
        low: 最低價
        close: 收盤價
        period: ATR 週期
        
    Returns:
        ATR 序列
    """
    tr1 = high - low
    tr2 = abs(high - close.shift(1))
    tr3 = abs(low - close.shift(1))
    
    true_range = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    atr = true_range.rolling(window=period).mean()
    
    return atr


# ==================== 信號分析 ====================

def analyze_ma_crossover(ma_short: pd.Series, ma_long: pd.Series) -> int:
    """
    分析 MA 交叉信號
    
    Args:
        ma_short: 短期 MA
        ma_long: 長期 MA
        
    Returns:
        信號值: 1 (買入), -1 (賣出), 0 (無信號)
    """
    if len(ma_short) < 2 or len(ma_long) < 2:
        return 0
    
    # 檢查最新兩個點的交叉
    prev_short = ma_short.iloc[-2]
    prev_long = ma_long.iloc[-2]
    curr_short = ma_short.iloc[-1]
    curr_long = ma_long.iloc[-1]
    
    # 黃金交叉 (買入)
    if prev_short <= prev_long and curr_short > curr_long:
        return 1
    
    # 死亡交叉 (賣出)
    if prev_short >= prev_long and curr_short < curr_long:
        return -1
    
    return 0


def analyze_macd_signal(
    macd_line: pd.Series, 
    signal_line: pd.Series, 
    histogram: pd.Series
) -> int:
    """
    分析 MACD 信號
    
    Args:
        macd_line: MACD 線
        signal_line: 訊號線
        histogram: MACD 柱狀圖
        
    Returns:
        信號值: 1 (買入), -1 (賣出), 0 (無信號)
    """
    if len(macd_line) < 2 or len(signal_line) < 2:
        return 0
    
    # 檢查 MACD 與訊號線的交叉
    prev_macd = macd_line.iloc[-2]
    prev_signal = signal_line.iloc[-2]
    curr_macd = macd_line.iloc[-1]
    curr_signal = signal_line.iloc[-1]
    
    #  MACD 上穿訊號線 (買入)
    if prev_macd <= prev_signal and curr_macd > curr_signal:
        return 1
    
    #  MACD 下穿訊號線 (賣出)
    if prev_macd >= prev_signal and curr_macd < curr_signal:
        return -1
    
    # 檢查柱狀圖方向 (輔助信號)
    curr_hist = histogram.iloc[-1]
    prev_hist = histogram.iloc[-2] if len(histogram) > 2 else 0
    
    # 柱狀圖由負轉正 (潛在買入)
    if prev_hist < 0 and curr_hist > 0:
        return 1
    
    # 柱狀圖由正轉負 (潛在賣出)
    if prev_hist > 0 and curr_hist < 0:
        return -1
    
    return 0


def analyze_cci(cci: pd.Series) -> int:
    """
    分析 CCI 信號
    
    Args:
        cci: CCI 序列
        
    Returns:
        信號值: 1 (買入), -1 (賣出), 0 (無信號)
    """
    if len(cci) < 1:
        return 0
    
    curr_cci = cci.iloc[-1]
    prev_cci = cci.iloc[-2] if len(cci) > 2 else curr_cci
    
    # 超買區域 + CCI 向下轉折 (潛在賣出)
    if curr_cci > CCI_OVERBOUGHT and prev_cci > curr_cci:
        return -1
    
    # 超賣區域 + CCI 向上轉折 (潛在買入)
    if curr_cci < CCI_OVERSOLD and prev_cci < curr_cci:
        return 1
    
    # 在超買區域 (賣出信號)
    if curr_cci > CCI_OVERBOUGHT:
        return -1
    
    # 在超賣區域 (買入信號)
    if curr_cci < CCI_OVERSOLD:
        return 1
    
    return 0


def calculate_signal_strength(
    ma_signal: int, 
    macd_signal: int, 
    cci_signal: int
) -> Tuple[int, str, float]:
    """
    計算綜合信號強度
    
    Args:
        ma_signal: MA 交叉信號
        macd_signal: MACD 信號
        cci_signal: CCI 信號
        
    Returns:
        (綜合信號, 信號描述, 信號強度百分比)
    """
    # 權重分配
    weights = {
        "ma": 0.35,
        "macd": 0.40,
        "cci": 0.25
    }
    
    weighted_score = (
        ma_signal * weights["ma"] + 
        macd_signal * weights["macd"] + 
        cci_signal * weights["cci"]
    )
    
    # 判斷信號
    if weighted_score >= 0.5:
        signal = 1
        description = "強烈買入"
    elif weighted_score >= 0.2:
        signal = 1
        description = "買入"
    elif weighted_score <= -0.5:
        signal = -1
        description = "強烈賣出"
    elif weighted_score <= -0.2:
        signal = -1
        description = "賣出"
    else:
        signal = 0
        description = "觀望"
    
    # 計算強度百分比
    strength = abs(weighted_score) * 100
    
    return signal, description, strength


def multi_timeframe_confirmation(
    h4_analysis: Dict, 
    daily_analysis: Dict
) -> Tuple[int, str, float]:
    """
    多周期確認
    
    Args:
        h4_analysis: H4 週期分析結果
        daily_analysis: 日線週期分析結果
        
    Returns:
        (綜合信號, 信號描述, 信號強度)
    """
    h4_signal = h4_analysis.get("signal", 0)
    daily_signal = daily_analysis.get("signal", 0)
    
    h4_strength = h4_analysis.get("strength", 0)
    daily_strength = daily_analysis.get("strength", 0)
    
    # 加權計算
    weighted_signal = (
        h4_signal * h4_strength * H4_WEIGHT + 
        daily_signal * daily_strength * DAILY_WEIGHT
    ) / 100
    
    # 判斷確認
    if h4_signal == daily_signal and h4_signal != 0:
        # 兩個週期信號一致
        if abs(weighted_signal) >= 0.5:
            description = f"{'買入' if weighted_signal > 0 else '賣出'} (雙周期確認)"
        else:
            description = f"{'買入' if weighted_signal > 0 else '賣出'} (初步確認)"
    elif h4_signal != 0 and daily_signal == 0:
        description = f"{'買入' if h4_signal > 0 else '賣出'} (H4 週期信號)"
    elif h4_signal == 0 and daily_signal != 0:
        description = f"{'買入' if daily_signal > 0 else '賣出'} (日線週期信號)"
    else:
        description = "觀望 (無明確信號)"
        weighted_signal = 0
    
    strength = min(abs(weighted_signal) * 100, 100)
    
    return int(np.sign(weighted_signal)), description, strength


# ==================== 數據處理 ====================

def fetch_stock_data(
    symbol: str, 
    timeframe: str = "4h", 
    period: str = DEFAULT_PERIOD,
    logger: Optional[logging.Logger] = None
) -> Optional[pd.DataFrame]:
    """
    獲取股票數據
    
    Args:
        symbol: 股票代碼 (如 AAPL, 2330.TW)
        timeframe: 時間框架 (4h, 1d)
        period: 數據週期
        logger: 日誌實例
        
    Returns:
        股票數據 DataFrame 或 None
    """
    if logger is None:
        logger = logging.getLogger("StockTracker")
    
    try:
        # 添加正確的市場後綴
        if not symbol.endswith(".TW") and not symbol.endswith(".HK"):
            # 美股不需要後綴
            ticker = yf.Ticker(symbol)
        else:
            ticker = yf.Ticker(symbol)
        
        # 獲取歷史數據
        df = ticker.history(period=period, interval=timeframe)
        
        if df.empty:
            logger.warning(f"無法獲取 {symbol} 的數據")
            return None
        
        # 重置索引
        df = df.reset_index()
        
        # 確保列名正確
        df.columns = df.columns.str.lower()
        
        logger.info(f"成功獲取 {symbol} {timeframe} 數據，共 {len(df)} 條記錄")
        
        return df
        
    except Exception as e:
        logger.error(f"獲取 {symbol} 數據時出錯: {e}")
        return None


def load_csv_data(
    file_path: str, 
    logger: Optional[logging.Logger] = None
) -> Optional[pd.DataFrame]:
    """
    從 CSV 載入數據
    
    Args:
        file_path: CSV 文件路徑
        logger: 日誌實例
        
    Returns:
        DataFrame 或 None
    """
    if logger is None:
        logger = logging.getLogger("StockTracker")
    
    try:
        # 檢查文件是否存在
        if not os.path.exists(file_path):
            logger.error(f"文件不存在: {file_path}")
            return None
        
        # 讀取 CSV
        df = pd.read_csv(file_path)
        
        # 標準化列名
        df.columns = df.columns.str.lower()
        
        # 確保必要的列存在
        required_columns = ['open', 'high', 'low', 'close', 'volume', 'date']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            logger.error(f"CSV 缺少必要列: {missing_columns}")
            return None
        
        logger.info(f"成功從 CSV 載入 {len(df)} 條記錄")
        
        return df
        
    except Exception as e:
        logger.error(f"讀取 CSV 時出錯: {e}")
        return None


def analyze_stock_data(
    df: pd.DataFrame, 
    logger: Optional[logging.Logger] = None
) -> Dict[str, Any]:
    """
    分析股票數據
    
    Args:
        df: 股票數據 DataFrame
        logger: 日誌實例
        
    Returns:
        分析結果字典
    """
    if logger is None:
        logger = logging.getLogger("StockTracker")
    
    try:
        # 確保必要的列存在
        required = ['open', 'high', 'low', 'close', 'volume']
        if not all(col in df.columns for col in required):
            raise ValueError(f"數據缺少必要列: {required}")
        
        # 提取價格數據
        close = df['close']
        high = df['high']
        low = df['low']
        open_price = df['open']
        
        # 計算技術指標
        ma_short = calculate_ma(close, MA_SHORT)
        ma_long = calculate_ma(close, MA_LONG)
        
        macd_line, signal_line, macd_histogram = calculate_macd(close)
        
        cci = calculate_cci(high, low, close)
        
        atr = calculate_atr(high, low, close)
        
        # 分析各指標信號
        ma_signal = analyze_ma_crossover(ma_short, ma_long)
        macd_signal = analyze_macd_signal(macd_line, signal_line, macd_histogram)
        cci_signal = analyze_cci(cci)
        
        # 計算綜合信號
        signal, description, strength = calculate_signal_strength(
            ma_signal, macd_signal, cci_signal
        )
        
        # 計算止盈止損
        current_price = close.iloc[-1]
        atr_value = atr.iloc[-1]
        
        take_profit = current_price * (1 + TAKE_PROFIT_PERCENT / 100)
        stop_loss = current_price * (1 - STOP_LOSS_PERCENT / 100)
        dynamic_stop_loss = current_price - atr_value * ATR_MULTIPLIER
        
        # 選擇較嚴格的止損
        final_stop_loss = max(stop_loss, dynamic_stop_loss)
        
        # 風險回報比
        risk = current_price - final_stop_loss
        reward = take_profit - current_price
        rr_ratio = reward / risk if risk > 0 else 0
        
        # 獲取最新指標值
        latest_indicators = {
            "price": current_price,
            "ma_short": ma_short.iloc[-1],
            "ma_long": ma_long.iloc[-1],
            "macd": macd_line.iloc[-1],
            "macd_signal": signal_line.iloc[-1],
            "macd_hist": macd_histogram.iloc[-1],
            "cci": cci.iloc[-1],
            "atr": atr_value
        }
        
        result = {
            "signal": signal,
            "description": description,
            "strength": strength,
            "indicators": latest_indicators,
            "take_profit": take_profit,
            "stop_loss": final_stop_loss,
            "rr_ratio": rr_ratio,
            "data_points": len(df),
            "timestamp": datetime.now().isoformat()
        }
        
        logger.info(f"分析完成: 信號={description}, 強度={strength:.1f}%")
        
        return result
        
    except Exception as e:
        logger.error(f"分析數據時出錯: {e}")
        raise


# ==================== 輸出格式化 ====================

def format_signal_output(
    symbol: str, 
    h4_result: Dict, 
    daily_result: Dict,
    multi_tf_result: Tuple
) -> str:
    """
    格式化信號輸出
    
    Args:
        symbol: 股票代碼
        h4_result: H4 分析結果
        daily_result: 日線分析結果
        multi_tf_result: 多周期確認結果
        
    Returns:
        格式化後的信號字符串
    """
    signal, description, strength = multi_tf_result
    
    # 符號 Emoji
    signal_emoji = {
        1: "🟢",
        -1: "🔴",
        0: "⚪"
    }
    
    output = []
    output.append("=" * 60)
    output.append(f"📈 股票分析報告 - {symbol}")
    output.append("=" * 60)
    output.append(f"\n{signal_emoji.get(signal, '⚪')} 綜合信號: {description}")
    output.append(f"📊 信號強度: {strength:.1f}%")
    
    output.append("\n" + "-" * 60)
    output.append("H4 (4小時) 週期分析:")
    output.append(f"  信號: {h4_result.get('description', 'N/A')}")
    output.append(f"  強度: {h4_result.get('strength', 0):.1f}%")
    if 'indicators' in h4_result:
        ind = h4_result['indicators']
        output.append(f"  MA(5): {ind.get('ma_short', 0):.2f}")
        output.append(f"  MA(20): {ind.get('ma_long', 0):.2f}")
        output.append(f"  CCI: {ind.get('cci', 0):.2f}")
    
    output.append("\n" + "-" * 60)
    output.append("日線 (Daily) 週期分析:")
    output.append(f"  信號: {daily_result.get('description', 'N/A')}")
    output.append(f"  強度: {daily_result.get('strength', 0):.1f}%")
    if 'indicators' in daily_result:
        ind = daily_result['indicators']
        output.append(f"  MA(5): {ind.get('ma_short', 0):.2f}")
        output.append(f"  MA(20): {ind.get('ma_long', 0):.2f}")
        output.append(f"  CCI: {ind.get('cci', 0):.2f}")
    
    output.append("\n" + "-" * 60)
    output.append("💰 交易建議:")
    output.append(f"  當前價格: {h4_result.get('indicators', {}).get('price', 0):.2f}")
    output.append(f"  止盈 (TP): {h4_result.get('take_profit', 0):.2f} (+{TAKE_PROFIT_PERCENT}%)")
    output.append(f"  止損 (SL): {h4_result.get('stop_loss', 0):.2f} (-{STOP_LOSS_PERCENT}%)")
    output.append(f"  風險回報比: {h4_result.get('rr_ratio', 0):.2f}R")
    
    output.append("\n" + "-" * 60)
    output.append(f"分析時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    output.append("=" * 60)
    
    return "\n".join(output)


def format_report_output(results: List[Dict]) -> str:
    """
    格式化報告輸出
    
    Args:
        results: 多個股票分析結果
        
    Returns:
        格式化後的報告字符串
    """
    output = []
    output.append("=" * 80)
    output.append("📊 股票追蹤信號報告")
    output.append("=" * 80)
    output.append(f"\n生成時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    output.append(f"股票數量: {len(results)}")
    output.append("\n" + "-" * 80)
    
    # 按信號強度排序
    sorted_results = sorted(results, key=lambda x: x.get("strength", 0), reverse=True)
    
    for i, result in enumerate(sorted_results, 1):
        symbol = result.get("symbol", "Unknown")
        signal = result.get("signal", 0)
        description = result.get("description", "N/A")
        strength = result.get("strength", 0)
        price = result.get("h4_indicators", {}).get("price", 0)
        
        signal_emoji = {1: "🟢 買入", -1: "🔴 賣出", 0: "⚪ 觀望"}
        
        output.append(f"\n{i}. {symbol}")
        output.append(f"   信號: {signal_emoji.get(signal, '⚪ 觀望')} - {description}")
        output.append(f"   強度: {strength:.1f}%")
        output.append(f"   價格: {price:.2f}")
        output.append(f"   止盈: {result.get('take_profit', 0):.2f}")
        output.append(f"   止損: {result.get('stop_loss', 0):.2f}")
    
    output.append("\n" + "=" * 80)
    output.append("備註: 此報告僅供參考，不構成投資建議。")
    output.append("=" * 80)
    
    return "\n".join(output)


# ==================== 主程式 ====================

class StockTracker:
    """股票追蹤器主類"""
    
    def __init__(self, verbose: bool = False):
        """
        初始化股票追蹤器
        
        Args:
            verbose: 詳細輸出模式
        """
        self.logger = setup_logging(
            logging.DEBUG if verbose else logging.INFO
        )
        self.results_history = []
    
    def analyze_symbol(
        self, 
        symbol: str, 
        use_csv: bool = False, 
        csv_path: Optional[str] = None
    ) -> Optional[Dict]:
        """
        分析單支股票
        
        Args:
            symbol: 股票代碼
            use_csv: 是否使用 CSV 數據
            csv_path: CSV 文件路徑
            
        Returns:
            分析結果字典
        """
        self.logger.info(f"開始分析: {symbol}")
        
        try:
            if use_csv and csv_path:
                # 使用 CSV 數據
                df = load_csv_data(csv_path, self.logger)
                if df is None:
                    return None
                
                h4_result = analyze_stock_data(df, self.logger)
                daily_result = h4_result  # CSV 數據可能只有一種週期
                
            else:
                # 使用 yfinance 獲取數據
                # H4 數據
                h4_df = fetch_stock_data(symbol, "4h", DEFAULT_PERIOD, self.logger)
                if h4_df is None:
                    return None
                
                # 日線數據
                daily_df = fetch_stock_data(symbol, "1d", DEFAULT_PERIOD, self.logger)
                if daily_df is None:
                    daily_df = h4_df.copy()  # 降級使用 H4 數據
                
                # 分析兩個週期
                h4_result = analyze_stock_data(h4_df, self.logger)
                daily_result = analyze_stock_data(daily_df, self.logger)
            
            # 多周期確認
            multi_tf_result = multi_timeframe_confirmation(h4_result, daily_result)
            
            # 組合結果
            result = {
                "symbol": symbol,
                "signal": multi_tf_result[0],
                "description": multi_tf_result[1],
                "strength": multi_tf_result[2],
                "h4_result": h4_result,
                "daily_result": daily_result,
                "h4_indicators": h4_result.get("indicators", {}),
                "take_profit": h4_result.get("take_profit", 0),
                "stop_loss": h4_result.get("stop_loss", 0),
                "rr_ratio": h4_result.get("rr_ratio", 0),
                "timestamp": datetime.now().isoformat()
            }
            
            # 保存到歷史記錄
            self.results_history.append(result)
            
            # 輸出結果
            output = format_signal_output(symbol, h4_result, daily_result, multi_tf_result)
            print(output)
            
            return result
            
        except Exception as e:
            self.logger.error(f"分析 {symbol} 時出錯: {e}")
            return None
    
    def analyze_watchlist(
        self, 
        symbols: List[str],
        output_file: Optional[str] = None
    ) -> List[Dict]:
        """
        分析觀察清單中的多支股票
        
        Args:
            symbols: 股票代碼列表
            output_file: 輸出文件路徑
            
        Returns:
            分析結果列表
        """
        self.logger.info(f"開始分析觀察清單: {symbols}")
        
        results = []
        
        for symbol in symbols:
            self.logger.info(f"分析 {symbol} ({len(results)+1}/{len(symbols)})")
            
            result = self.analyze_symbol(symbol.strip())
            if result:
                results.append(result)
            
            # 避免 API 請求過快
            import time
            time.sleep(0.5)
        
        # 生成報告
        if results:
            report = format_report_output(results)
            print("\n" + report)
            
            # 保存到文件
            if output_file:
                try:
                    with open(output_file, 'w', encoding=OUTPUT_ENCODING) as f:
                        f.write(report)
                    self.logger.info(f"報告已保存到: {output_file}")
                except Exception as e:
                    self.logger.error(f"保存報告失敗: {e}")
        
        return results
    
    def export_results(
        self, 
        file_path: str, 
        format: str = "json"
    ) -> bool:
        """
        導出結果
        
        Args:
            file_path: 文件路徑
            format: 導出格式 (json, csv)
            
        Returns:
            是否成功
        """
        try:
            if format == "json":
                with open(file_path, 'w', encoding=OUTPUT_ENCODING) as f:
                    json.dump(self.results_history, f, ensure_ascii=False, indent=2)
            
            elif format == "csv":
                import csv
                with open(file_path, 'w', encoding=OUTPUT_ENCODING, newline='') as f:
                    if self.results_history:
                        writer = csv.DictWriter(f, fieldnames=self.results_history[0].keys())
                        writer.writeheader()
                        writer.writerows(self.results_history)
            
            else:
                self.logger.error(f"不支持的格式: {format}")
                return False
            
            self.logger.info(f"結果已導出到: {file_path}")
            return True
            
        except Exception as e:
            self.logger.error(f"導出失敗: {e}")
            return False


# ==================== 命令行介面 ====================

def main():
    """主函數"""
    parser = argparse.ArgumentParser(
        description="股票追蹤程式 - 基於技術指標的多周期分析系統",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用範例:
  # 追蹤單支股票
  python tracker.py --symbol=AAPL
  
  # 追蹤多支股票
  python tracker.py --watchlist="AAPL,GOOGL,MSFT"
  
  # 使用 CSV 數據
  python tracker.py --symbol=MY_STOCK --csv --file=my_data.csv
  
  # 產生信號報告
  python tracker.py --watchlist="AAPL,MSFT" --report --output=signals.txt
  
  # 導出 JSON 結果
  python tracker.py --symbol=AAPL --export=results.json
        """
    )
    
    # 基本參數
    parser.add_argument(
        "--symbol", "-s",
        help="股票代碼 (如 AAPL, 2330.TW)"
    )
    parser.add_argument(
        "--watchlist", "-w",
        help="觀察清單，多個股票用逗號分隔 (如 AAPL,GOOGL,MSFT)"
    )
    parser.add_argument(
        "--period", "-p",
        default=DEFAULT_PERIOD,
        choices=["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"],
        help=f"數據週期 (預設: {DEFAULT_PERIOD})"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="詳細輸出模式"
    )
    
    # CSV 模式
    parser.add_argument(
        "--csv",
        action="store_true",
        help="使用本地 CSV 數據"
    )
    parser.add_argument(
        "--file", "-f",
        help="CSV 文件路徑"
    )
    
    # 報告模式
    parser.add_argument(
        "--report", "-r",
        action="store_true",
        help="產生信號報告"
    )
    parser.add_argument(
        "--output", "-o",
        help="輸出文件路徑"
    )
    
    # 導出模式
    parser.add_argument(
        "--export", "-e",
        help="導出結果到文件 (需要指定文件路徑)"
    )
    parser.add_argument(
        "--format",
        default="json",
        choices=["json", "csv"],
        help="導出格式 (預設: json)"
    )
    
    args = parser.parse_args()
    
    # 初始化追蹤器
    tracker = StockTracker(verbose=args.verbose)
    
    try:
        # 檢查必要參數
        if not args.symbol and not args.watchlist:
            parser.error("必須指定 --symbol 或 --watchlist")
        
        # 執行分析
        if args.symbol:
            tracker.analyze_symbol(
                args.symbol,
                use_csv=args.csv,
                csv_path=args.file
            )
        
        elif args.watchlist:
            symbols = [s.strip() for s in args.watchlist.split(",")]
            tracker.analyze_watchlist(
                symbols,
                output_file=args.output if args.report else None
            )
        
        # 導出結果
        if args.export:
            tracker.export_results(args.export, args.format)
        
    except KeyboardInterrupt:
        print("\n用戶中斷執行")
        sys.exit(0)
    except Exception as e:
        tracker.logger.error(f"執行時出錯: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
