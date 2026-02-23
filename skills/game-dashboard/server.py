#!/usr/bin/env python3
"""
OpenClaw Game Dashboard Server
A simple HTTP server with game-like dashboard UI
"""

import http.server
import socketserver
import json
import os
import sys
from datetime import datetime
from urllib.parse import urlparse, parse_qs

PORT = 8081
STATUS_FILE = os.path.dirname(os.path.abspath(__file__)) + "/status.json"

# Default status data
default_status = {
    "agents": [
        {"id": "agent-1", "name": "Research", "status": "idle", "task": "Waiting"},
        {"id": "agent-2", "name": "Writer", "status": "idle", "task": "Waiting"},
        {"id": "agent-3", "name": "Coder", "status": "idle", "task": "Waiting"},
        {"id": "agent-4", "name": "Monitor", "status": "idle", "task": "Waiting"}
    ],
    "system": {
        "cpu": 0,
        "memory": 0,
        "uptime": "0m"
    },
    "notifications": [],
    "activity": []
}

def load_status():
    """Load status from JSON file"""
    if os.path.exists(STATUS_FILE):
        try:
            with open(STATUS_FILE, 'r') as f:
                return json.load(f)
        except:
            return default_status.copy()
    return default_status.copy()

def save_status(data):
    """Save status to JSON file"""
    with open(STATUS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler for dashboard"""
    
    def do_GET(self):
        """Handle GET requests"""
        parsed = urlparse(self.path)
        
        if parsed.path == '/' or parsed.path == '/index.html':
            self.path = '/dashboard-tw.html'
        elif parsed.path == '/status':
            # Return JSON status
            status = load_status()
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(status).encode())
            return
        elif parsed.path == '/api/health':
            # Health check endpoint
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok"}).encode())
            return
            
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    
    def do_POST(self):
        """Handle POST requests for updates"""
        parsed = urlparse(self.path)
        
        if parsed.path == '/api/update':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body.decode())
            
            status = load_status()
            
            # Update agent
            if 'agent_id' in data:
                for agent in status['agents']:
                    if agent['id'] == data['agent_id']:
                        agent['status'] = data.get('status', agent['status'])
                        agent['task'] = data.get('task', agent['task'])
                        status['activity'].insert(0, {
                            "time": datetime.now().strftime("%H:%M:%S"),
                            "message": f"Agent {agent['name']} → {data.get('task', 'Updated')}"
                        })
                        break
            
            # Update system
            if 'cpu' in data:
                status['system']['cpu'] = data['cpu']
            if 'memory' in data:
                status['system']['memory'] = data['memory']
            
            # Add notification
            if 'notification' in data:
                status['notifications'].insert(0, {
                    "message": data['notification'],
                    "time": datetime.now().strftime("%H:%M:%S")
                })
                # Keep only last 5 notifications
                status['notifications'] = status['notifications'][:5]
            
            # Keep only last 20 activities
            status['activity'] = status['activity'][:20]
            
            save_status(status)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"success": True}).encode())
            return
        
        self.send_response(404)
        self.end_headers()

def main():
    """Main function"""
    # Initialize status file if not exists
    if not os.path.exists(STATUS_FILE):
        save_status(default_status)
    
    # Parse command line args
    if len(sys.argv) > 1:
        if sys.argv[1] == '--update':
            # Update agent status from CLI
            status = load_status()
            agent_id = sys.argv[2] if len(sys.argv) > 2 else "agent-1"
            task = sys.argv[3] if len(sys.argv) > 3 else "Updated"
            
            for agent in status['agents']:
                if agent['id'] == agent_id:
                    agent['status'] = 'active'
                    agent['task'] = task
                    break
            
            status['activity'].insert(0, {
                "time": datetime.now().strftime("%H:%M:%S"),
                "message": f"Updated {agent_id}: {task}"
            })
            status['activity'] = status['activity'][:20]
            save_status(status)
            print(f"✅ Updated {agent_id} → {task}")
            return
        
        elif sys.argv[1] == '--health':
            # Update system health from CLI
            status = load_status()
            status['system']['cpu'] = int(sys.argv[2]) if len(sys.argv) > 2 else 0
            status['system']['memory'] = int(sys.argv[3]) if len(sys.argv) > 3 else 0
            save_status(status)
            print(f"✅ Updated health: CPU {status['system']['cpu']}%, Mem {status['system']['memory']}%")
            return
        
        elif sys.argv[1] == '--notify':
            # Add notification from CLI
            status = load_status()
            msg = sys.argv[2] if len(sys.argv) > 2 else "Notification"
            status['notifications'].insert(0, {
                "message": msg,
                "time": datetime.now().strftime("%H:%M:%S")
            })
            status['notifications'] = status['notifications'][:5]
            save_status(status)
            print(f"✅ Notification: {msg}")
            return
    
    # Start HTTP server
    print(f"🎮 Starting OpenClaw Dashboard on http://localhost:{PORT}")
    print(f"📊 Dashboard: http://localhost:{PORT}/")
    print(f"📡 API: http://localhost:{PORT}/status")
    print(f"\nPress Ctrl+C to stop\n")
    
    with socketserver.TCPServer(("", PORT), DashboardHandler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    main()
