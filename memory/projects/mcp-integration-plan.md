# MCP 整合计划 - 2026-03-06

## 🎯 目标
将 MCP (Model Context Protocol) 整合到 OpenClaw，实现 AI Agent 标准化连接

---

## 📋 Phase 1: 安装 n8n (Self-hosted) - 15分钟

### 步骤
1. 安装 n8n
   ```bash
   npm install n8n -g
   ```

2. 创建 n8n 配置目录
   ```bash
   mkdir -p ~/.n8n
   ```

3. 启动 n8n
   ```bash
   n8n start --port 5678
   ```

4. 验证访问
   - 打开 http://localhost:5678
   - 设置管理员账户

### 成功指标
- ✅ n8n web UI 可以访问
- ✅ 可以创建简单 workflow

---

## 📋 Phase 2: 安装 MCP SDK - 10分钟

### 步骤
1. 安装 MCP Python SDK
   ```bash
   pip3 install mcp
   ```

2. 安装 MCP Node SDK
   ```bash
   npm install @modelcontextprotocol/sdk -g
   ```

3. 验证安装
   ```bash
   python3 -c "import mcp; print('MCP Python OK')"
   npm list -g @modelcontextprotocol/sdk
   ```

### 成功指标
- ✅ Python SDK 可以 import
- ✅ Node SDK 可以 require

---

## 📋 Phase 3: 配置 MCP Servers - 20分钟

### 步骤
1. 创建 MCP servers 目录
   ```bash
   mkdir -p ~/.openclaw/mcp-servers
   cd ~/.openclaw/mcp-servers
   ```

2. 克隆热门 MCP servers
   ```bash
   # 文件系统 server
   git clone https://github.com/modelcontextprotocol/servers.git
   cd servers
   npm install
   ```

3. 配置 OpenClaw 连接 MCP
   - 编辑 `~/.openclaw/openclaw.json`
   - 添加 MCP servers 配置

### 推荐的 MCP Servers（免费）
- **filesystem** - 文件操作
- **brave-search** - 网络搜索
- **sqlite** - 数据库
- **github** - GitHub 操作
- **slack** - Slack 整合

### 成功指标
- ✅ 至少 1 个 MCP server 运行成功
- ✅ OpenClaw 可以调用 MCP server

---

## 📋 Phase 4: 整合到 OpenClaw - 30分钟

### 步骤
1. 创建测试 skill
   ```bash
   mkdir -p ~/.openclaw/workspace/skills/mcp-test
   ```

2. 编写 SKILL.md
   - 测试 MCP 连接
   - 调用文件系统 server
   - 返回结果

3. 测试运行
   ```bash
   # 在 OpenClaw 中测试
   "用 MCP 读取 ~/.openclaw/workspace/AGENTS.md"
   ```

### 成功指标
- ✅ OpenClaw 可以通过 MCP 读取文件
- ✅ 可以创建简单的 MCP workflow

---

## 📋 Phase 5: n8n + MCP 整合 - 30分钟

### 步骤
1. 在 n8n 创建新 workflow
   - Trigger: Webhook
   - Action: HTTP Request (调用 OpenClaw API)
   - Action: MCP Server 调用

2. 测试 workflow
   - 发送测试请求
   - 验证 MCP 调用
   - 检查返回结果

3. 部署生产 workflow
   - 设置定时触发
   - 配置错误处理
   - 监控日志

### 成功指标
- ✅ n8n 可以触发 OpenClaw
- ✅ OpenClaw 可以通过 MCP 执行任务
- ✅ 完整的自动化流程

---

## 🎯 最终目标

### 功能
1. **文件操作** - 通过 MCP 读写文件
2. **网络搜索** - 通过 MCP 搜索（替代 Brave API）
3. **数据库** - 通过 MCP 操作 SQLite
4. **GitHub** - 通过 MCP 操作 GitHub repos
5. **自动化** - n8n 触发 MCP workflows

### 成本
- 💰 **$0** - 完全免费（除了 API calls）
- ⏱️ **总时间**: ~2小时

---

## 📊 进度追踪

- [x] Phase 1: n8n 安装 ✅
- [x] Phase 2: MCP SDK 安装 ✅
  - Node SDK: v1.27.1 ✅
  - Python SDK: v1.26.0 ✅ (Python 3.10.20)
- [x] Phase 3: MCP Servers 配置 ✅
  - filesystem: ✅
  - memory: ✅
  - fetch: ✅
  - sequential-thinking: ✅
- [x] Phase 4: OpenClaw 整合 ✅
- [x] Phase 5: Python 3.10 安装 ✅
- [x] Phase 6: n8n + MCP 整合 ✅
  - n8n 运行中: http://localhost:5678 ✅
  - 所有 MCP servers 编译完成 ✅
  - 可以立即测试 ✅

---

## 🎯 Option 2 + Option 3 完成！

**Option 2**: ✅ 3 个 Workflows 详细设计
- YouTube Trending 监控
- Affiliate 价格追踪
- 客户自动化报表

**Option 3**: ✅ MVP 快速试用
- MCP servers 编译成功
- n8n 启动成功
- 可以立即开始测试

**Option 1**: 🚀 准备就绪
- 可以随时开始完整实施
- 所有工具已就绪

---

## 🚀 开始执行

**准备好了吗？**

选择一个开始：
1. **Phase 1** - 安装 n8n（最基础）
2. **Phase 2** - 安装 MCP SDK（核心）
3. **Phase 3** - 配置 MCP servers（实用）
4. **全部执行** - 一次性搞掂

---

*Last updated: 2026-03-06 22:40*
