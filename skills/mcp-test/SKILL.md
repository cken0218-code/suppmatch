---
name: mcp-test
description: 测试 MCP (Model Context Protocol) 连接和功能。用于验证 OpenClaw 与 MCP servers 的整合。
---

# MCP Test Skill

测试 MCP 协议整合到 OpenClaw。

## 用途

- 验证 MCP SDK 安装
- 测试 MCP server 连接
- 演示基本 MCP 功能

## 触发条件

- "测试 MCP"
- "MCP 连接"
- "验证 MCP"

## 使用方式

### 1. 检查 MCP SDK

```bash
# 检查 Node SDK
npm list -g @modelcontextprotocol/sdk

# 测试 Python SDK（如果已安装）
python3 -c "import mcp; print('MCP OK')"
```

### 2. 运行简单 MCP Server

```bash
cd ~/.openclaw/mcp-servers/mcp-official-servers/src/filesystem
node dist/index.js /tmp/test-mcp
```

### 3. 测试连接

使用 OpenClaw 调用 MCP server，验证读写文件功能。

## MCP Servers 位置

- **官方 servers**: `~/.openclaw/mcp-servers/mcp-official-servers/`
- **自定义 servers**: `~/.openclaw/mcp-servers/custom/`

## 可用的 MCP Servers

### 官方 Servers（推荐）
1. **filesystem** - 文件系统操作
2. **brave-search** - 网络搜索（需 API key）
3. **sqlite** - SQLite 数据库
4. **github** - GitHub 操作
5. **slack** - Slack 整合

### 安装新 Server

```bash
cd ~/.openclaw/mcp-servers/mcp-official-servers/src/[server-name]
npm install
npm run build
```

## 配置 OpenClaw

编辑 `~/.openclaw/openclaw.json`，添加 MCP servers：

```json
{
  "mcp": {
    "servers": {
      "filesystem": {
        "command": "node",
        "args": ["~/.openclaw/mcp-servers/mcp-official-servers/src/filesystem/dist/index.js"]
      }
    }
  }
}
```

## 测试案例

### 案例 1: 读取文件
```
用户: 用 MCP 读取 ~/.openclaw/workspace/AGENTS.md
AI: [通过 MCP filesystem server 读取文件]
```

### 案例 2: 写入文件
```
用户: 用 MCP 创建测试文件 /tmp/mcp-test.txt
AI: [通过 MCP filesystem server 写入文件]
```

### 案例 3: 搜索
```
用户: 用 MCP 搜索 "AI trends 2026"
AI: [通过 MCP brave-search server 搜索]
```

## 故障排除

### 问题 1: MCP server 无法启动
- 检查 Node.js 版本（需要 18+）
- 检查 server 目录是否有 `dist/` 文件夹
- 运行 `npm install && npm run build`

### 问题 2: OpenClaw 无法连接 MCP
- 检查 `openclaw.json` 配置路径
- 确认 server 进程正在运行
- 查看 OpenClaw logs

### 问题 3: Python SDK 安装失败
- 需要 Python 3.10+
- 或使用 Node SDK 代替

## 下一步

- ✅ 测试基本 MCP 功能
- 📝 整合到实际 skills
- 🔄 创建自动化 workflows
- 🚀 部署到生产环境

## 资源

- [MCP 官方文档](https://modelcontextprotocol.io)
- [MCP GitHub](https://github.com/modelcontextprotocol)
- [OpenClaw 文档](https://docs.openclaw.ai)

---

*Last updated: 2026-03-06*
