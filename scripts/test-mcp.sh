#!/bin/bash
# MCP Filesystem Server 测试脚本

echo "🧪 测试 MCP Filesystem Server..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 1. 检查 server 文件
echo "✅ 1. 检查 server 文件"
if [ -f ~/.openclaw/mcp-servers/mcp-official-servers/src/filesystem/dist/index.js ]; then
    echo "   ✓ Filesystem server 存在"
else
    echo "   ✗ Filesystem server 不存在"
    exit 1
fi

# 2. 测试 server 文件完整性
echo ""
echo "✅ 2. 检查 server 编译"
if [ -d ~/.openclaw/mcp-servers/mcp-official-servers/src/filesystem/dist ]; then
    FILE_COUNT=$(ls ~/.openclaw/mcp-servers/mcp-official-servers/src/filesystem/dist/*.js 2>/dev/null | wc -l)
    if [ $FILE_COUNT -gt 0 ]; then
        echo "   ✓ Server 编译成功 ($FILE_COUNT files)"
    else
        echo "   ✗ Server 编译失败（无 JS 文件）"
        exit 1
    fi
else
    echo "   ✗ Dist 目录不存在"
    exit 1
fi

# 3. 检查 MCP SDK
echo ""
echo "✅ 3. 检查 MCP SDK"
if npm list -g @modelcontextprotocol/sdk > /dev/null 2>&1; then
    VERSION=$(npm list -g @modelcontextprotocol/sdk | grep @modelcontextprotocol/sdk | awk '{print $2}')
    echo "   ✓ MCP Node SDK 已安装 ($VERSION)"
else
    echo "   ✗ MCP Node SDK 未安装"
    exit 1
fi

# 4. 检查配置文件
echo ""
echo "✅ 4. 检查配置文件"
if [ -f ~/.openclaw/mcp-config.json ]; then
    echo "   ✓ MCP 配置文件存在"
else
    echo "   ✗ MCP 配置文件不存在"
    exit 1
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉 所有测试通过！"
echo ""
echo "📋 下一步："
echo "   1. 启动 n8n: n8n start"
echo "   2. 打开 http://localhost:5678"
echo "   3. 创建 MCP workflow"
echo ""
