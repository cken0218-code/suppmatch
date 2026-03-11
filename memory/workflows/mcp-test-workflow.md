# MCP 测试 Workflow

## 🎯 目标
快速测试 MCP fetch server 是否可以正常工作

---

## 📊 流程（最简单版本）

```
[手动触发]
    ↓
[MCP: fetch 抓取网页]
    ↓
[显示结果]
```

---

## 🔧 配置

### Step 1: 手动触发
**类型**: Manual Trigger
**说明**: 在 n8n 介面点击"Execute"按钮

---

### Step 2: MCP Fetch 抓取
**工具**: MCP Server - fetch
**配置**:
```json
{
  "command": "node",
  "args": [
    "/Users/cken0218/.openclaw/mcp-servers/mcp-official-servers/src/fetch/dist/index.js"
  ],
  "tool": "fetch",
  "params": {
    "url": "https://www.youtube.com/feed/trending"
  }
}
```

---

### Step 3: 显示结果
**类型**: Set Node
**配置**:
```javascript
{
  "url": $input.item.json.url,
  "content": $input.item.json.content,
  "timestamp": new Date().toISOString()
}
```

---

## 📋 测试步骤

1. 启动 n8n: `n8n start`
2. 打开 http://localhost:5678
3. 创建新 workflow
4. 添加 3 个 nodes（见上图）
5. 点击"Execute"
6. 查看结果

---

## ✅ 成功标准

- 可以抓取网页内容
- 返回 HTML 或文本
- 没有错误信息

---

## 🎯 下一步

如果测试成功：
- ✅ MCP 正常工作
- 🚀 可以开始 Workflow 1 实施

如果测试失败：
- 🐛 检查配置
- 📝 查看错误日志
- 🔧 调整参数
