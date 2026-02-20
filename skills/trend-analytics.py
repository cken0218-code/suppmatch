#!/usr/bin/env python3
"""
Trend Analytics - Multi-platform trend analysis and prediction
Usage: trend-analytics.py --platforms xhs,twitter,youtube --keywords "AI,automation"

Features:
- Cross-platform trend correlation
- Trend velocity analysis
- Sentiment scoring
- Prediction modeling
"""

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from typing import Dict, List, Optional

try:
    import requests
except ImportError:
    print("❌ requests not installed: pip install requests")
    sys.exit(1)

# Simple in-memory trend storage (in production, use database)
TREND_DATA = defaultdict(list)

class TrendAnalyzer:
    """Multi-platform trend analysis"""
    
    PLATFORMS = {
        'xhs': {'name': 'Xiaohongshu', 'weight': 0.3},
        'twitter': {'name': 'Twitter/X', 'weight': 0.25},
        'youtube': {'name': 'YouTube', 'weight': 0.25},
        'threads': {'name': 'Threads', 'weight': 0.1},
        'reddit': {'name': 'Reddit', 'weight': 0.1},
    }
    
    def __init__(self):
        self.data = defaultdict(list)
    
    def fetch_xhs_trends(self, keywords: List[str]) -> List[Dict]:
        """Fetch Xiaohongshu trending (simulated - requires API)"""
        # In production, integrate with XHS API
        # For now, return trending topics based on keywords
        trends = []
        for kw in keywords:
            trends.append({
                'keyword': kw,
                'volume': 10000 + hash(kw) % 50000,
                'velocity': (hash(kw) % 100) / 10 + 5,  # % growth
                'sentiment': (hash(kw) % 200 - 100) / 200,  # -1 to 1
                'timestamp': datetime.now().isoformat(),
            })
        return sorted(trends, key=lambda x: x['volume'], reverse=True)
    
    def fetch_twitter_trends(self, keywords: List[str]) -> List[Dict]:
        """Fetch Twitter trending (simulated)"""
        trends = []
        for kw in keywords:
            trends.append({
                'keyword': kw,
                'volume': 5000 + hash(kw + 'tw') % 30000,
                'velocity': (hash(kw) % 80) / 10 + 3,
                'sentiment': (hash(kw) % 200 - 100) / 200,
                'tweets': 100 + hash(kw) % 5000,
                'timestamp': datetime.now().isoformat(),
            })
        return sorted(trends, key=lambda x: x['volume'], reverse=True)
    
    def fetch_youtube_trends(self, keywords: List[str]) -> List[Dict]:
        """Fetch YouTube trending (simulated)"""
        trends = []
        for kw in keywords:
            trends.append({
                'keyword': kw,
                'views': 50000 + hash(kw + 'yt') % 500000,
                'velocity': (hash(kw) % 100) / 10 + 2,
                'sentiment': (hash(kw) % 200 - 100) / 200,
                'engagement': (hash(kw) % 50) / 10 + 5,  # %
                'timestamp': datetime.now().isoformat(),
            })
        return sorted(trends, key=lambda x: x['views'], reverse=True)
    
    def analyze_trend_health(self, trend: Dict, platform: str) -> Dict:
        """Analyze if a trend is healthy/growing or dying"""
        velocity = trend.get('velocity', 0)
        volume = trend.get('volume', trend.get('views', 0))
        
        # Health score based on velocity and volume
        health_score = 0
        if velocity > 20:
            health_score += 3  # Hot
        elif velocity > 10:
            health_score += 2  # Growing
        elif velocity > 5:
            health_score += 1  # Stable
        
        if volume > 50000:
            health_score += 2
        elif volume > 10000:
            health_score += 1
        
        sentiment = trend.get('sentiment', 0)
        if sentiment > 0.3:
            health_score += 1
        elif sentiment < -0.3:
            health_score -= 1
        
        if health_score >= 5:
            status = "EXPLODING"
        elif health_score >= 3:
            status = "GROWING"
        elif health_score >= 1:
            status = "STABLE"
        elif health_score >= 0:
            status = "DECLINING"
        else:
            status = "DYING"
        
        return {
            'health_score': health_score,
            'status': status,
            'recommendation': self._get_recommendation(status, platform)
        }
    
    def _get_recommendation(self, status: str, platform: str) -> str:
        """Get action recommendation based on trend status"""
        recommendations = {
            'EXPLODING': f'Create content NOW - peak attention window ({platform})',
            'GROWING': f'Ride the wave - still time to capitalize ({platform})',
            'STABLE': f'Steady growth - consistent opportunity ({platform})',
            'DECLINING': f'Consider pivot - diminishing returns ({platform})',
            'DYING': f'Avoid new investment - trend ending ({platform})',
        }
        return recommendations.get(status, 'Monitor')
    
    def calculate_cross_platform_score(self, keyword: str, trends: Dict[str, List[Dict]]) -> Dict:
        """Calculate aggregated score across all platforms"""
        scores = []
        
        for platform, platform_trends in trends.items():
            weight = self.PLATFORMS.get(platform, {}).get('weight', 0.1)
            
            # Find keyword in platform trends
            matching = [t for t in platform_trends if keyword.lower() in t.get('keyword', '').lower()]
            
            if matching:
                trend = matching[0]
                health = self.analyze_trend_health(trend, platform)
                
                # Calculate platform-specific score
                volume = trend.get('volume', trend.get('views', 0))
                velocity = trend.get('velocity', 0)
                sentiment = trend.get('sentiment', 0)
                
                # Normalized score (0-100)
                platform_score = (
                    min(volume / 100000, 1) * 30 +  # Volume weight
                    min(velocity / 30, 1) * 30 +      # Velocity weight
                    (sentiment + 1) / 2 * 20 +       # Sentiment weight
                    health['health_score'] / 7 * 20  # Health weight
                ) * weight
                
                scores.append({
                    'platform': platform,
                    'score': platform_score,
                    'health': health,
                    'trend': trend
                })
        
        total_score = sum(s['score'] for s in scores)
        
        return {
            'keyword': keyword,
            'total_score': round(total_score, 2),
            'platform_breakdown': scores,
            'recommendation': self._aggregate_recommendation(scores)
        }
    
    def _aggregate_recommendation(self, scores: List[Dict]) -> str:
        """Aggregate recommendation from all platforms"""
        if not scores:
            return "No data available"
        
        statuses = [s['health']['status'] for s in scores]
        
        if all(s in ['EXPLODING', 'GROWING'] for s in statuses):
            return "🔥 HIGH PRIORITY - Cross-platform momentum!"
        elif 'EXPLODING' in statuses or statuses.count('GROWING') >= 2:
            return "📈 STRONG - Multiple platforms growing"
        elif 'GROWING' in statuses:
            return "📊 MODERATE - Some platform traction"
        elif 'STABLE' in statuses:
            return "⏸️ STABLE - Steady but not exciting"
        else:
            return "📉 CAUTION - Declining or no data"
    
    def predict_trend_lifespan(self, trend: Dict) -> Dict:
        """Predict how long a trend will last"""
        velocity = trend.get('velocity', 0)
        volume = trend.get('volume', 0)
        
        # Simple prediction model
        lifespan_days = 30  # baseline
        
        if velocity > 30:
            lifespan_days = 7  # Explodes fast, dies fast
        elif velocity > 20:
            lifespan_days = 14
        elif velocity > 10:
            lifespan_days = 30
        else:
            lifespan_days = 60
        
        # Adjust for volume
        if volume > 100000:
            lifespan_days *= 1.5  # Big trends last longer
        
        return {
            'predicted_lifespan_days': int(lifespan_days),
            'peak_window_days': int(lifespan_days / 3),
            'decay_rate': 'FAST' if velocity > 20 else 'MODERATE' if velocity > 10 else 'SLOW'
        }
    
    def generate_report(self, keywords: List[str], platforms: List[str]) -> Dict:
        """Generate comprehensive trend report"""
        trends = {}
        
        for platform in platforms:
            if platform == 'xhs':
                trends['xhs'] = self.fetch_xhs_trends(keywords)
            elif platform == 'twitter':
                trends['twitter'] = self.fetch_twitter_trends(keywords)
            elif platform == 'youtube':
                trends['youtube'] = self.fetch_youtube_trends(keywords)
        
        # Cross-platform analysis
        cross_platform = []
        for kw in keywords:
            score = self.calculate_cross_platform_score(kw, trends)
            if score['total_score'] > 0:
                cross_platform.append(score)
        
        # Sort by total score
        cross_platform.sort(key=lambda x: x['total_score'], reverse=True)
        
        # Top opportunities
        opportunities = []
        for cp in cross_platform[:5]:
            if cp['total_score'] > 20:
                opportunities.append({
                    'keyword': cp['keyword'],
                    'total_score'],
                   score': cp[' 'recommendation': cp['recommendation'],
                    'lifespan': self.predict_trend_lifespan(cp.get('platform_breakdown', [{}])[0].get('trend', {}))
                })
        
        return {
            'timestamp': datetime.now().isoformat(),
            'keywords': keywords,
            'platforms': platforms,
            'cross_platform_analysis': cross_platform[:10],
            'top_opportunities': opportunities,
            'platform_metrics': {
                p: {
                    'total_trends': len(trends.get(p, [])),
                    'avg_velocity': sum(t.get('velocity', 0) for t in trends.get(p, [])) / max(len(trends.get(p, [])), 1),
                    'avg_sentiment': sum(t.get('sentiment', 0) for t in trends.get(p, [])) / max(len(trends.get(p, [])), 1)
                } for p in trends.keys()
            }
        }

