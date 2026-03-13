#!/usr/bin/env python3
"""
JSON 关键提取工具
JSON Key Extractor

功能：从大型 JSON 文件中提取关键数据，减少 token 使用
"""

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Union


def extract_value(data: Dict, key_path: str) -> Any:
    """
    从嵌套字典中提取值

    Args:
        data: JSON 数据
        key_path: 键路径，例如 "stocks.CBA.price"

    Returns:
        提取的值，如果不存在则返回 None
    """
    keys = key_path.split(".")
    current = data

    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None

    return current


def format_output(data: Dict, key_paths: List[str], format_type: str = "compact") -> str:
    """
    格式化输出

    Args:
        data: JSON 数据
        key_paths: 要提取的键路径列表
        format_type: 输出格式（compact, detailed）

    Returns:
        格式化的字符串
    """
    results = []

    for key_path in key_paths:
        value = extract_value(data, key_path)

        if value is not None:
            if format_type == "compact":
                # 紧凑格式：CBA: $174.25
                parts = key_path.split(".")
                label = parts[-1] if len(parts) > 1 else parts[0]
                results.append(f"{label}: {value}")
            else:
                # 详细格式：stocks.CBA.price = $174.25
                results.append(f"{key_path} = {value}")

    return "\n".join(results)


def calculate_token_savings(original: str, compressed: str) -> Dict:
    """计算 token 节省"""
    original_tokens = len(original.split())  # 粗略估算
    compressed_tokens = len(compressed.split())

    savings = original_tokens - compressed_tokens
    percentage = (savings / original_tokens * 100) if original_tokens > 0 else 0

    return {
        "original_tokens": original_tokens,
        "compressed_tokens": compressed_tokens,
        "savings": savings,
        "percentage": round(percentage, 1)
    }


def main():
    """主程序"""
    import argparse

    parser = argparse.ArgumentParser(description="JSON 关键提取工具")
    parser.add_argument("--file", "-f", required=True, help="JSON 文件路径")
    parser.add_argument("--keys", "-k", required=True, help="要提取的键（逗号分隔）")
    parser.add_argument("--format", "-fmt", choices=["compact", "detailed"], default="compact", help="输出格式")
    parser.add_argument("--stats", "-s", action="store_true", help="显示 token 节省统计")

    args = parser.parse_args()

    # 读取 JSON 文件
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ 文件不存在: {args.file}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"❌ JSON 解析错误: {args.file}")
        sys.exit(1)

    # 解析键路径
    key_paths = [k.strip() for k in args.keys.split(",")]

    # 提取并格式化
    output = format_output(data, key_paths, args.format)

    print("📊 JSON 关键数据提取")
    print("=" * 60)
    print(output)

    # 显示统计
    if args.stats:
        original = json.dumps(data, indent=2)
        savings = calculate_token_savings(original, output)

        print("\n" + "=" * 60)
        print("📈 Token 节省统计：")
        print(f"  原始: {savings['original_tokens']} tokens")
        print(f"  压缩后: {savings['compressed_tokens']} tokens")
        print(f"  节省: {savings['savings']} tokens ({savings['percentage']}%)")


if __name__ == "__main__":
    # 如果没有命令行参数，运行演示
    if len(sys.argv) == 1:
        print("📊 JSON 关键提取工具 - 演示模式")
        print("=" * 60)

        # 示例数据
        sample_data = {
            "date": "2026-03-13",
            "stocks": {
                "CBA": {
                    "price": 174.25,
                    "rsi": 38.65,
                    "signal": "🟢 BUY"
                },
                "ANZ": {
                    "price": 37.51,
                    "rsi": 33.62,
                    "signal": "🟢 BUY"
                },
                "BHP": {
                    "price": 50.12,
                    "signal": "🟡 HOLD"
                }
            }
        }

        # 演示提取
        keys = ["stocks.CBA.price", "stocks.CBA.signal", "stocks.ANZ.price", "stocks.ANZ.signal"]
        output = format_output(sample_data, keys, "compact")

        print("原始 JSON (300+ tokens):")
        print(json.dumps(sample_data, indent=2)[:200] + "...\n")

        print("提取后 (50 tokens):")
        print(output + "\n")

        # 计算节省
        original = json.dumps(sample_data, indent=2)
        savings = calculate_token_savings(original, output)

        print("=" * 60)
        print("📈 Token 节省统计：")
        print(f"  原始: {savings['original_tokens']} tokens")
        print(f"  压缩后: {savings['compressed_tokens']} tokens")
        print(f"  节省: {savings['savings']} tokens ({savings['percentage']}%)")
        print("\n💡 使用方式:")
        print("  python3 json-extract.py --file data.json --keys 'stocks.CBA.price,stocks.ANZ.price' --stats")

    else:
        main()
