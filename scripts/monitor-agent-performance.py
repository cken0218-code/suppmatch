#!/usr/bin/env python3
"""
Agent Performance Monitoring System
Created: 2026-03-13
Purpose: Track and monitor agent performance metrics
"""

import json
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

# Configuration
MEMORY_DIR = Path.home() / ".openclaw" / "workspace" / "memory"
REPORTS_DIR = MEMORY_DIR / "reports"
PERFORMANCE_FILE = MEMORY_DIR / "agent-performance.json"

# Ensure directories exist
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# Agent definitions (from ai-company-architecture.md)
AGENTS = {
    "ken-main": {"name": "Ken (Main)", "model": "GLM-5", "level": "Command"},
    "operations-agent": {"name": "Operations Agent", "model": "MiniMax", "level": "Operations"},
    "youtube-agent": {"name": "YouTube Agent", "model": "GLM-5", "level": "Content"},
    "newsletter-agent": {"name": "Newsletter Agent", "model": "GLM-5", "level": "Content"},
    "blog-agent": {"name": "Blog Agent", "model": "GLM-5", "level": "Content"},
    "affiliate-agent": {"name": "Affiliate Agent", "model": "GLM-5", "level": "Content"},
    "stock-agent": {"name": "Stock Agent", "model": "MiniMax", "level": "Research"},
    "crypto-agent": {"name": "Crypto Agent", "model": "MiniMax", "level": "Research"},
    "research-agent": {"name": "Research Agent", "model": "GLM-5", "level": "Research"},
    "evolution-agent": {"name": "Evolution Agent", "model": "GLM-5", "level": "Infrastructure"},
    "mcp-agent": {"name": "MCP Agent", "model": "GLM-5", "level": "Infrastructure"},
    "qa-agent": {"name": "QA Agent", "model": "GLM-5", "level": "QA"},
    "rd-agent": {"name": "R&D Agent", "model": "GLM-5", "level": "QA"},
    "integration-agent": {"name": "Integration Agent", "model": "MiniMax", "level": "QA"},
}

def load_performance_data():
    """Load existing performance data"""
    try:
        with open(PERFORMANCE_FILE, 'r') as f:
            return json.load(f)
    except:
        return {
            "agents": {},
            "last_updated": "",
            "daily_stats": []
        }

