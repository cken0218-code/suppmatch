#!/bin/bash
# MCP Phase 1 完整测试脚本
# Created: 2026-03-13

echo "━━━━━━━━━━━━━━━━━━━━"
echo "🧪 MCP Phase 1 完整测试"
echo "━━━━━━━━━━━━━━━━━━━━"
echo ""

cd ~/.openclaw/workspace/skills/mcp-test

# Test 1: Initialize
echo "📋 Test 1: Initialize..."
node -e "
const server = require('child_process').spawn('node', ['dist/github-server.js']);
const req = {jsonrpc:'2.0', id:1, method:'initialize', params:{protocolVersion:'2024-11-05', capabilities:{}, clientInfo:{name:'test', version:'1.0'}}};
server.stdin.write(JSON.stringify(req) + '\\n');
setTimeout(() => { server.kill(); process.exit(0); }, 2000);
server.stdout.on('data', d => console.log('✅', d.toString()));
"

echo ""
echo "📋 Test 2: List Tools..."
node test-mcp.js 2>&1 | grep -A 20 "Test 2"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━"
echo "✅ 测试完成"
echo "━━━━━━━━━━━━━━━━━━━━"
