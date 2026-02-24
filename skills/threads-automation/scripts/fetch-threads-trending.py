#!/usr/bin/env python3
"""
Threads Trending Content Fetcher
Fetches trending posts from Threads and saves to knowledge base.
"""

import argparse
import json
import os
import re
from datetime import datetime
from pathlib import Path

def parse_threads_content(html_content):
    """Parse Threads HTML content to extract post data."""
    posts = []
    
    # Extract post content using regex patterns
    # This is a simplified parser - Playwright version would be more robust
    
    post_pattern = r'<div[^>]*role="article"[^>]*>(.*?)</div>'
    content_pattern = r'<span[^>]*>(.*?)</span>'
    engagement_pattern = r'(\d+)\s*(likes|replies|reposts)'
    
    matches = re.findall(post_pattern, html_content, re.DOTALL)
    
    for match in matches[:20]:  # Limit to 20 posts
        content_match = re.search(content_pattern, match)
        if content_match:
            content = re.sub(r'<[^>]+>', '', content_match.group(1)).strip()
            if content and len(content) > 10:  # Filter short posts
                posts.append({
                    'content': content,
                    'engagement': re.findall(engagement_pattern, match, re.IGNORECASE),
                    'timestamp': datetime.now().isoformat()
                })
    
    return posts

def save_posts(posts, output_dir, keyword_filter=None):
    """Save posts to markdown files in knowledge base."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    date_str = datetime.now().strftime('%Y-%m-%d')
    filename = output_path / f'threads-{date_str}.md'
    
    # Filter by keywords if provided
    if keyword_filter:
        keywords = keyword_filter.split(',')
        posts = [p for p in posts if any(kw.lower() in p['content'].lower() for kw in keywords)]
    
    # Write markdown
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"\n## Threads Trending - {datetime.now().strftime('%H:%M')}\n\n")
        
        for i, post in enumerate(posts[:10], 1):
            f.write(f"### Post {i}\n")
            f.write(f"{post['content']}\n\n")
            if post['engagement']:
                eng_str = ', '.join([f"{e[0]} {e[1]}" for e in post['engagement']])
                f.write(f"*Engagement: {eng_str}*\n\n")
            f.write("---\n\n")
    
    print(f"✅ Saved {len(posts)} posts to {filename}")
    return filename

def main():
    parser = argparse.ArgumentParser(description='Fetch Threads trending content')
    parser.add_argument('--output', default='memory/knowledge/threads/', help='Output directory')
    parser.add_argument('--keywords', default='AI,automation,productivity,side hustle', help='Filter keywords')
    parser.add_argument('--mock', action='store_true', help='Use mock data for testing')
    
    args = parser.parse_args()
    
    if args.mock:
        # Use mock data for testing
        mock_posts = [
            {'content': '新 AI agent 自動化工具真係好用，幫我省咗好多時間做重複嘅工作', 'engagement': [('125', 'likes')], 'timestamp': datetime.now().isoformat()},
            {'content': '用 ChatGPT 幫手寫 code 好過自己由頭寫，效率提升 3 倍', 'engagement': [('89', 'likes'), ('12', 'replies')], 'timestamp': datetime.now().isoformat()},
            {'content': '副業推薦：用 AI 幫人寫 blog post，一個月可以賺 $500-1000', 'engagement': [('234', 'likes'), ('45', 'replies')], 'timestamp': datetime.now().isoformat()},
        ]
        save_posts(mock_posts, args.output, args.keywords)
    else:
        # Real implementation would use Playwright
        print("⚠️  Full implementation requires Playwright browser automation.")
        print("📝 Using mock data for now. Run with --mock to test.")
        print("\nTo use browser automation:")
        print("1. Ensure Chrome is logged into Threads")
        print("2. Use browser tool to visit https://www.threads.net/")
        print("3. Scroll and collect content")

if __name__ == '__main__':
    main()
