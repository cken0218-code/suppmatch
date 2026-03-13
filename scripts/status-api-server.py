#!/usr/bin/env python3
"""
Ken AI Status API Server
Created: 2026-03-13
Purpose: Provide real-time API for dashboard monitoring
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from datetime import datetime
from pathlib import Path
import os

# Configuration
PORT = 18790
WORKSPACE = Path.home() / ".openclaw" / "workspace"
MEMORY_DIR = WORKSPACE / "memory"
STATUS_FILE = MEMORY_DIR / "ken-status.json"

class StatusHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers(200)

    def do_GET(self):
        if self.path == '/api/status':
            self._handle_status()
        elif self.path == '/api/health':
            self._handle_health()
        elif self.path == '/api/tasks':
            self._handle_tasks()
        elif self.path == '/api/models':
            self._handle_models()
        elif self.path == '/api/activity':
            self._handle_activity()
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not found"}).encode())

    def do_POST(self):
        if self.path == '/api/update':
            self._handle_update()
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Not found"}).encode())

    def _handle_status(self):
        """Get full status"""
        try:
            with open(STATUS_FILE, 'r') as f:
                status = json.load(f)
            self._set_headers(200)
            self.wfile.write(json.dumps(status, ensure_ascii=False).encode())
        except Exception as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def _handle_health(self):
        """Health check"""
        self._set_headers(200)
        self.wfile.write(json.dumps({
            "status": "ok",
            "timestamp": datetime.now().isoformat(),
            "server": "Ken AI Status API"
        }).encode())

    def _handle_tasks(self):
        """Get task queue"""
        try:
            with open(STATUS_FILE, 'r') as f:
                status = json.load(f)
            self._set_headers(200)
            self.wfile.write(json.dumps({
                "active": status.get("activeTasks", []),
                "queue": status.get("taskQueue", []),
                "completed": status.get("completedTasks", [])
            }, ensure_ascii=False).encode())
        except Exception as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def _handle_models(self):
        """Get model status"""
        try:
            with open(STATUS_FILE, 'r') as f:
                status = json.load(f)
            self._set_headers(200)
            self.wfile.write(json.dumps(status.get("models", {}), ensure_ascii=False).encode())
        except Exception as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def _handle_activity(self):
        """Get recent activity"""
        try:
            with open(STATUS_FILE, 'r') as f:
                status = json.load(f)
            self._set_headers(200)
            self.wfile.write(json.dumps({
                "recentActions": status.get("recentActions", []),
                "currentAction": status.get("currentAction", "闲置")
            }, ensure_ascii=False).encode())
        except Exception as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def _handle_update(self):
        """Update status (called by Ken AI)"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            update = json.loads(post_data.decode())

            # Read current status
            try:
                with open(STATUS_FILE, 'r') as f:
                    status = json.load(f)
            except:
                status = {}

            # Update status
            status.update(update)
            status["lastUpdated"] = datetime.now().isoformat()

            # Save status
            with open(STATUS_FILE, 'w') as f:
                json.dump(status, f, indent=2, ensure_ascii=False)

            self._set_headers(200)
            self.wfile.write(json.dumps({"success": True}).encode())
        except Exception as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({"error": str(e)}).encode())

    def log_message(self, format, *args):
        # Suppress default logging
        pass

def run_server():
    # Ensure memory directory exists
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)

    # Initialize status file if not exists
    if not STATUS_FILE.exists():
        initial_status = {
            "server": "Ken AI Status API",
            "version": "1.0",
            "lastUpdated": datetime.now().isoformat(),
            "currentAction": "闲置",
            "activeTasks": [],
            "taskQueue": [],
            "completedTasks": [],
            "recentActions": [],
            "models": {
                "glm5": {
                    "name": "GLM-5",
                    "status": "idle",
                    "context": 0,
                    "messages": 0,
                    "lastUsed": None
                },
                "minimax": {
                    "name": "MiniMax 2.5",
                    "status": "idle",
                    "context": 0,
                    "messages": 0,
                    "lastUsed": None
                }
            },
            "stats": {
                "totalMessages": 0,
                "tasksCompleted": 0,
                "tokensUsed": 0,
                "uptime": 0
            }
        }
        with open(STATUS_FILE, 'w') as f:
            json.dump(initial_status, f, indent=2, ensure_ascii=False)

    server = HTTPServer(('0.0.0.0', PORT), StatusHandler)
    print(f"🚀 Ken AI Status API running on http://0.0.0.0:{PORT}")
    print(f"📊 Dashboard can connect to: http://127.0.0.1:{PORT}")
    print(f"📝 Status file: {STATUS_FILE}")
    print("")
    print("API Endpoints:")
    print(f"  - GET  http://127.0.0.1:{PORT}/api/status")
    print(f"  - GET  http://127.0.0.1:{PORT}/api/tasks")
    print(f"  - GET  http://127.0.0.1:{PORT}/api/models")
    print(f"  - GET  http://127.0.0.1:{PORT}/api/activity")
    print(f"  - POST http://127.0.0.1:{PORT}/api/update")
    print("")
    print("Press Ctrl+C to stop")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Server stopped")
        server.shutdown()

if __name__ == "__main__":
    run_server()
