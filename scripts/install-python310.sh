#!/bin/bash
# Python 3.10 安装脚本（使用 pyenv）

echo "🐍 Python 3.10 安装脚本"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 1. 检查 pyenv
echo "✅ 1. 检查 pyenv"
if command -v pyenv &> /dev/null; then
    PYENV_VERSION=$(pyenv --version)
    echo "   ✓ pyenv 已安装 ($PYENV_VERSION)"
else
    echo "   ⏳ 正在安装 pyenv..."
    brew install pyenv
    echo "   ✓ pyenv 安装完成"
fi

# 2. 配置 shell（zsh）
echo ""
echo "✅ 2. 配置 zsh"
if ! grep -q 'pyenv init' ~/.zshrc; then
    echo '' >> ~/.zshrc
    echo '# pyenv configuration' >> ~/.zshrc
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
    echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
    echo 'eval "$(pyenv init -)"' >> ~/.zshrc
    echo "   ✓ 已添加 pyenv 配置到 ~/.zshrc"
else
    echo "   ✓ pyenv 配置已存在"
fi

# 3. 加载 pyenv
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

# 4. 安装 Python 3.10
echo ""
echo "✅ 3. 安装 Python 3.10"
LATEST_310=$(pyenv install -l | grep "^\s*3\.10" | tail -1 | tr -d ' ')
echo "   最新版本: $LATEST_310"

if pyenv versions | grep -q "$LATEST_310"; then
    echo "   ✓ Python $LATEST_310 已安装"
else
    echo "   ⏳ 正在安装 Python $LATEST_310（可能需要 5-10 分钟）..."
    pyenv install $LATEST_310
    echo "   ✓ Python $LATEST_310 安装完成"
fi

# 5. 设置全局版本
echo ""
echo "✅ 4. 设置 Python 版本"
pyenv global $LATEST_310
echo "   ✓ 已设置 Python $LATEST_310 为全局版本"

# 6. 验证安装
echo ""
echo "✅ 5. 验证安装"
PYTHON_VERSION=$(python --version 2>&1)
PIP_VERSION=$(pip --version 2>&1 | awk '{print $1, $2}')
echo "   ✓ $PYTHON_VERSION"
echo "   ✓ $PIP_VERSION"

# 7. 安装 MCP Python SDK
echo ""
echo "✅ 6. 安装 MCP Python SDK"
pip install "mcp[cli]"
if python -c "import mcp" 2>/dev/null; then
    echo "   ✓ MCP Python SDK 安装成功"
else
    echo "   ✗ MCP Python SDK 安装失败"
    exit 1
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉 Python 3.10 + MCP SDK 安装完成！"
echo ""
echo "📋 重要提示："
echo "   1. 重新打开终端，或运行: source ~/.zshrc"
echo "   2. 验证: python --version"
echo "   3. 测试: python -c 'import mcp; print(\"MCP OK\")'"
echo ""
