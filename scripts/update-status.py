#!/usr/bin/env python3
"""
Ken AI Status Updater
Created: 2026-03-13
Purpose: Update Ken AI status for dashboard monitoring
"""

import json
import sys
from datetime import datetime
from pathlib import Path
import requests

# Configuration
API_URL = "http://127.0.0.1:18790/api/update"
STATUS_FILE = Path.home() / ".openclaw" / "workspace" / "memory" / "ken-status.json"

def update_status(action=None, task=None, model=None, stats=None):
    """Update Ken AI status"""
    update = {}

    if action:
        update["currentAction"] = action

    if task:
        # Add to active tasks
        try:
            with open(STATUS_FILE, 'r') as f:
                status = json.load(f)
        except:
            status = {"activeTasks": [], "completedTasks": [], "recentActions": []}

        if task.get("status") == "active":
            # Add or update active task
            found = False
            for i, t in enumerate(status.get("activeTasks", [])):
                if t.get("id") == task.get("id"):
                    status["activeTasks"][i] = task
                    found = True
                    break
            if not found:
                status.setdefault("activeTasks", []).append(task)
        elif task.get("status") == "completed":
            # Move to completed
            status["activeTasks"] = [t for t in status.get("activeTasks", []) if t.get("id") != task.get("id")]
            status.setdefault("completedTasks", []).insert(0, task)
            # Keep only last 50 completed tasks
            status["completedTasks"] = status["completedTasks"][:50]
        elif task.get("status") == "queued":
            # Add to queue
            status.setdefault("taskQueue", []).append(task)

        # Add to recent actions
        recent = {
            "action": task.get("name", "Unknown task"),
            "model": task.get("model", "Unknown"),
            "timestamp": datetime.now().isoformat(),
            "status": task.get("status", "active")
        }
        status.setdefault("recentActions", []).insert(0, recent)
        status["recentActions"] = status["recentActions"][:20]  # Keep last 20

        update["activeTasks"] = status.get("activeTasks", [])
        update["taskQueue"] = status.get("taskQueue", [])
        update["completedTasks"] = status.get("completedTasks", [])
        update["recentActions"] = status.get("recentActions", [])

    if model:
        update["models"] = model

    if stats:
        update["stats"] = stats

    update["lastUpdated"] = datetime.now().isoformat()

    # Try API first
    try:
        response = requests.post(API_URL, json=update, timeout=2)
        if response.status_code == 200:
            return True
    except:
        pass

    # Fallback: direct file update
    try:
        try:
            with open(STATUS_FILE, 'r') as f:
                status = json.load(f)
        except:
            status = {}

        status.update(update)

        with open(STATUS_FILE, 'w') as f:
            json.dump(status, f, indent=2, ensure_ascii=False)

        return True
    except Exception as e:
        print(f"Error updating status: {e}", file=sys.stderr)
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 update-status.py action '<action>'")
        print("  python3 update-status.py task '<json>'")
        print("  python3 update-status.py model '<json>'")
        print("  python3 update-status.py stats '<json>'")
        sys.exit(1)

    command = sys.argv[1]

    if command == "action" and len(sys.argv) > 2:
        action = sys.argv[2]
        success = update_status(action=action)
        print(f"✅ Action updated: {action}" if success else "❌ Failed to update")

    elif command == "task" and len(sys.argv) > 2:
        task = json.loads(sys.argv[2])
        success = update_status(task=task)
        print(f"✅ Task updated: {task.get('name', 'Unknown')}" if success else "❌ Failed to update")

    elif command == "model" and len(sys.argv) > 2:
        model = json.loads(sys.argv[2])
        success = update_status(model=model)
        print(f"✅ Model updated" if success else "❌ Failed to update")

    elif command == "stats" and len(sys.argv) > 2:
        stats = json.loads(sys.argv[2])
        success = update_status(stats=stats)
        print(f"✅ Stats updated" if success else "❌ Failed to update")

    else:
        print("Invalid command or missing arguments")
        sys.exit(1)

if __name__ == "__main__":
    main()
