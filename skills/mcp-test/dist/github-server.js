#!/usr/bin/env node
/**
 * GitHub MCP Server - Phase 1 測試
 *
 * 功能：
 * - list_commits - 列出 repo commits
 * - list_issues - 列出 repo issues
 * - read_file - 讀取 repo 文件
 */
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema, } from "@modelcontextprotocol/sdk/types.js";
// GitHub API helper
async function githubAPI(endpoint, token) {
    const headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "OpenClaw-MCP-Server/1.0"
    };
    if (token) {
        headers["Authorization"] = `Bearer ${token}`;
    }
    const response = await fetch(`https://api.github.com${endpoint}`, { headers });
    if (!response.ok) {
        throw new Error(`GitHub API error: ${response.status} ${response.statusText}`);
    }
    return await response.json();
}
// Create server instance
const server = new Server({
    name: "github-mcp-server",
    version: "1.0.0",
}, {
    capabilities: {
        tools: {},
    },
});
// List available tools
server.setRequestHandler(ListToolsRequestSchema, async () => {
    return {
        tools: [
            {
                name: "list_commits",
                description: "List commits in a GitHub repository",
                inputSchema: {
                    type: "object",
                    properties: {
                        owner: {
                            type: "string",
                            description: "Repository owner (username or organization)",
                        },
                        repo: {
                            type: "string",
                            description: "Repository name",
                        },
                        per_page: {
                            type: "number",
                            description: "Number of commits to return (default: 10)",
                        },
                    },
                    required: ["owner", "repo"],
                },
            },
            {
                name: "list_issues",
                description: "List issues in a GitHub repository",
                inputSchema: {
                    type: "object",
                    properties: {
                        owner: {
                            type: "string",
                            description: "Repository owner",
                        },
                        repo: {
                            type: "string",
                            description: "Repository name",
                        },
                        state: {
                            type: "string",
                            enum: ["open", "closed", "all"],
                            description: "Issue state filter (default: open)",
                        },
                        per_page: {
                            type: "number",
                            description: "Number of issues to return (default: 10)",
                        },
                    },
                    required: ["owner", "repo"],
                },
            },
            {
                name: "read_file",
                description: "Read a file from a GitHub repository",
                inputSchema: {
                    type: "object",
                    properties: {
                        owner: {
                            type: "string",
                            description: "Repository owner",
                        },
                        repo: {
                            type: "string",
                            description: "Repository name",
                        },
                        path: {
                            type: "string",
                            description: "File path in the repository",
                        },
                        branch: {
                            type: "string",
                            description: "Branch name (default: main)",
                        },
                    },
                    required: ["owner", "repo", "path"],
                },
            },
        ],
    };
});
// Handle tool execution
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;
    // Get GitHub token from environment
    const token = process.env.GITHUB_TOKEN;
    try {
        switch (name) {
            case "list_commits": {
                const { owner, repo, per_page = 10 } = args;
                const commits = await githubAPI(`/repos/${owner}/${repo}/commits?per_page=${per_page}`, token);
                const result = commits.map((commit) => ({
                    sha: commit.sha,
                    message: commit.commit.message,
                    author: commit.commit.author.name,
                    date: commit.commit.author.date,
                }));
                return {
                    content: [
                        {
                            type: "text",
                            text: JSON.stringify(result, null, 2),
                        },
                    ],
                };
            }
            case "list_issues": {
                const { owner, repo, state = "open", per_page = 10 } = args;
                const issues = await githubAPI(`/repos/${owner}/${repo}/issues?state=${state}&per_page=${per_page}`, token);
                const result = issues.map((issue) => ({
                    number: issue.number,
                    title: issue.title,
                    state: issue.state,
                    user: issue.user.login,
                    created_at: issue.created_at,
                }));
                return {
                    content: [
                        {
                            type: "text",
                            text: JSON.stringify(result, null, 2),
                        },
                    ],
                };
            }
            case "read_file": {
                const { owner, repo, path, branch = "main" } = args;
                const file = await githubAPI(`/repos/${owner}/${repo}/contents/${path}?ref=${branch}`, token);
                if (file.type !== "file") {
                    throw new Error("Path is not a file");
                }
                // Decode base64 content
                const content = Buffer.from(file.content, "base64").toString("utf-8");
                return {
                    content: [
                        {
                            type: "text",
                            text: `File: ${file.path}\nSize: ${file.size} bytes\n\n${content}`,
                        },
                    ],
                };
            }
            default:
                throw new Error(`Unknown tool: ${name}`);
        }
    }
    catch (error) {
        return {
            content: [
                {
                    type: "text",
                    text: `Error: ${error.message}`,
                },
            ],
            isError: true,
        };
    }
});
// Start server
async function main() {
    const transport = new StdioServerTransport();
    await server.connect(transport);
    console.error("GitHub MCP Server running on stdio");
}
main().catch((error) => {
    console.error("Fatal error in main():", error);
    process.exit(1);
});
