#!/usr/bin/env python3
"""
Token Usage Visualization Script
Created: 2026-03-13
Purpose: Generate visual reports of token usage with charts
"""

import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from pathlib import Path
import numpy as np

# Configuration
OUTPUT_DIR = Path.home() / ".openclaw" / "workspace" / "memory" / "reports"
DATA_FILE = Path.home() / ".openclaw" / "workspace" / "memory" / "token-usage.json"

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def load_usage_data():
    """Load token usage data from JSON"""
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        return {"dailyUsage": [], "totalUsage": {}, "topSessions": []}

def create_usage_chart(data, days=7):
    """Create token usage chart for the past N days"""
    if not data.get("dailyUsage"):
        print("❌ No usage data available")
        return

    # Extract data
    dates = []
    input_tokens = []
    output_tokens = []

    for daily in data["dailyUsage"][-days:]:
        dates.append(datetime.strptime(daily["date"], "%Y-%m-%d"))
        input_tokens.append(daily["total_in"] / 1000)  # Convert to K
        output_tokens.append(daily["total_out"] / 1000)

    if not dates:
        print("❌ No data to visualize")
        return

    # Create figure with 2 subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    # Plot 1: Daily token usage
    ax1.plot(dates, input_tokens, 'b-o', label='Input Tokens (K)', linewidth=2, markersize=8)
    ax1.plot(dates, output_tokens, 'r-o', label='Output Tokens (K)', linewidth=2, markersize=8)
    ax1.fill_between(dates, input_tokens, alpha=0.3, color='blue')
    ax1.fill_between(dates, output_tokens, alpha=0.3, color='red')

    ax1.set_xlabel('Date', fontsize=12)
    ax1.set_ylabel('Tokens (K)', fontsize=12)
    ax1.set_title(f'Token Usage - Last {days} Days', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d'))
    ax1.xaxis.set_major_locator(mdates.DayLocator())
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)

    # Plot 2: Top sessions
    if data.get("topSessions"):
        sessions = [s["session"].split(":")[-1][:20] + "..." for s in data["topSessions"][:5]]
        totals = [s["total"] / 1000 for s in data["topSessions"][:5]]

        ax2.barh(sessions, totals, color='skyblue', edgecolor='navy')
        ax2.set_xlabel('Tokens (K)', fontsize=12)
        ax2.set_ylabel('Session', fontsize=12)
        ax2.set_title('Top 5 Sessions by Token Usage', fontsize=14, fontweight='bold')
        ax2.grid(True, alpha=0.3, axis='x')

        # Add value labels
        for i, (session, total) in enumerate(zip(sessions, totals)):
            ax2.text(total + 0.5, i, f'{total:.1f}K', va='center')

    plt.tight_layout()

    # Save chart
    today = datetime.now().strftime("%Y-%m-%d")
    output_file = OUTPUT_DIR / f"token-usage-chart-{today}.png"
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"✅ Chart saved to: {output_file}")

    # Also create a summary text file
    summary_file = OUTPUT_DIR / f"token-usage-summary-{today}.txt"
    with open(summary_file, 'w') as f:
        f.write(f"📊 Token Usage Summary - {today}\n")
        f.write(f"{'=' * 50}\n\n")

        f.write(f"Total Usage ({days} days):\n")
        f.write(f"  Input:  {data['totalUsage'].get('in', 0):,} tokens\n")
        f.write(f"  Output: {data['totalUsage'].get('out', 0):,} tokens\n")
        f.write(f"  Total:  {data['totalUsage'].get('total', 0):,} tokens\n\n")

        f.write(f"Average Daily:\n")
        f.write(f"  Input:  {data['averageDaily'].get('in', 0):,.0f} tokens\n")
        f.write(f"  Output: {data['averageDaily'].get('out', 0):,.0f} tokens\n")
        f.write(f"  Total:  {data['averageDaily'].get('total', 0):,.0f} tokens\n\n")

        if data.get("topSessions"):
            f.write("Top 5 Sessions:\n")
            for i, session in enumerate(data["topSessions"][:5], 1):
                f.write(f"  {i}. {session['session'][:30]}...\n")
                f.write(f"     Total: {session['total']:,} tokens\n")

    print(f"✅ Summary saved to: {summary_file}")

def create_pie_chart(data):
    """Create pie chart of token distribution"""
    if not data.get("topSessions"):
        return

    # Prepare data
    labels = [s["session"].split(":")[-1][:15] for s in data["topSessions"][:7]]
    sizes = [s["total"] for s in data["topSessions"][:7]]

    # Add "Others" if there are more sessions
    if len(data["topSessions"]) > 7:
        others_total = sum(s["total"] for s in data["topSessions"][7:])
        labels.append("Others")
        sizes.append(others_total)

    # Create pie chart
    fig, ax = plt.subplots(figsize=(10, 8))
    colors = plt.cm.Spectral(np.linspace(0, 1, len(labels)))

    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        colors=colors,
        startangle=90,
        pctdistance=0.85
    )

    # Improve text
    for text in texts:
        text.set_fontsize(10)
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')

    ax.set_title('Token Usage Distribution by Session', fontsize=14, fontweight='bold')

    # Save chart
    today = datetime.now().strftime("%Y-%m-%d")
    output_file = OUTPUT_DIR / f"token-distribution-pie-{today}.png"
    plt.savefig(output_file, dpi=150, bbox_inches='tight')
    print(f"✅ Pie chart saved to: {output_file}")

if __name__ == "__main__":
    import sys

    days = int(sys.argv[1]) if len(sys.argv) > 1 else 7

    print(f"📊 Generating token usage visualization...")
    print(f"Period: Last {days} days\n")

    data = load_usage_data()
    create_usage_chart(data, days)
    create_pie_chart(data)

    print("\n✅ Visualization complete!")
