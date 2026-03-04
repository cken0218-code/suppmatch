#!/usr/bin/env python3
"""
Stock Alert Notifier - 自动通知值得买的澳股
当发现 BUY 信号时，自动发送 Discord 通知
"""

import sys
import json
from datetime import datetime
from pathlib import Path

# Import stock tracker functions
sys.path.insert(0, str(Path(__file__).parent))

# 动态导入，避免命名冲突
import importlib.util
spec = importlib.util.spec_from_file_location("stock_tracker_module", 
    str(Path(__file__).parent / "stock-tracker.py"))
stock_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stock_module)

# 使用别名导入函数
get_stock_analysis_orig = stock_module.get_stock_analysis
DEFAULT_ASX_STOCKS = stock_module.DEFAULT_ASX_STOCKS
save_history_orig = stock_module.save_history

def get_stock_analysis(ticker):
    """
    包装 stock_tracker 的 get_stock_analysis，添加错误处理和额外字段
    """
    try:
        analysis = get_stock_analysis_orig(ticker)
        
        if "error" not in analysis:
            # 确保有 name 字段
            if "name" not in analysis:
                analysis["name"] = ticker
            
            # 添加建议买入价（如果有 BUY 信号）
            if analysis.get("signal", "").startswith("🟢"):
                current_price = analysis.get("price", 0)
                if current_price > 0:
                    analysis["buy_price"] = round(current_price * 0.98, 2)  # 2% below current
                else:
                    analysis["buy_price"] = None
            else:
                analysis["buy_price"] = None
        
        return analysis
    except Exception as e:
        return {"error": str(e), "ticker": ticker}

# Discord notification function
def send_discord_notification(buy_signals):
    """发送 Discord 通知"""
    if not buy_signals:
        return
    
    # 构建消息
    message = "🚨 **澳股买入信号提醒** 🚨\n"
    message += f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
    message += "─" * 40 + "\n\n"
    
    for stock in buy_signals:
        ticker_ax = f"{stock['ticker']}.AX"
        message += f"📊 **{ticker_ax}** - {stock.get('name', ticker_ax)}\n"
        message += f"💰 价格: ${stock['price']:.2f}\n"
        
        # 变动
        change_pct = stock.get('change_pct', 0)
        message += f"📈 变动: {change_pct:+.2f}%\n"
        
        # 技术指标
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
    message += f"🎯 发现 {len(buy_signals)} 只股票有买入信号\n"
    message += "⚠️ 注意：以上纯属技术分析，不构成投资建议"
    
    # 保存到文件，由 OpenClaw 读取并发送
    notification_file = Path("/tmp/stock-alert.json")
    notification_data = {
        "type": "stock_alert",
        "message": message,
        "timestamp": datetime.now().isoformat(),
        "stocks": [s['ticker'] for s in buy_signals]
    }
    
    with open(notification_file, 'w') as f:
        json.dump(notification_data, f, indent=2)
    
    print(f"✅ Notification saved to {notification_file}")
    return message

def check_buy_signals(stocks=None, rsi_threshold=35, adx_threshold=20):
    """
    检查买入信号
    
    Args:
        stocks: 股票列表（默认使用 DEFAULT_ASX_STOCKS）
        rsi_threshold: RSI 阈值（低于此值视为超卖）
        adx_threshold: ADX 阈值（高于此值视为有趋势）
    
    Returns:
        list: 有买入信号的股票列表
    """
    if stocks is None:
        stocks = DEFAULT_ASX_STOCKS
    
    buy_signals = []
    
    print(f"🔍 正在扫描 {len(stocks)} 只澳股...")
    print(f"   RSI 阈值: < {rsi_threshold}")
    print(f"   ADX 阈值: > {adx_threshold}")
    print()
    
    for ticker in stocks:
        analysis = get_stock_analysis(ticker)
        
        if "error" in analysis:
            print(f"❌ {ticker}: {analysis['error']}")
            continue
        
        # 检查信号
        signal = analysis.get("signal", "")
        rsi = analysis.get("rsi")
        adx = analysis.get("adx")
        
        # 买入条件：
        # 1. 信号是 BUY
        # 2. 或者 RSI < rsi_threshold (超卖)
        # 3. 或者 ADX > adx_threshold 且 RSI < 40 (强趋势 + 未超买)
        
        is_buy = signal.startswith("🟢")
        is_oversold = rsi and rsi < rsi_threshold
        is_strong_trend = adx and adx > adx_threshold and rsi and rsi < 40
        
        if is_buy or is_oversold or is_strong_trend:
            buy_signals.append(analysis)
            
            # 打印详情
            reason = []
            if is_buy:
                reason.append("信号=BUY")
            if is_oversold:
                reason.append(f"RSI超卖({rsi:.1f})")
            if is_strong_trend:
                reason.append(f"强趋势(ADX={adx:.1f})")
            
            print(f"✅ {ticker}: ${analysis['price']:.2f} | {' + '.join(reason)}")
    
    return buy_signals

def load_portfolio():
    """加载持仓配置"""
    portfolio_file = Path(__file__).parent / "portfolio.json"
    
    if portfolio_file.exists():
        with open(portfolio_file, 'r') as f:
            return json.load(f)
    else:
        return {
            "system_1_owned": [],
            "system_2_watchlist": DEFAULT_ASX_STOCKS,
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "notes": {}
        }

def main():
    """主函数 - 系统一：固定监察（已持有股票）"""
    print("=" * 60)
    print("🔔 系统一：固定监察（已持有股票）")
    print("=" * 60)
    print()
    
    # 加载持仓
    portfolio = load_portfolio()
    owned = portfolio.get("system_1_owned", [])
    
    if not owned:
        print("😴 系统一暂无持有股票")
        print()
        print("💡 提示：告诉我你买了什么股票，我会加入固定监察")
        print("   用法: python3 stock-alert-manager.py buy <股票代码>")
        return
    
    print(f"📊 正在监察 {len(owned)} 只已持有股票:")
    for ticker in owned:
        print(f"   - {ticker}.AX")
    print()
    
    # 扫描买入信号
    buy_signals = check_buy_signals(stocks=owned)
    
    print()
    print("=" * 60)
    
    if buy_signals:
        print(f"🎯 发现 {len(buy_signals)} 只持有股票有买入信号！")
        print()
        
        # 发送通知
        message = send_discord_notification(buy_signals)
        
        print("📝 通知内容:")
        print(message)
        
        # 保存到历史
        save_history_orig(buy_signals)
    else:
        print("😴 今日持有股票没有新的买入信号")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
