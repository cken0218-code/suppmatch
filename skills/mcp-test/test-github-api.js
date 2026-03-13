#!/usr/bin/env node
/**
 * MCP GitHub API 完整测试
 */

import { spawn } from "child_process";

console.log("━━━━━━━━━━━━━━━━━━━━");
console.log("🧪 MCP GitHub API 完整测试");
console.log("━━━━━━━━━━━━━━━━━━━━\n");

const server = spawn("node", ["dist/github-server.js"], {
  cwd: process.cwd(),
  env: { ...process.env }
});

let requestId = 0;
let testsCompleted = 0;

// 发送 JSON-RPC 请求
function sendRequest(method, params = {}) {
  const request = {
    jsonrpc: "2.0",
    id: ++requestId,
    method,
    params
  };

  const message = JSON.stringify(request) + "\n";
  server.stdin.write(message);
  console.log(`\n📤 Test ${requestId}: ${method}`);
  console.log("Request:", JSON.stringify(params, null, 2));
}

// 处理响应
server.stdout.on("data", (data) => {
  const lines = data.toString().split("\n").filter(line => line.trim());

  lines.forEach(line => {
    try {
      const response = JSON.parse(line);
      console.log("\n✅ Response:");

      if (response.result) {
        if (response.result.tools) {
          console.log(`   找到 ${response.result.tools.length} 个工具`);
          response.result.tools.forEach(tool => {
            console.log(`   - ${tool.name}: ${tool.description}`);
          });
        } else if (response.result.content) {
          console.log("   内容已返回");
          if (Array.isArray(response.result.content)) {
            const text = response.result.content[0]?.text || "";
            if (text.length > 200) {
              console.log(`   ${text.substring(0, 200)}...`);
            } else {
              console.log(`   ${text}`);
            }
          }
        } else {
          console.log("   ", JSON.stringify(response.result, null, 2).substring(0, 300));
        }
      } else if (response.error) {
        console.log("   ❌ Error:", response.error.message);
      }

      testsCompleted++;

      // 所有测试完成后退出
      if (testsCompleted >= 4) {
        console.log("\n━━━━━━━━━━━━━━━━━━━━");
        console.log("✅ 所有测试完成");
        console.log("━━━━━━━━━━━━━━━━━━━━\n");
        server.kill();
        process.exit(0);
      }
    } catch (e) {
      // 忽略非 JSON 输出
    }
  });
});

server.stderr.on("data", (data) => {
  console.log("⚠️  Server:", data.toString());
});

// 测试序列
setTimeout(() => sendRequest("initialize", {
  protocolVersion: "2024-11-05",
  capabilities: {},
  clientInfo: { name: "test-client", version: "1.0.0" }
}), 500);

setTimeout(() => sendRequest("tools/list"), 1500);

setTimeout(() => sendRequest("tools/call", {
  name: "list_commits",
  arguments: {
    owner: "openclaw",
    repo: "openclaw",
    per_page: 3
  }
}), 2500);

setTimeout(() => sendRequest("tools/call", {
  name: "list_issues",
  arguments: {
    owner: "openclaw",
    repo: "openclaw",
    state: "open",
    per_page: 3
  }
}), 3500);

// 超时保护
setTimeout(() => {
  console.log("\n⏱️  测试超时，强制退出");
  server.kill();
  process.exit(1);
}, 10000);
