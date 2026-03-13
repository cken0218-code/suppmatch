# MCP Phase 2: Discord MCP Server 计划

> **Created**: 2026-03-13 12:55
> **Deadline**: 2026-03-24 (11 days)
> **Status**: Research complete, ready for implementation
> **Priority**: 🟠 High

---

## 📋 研究发现

### 官方资源
1. **GitHub - modelcontextprotocol/servers**
   - ✅ 官方 Discord MCP Server 已存在
   - 提供 comprehensive integration with Discord
   
2. **Speakeasy Tutorial**
   - 完整的 MCP server 开发教程
   - Discord API 整合示例
   - 使用 discord.py

3. **SaseQ/discord-mcp**
   - 社区实现的 Discord MCP server
   - 使用 JDA (Java Discord API)
   - MCP-compatible applications

---

## 🎯 Phase 2 目标

### 主要目标
建立 Discord MCP Server，实现：
- ✅ 发送消息到 Discord channel
- ✅ 读取消息历史
- ✅ 管理频道和用户
- ✅ 与 GitHub MCP 整合（GitHub → Discord 通知）

### 成功指标
- ✅ Discord server 成功连线
- ✅ 至少 5 个工具正常运作
- ✅ GitHub ↔ Discord 整合运作
- ✅ 可以从 OpenClaw 调用

---

## 🏗️ 技术架构

### 选项 1: 使用官方 Discord MCP Server（推荐）
```bash
# 安装官方 server
cd ~/.openclaw/mcp-servers/mcp-official-servers/src/discord
npm install
npm run build

# 配置
export DISCORD_BOT_TOKEN="your_bot_token"
```

**优点**:
- ✅ 官方支持
- ✅ 维护良好
- ✅ 快速部署

**缺点**:
- ❓ 可能功能有限
- ❓ 定制化程度低

---

### 选项 2: 自建 Discord MCP Server（学习用）
```typescript
// discord-mcp-server.ts
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { Client as DiscordClient, GatewayIntentBits } from "discord.js";

// 创建 Discord client
const discordClient = new DiscordClient({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent
  ]
});

// 创建 MCP server
const server = new Server(
  { name: "discord-mcp-server", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

// Tool: 发送消息
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "send_message") {
    const { channelId, message } = request.params.arguments;
    
    const channel = await discordClient.channels.fetch(channelId);
    await channel.send(message);
    
    return {
      content: [{ type: "text", text: "Message sent successfully" }]
    };
  }
});

// 启动
discordClient.login(process.env.DISCORD_BOT_TOKEN);
const transport = new StdioServerTransport();
server.connect(transport);
```

**优点**:
- ✅ 完全定制
- ✅ 学习价值高
- ✅ 可以添加特殊功能

**缺点**:
- ❌ 需要更多时间
- ❌ 需要维护

---

## 📅 实施计划

### Day 1-2: 环境准备（3月13-14日）
**任务**:
- [ ] 安装 Discord MCP Server（官方或自建）
- [ ] 创建 Discord Bot 并获取 token
- [ ] 配置环境变量
- [ ] 测试基本连接

**预计时间**: 2 hours

---

### Day 3-4: 工具开发（3月15-16日）
**任务**:
- [ ] 实现 `send_message` 工具
- [ ] 实现 `read_messages` 工具
- [ ] 实现 `list_channels` 工具
- [ ] 实现 `manage_users` 工具
- [ ] 测试所有工具

**预计时间**: 3 hours

---

### Day 5-6: GitHub 整合（3月17-18日）
**任务**:
- [ ] 设计 GitHub → Discord 通知流程
- [ ] 实现事件监听
- [ ] 测试整合
- [ ] 优化性能

**预计时间**: 2 hours

---

### Day 7: 测试与文档（3月19-20日）
**任务**:
- [ ] 完整功能测试
- [ ] 错误处理优化
- [ ] 编写使用文档
- [ ] 整合到 OpenClaw

**预计时间**: 2 hours

---

## 🔧 Discord Bot 设置

### 步骤 1: 创建 Discord Application
1. 访问 https://discord.com/developers/applications
2. 创建新应用
3. 创建 Bot user
4. 获取 Bot Token

### 步骤 2: 添加 Bot 到服务器
1. 生成 OAuth2 URL
2. 选择权限：Send Messages, Read Messages, Manage Channels
3. 邀请 Bot 到服务器

### 步骤 3: 配置环境变量
```bash
# ~/.openclaw/openclaw.json
{
  "mcpServers": {
    "discord": {
      "command": "node",
      "args": ["~/.openclaw/mcp-servers/discord-mcp/dist/index.js"],
      "env": {
        "DISCORD_BOT_TOKEN": "your_token_here"
      }
    }
  }
}
```

---

## 📊 预期工具列表

### 核心工具（必须）
1. **send_message** - 发送消息到频道
2. **read_messages** - 读取频道消息历史
3. **list_channels** - 列出服务器频道
4. **get_user_info** - 获取用户信息
5. **manage_roles** - 管理用户角色

### 整合工具（可选）
6. **github_notification** - GitHub 事件通知
7. **schedule_message** - 定时发送消息
8. **search_messages** - 搜索消息内容

---

## 🎯 优先级建议

### 推荐路径（快速部署）
```
Day 1-2: 安装官方 Discord MCP Server
Day 3-4: 测试和配置
Day 5-6: GitHub 整合
Day 7: 文档化
```

**优点**: 快速上线，稳定可靠
**缺点**: 定制化程度低

### 学习路径（深度学习）
```
Day 1-2: 研究架构 + 设计
Day 3-4: 开发自建 server
Day 5-6: 测试 + GitHub 整合
Day 7: 文档化 + 优化
```

**优点**: 完全掌握，可定制
**缺点**: 需要更多时间

---

## 📝 下一步行动

### 立即可做（今日）
1. [ ] 决定使用官方还是自建
2. [ ] 创建 Discord Bot（如果还没有）
3. [ ] 安装基础依赖

### 本周（3月14-20日）
1. [ ] 完成基本功能实现
2. [ ] 测试核心工具
3. [ ] 开始 GitHub 整合

### 下周（3月21-27日）
1. [ ] 完成 GitHub 整合
2. [ ] 全面测试
3. [ ] 准备 Phase 3

---

## 🔗 相关资源

- [MCP 官方文档](https://modelcontextprotocol.io)
- [Discord.js 文档](https://discord.js.org)
- [Speakeasy 教程](https://www.speakeasy.com/blog/build-a-mcp-server-tutorial)
- [SaseQ/discord-mcp](https://github.com/SaseQ/discord-mcp)

---

**Created by**: Ken AI Assistant
**Date**: 2026-03-13
**Next Review**: 2026-03-14
**Status**: Research complete, ready for implementation decision
