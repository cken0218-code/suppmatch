# TOOLS.md - Local Notes

> **Last Updated**: 2026-02-23

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

---

## 🖥️ 系統信息

### 主機
- **Name**: lau的Mac mini
- **Hostname**: laudeMac-mini.local
- **OS**: macOS Darwin 25.3.0 (arm64)
- **Shell**: zsh
- **Timezone**: Asia/Taipei (CST +0800)

### Runtime
- **Node**: v22.22.0
- **Python**: 3.9.6
- **OpenClaw**: 2026.2.22-2

---

## 🔗 SSH / Remote

### Nodes
- **lau的Mac mini** (local) → Primary workstation

### 常用命令
```bash
# OpenClaw status
openclaw status

# Gateway control
openclaw gateway status
openclaw gateway restart

# Config edit
code ~/.openclaw/openclaw.json
```

---

## 💬 通訊渠道

### Discord
- **User**: ken000ken
- **User ID**: 964140590868594740
- **主要通知渠道**: Discord DM

### 其他渠道
- Signal（已配置）
- Telegram（已配置）

---

## 🤖 Models

### 主要 Models
| Model | Provider | 用途 |
|-------|----------|------|
| GLM-5 | Zai | 复杂任务 |
| MiniMax-M2.5 | MiniMax | 日常对话 |

### Aliases
- `glm-5` → zai/glm-5
- `minimax` → minimax-portal/MiniMax-M2.5

---

## 🎤 TTS

### 预设
- **Language**: Cantonese/Chinese
- **Speed**: Normal

---

## 📂 重要路径

### OpenClaw
- **Config**: `~/.openclaw/openclaw.json`
- **Workspace**: `~/.openclaw/workspace`
- **Logs**: `/tmp/openclaw/openclaw-*.log`
- **Gateway Log**: `~/.openclaw/logs/gateway.log`

### Memory
- **L0-core**: `~/.openclaw/workspace/memory/L0-core.md`
- **L1-daily**: `~/.openclaw/workspace/memory/L1-daily/`
- **Learning**: `~/.openclaw/workspace/memory/learning/`
- **Projects**: `~/.openclaw/workspace/memory/projects/`

### Skills
- **Local Skills**: `~/.openclaw/workspace/skills/`
- **Count**: ~47 个

### Backup
- **Location**: `~/backup/`
- **Latest**: `openclaw-core-backup-20260223-175708.tar.gz`

---

## 🔐 API Keys 位置

**所有 API Keys 都喺**: `~/.openclaw/openclaw.json`

- YouTube Data API ✅
- Brave Search ✅
- X (Twitter) API ✅
- MiniMax API ✅
- Composio ✅

**⚠️ 注意**: 唔好喺任何 log 或回复中暴露 API keys

---

## 🛠️ 常用脚本

### 记忆压缩
```bash
python3 scripts/compress-memory.py
```

### Backup
```bash
tar -czf ~/backup/openclaw-backup-$(date +%Y%m%d).tar.gz \
  -C ~/.openclaw/workspace \
  AGENTS.md SOUL.md USER.md MEMORY.md HEARTBEAT.md TOOLS.md IDENTITY.md
```

### Git Commit
```bash
cd ~/.openclaw/workspace
git add -A
git commit -m "docs: update [file] - [reason]"
```

---

## 📊 Quota 监控

### Brave API
- **Limit**: 2000 requests/month
- **Current**: Check `memory/quota-state.json`
- **Rule**: >80% 就停止搜寻

---

## 🎯 技能索引

### 常用 Skills
- `stock-agent` - 澳股分析
- `youtube-agent` - YouTube 自动化
- `research-agent` - 研究助手
- `skill-scanner` - ClawHub 扫描
- `cron-manager` - 定时任务
- `system-monitor` - 系统监控
- `backup-manager` - 备份管理

### 查询方式
```
有冇新嘅 skills？ → skill-scanner
上次发现咩？ → skill-history
```

---

*This is your cheat sheet. Keep it updated.*
