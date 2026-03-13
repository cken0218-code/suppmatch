# TOOLS-compact - 工具精简版

> **Last Updated**: 2026-03-13
> **Version**: 2.0
> **Purpose**: 启动时必读（核心工具，50 行以内）

---

## 🖥️ 系統信息

- **Name**: lau的Mac mini
- **OS**: macOS Darwin 25.3.0 (arm64)
- **Shell**: zsh
- **Timezone**: Asia/Taipei (CST +0800)
- **Node**: v22.22.0
- **Python**: 3.9.6
- **OpenClaw**: 2026.2.22-2

---

## 🤖 Models

### 主要 Models
| Model | Provider | 用途 | 状态 |
|-------|----------|------|------|
| GLM-5 | Zai | 复杂任务（Primary）| ⚠️ 偶尔 timeout |
| MiniMax-M2.1 | MiniMax | 日常任务（Fallback）| ✅ 稳定 |
| MiniMax-M2.5 | MiniMax | ❌ 不支持 | 当前计划不支持 |

### 默认配置（2026-03-13 18:27）
- **Primary**: GLM-5
- **Fallback**: MiniMax-M2.1

### Aliases
- `glm-5` → zai/glm-5
- `minimax` → minimax-portal/MiniMax-M2.1
- `minimax-m2.5` → ❌ 不可用

---

## 🌐 瀏覽器工具

### 可用工具（按优先级）

1. **Chrome Extension Relay** ✅
   - 最快，需要用户 attach tab
   - 已有登录状态

2. **OpenClaw Browser** ✅
   - 独立浏览器
   - Playwright 功能受限（无 act:click/type）

3. **web_fetch** ✅
   - 轻量级，只支持静态页面
   - 无法处理 JS 渲染

4. **AppleScript** ✅
   - macOS 自动化
   - 需要权限，可能不稳定

### ⚠️ 已知限制
- Playwright 不可用 → 无法使用 `act:click`、`act:type`
- 可用功能：`screenshot`、`open`、`tabs`、`focus`

---

## 💬 通訊渠道

- **Discord**: ken000ken
- **Telegram**: @kk629
- **Email**: cken0218@gmail.com

---

## 📂 重要路径

### OpenClaw
- **Config**: `~/.openclaw/openclaw.json`
- **Workspace**: `~/.openclaw/workspace`
- **Logs**: `/tmp/openclaw/openclaw-*.log`
- **Gateway Log**: `~/.openclaw/logs/gateway.log`

### Memory
- **Identity**: `memory/identity-compact.md`
- **L1-daily**: `memory/L1-daily/`
- **L2-weekly**: `memory/L2-weekly/`
- **User Patterns**: `memory/user-patterns.md`

### Skills
- **Local Skills**: `~/.openclaw/workspace/skills/`
- **Count**: ~47 个

---

## 🔐 API Keys

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

### Git Commit
```bash
cd ~/.openclaw/workspace
git add -A
git commit -m "docs: update [file] - [reason]"
git push origin main
```

---

## 🔧 故障排除

### 常见错误 + 解决

| 错误 | 原因 | 解决方法 |
|------|------|----------|
| `API quota exceeded` | Brave API 用完 | 改用 DuckDuckGo (`ddg-search` skill) |
| `Model not allowed` | 模型未配置 | 检查 `openclaw.json` |
| `Browser not attached` | Chrome 未连接 | Click OpenClaw extension icon |
| `Gateway not running` | Gateway 停咗 | `openclaw gateway start` |
| `web_fetch 403` | Cloudflare block | 改用 browser automation |

### 重启服务
```bash
# 重启 Gateway
openclaw gateway restart

# 检查状态
openclaw status
```

---

**详细版本**：见 `TOOLS.md`（227 行）
**浏览器工具详情**：见 `memory/browser-tools-detail.md`
**Created**: 2026-03-13
**Status**: Active
