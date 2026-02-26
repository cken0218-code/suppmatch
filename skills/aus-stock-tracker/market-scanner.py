#!/usr/bin/env python3
"""
Market Scanner - 扫描 ASX 200 寻找买入机会
每周运行两次，发现新机会时通知用户
"""

import sys
import json
from datetime import datetime
from pathlib import Path

# Import stock tracker functions
sys.path.insert(0, str(Path(__file__).parent))
import importlib.util

spec = importlib.util.spec_from_file_location("stock_tracker_module", 
    str(Path(__file__).parent / "stock-tracker.py"))
stock_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stock_module)

get_stock_analysis_orig = stock_module.get_stock_analysis
save_history_orig = stock_module.save_history

# ASX 200 主要股票列表（按市值排序）
ASX_200_TOP = [
    # 前 50 大（蓝筹股）
    "BHP", "CBA", "CSL", "NAB", "ANZ", "WBC", "MQG", "WES", "WOW", "TLS",
    "RIO", "WDS", "NEM", "FMG", "S32", "ALL", "SUN", "QBE", "IAG", "AMP",
    "BXB", "TCL", "SYD", "SCG", "GMG", "LLC", "VCX", "SGP", "COH", "RMD",
    "SHL", "RHC", "FPH", "CSL", "SEK", "WTC", "XRO", "ALT", "APX", "NEA",
    "PME", "TNE", "CPU", "MQG", "MFG", "SGP", "QAN", "VAS", "A200", "IOZ",
    
    # 51-100（大型股）
    "AMC", "BEN", "BOQ", "QBE", "SUN", "AMP", "IAG", "WES", "WOW", "TLS",
    "RMD", "FPH", "COH", "RHC", "SHL", "SEK", "WTC", "XRO", "ALT", "APX",
    "NEA", "PME", "TNE", "CPU", "MQG", "MFG", "SGP", "QAN", "NCM", "EVN",
    "NST", "SAR", "RRL", "SBM", "RIO", "BHP", "FMG", "S32", "WDS", "NEM",
    "ORG", "STO", "WPL", "OSH", "KAR", "BPT", "WHC", "YAL", "NCM", "EVN",
    
    # 101-150（中型股）
    "ARB", "BKW", "CCP", "CNU", "CPU", "DMP", "DXS", "ECH", "GNC", "HLO",
    "HVN", "ILU", "ING", "JHG", "KMD", "LYC", "MGR", "MOT", "NHF", "ORI",
    "PAN", "PPT", "QUB", "REA", "RMD", "SDF", "SGA", "SKC", "SOL", "SRX",
    "SXL", "TAH", "TGA", "TGG", "TLC", "TLS", "TNE", "TWE", "VRL", "WAM",
    "WAX", "WES", "WOW", "WPL", "WTC", "XRO", "YAL", "Z1P", "ZIM", "ZLD",
    
    # 151-200（小型高增长股）
    "1AD", "1ST", "4DS", "4DX", "86I", "A2M", "AAN", "ABP", "ABT", "AD8",
    "AFC", "AGL", "AHG", "AIA", "ALD", "ALQ", "AMX", "AO1", "AO2", "APC",
    "API", "APX", "ARB", "ARD", "ARK", "ARU", "AVH", "AX1", "BAP", "BGL",
    "BNK", "BTH", "CTT", "ELD", "FANG", "KMD", "KTC", "LYL", "M7T", "M8S",
    "MLX", "NAN", "NCL", "NEA", "PME", "RMD", "SGA", "TNE", "VHT", "VR1"
]

def get_stock_analysis(ticker):
    """包装 stock_tracker 的 get_stock_analysis"""
    try:
        analysis = get_stock_analysis_orig(ticker)
        
        if "error" not in analysis:
            if "name" not in analysis:
                analysis["name"] = ticker
            
            if analysis.get("signal", "").startswith("🟢"):
                current_price = analysis.get("price", 0)
                if current_price > 0:
                    analysis["buy_price"] = round(current_price * 0.98, 2)
                else:
                    analysis["buy_price"] = None
            else:
                analysis["buy_price"] = None
        
        return analysis
    except Exception as e:
        return {"error": str(e), "ticker": ticker}

def load_portfolio():
    """加载持仓配置"""
    portfolio_file = Path(__file__).parent / "portfolio.json"
    
    if portfolio_file.exists():
        with open(portfolio_file, 'r') as f:
            return json.load(f)
    else:
        return {
            "system_1_owned": [],
            "system_2_watchlist": [],
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "notes": {}
        }