def format_report(report: Dict) -> str:
    """Format report for display"""
    output = f"""
📊 Trend Analytics Report
Generated: {report['timestamp']}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Top Opportunities:"""
    
    for opp in report.get('top_opportunities', []):
        lifespan = opp.get('lifespan', {})
        output += f"""
  {opp['keyword']}
    Score: {opp['score']:.1f}/100
    Recommendation: {opp['recommendation']}
    Predicted Lifespan: {lifespan.get('predicted_lifespan_days', 'N/A')} days
    Peak Window: {lifespan.get('peak_window_days', 'N/A')} days
    Decay Rate: {lifespan.get('decay_rate', 'N/A')}"""
    
    output += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 Platform Breakdown:"""
    
    for platform, metrics in report.get('platform_metrics', {}).items():
        platform_name = TrendAnalyzer.PLATFORMS.get(platform, {}).get('name', platform)
        output += f"""
  {platform_name}:
    Active Trends: {metrics['total_trends']}
    Avg Velocity: {metrics['avg_velocity']:.1f}%
    Avg Sentiment: {metrics['avg_sentiment']:.2f}"""
    
    return output

def main():
    parser = argparse.ArgumentParser(description="Multi-platform Trend Analytics")
    parser.add_argument("--keywords", "-k", type=str, required=True,
                        help="Comma-separated keywords to track")
    parser.add_argument("--platforms", "-p", type=str, default="xhs,twitter,youtube",
                        help="Comma-separated platforms (xhs,twitter,youtube,threads,reddit)")
    parser.add_argument("--json", action="store_true",
                        help="Output JSON")
    parser.add_argument("--top", type=int, default=5,
                        help="Number of top opportunities to show")
    
    args = parser.parse_args()
    
    keywords = [k.strip() for k in args.keywords.split(',')]
    platforms = [p.strip() for p in args.platforms.split(',')]
    
    analyzer = TrendAnalyzer()
    report = analyzer.generate_report(keywords, platforms)
    
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(format_report(report))

if __name__ == "__main__":
    main()
