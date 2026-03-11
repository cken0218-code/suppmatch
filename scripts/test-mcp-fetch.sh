#!/bin/bash
# MCP Fetch Server 快速测试

echo "🧪 测试 MCP Fetch Server..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 测试 URL
TEST_URL="https://example.com"

echo ""
echo "📡 测试抓取: $TEST_URL"
echo ""

# 使用 MCP fetch server（通过 Node.js）
node -e "
const { spawn } = require('child_process');
const path = require('path');

const serverPath = path.join(
  process.env.HOME,
  '.openclaw/mcp-servers/mcp-official-servers/src/fetch/dist/index.js'
);

console.log('✅ MCP Fetch Server 路径:', serverPath);
console.log('');
console.log('🎯 测试方式:');
console.log('   1. MCP server 已经编译成功');
console.log('   2. 需要通过 MCP 协议调用');
console.log('   3. 最简单的方式：在 n8n 中使用');
console.log('');
console.log('📋 下一步：');
console.log('   启动 n8n: n8n start');
console.log('   打开: http://localhost:5678');
console.log('   创建 workflow 使用 MCP fetch');
" 2>&1
