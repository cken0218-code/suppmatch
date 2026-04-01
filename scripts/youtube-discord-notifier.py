#!/usr/bin/env python3
"""
YouTube Workflow Discord Notifier
================================
Send automated notifications to Discord when YouTube scripts are generated.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
import requests

class YouTubeDiscordNotifier:
    """Send YouTube workflow notifications to Discord."""
    
    def __init__(self, workspace_dir="/Users/cken0218/.openclaw/workspace"):
        self.workspace_dir = Path(workspace_dir)
        self.youtube_scripts_dir = self.workspace_dir / "youtube-scripts"
        self.discord_token = os.getenv("DISCORD_BOT_TOKEN")  # 从环境变量获取
        self.discord_user_id = "964140590868594740"
        
    def send_discord_message(self, content: str, embed=None) -> bool:
        """Send message to Discord DM."""
        url = f"https://discord.com/api/v10/users/@me/channels"
        
        # Create DM channel
        headers = {
            "Authorization": f"Bot {self.discord_token}",
            "Content-Type": "application/json"
        }
        
        try:
            # Create DM channel
            response = requests.post(url, json={"recipient_id": self.discord_user_id}, headers=headers)
            response.raise_for_status()
            dm_channel = response.json()
            dm_id = dm_channel["id"]
            
            # Send message
            message_url = f"https://discord.com/api/v10/channels/{dm_id}/messages"
            payload = {"content": content}
            
            if embed:
                payload["embeds"] = [embed]
            
            message_response = requests.post(message_url, json=payload, headers=headers)
            message_response.raise_for_status()
            return True
            
        except requests.RequestException as e:
            print(f"Error sending Discord message: {e}")
            return False
    
    def read_notification_file(self, filename: str) -> dict:
        """Read and parse notification file."""
        notification_path = self.youtube_scripts_dir / filename
        if not notification_path.exists():
            return None
            
        with open(notification_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        return {
            "filename": filename,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "generated_date": filename.split('-')[1] if '-' in filename else str(datetime.now().date())
        }
    
    def create_notification_embed(self, notification_data: dict) -> dict:
        """Create Discord embed for YouTube notification."""
        content = notification_data["content"]
        
        # Extract key information from notification
        title_match = content.find("🎯 **題目**：")
        if title_match != -1:
            title_end = content.find("\n", title_match)
            title = content[title_match+7:title_end]
        else:
            title = "Unknown Topic"
        
        score_match = content.find("📊 **潛力分數**：")
        if score_match != -1:
            score_end = content.find("\n", score_match)
            score = content[score_match+7:score_end]
        else:
            score = "N/A"
        
        # Create embed
        embed = {
            "title": "🎬 YouTube Script Generated",
            "description": f"**{title}**",
            "color": 0x3498db,
            "fields": [
                {
                    "name": "📊 Quality Score",
                    "value": score,
                    "inline": True
                },
                {
                    "name": "📅 Generated",
                    "value": notification_data["generated_date"],
                    "inline": True
                },
                {
                    "name": "📄 Script File",
                    "value": f"`{notification_data['filename']}`",
                    "inline": True
                }
            ],
            "footer": {
                "text": "YouTube Workflow Automation",
                "icon_url": "https://static-00.iconduck.com/assets.00/youtube-icon-2048x2048-ku6j0smp.png"
            },
            "timestamp": notification_data["timestamp"]
        }
        
        return embed
    
    def send_youtube_notification(self, notification_filename: str) -> bool:
        """Send notification for generated YouTube script."""
        notification_data = self.read_notification_file(notification_filename)
        if not notification_data:
            print(f"Notification file not found: {notification_filename}")
            return False
        
        embed = self.create_notification_embed(notification_data)
        message = f"🎬 **New YouTube Script Generated**\n\nYour automated YouTube workflow has generated a new script!"
        
        return self.send_discord_message(message, embed)
    
    def send_daily_summary(self, date: str = None) -> bool:
        """Send daily summary of generated scripts."""
        if not date:
            date = datetime.now().strftime("%Y-%m-%d")
        
        # Count scripts generated today
        script_files = list(self.youtube_scripts_dir.glob(f"script-{date}-*.md"))
        notification_files = list(self.youtube_scripts_dir.glob(f"notification-{date}-*.txt"))
        
        if not script_files and not notification_files:
            return False
        
        embed = {
            "title": "📊 YouTube Workflow Daily Summary",
            "description": f"Daily summary for {date}",
            "color": 0x2ecc71,
            "fields": [
                {
                    "name": "📄 Scripts Generated",
                    "value": str(len(script_files)),
                    "inline": True
                },
                {
                    "name": "🔔 Notifications Sent",
                    "value": str(len(notification_files)),
                    "inline": True
                }
            ],
            "footer": {
                "text": "YouTube Workflow Automation"
            },
            "timestamp": datetime.now().isoformat()
        }
        
        message = f"📊 **Daily YouTube Summary**\n\nYour YouTube automation system generated {len(script_files)} scripts today!"
        
        return self.send_discord_message(message, embed)

def main():
    """Main function - can be called from cron job."""
    notifier = YouTubeDiscordNotifier()
    
    # Check for latest notification file
    notification_files = list(notifier.youtube_scripts_dir.glob("notification-*.txt"))
    if notification_files:
        latest_file = max(notification_files, key=os.path.getctime)
        print(f"Processing notification: {latest_file.name}")
        
        success = notifier.send_youtube_notification(latest_file.name)
        if success:
            print(f"✅ Successfully sent Discord notification for {latest_file.name}")
        else:
            print(f"❌ Failed to send Discord notification for {latest_file.name}")
    else:
        print("No new notification files found")

if __name__ == "__main__":
    main()