def save_performance_data(data):
    """Save performance data"""
    data["last_updated"] = datetime.now().isoformat()
    with open(PERFORMANCE_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def initialize_agent(agent_id):
    """Initialize performance tracking for an agent"""
    if agent_id not in AGENTS:
        return None

    return {
        "name": AGENTS[agent_id]["name"],
        "model": AGENTS[agent_id]["model"],
        "level": AGENTS[agent_id]["level"],
        "tasks_completed": 0,
        "tasks_failed": 0,
        "total_time_seconds": 0,
        "total_tokens_in": 0,
        "total_tokens_out": 0,
        "errors": [],
        "last_task": "",
        "average_time": 0,
        "success_rate": 100.0
    }

def record_task(agent_id, success=True, time_seconds=0, tokens_in=0, tokens_out=0, error=None):
    """Record a task execution"""
    data = load_performance_data()

    # Initialize agent if needed
    if agent_id not in data["agents"]:
        data["agents"][agent_id] = initialize_agent(agent_id)

    if not data["agents"][agent_id]:
        return

    agent = data["agents"][agent_id]

    # Update metrics
    if success:
        agent["tasks_completed"] += 1
    else:
        agent["tasks_failed"] += 1
        if error:
            agent["errors"].append({
                "error": str(error),
                "timestamp": datetime.now().isoformat()
            })
            # Keep only last 10 errors
            agent["errors"] = agent["errors"][-10:]

    agent["total_time_seconds"] += time_seconds
    agent["total_tokens_in"] += tokens_in
    agent["total_tokens_out"] += tokens_out
    agent["last_task"] = datetime.now().isoformat()

    # Calculate averages
    total_tasks = agent["tasks_completed"] + agent["tasks_failed"]
    if total_tasks > 0:
        agent["average_time"] = agent["total_time_seconds"] / total_tasks
        agent["success_rate"] = (agent["tasks_completed"] / total_tasks) * 100

    save_performance_data(data)

def generate_daily_report():
    """Generate daily performance report"""
    data = load_performance_data()

    if not data["agents"]:
        return "❌ No agent data available"

    today = datetime.now().strftime("%Y-%m-%d")
    report_lines = [
        f"# Agent Performance Report - {today}",
        "",
        "## 📊 Overall Statistics",
        "",
        f"- **Total Agents**: {len(data['agents'])}",
        f"- **Last Updated**: {data['last_updated']}",
        "",
        "## 🤖 Agent Performance",
        "",
        "| Agent | Tasks | Success Rate | Avg Time | Tokens | Status |",
        "|-------|-------|--------------|----------|--------|--------|"
    ]

    # Sort agents by tasks completed
    sorted_agents = sorted(
        data["agents"].items(),
        key=lambda x: x[1]["tasks_completed"],
        reverse=True
    )

    for agent_id, agent in sorted_agents:
        tasks = agent["tasks_completed"] + agent["tasks_failed"]
        success_rate = f"{agent['success_rate']:.1f}%"
        avg_time = f"{agent['average_time']:.1f}s"
        total_tokens = (agent["total_tokens_in"] + agent["total_tokens_out"]) / 1000
        tokens_str = f"{total_tokens:.1f}K"

        # Determine status
        if agent["success_rate"] >= 95:
            status = "✅"
        elif agent["success_rate"] >= 80:
            status = "⚠️"
        else:
            status = "❌"

        report_lines.append(
            f"| {agent['name']} | {tasks} | {success_rate} | {avg_time} | {tokens_str} | {status} |"
        )

    report_lines.extend([
        "",
        "## 📈 Top Performers",
        ""
    ])

    # Top 3 by tasks completed
    top_agents = sorted_agents[:3]
    for i, (agent_id, agent) in enumerate(top_agents, 1):
        report_lines.append(
            f"{i}. **{agent['name']}** - {agent['tasks_completed']} tasks completed"
        )

    report_lines.extend([
        "",
        "## ⚠️ Agents Needing Attention",
        ""
    ])

    # Agents with success rate < 80%
    low_performers = [
        (agent_id, agent) for agent_id, agent in sorted_agents
        if agent["success_rate"] < 80
    ]

    if low_performers:
        for agent_id, agent in low_performers:
            report_lines.append(
                f"- **{agent['name']}**: {agent['success_rate']:.1f}% success rate"
            )
            if agent["errors"]:
                report_lines.append(f"  - Last error: {agent['errors'][-1]['error']}")
    else:
        report_lines.append("✅ All agents performing well!")

    # Save report
    report_file = REPORTS_DIR / f"agent-performance-{today}.md"
    with open(report_file, 'w') as f:
        f.write("\n".join(report_lines))

    return report_file

def print_summary():
    """Print summary to console"""
    data = load_performance_data()

    print("📊 Agent Performance Summary")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"Last Updated: {data['last_updated']}\n")

    if not data["agents"]:
        print("❌ No agent data available")
        return

    # Sort by tasks completed
    sorted_agents = sorted(
        data["agents"].items(),
        key=lambda x: x[1]["tasks_completed"],
        reverse=True
    )

    print("Top 5 Agents by Tasks Completed:\n")
    for i, (agent_id, agent) in enumerate(sorted_agents[:5], 1):
        tasks = agent["tasks_completed"] + agent["tasks_failed"]
        print(f"{i}. {agent['name']}")
        print(f"   Tasks: {tasks} | Success: {agent['success_rate']:.1f}% | Time: {agent['average_time']:.1f}s")

    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    # Generate report
    report_file = generate_daily_report()
    print(f"✅ Full report saved to: {report_file}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "record" and len(sys.argv) >= 5:
            # Record a task: python3 script.py record <agent_id> <success> <time> <tokens_in> <tokens_out>
            agent_id = sys.argv[2]
            success = sys.argv[3].lower() == "true"
            time_seconds = float(sys.argv[4])
            tokens_in = int(sys.argv[5]) if len(sys.argv) > 5 else 0
            tokens_out = int(sys.argv[6]) if len(sys.argv) > 6 else 0
            record_task(agent_id, success, time_seconds, tokens_in, tokens_out)

        elif command == "report":
            report_file = generate_daily_report()
            print(f"✅ Report generated: {report_file}")

    else:
        # Default: print summary
        print_summary()
