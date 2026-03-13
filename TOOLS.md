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
| Model | Provider | 用途 | 状态 |
|-------|----------|------|------|
| MiniMax-M2.1 | MiniMax | 日常对话（推荐）| ✅ 稳定 |
| GLM-5 | Zai | 复杂任务 | ⚠️ 偶尔 timeout |
| MiniMax-M2.5 | MiniMax | ❌ 不支持 | 当前计划不支持 |

### 默认配置（已更新 2026-03-13）
- **Primary**: MiniMax-M2.1
- **Fallback**: GLM-5

### Aliases
- `minimax` → minimax-portal/MiniMax-M2.1（更新）
- `glm-5` → zai/glm-5
- `minimax-m2.5` → ❌ 不可用

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

### Backup（自动）
```bash
# 手动 backup
tar -czf ~/backup/openclaw-backup-$(date +%Y%m%d).tar.gz \
  -C ~/.openclaw/workspace \
  AGENTS.md SOUL.md USER.md MEMORY.md HEARTBEAT.md TOOLS.md IDENTITY.md

# 自动 backup（cron）
# 每日 00:00 执行
0 0 * * * cd ~/.openclaw/workspace && tar -czf ~/backup/openclaw-auto-$(date +\%Y\%m\%d).tar.gz AGENTS.md SOUL.md USER.md MEMORY.md HEARTBEAT.md TOOLS.md IDENTITY.md memory/ && git add -A && git commit -m "chore: daily backup $(date +\%Y\%m\%d)" && git push origin main
```

### Git Commit
```bash
cd ~/.openclaw/workspace
git add -A
git commit -m "docs: update [file] - [reason]"
git push origin main
```

### 自动化 Backup 设置
```bash
# 编辑 crontab
crontab -e

# 加这一行（每日 00:00）
0 0 * * * cd /Users/cken0218/.openclaw/workspace && tar -czf ~/backup/openclaw-auto-$(date +\%Y\%m\%d).tar.gz AGENTS.md SOUL.md USER.md MEMORY.md HEARTBEAT.md TOOLS.md IDENTITY.md memory/ 2>/dev/null && git add -A && git commit -m "chore: daily backup" && git push origin main 2>/dev/null
```

---

## 🌐 瀏覽器工具

### 可用工具

| 工具 | 狀態 | 用途 | 限制 |
|------|------|------|------|
| **Chrome Extension Relay** | ✅ 可用 | 操作已登入的 Chrome tabs | 需要用户点击 extension attach tab |
| **OpenClaw Browser** | ✅ 可用 | 独立浏览器 | Playwright 功能受限（无 act/click） |
| **web_fetch** | ✅ 可用 | 轻量级抓取 | 只支持静态页面，无法处理 JS |
| **AppleScript** | ✅ 可用 | macOS 自动化 | 需要权限，可能不稳定 |

### 檢查步驟（遇到瀏覽器任務時）

```bash
# 1. 檢查 Chrome tabs（如果已 attach）
browser action=tabs profile=chrome

# 2. 檢查 OpenClaw browser 狀態
browser action=status profile=openclaw

# 3. 如果都唔得 → 用 web_fetch
web_fetch url="..."
```

### 優先順序

1. **Chrome Extension Relay**（最快，已有登录状态）
2. **OpenClaw Browser**（独立，需要重新登录）
3. **web_fetch**（轻量，静态页面）
4. **AppleScript**（最后手段）

### 已知限制

- **Playwright 不可用**：无法使用 `act:click`、`act:type`、`snapshot`
- **可用功能**：`screenshot`、`open`、`tabs`、`focus`
- **变通方法**：用截图 + 图像识别 + AppleScript 模拟点击

---

## 📊 Quota 监控

### Brave API
- **Limit**: 2000 requests/month
- **Current**: Check `memory/quota-state.json`
- **Rule**: >80% 就停止搜寻

---

## 🎯 技能索引（含安装）

### 常用 Skills

| Skill | 用途 | 安装方式 | 状态 |
|-------|------|----------|------|
| `stock-agent` | 澳股分析 | 已安装（本地） | ✅ |
| `youtube-agent` | YouTube 自动化 | 已安装（本地） | ✅ |
| `research-agent` | 研究助手 | 已安装（本地） | ✅ |
| `skill-scanner` | ClawHub 扫描 | `clawhub install skill-scanner` | ✅ |
| `cron-manager` | 定时任务 | `clawhub install cron-manager` | ✅ |
| `system-monitor` | 系统监控 | `clawhub install system-monitor` | ✅ |
| `backup-manager` | 备份管理 | `clawhub install backup-manager` | ✅ |
| `ddg-search` | DuckDuckGo 搜索 | `clawhub install ddg-search` | ✅ |
| `coingecko` | 加密货币数据 | `clawhub install coingecko` | ✅ |

### 安装新 Skill
```bash
# 从 ClawHub 安装
clawhub install <skill-name>

# 检查已安装
clawhub list

# 更新 skill
clawhub update <skill-name>
```

### 查询方式
```
有冇新嘅 skills？ → skill-scanner
上次发现咩？ → skill-history
边个 skill 好用？ → memory/skills-ecosystem.md
```

---

## 🔧 故障排除

### 常见错误 + 解决

| 错误 | 原因 | 解决方法 |
|------|------|----------|
| `API quota exceeded` | Brave API 用完 | 改用 DuckDuckGo (`ddg-search` skill) |
| `Model not allowed` | 模型未配置 | 检查 `~/.openclaw/openclaw.json` → `models.allowed` |
| `Browser not attached` | Chrome 未连接 | Click OpenClaw extension icon attach tab |
| `Discord target error` | target 格式错 | 用 `user:ID` 格式（e.g. `user:964140590868594740`） |
| `Gateway not running` | Gateway 停咗 | `openclaw gateway start` |
| `File not found` | 档案不存在 | 用 `ls` 检查路径，或创建档案 |
| `web_fetch 403` | Cloudflare block | 改用 browser automation 或 DuckDuckGo |
| `Memory too large` | L1-daily 太多 | 运行 `python3 scripts/compress-memory.py` |

### Log 检查
```bash
# 检查今日错误
grep "ERROR" /tmp/openclaw/openclaw-$(date +%Y-%m-%d).log | tail -20

# 检查 Gateway 错误
tail -50 ~/.openclaw/logs/gateway.log | grep -i error
```

### 重启服务
```bash
# 重启 Gateway
openclaw gateway restart

# 检查状态
openclaw status
```

---

*This is your cheat sheet. Keep it updated.*
