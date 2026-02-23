# Skills 待安装列表（已验证安全）

**最後更新**: 2026-02-20 23:00

---

## ✅ 已验证安全的 Skills (可直接安装)

### 核心基础设施
| Skill | 状态 | 说明 |
|-------|------|------|
| github | ✅ 已安装 | 官方 GitHub 工具 |
| openclaw-orchestration | ✅ 已安装 | 多代理编排 |
| openclaw-crm | ✅ 已安装 | CRM 工具 |
| openclaw-comfyui | ✅ 已安装 | 图像生成 |
| openclaw-voice | ✅ 已安装 | 语音处理 |
| automation-workflows | ✅ 已安装 | 本地自动化 |

### 🆕 2026-02-20 新增安全推荐

| Skill | 风险 | 说明 |
|-------|------|------|
| crypto-address-checker | ✅ 安全 | 加密货币反诈骗工具，本地数据库 |
| web-mcp | ✅ 安全 | Web 集成框架，标准协议 |
| data-automation-service | ✅ 安全 | 本地数据处理 |

---

## ⚠️ 需要修改后安装

| Skill | 风险 | 修改要求 |
|-------|------|----------|
| meme-signal | 🟡 中 | 添加免责声明，禁用评分 |

---

## 🔴 拒绝安装 (高风险)

### 2026-02-20 扫描发现

| Skill | 风险 | 原因 |
|-------|------|------|
| x-twitter-scraper | 🔴🔴🔴 | 反检测技术、恶意爬取 |
| x-post-automation | 🔴🔴 | Twitter API、自动化发布风险 |

---

## 📋 待深度分析清单

### 2026-02-20 傍晚扫描 (6 skills)
- x-post-automation - 已记录概念
- ai-automation-workflows - 评估成本
- afrexai-business-automation - 本地优先
- mlops-automation-cn - 需要时部署
- data-automation-service - ✅ 安全
- activecampaign-automation - 需要时考虑

---

## ⚠️ 2026-02-18 扫描发现（但被标记为可疑）

### 不建议安装（VirusTotal Code Insight 标记）

1. **unibase-membase** ⚠️
   - 风险: 加密、去中心化网络
   - 状态: 不安装
   - 概念: 已记录到 concepts-to-develop.md

2. **n8n-dispatch** ⚠️
   - 风险: 外部 API 调用
   - 状态: 不安装
   - 概念: 已记录到 concepts-to-develop.md

3. **claude-chrome** ⚠️
   - 风险: 浏览器扩展、外部 API
   - 状态: 不安装
   - 替代: 使用 OpenClaw browser tool

4. **app-builder** ⚠️
   - 风险: 外部服务集成
   - 状态: 不安装
   - 概念: 已记录到 concepts-to-develop.md

---

## 📊 统计

- **扫描总数**: 46 (今日)
- **高风险拒绝**: 2
- **中等风险待评估**: 5
- **安全推荐**: 9
- **已安装**: 6

---

## 🎯 安装命令

```bash
# 已验证安全的 skills
clawhub install crypto-address-checker
clawhub install web-mcp
clawhub install data-automation-service
```
