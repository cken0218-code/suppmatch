#!/usr/bin/env node
/**
 * MCP Server Test Script
 * 
 * 測試 GitHub MCP Server 嘅基本功能
 */

import { spawn } from "child_process";
import { createInterface } from "readline";

console.log("━━━━━━━━━━━━━━━━━━━━");
console.log("🧪 MCP Server Test");
console.log("━━━━━━━━━━━━━━━━━━━━");
console.log();

// 啟動 MCP server
const server = spawn("node", ["dist/github-server.js"], {
  cwd: process.cwd(),
  env: { ...process.env }
});

let requestId = 0;

// 創建 readline interface
const rl = createInterface({
  input: server.stdout,
  terminal: false
});

// 處理 server 輸出
rl.on("line", (line) => {
  try {
    const response = JSON.parse(line);
    console.log("✅ Response:", JSON.stringify(response, null, 2));
  } catch (e) {
    // 可能係日誌輸出
    console.log("📝 Server:", line);
  }
});

// 錯誤處理
server.stderr.on("data", (data) => {
  console.log("⚠️  Server log:", data.toString());
});

server.on("error", (error) => {
  console.error("❌ Server error:", error);
});

// 發送 JSON-RPC 請求
function sendRequest(method, params = {}) {
  const request = {
    jsonrpc: "2.0",
    id: ++requestId,
    method,
    params
  };
  
  const message = JSON.stringify(request) + "\n";
  server.stdin.write(message);
  console.log("\n📤 Request:", JSON.stringify(request, null, 2));
}

// 測試序列
setTimeout(() => {
  console.log("\n━━━━━━━━━━━━━━━━━━━━");
  console.log("📋 Test 1: Initialize");
  console.log("━━━━━━━━━━━━━━━━━━━━\n");
  sendRequest("initialize", {
    protocolVersion: "2024-11-05",
    capabilities: {},
    clientInfo: {
      name: "test-client",
      version: "1.0.0"
    }
  });
}, 1000);

setTimeout(() => {
  console.log("\n━━━━━━━━━━━━━━━━━━━━");
  console.log("📋 Test 2: List Tools");
  console.log("━━━━━━━━━━━━━━━━━━━━\n");
  sendRequest("tools/list");
}, 2000);

setTimeout(() => {
  console.log("\n━━━━━━━━━━━━━━━━━━━━");
  console.log("📋 Test 3: Call Tool - list_commits");
  console.log("━━━━━━━━━━━━━━━━━━━━\n");
  sendRequest("tools/call", {
    name: "list_commits",
    arguments: {
      owner: "openclaw",
      repo: "openclaw",
      per_page: 3
    }
  });
}, 3000);

setTimeout(() => {
  console.log("\n━━━━━━━━━━━━━━━━━━━━");
  console.log("📋 Test 4: Call Tool - list_issues");
  console.log("━━━━━━━━━━━━━━━━━━━━\n");
  sendRequest("tools/call", {
    name: "list_issues",
    arguments: {
      owner: "openclaw",
      repo: "openclaw",
      state: "open",
      per_page: 3
    }
  });
}, 4000);

setTimeout(() => {
  console.log("\n━━━━━━━━━━━━━━━━━━━━");
  console.log("✅ Test Complete!");
  console.log("━━━━━━━━━━━━━━━━━━━━\n");
  server.kill();
  process.exit(0);
}, 6000);
