#!/usr/bin/env python3
"""
compress-memory.py - 自動壓縮記憶系統
用途：將舊的 L1-daily 壓縮到 L2-weekly，L2-weekly 壓縮到 L3-monthly
"""

import os
import shutil
from datetime import datetime, timedelta
from pathlib import Path

# 配置
WORKSPACE = Path.home() / ".openclaw" / "workspace"
MEMORY_DIR = WORKSPACE / "memory"
L1_DIR = MEMORY_DIR / "L1-daily"
L2_DIR = MEMORY_DIR / "L2-weekly"
L3_DIR = MEMORY_DIR / "L3-monthly"
LOG_FILE = MEMORY_DIR / "memory-cleanup-log.md"

def get_file_age_days(file_path):
    """計算檔案年齡（天數）"""
    mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
    age = datetime.now() - mtime
    return age.days

def compress_files(source_dir, target_dir, max_age_days, compress_type):
    """
    壓縮超過指定天數的檔案

    Args:
        source_dir: 來源目錄
        target_dir: 目標目錄
        max_age_days: 最大天數
        compress_type: 壓縮類型（weekly/monthly）
    """
    if not source_dir.exists():
        print(f"⚠️ 來源目錄不存在: {source_dir}")
        return 0

    compressed_count = 0

    for file_path in source_dir.glob("*.md"):
        age_days = get_file_age_days(file_path)

        if age_days > max_age_days:
            # 創建目標目錄
            target_dir.mkdir(parents=True, exist_ok=True)

            # 移動檔案
            target_path = target_dir / file_path.name
            shutil.move(str(file_path), str(target_path))

            print(f"✅ 壓縮: {file_path.name} → {target_dir.name}/ (年齡: {age_days}天)")
            compressed_count += 1

    return compressed_count

def update_cleanup_log(l1_compressed, l2_compressed):
    """更新清理日誌"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"""
## {timestamp} - 自動壓縮

- L1-daily → L2-weekly: {l1_compressed} 個檔案
- L2-weekly → L3-monthly: {l2_compressed} 個檔案
- 總共壓縮: {l1_compressed + l2_compressed} 個檔案

---
"""

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

    print(f"📝 已更新清理日誌: {LOG_FILE}")

def main():
    print("🔄 開始記憶壓縮...")
    print(f"📂 工作目錄: {WORKSPACE}")
    print()

    # 壓縮 L1-daily → L2-weekly（超過7天）
    print("📦 壓縮 L1-daily → L2-weekly（>7天）")
    l1_compressed = compress_files(L1_DIR, L2_DIR, 7, "weekly")
    print(f"   壓縮了 {l1_compressed} 個檔案")
    print()

    # 壓縮 L2-weekly → L3-monthly（超過30天）
    print("📦 壓縮 L2-weekly → L3-monthly（>30天）")
    l2_compressed = compress_files(L2_DIR, L3_DIR, 30, "monthly")
    print(f"   壓縮了 {l2_compressed} 個檔案")
    print()

    # 更新日誌
    update_cleanup_log(l1_compressed, l2_compressed)

    print("✨ 記憶壓縮完成！")
    print(f"   總共壓縮: {l1_compressed + l2_compressed} 個檔案")

if __name__ == "__main__":
    main()
