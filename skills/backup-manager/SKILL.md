---
name: backup-manager
description: 备份管理 skill - 自动备份 OpenClaw 配置和 skills
version: 1.0.0
author: local
license: MIT
---

# Backup Manager Skill

## 功能
- 备份 OpenClaw 配置文件
- 备份已安装的 skills
- 备份工作空间文件
- 创建时间戳备份
- 恢复备份

## 使用方式

### 创建备份
```bash
# 创建备份目录
BACKUP_DIR="~/.openclaw/backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

# 备份配置
cp -r ~/.openclaw/openclaw.json "$BACKUP_DIR/"
cp -r ~/.openclaw/workspace "$BACKUP_DIR/"

# 备份 skills
cp -r ~/.openclaw/skills "$BACKUP_DIR/" 2>/dev/null || true

# 创建压缩包
cd ~/.openclaw/backups
tar -czf "backup_$(date +%Y%m%d_%H%M%S).tar.gz" "$(basename $BACKUP_DIR)"
```

### 列出备份
```bash
ls -lh ~/.openclaw/backups/
```

### 恢复备份
```bash
# 解压备份
cd ~/.openclaw/backups
tar -xzf backup_YYYYMMDD_HHMMSS.tar.gz

# 恢复文件（谨慎操作）
# cp -r backup_YYYYMMDD_HHMMSS/* ~/.openclaw/
```

## 自动备份计划

建议设置 cron job：
- 每日备份：凌晨 2:00
- 保留最近 7 天的备份
- 每周完整备份

## 备份内容

✅ openclaw.json（配置）
✅ workspace/（工作空间）
✅ skills/（已安装 skills）
✅ memory/（记忆文件）
