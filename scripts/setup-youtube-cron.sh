#!/bin/bash

# YouTube Automation Cron Job Setup
# This script sets up automated YouTube content generation

CRON_JOB="0 10 * * 1,3,5 cd /Users/cken0218/.openclaw/workspace && /usr/bin/python3 skills/youtube-workflow-local/run.py >> logs/youtube-workflow.log 2>&1"

# Create temporary cron file
echo "Setting up YouTube automation cron job..."
echo "$CRON_JOB" > /tmp/youtube_cron.txt

# Install cron job
crontab /tmp/youtube_cron.txt

# Clean up
rm -f /tmp/youtube_cron.txt

echo "✅ YouTube automation cron job set up successfully!"
echo "Schedule: Every Monday, Wednesday, Friday at 10:00 AM"
echo "Log file: logs/youtube-workflow.log"