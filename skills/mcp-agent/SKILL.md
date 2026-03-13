# MCP Agent - Model Context Protocol 整合

## 用途
管理 MCP servers（GitHub, Discord, n8n），负责 Phase 1-4 整合，监控 API 连接。

## 触发条件
- MCP server 启动/停止
- API 连接失败
- 用户要求「整合 [tool]」

## 使用方式

### 1. 测试 MCP Server
```bash
# 测试 GitHub MCP
cd skills/mcp-test
node github-server.ts

# 测试 API
node test-github-api.js
```

### 2. 整合新 Server
```bash
# 创建新 MCP server
python3 scripts/create-mcp-server.py --name [tool]

# 输出位置
# skills/mcp-[tool]/
```

### 3. 监控连接
```bash
# 检查所有 MCP servers
python3 scripts/check-mcp-status.py

# 输出位置
# memory/reports/mcp-YYYY-MM-DD.md
```

## 范例

**用户**：「整合 Discord MCP」

**MCP Agent**：
1. 研究 Discord MCP Server
2. 创建 MCP server 文件
3. 测试 API 连接
4. 输出报告

## 报告格式

```markdown
# MCP Report - YYYY-MM-DD

## 🔌 Server 状态
| Server | 状态 | Tools | 最后检查 |
|--------|------|-------|----------|
| GitHub | ✅ | 3 | HH:MM |
| Discord | ⏳ | - | - |
| n8n | ❌ | - | - |

## 📊 Phase 进度
- Phase 1 (GitHub): ✅ 完成
- Phase 2 (Discord): ⏳ 进行中
- Phase 3 (n8n): ⏳ 待开始
- Phase 4 (Full Integration): ⏳ 待开始

## ❌ 错误
- [如果有]

## 🎯 下一步
- [ ] [任务 1]
- [ ] [任务 2]
```

## 整合计划

### Phase 1: GitHub MCP ✅（已完成 2026-03-13）
- ✅ GitHub Server 测试成功
- ✅ 3 tools 可用（list_commits, list_issues, read_file）

### Phase 2: Discord MCP ⏳（Deadline: 2026-03-24）
- 研究计划：`memory/projects/mcp-discord-phase2-plan.md`
- 目标：管理 Discord server, 自动回复, 角色管理

### Phase 3: n8n MCP ⏳（Deadline: 2026-03-31）
- 目标：工作流自动化

### Phase 4: Full Integration ⏳（Deadline: 2026-04-01）
- 目标：所有 servers 协同工作

## 相关文件
- 测试代码：`skills/mcp-test/`
- 研究计划：`memory/projects/mcp-*.md`
- 报告：`memory/reports/mcp-*.md`

## 模型
- **技术整合**：GLM-5

## 依赖
- Node.js
- TypeScript
- 各工具 API keys

## 状态
- ✅ Phase 1 完成
- ⏳ Phase 2 研究中
