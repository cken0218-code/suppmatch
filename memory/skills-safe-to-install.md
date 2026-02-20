# Skills 待安装列表（已验证安全）

**最後更新**: 2026-02-20 10:50
**重要说明**: ⚠️ VirusTotal 检查更严格，所有 skills 需要通过安装阶段检查

---

## ✅ 可以安装的 Skills

### GitHub & Git
- github ✅ - 已安装（官方验证）

### 自动化工作流
- **automation-workflows** ✅ - 已安装并深度验证（2026-02-19）
  - 纯本地操作（文件、Git）
  - 无外部 API 调用
  - 代码清晰可审查
  - 依赖：仅 glob

### 🔍 2026-02-20 Light Scan 新發現

#### 需深度分析清單
- x-post-automation ⭐3.442 - Twitter 自動化（概念已記錄）
- ai-automation-workflows ⭐3.406 - AI 工作流
- afrexai-business-automation ⭐3.315 - 商業自動化
- mlops-automation-cn ⭐3.138 - MLOps
- data-automation-service ⭐3.107 - 數據自動化
- activecampaign-automation ⭐3.395 - 行銷自動化

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

5-10. **其他 6 个 skills** ⚠️
   - 风险: 同样被标记
   - 状态: 不安装

---

## 📊 统计

- **扫描总数**: 10 个
- **安装阶段可疑**: 10 个 ⚠️
- **实际可安装**: 0 个
- **已记录概念**: 10 个

---

## 🎯 下次扫描策略

**更严格的筛选**:
1. ✅ 优先考虑官方 skills
2. ✅ 优先考虑知名开发者
3. ✅ 检查是否有详细文档
4. ✅ 检查是否有 GitHub 源码
5. ✅ 安装前先 inspect 查看详情

**目标分类**:
- 数据分析（YouTube analytics）
- 内容创作（文案生成）
- 自动化工具（工作流）
- 系统管理（监控、备份）

---

**备注**:
- 安全第一，宁可错过，不可冒险
- 所有可疑 skills 的概念都已记录
- 可以根据概念自行开发安全版本
- 继续监控，等待更安全的 skills

**安装命令**:
```bash
# 只有通过两阶段检查的 skills 才能安装
clawhub install <skill-name>
```
