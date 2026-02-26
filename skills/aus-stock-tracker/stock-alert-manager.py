#!/usr/bin/env python3
"""
Stock Alert Manager - 管理持仓和监察列表
"""

import sys
import json
from datetime import datetime
from pathlib import Path

# Import stock tracker
sys.path.insert(0, str(Path(__file__).parent))
import importlib.util

spec = importlib.util.spec_from_file_location("stock_tracker_module", 
    str(Path(__file__).parent / "stock-tracker.py"))
stock_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stock_module)

get_stock_analysis_orig = stock_module.get_stock_analysis
DEFAULT_ASX_STOCKS = stock_module.DEFAULT_ASX_STOCKS

PORTFOLIO_FILE = Path(__file__).parent / "portfolio.json"

def load_portfolio():
    """加载持仓配置"""
    if PORTFOLIO_FILE.exists():
        with open(PORTFOLIO_FILE, 'r') as f:
            return json.load(f)
    else:
        return {
            "system_1_owned": [],
            "system_2_watchlist": DEFAULT_ASX_STOCKS.copy(),
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "notes": {}
        }

def save_portfolio(portfolio):
    """保存持仓配置"""
    portfolio["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    with open(PORTFOLIO_FILE, 'w') as f:
        json.dump(portfolio, f, indent=2)
    print(f"✅ 配置已保存到 {PORTFOLIO_FILE}")

def add_to_owned(ticker, note=None):
    """将股票移到系统一（已持有）"""
    portfolio = load_portfolio()
    ticker = ticker.upper().replace(".AX", "")
    
    # 从系统二移除
    if ticker in portfolio["system_2_watchlist"]:
        portfolio["system_2_watchlist"].remove(ticker)
    
    # 添加到系统一
    if ticker not in portfolio["system_1_owned"]:
        portfolio["system_1_owned"].append(ticker)
    
    # 添加备注
    if note:
        portfolio["notes"][ticker] = note
    
    save_portfolio(portfolio)
    
    print(f"✅ {ticker}.AX 已添加到系统一（固定监察）")
    print(f"   系统一（已持有）: {len(portfolio['system_1_owned'])} 只")
    print(f"   系统二（观察中）: {len(portfolio['system_2_watchlist'])} 只")

def add_to_watchlist(ticker, note=None):
    """将股票添加到系统二（观察中）"""
    portfolio = load_portfolio()
    ticker = ticker.upper().replace(".AX", "")
    
    # 确保不在系统一
    if ticker in portfolio["system_1_owned"]:
        print(f"⚠️ {ticker}.AX 已在系统一（已持有），无需添加到系统二")
        return
    
    # 添加到系统二
    if ticker not in portfolio["system_2_watchlist"]:
        portfolio["system_2_watchlist"].append(ticker)
    
    # 添加备注
    if note:
        portfolio["notes"][ticker] = note
    
    save_portfolio(portfolio)
    
    print(f"✅ {ticker}.AX 已添加到系统二（市场扫描）")
    print(f"   系统一（已持有）: {len(portfolio['system_1_owned'])} 只")
    print(f"   系统二（观察中）: {len(portfolio['system_2_watchlist'])} 只")

def remove_stock(ticker):
    """从所有系统移除股票"""
    portfolio = load_portfolio()
    ticker = ticker.upper().replace(".AX", "")
    
    removed = False
    
    if ticker in portfolio["system_1_owned"]:
        portfolio["system_1_owned"].remove(ticker)
        removed = True
        print(f"✅ {ticker}.AX 已从系统一移除")
    
    if ticker in portfolio["system_2_watchlist"]:
        portfolio["system_2_watchlist"].remove(ticker)
        removed = True
        print(f"✅ {ticker}.AX 已从系统二移除")
    
    if ticker in portfolio["notes"]:
        del portfolio["notes"][ticker]
    
    if removed:
        save_portfolio(portfolio)
    else:
        print(f"⚠️ {ticker}.AX 不在任何系统中")

def show_status():
    """显示当前状态"""
    portfolio = load_portfolio()
    
    print("=" * 60)
    print("📊 持仓状态")
    print("=" * 60)
    print(f"📅 最后更新: {portfolio['last_updated']}")
    print()
    
    # 系统一
    print("🟢 系统一（已持有 - 每日监察）")
    print("-" * 60)
    if portfolio["system_1_owned"]:
        for ticker in portfolio["system_1_owned"]:
            note = portfolio["notes"].get(ticker, "")
            print(f"   {ticker}.AX {f'- {note}' if note else ''}")
    else:
        print("   （暂无）")
    print()
    
    # 系统二
    print("🟡 系统二（观察中 - 每周扫描两次）")
    print("-" * 60)
    if portfolio["system_2_watchlist"]:
        for i, ticker in enumerate(portfolio["system_2_watchlist"], 1):
            note = portfolio["notes"].get(ticker, "")
            print(f"   {i:2d}. {ticker}.AX {f'- {note}' if note else ''}")
    else:
        print("   （暂无）")
    print()
    
    print("=" * 60)
    print(f"📈 总计: {len(portfolio['system_1_owned']) + len(portfolio['system_2_watchlist'])} 只股票")
    print("=" * 60)

def show_help():
    """显示帮助"""
    print("=" * 60)
    print("📖 Stock Alert Manager - 使用指南")
    print("=" * 60)
    print()
    print("用法:")
    print("  python3 stock-alert-manager.py [命令] [股票代码] [备注]")
    print()
    print("命令:")
    print("  status              显示当前持仓状态")
    print("  buy <股票> [备注]   标记为已买入（移到系统一）")
    print("  watch <股票> [备注] 添加到观察列表（系统二）")
    print("  remove <股票>       从所有系统移除")
    print("  help                显示此帮助")
    print()
    print("例子:")
    print("  python3 stock-alert-manager.py status")
    print("  python3 stock-alert-manager.py buy CSL 买入@280")
    print("  python3 stock-alert-manager.py watch BHP")
    print("  python3 stock-alert-manager.py remove AX1")
    print()
    print("=" * 60)

def main():
    """主函数"""
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == "status":
        show_status()
    elif command == "buy":
        if len(sys.argv) < 3:
            print("❌ 错误：请提供股票代码")
            print("   用法: python3 stock-alert-manager.py buy <股票> [备注]")
            return
        ticker = sys.argv[2]
        note = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else None
        add_to_owned(ticker, note)
    elif command == "watch":
        if len(sys.argv) < 3:
            print("❌ 错误：请提供股票代码")
            print("   用法: python3 stock-alert-manager.py watch <股票> [备注]")
            return
        ticker = sys.argv[2]
        note = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else None
        add_to_watchlist(ticker, note)
    elif command == "remove":
        if len(sys.argv) < 3:
            print("❌ 错误：请提供股票代码")
            print("   用法: python3 stock-alert-manager.py remove <股票>")
            return
        ticker = sys.argv[2]
        remove_stock(ticker)
    elif command == "help":
        show_help()
    else:
        print(f"❌ 未知命令: {command}")
        show_help()

if __name__ == "__main__":
    main()
