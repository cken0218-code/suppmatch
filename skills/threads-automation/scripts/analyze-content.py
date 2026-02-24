#!/usr/bin/env python3
"""
Threads Content Analyzer
Analyzes collected Threads content using AI and extracts actionable insights.
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path

def extract_insights(posts_file, keywords):
    """Extract actionable insights from posts."""
    insights = []
    
    with open(posts_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple keyword extraction
    # Full implementation would use GLM-5 API for deep analysis
    
    lines = content.split('\n')
    for line in lines:
        for keyword in keywords:
            if keyword.lower() in line.lower() and len(line) > 20:
                insights.append({
                    'keyword': keyword,
                    'content': line.strip(),
                    'timestamp': datetime.now().isoformat()
                })
    
    return insights[:10]  # Top 10 insights

def generate_summary(insights, output_file):
    """Generate markdown summary."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# Threads Insights Summary - {datetime.now().strftime('%Y-%m-%d')}\n\n")
        
        for i, insight in enumerate(insights, 1):
            f.write(f"## {i}. {insight['keyword'].upper()}\n")
            f.write(f"{insight['content']}\n\n")
        
        f.write(f"\n---\n*Generated: {datetime.now().isoformat()}*\n")
    
    print(f"✅ Generated summary: {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Analyze Threads content')
    parser.add_argument('--input', default='memory/knowledge/threads/', help='Input directory')
    parser.add_argument('--output', default='memory/knowledge/threads/summary.md', help='Output file')
    parser.add_argument('--keywords', default='AI,automation,productivity,side hustle,agent,tool', help='Keywords to track')
    
    args = parser.parse_args()
    
    keywords = [k.strip() for k in args.keywords.split(',')]
    
    # Find latest threads file
    input_path = Path(args.input)
    threads_files = sorted(input_path.glob('threads-*.md'), reverse=True)
    
    if not threads_files:
        print("❌ No Threads content found. Run fetch-threads-trending.py first.")
        return
    
    latest_file = threads_files[0]
    print(f"📖 Analyzing: {latest_file}")
    
    insights = extract_insights(latest_file, keywords)
    generate_summary(insights, args.output)

if __name__ == '__main__':
    main()
