#!/usr/bin/env python3
"""
Memory Compression Script
- L1-daily > 7 days → L2-weekly
- L2-weekly > 30 days → L3-monthly
"""

import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

WORKSPACE = Path.home() / ".openclaw" / "workspace"
MEMORY_DIR = WORKSPACE / "memory"
LOG_FILE = MEMORY_DIR / "memory-cleanup-log.md"

def log(message):
    """Log to both console and file"""
    print(message)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"- [{timestamp}] {message}\n")

def compress_l1_to_l2():
    """Compress L1-daily files older than 7 days to L2-weekly"""
    l1_dir = MEMORY_DIR / "L1-daily"
    l2_dir = MEMORY_DIR / "L2-weekly"
    
    if not l1_dir.exists():
        log("L1-daily directory not found")
        return
    
    cutoff = datetime.now() - timedelta(days=7)
    compressed = 0
    
    for file in l1_dir.glob("*.md"):
        # Parse date from filename (YYYY-MM-DD.md)
        try:
            file_date = datetime.strptime(file.stem, "%Y-%m-%d")
            if file_date < cutoff:
                # Move to archive
                archive_dir = MEMORY_DIR / "archive" / "daily" / file.stem[:7]
                archive_dir.mkdir(parents=True, exist_ok=True)
                dest = archive_dir / file.name
                file.rename(dest)
                compressed += 1
                log(f"Archived L1: {file.name} → {dest.relative_to(MEMORY_DIR)}")
        except ValueError:
            continue
    
    log(f"L1→Archive: {compressed} files compressed")

def compress_l2_to_l3():
    """Compress L2-weekly files older than 30 days to L3-monthly"""
    l2_dir = MEMORY_DIR / "L2-weekly"
    l3_dir = MEMORY_DIR / "L3-monthly"
    
    if not l2_dir.exists():
        log("L2-weekly directory not found")
        return
    
    cutoff = datetime.now() - timedelta(days=30)
    compressed = 0
    
    for file in l2_dir.glob("*.md"):
        try:
            # Parse date from filename (YYYY-WXX.md)
            if file.stem.startswith("20") and "-W" in file.stem:
                # Weekly format, skip for now
                continue
            file_date = datetime.strptime(file.stem, "%Y-%m-%d")
            if file_date < cutoff:
                archive_dir = MEMORY_DIR / "archive" / "weekly"
                archive_dir.mkdir(parents=True, exist_ok=True)
                dest = archive_dir / file.name
                file.rename(dest)
                compressed += 1
                log(f"Archived L2: {file.name} → {dest.relative_to(MEMORY_DIR)}")
        except ValueError:
            continue
    
    log(f"L2→Archive: {compressed} files compressed")

def main():
    log("=== Memory Compression Started ===")
    compress_l1_to_l2()
    compress_l2_to_l3()
    log("=== Memory Compression Complete ===")

if __name__ == "__main__":
    main()