def save_portfolio(portfolio):
    """保存持仓配置"""
    portfolio_file = Path(__file__).parent / "portfolio.json"
    portfolio["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    
    with open(portfolio_file, 'w') as f:
        json.dump(portfolio, f, indent=2)

def scan_market(stocks, rsi_threshold=30, adx_threshold=25, exclude_owned=True):
    """
    扫描市场寻找买入机会
    
    Args:
        stocks: 股票列表
        rsi_threshold: RSI 阈值（默认 30）
        adx_threshold: ADX 阈值（默认 25）
        exclude_owned: 是否排除已持有股票
    
    Returns:
        list: 有买入信号的股票
    """
    portfolio = load_portfolio()
    owned = portfolio.get("system_1_owned", [])
    
    buy_signals = []
    
    print(f"🔍 正在扫描 {len(stocks)} 只股票...")
    print(f"   RSI 阈值: < {rsi_threshold}")
    print(f"   ADX 阈值: > {adx_threshold}")
    if exclude_owned:
        print(f"   排除已持有: {len(owned)} 只")
    print()
    
    for ticker in stocks:
        # 排除已持有股票
        if exclude_owned and ticker in owned:
            continue
        
        analysis = get_stock_analysis(ticker)
        
        if "error" in analysis:
            continue
        
        signal = analysis.get("signal", "")
        rsi = analysis.get("rsi")
        adx = analysis.get("adx")
        
        # 更严格的买入条件
        is_buy = signal.startswith("🟢")
        is_oversold = rsi and rsi < rsi_threshold
        is_strong_trend = adx and adx > adx_threshold and rsi and rsi < 35
        
        if is_buy or is_oversold or is_strong_trend:
            buy_signals.append(analysis)
            
            reason = []
            if is_buy:
                reason.append("BUY信号")
            if is_oversold:
                reason.append(f"RSI超卖({rsi:.1f})")
            if is_strong_trend:
                reason.append(f"强趋势(ADX={adx:.1f})")
            
            print(f"✅ {ticker}: ${analysis['price']:.2f} | {' + '.join(reason)}")
    
    return buy_signals

def send_discord_notification(buy_signals, scan_type="market"):
    """发送 Discord 通知"""
    if not buy_signals:
        return
    
    # 构建消息
    if scan_type == "market":
        message = "🆕 **市场扫描 - 新发现机会** 🆕\n"
    else:
        message = "🔔 **固定监察 - 买入信号** 🔔\n"
    
    message += f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    message += "─" * 40 + "\n\n"
    
    for stock in buy_signals:
        ticker_ax = f"{stock['ticker']}.AX"
        message += f"📊 **{ticker_ax}**\n"
        message += f"💰 价格: ${stock['price']:.2f}\n"
        
        rsi = stock.get('rsi')
        adx = stock.get('adx')
        
        if rsi:
            message += f"📉 RSI: {rsi:.1f}"
            if rsi < 30:
                message += " (超卖 ✅)"
            message += "\n"
        
        if adx:
            message += f"💪 ADX: {adx:.1f}"
            if adx > 25:
                message += " (强趋势 ✅)"
            message += "\n"
        
        buy_price = stock.get('buy_price')
        if buy_price:
            message += f"💚 建议买入: ${buy_price:.2f}\n"
        
        message += "\n"
    
    message += "─" * 40 + "\n"
    message += f"🎯 发现 {len(buy_signals)} 只股票\n"
    
    if scan_type == "market":
        message += "💡 提示：这是市场扫描发现的新机会\n"
        message += "📝 如果买入，告诉我股票代码，我会加入固定监察\n"
    
    message += "⚠️ 注意：以上纯属技术分析，不构成投资建议"
    
    # 保存通知
    notification_file = Path("/tmp/stock-alert.json")
    notification_data = {
        "type": f"stock_alert_{scan_type}",
        "message": message,
        "timestamp": datetime.now().isoformat(),
        "stocks": [s['ticker'] for s in buy_signals],
        "scan_type": scan_type
    }
    
    with open(notification_file, 'w') as f:
        json.dump(notification_data, f, indent=2)
    
    print(f"✅ Notification saved to {notification_file}")
    return message

def main():
    """主函数"""
    print("=" * 60)
    print("🔍 ASX 200 市场扫描器")
    print("=" * 60)
    print()
    
    # 扫描 ASX 200
    buy_signals = scan_market(ASX_200_TOP, rsi_threshold=30, adx_threshold=25)
    
    print()
    print("=" * 60)
    
    if buy_signals:
        print(f"🎯 发现 {len(buy_signals)} 只股票有买入信号！")
        print()
        
        # 发送通知
        message = send_discord_notification(buy_signals, scan_type="market")
        
        print("📝 通知内容:")
        print(message)
        
        # 保存到历史
        save_history_orig(buy_signals)
    else:
        print("😴 今日市场扫描没有发现买入信号")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
