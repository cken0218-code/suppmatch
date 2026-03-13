#!/usr/bin/env python3
"""
Token Usage Tracker Script
Created: 2026-03-13
Purpose: Track and analyze token usage from OpenClaw logs
"""

import json
import re
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

# Paths
LOG_DIR = Path("/tmp/openclaw")
OUTPUT_FILE = Path.home() / ".openclaw" / "workspace" / "memory" / "token-usage.json"

def parse_log_file(log_file):
    """Parse a single log file and extract token usage"""
    usage = {
        "date": log_file.stem.split("-")[-1],
        "sessions": defaultdict(lambda: {"in": 0, "out": 0}),
        "total_in": 0,
        "total_out": 0
    }

    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            for line in f:
                # Look for token usage patterns
                if "Tokens:" in line or "tokens" in line.lower():
                    # Extract session ID and token counts
                    match = re.search(r'session[:\s]+([a-zA-Z0-9:-]+).*?(\d+)\s*k?\s*in.*?(\d+)\s*k?\s*out', line, re.IGNORECASE)
                    if match:
                        session_id = match.group(1)
                        tokens_in = int(match.group(2)) * 1000 if 'k' in match.group(2).lower() else int(match.group(2))
                        tokens_out = int(match.group(3)) * 1000 if 'k' in match.group(3).lower() else int(match.group(3))

                        usage["sessions"][session_id]["in"] += tokens_in
                        usage["sessions"][session_id]["out"] += tokens_out
                        usage["total_in"] += tokens_in
                        usage["total_out"] += tokens_out
    except Exception as e:
        print(f"Error parsing {log_file}: {e}")

    return usage

def analyze_usage(days=7):
    """Analyze token usage for the past N days"""
    usage_data = {
        "lastUpdated": datetime.now().isoformat(),
        "period": f"Last {days} days",
        "dailyUsage": [],
        "totalUsage": {"in": 0, "out": 0, "total": 0},
        "averageDaily": {"in": 0, "out": 0, "total": 0},
        "topSessions": []
    }

    # Get log files for the past N days
    for i in range(days):
        date = datetime.now() - timedelta(days=i)
        log_file = LOG_DIR / f"openclaw-{date.strftime('%Y-%m-%d')}.log"

        if log_file.exists():
            daily_usage = parse_log_file(log_file)
            usage_data["dailyUsage"].append(daily_usage)
            usage_data["totalUsage"]["in"] += daily_usage["total_in"]
            usage_data["totalUsage"]["out"] += daily_usage["total_out"]

    # Calculate totals and averages
    usage_data["totalUsage"]["total"] = (
        usage_data["totalUsage"]["in"] + usage_data["totalUsage"]["out"]
    )

    if len(usage_data["dailyUsage"]) > 0:
        usage_data["averageDaily"]["in"] = (
            usage_data["totalUsage"]["in"] / len(usage_data["dailyUsage"])
        )
        usage_data["averageDaily"]["out"] = (
            usage_data["totalUsage"]["out"] / len(usage_data["dailyUsage"])
        )
        usage_data["averageDaily"]["total"] = (
            usage_data["totalUsage"]["total"] / len(usage_data["dailyUsage"])
        )

    # Find top sessions
    all_sessions = defaultdict(lambda: {"in": 0, "out": 0})
    for daily in usage_data["dailyUsage"]:
        for session_id, tokens in daily["sessions"].items():
            all_sessions[session_id]["in"] += tokens["in"]
            all_sessions[session_id]["out"] += tokens["out"]

    # Sort by total usage
    sorted_sessions = sorted(
        all_sessions.items(),
        key=lambda x: x[1]["in"] + x[1]["out"],
        reverse=True
    )[:10]  # Top 10

    usage_data["topSessions"] = [
        {
            "session": session_id,
            "in": tokens["in"],
            "out": tokens["out"],
            "total": tokens["in"] + tokens["out"]
        }
        for session_id, tokens in sorted_sessions
    ]

    return usage_data

def print_summary(usage_data):
    """Print a summary to console"""
    print("📊 Token Usage Summary")
    print("━━━━━━━━━━━━━━━━━━━━━━")
    print(f"Period: {usage_data['period']}")
    print(f"Last Updated: {usage_data['lastUpdated']}")
    print()
    print(f"Total Usage:")
    print(f"  Input:  {usage_data['totalUsage']['in']:,} tokens")
    print(f"  Output: {usage_data['totalUsage']['out']:,} tokens")
    print(f"  Total:  {usage_data['totalUsage']['total']:,} tokens")
    print()
    print(f"Average Daily:")
    print(f"  Input:  {usage_data['averageDaily']['in']:,.0f} tokens")
    print(f"  Output: {usage_data['averageDaily']['out']:,.0f} tokens")
    print(f"  Total:  {usage_data['averageDaily']['total']:,.0f} tokens")
    print()
    print("Top 5 Sessions:")
    for i, session in enumerate(usage_data['topSessions'][:5], 1):
        print(f"  {i}. {session['session'][:30]}...")
        print(f"     Total: {session['total']:,} tokens")

def save_usage(usage_data):
    """Save usage data to JSON file"""
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(usage_data, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Usage data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    import sys

    days = int(sys.argv[1]) if len(sys.argv) > 1 else 7

    usage_data = analyze_usage(days)
    print_summary(usage_data)
    save_usage(usage_data)
