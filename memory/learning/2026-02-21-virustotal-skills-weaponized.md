# 2026-02-21 安全研究报告

## VirusTotal: OpenClaw Skills 被武器化

**来源**: VirusTotal Blog (2026-02-21)
**主题**: OpenClaw AI Agent Skills 正在成为恶意软件分发渠道

---

### 核心发现

1. **规模**: VirusTotal 已分析 3,016+ OpenClaw skills，数百个显示恶意特征
2. **攻击者**: 用户 "hightower6eu" 发布咗 314 个恶意 skills，全部被识别为恶意
3. **模式**: Skills 睇起身正常（crypto analytics, finance tracking），但内含"setup"步骤要求下载同执行 external code

### 攻击手法

- **Windows**: 要求下载 GitHub ZIP (password: 'openclaw')，入面有 `openclaw-agent.exe`
  - 检测为: Packed Trojan
- **macOS**: 提供 shell script (托管喺 glot.io，Base64 编码)
  - 最终 payload: Mach-O executable
  - 检测为: Atomic Stealer (AMOS) - 密码/cookie/crypto wallet 盗取器

### 安全建议 (from VirusTotal)

1. **Treat skill folders as trusted-code boundaries** - 严格控制边个可以改
2. **Prefer sandboxed executions** - 保护敏感凭据
3. **Be skeptical of skills requiring shell commands or downloaded binaries**
4. **Scan community skills before installing**
5. **For marketplaces: add publish-time scanning**

---

### 对比我哋既工作

✅ **我哋既security scanning方向完全正确！**
- 我哋早已意识到呢个风险
- 每日进行 skills 安全审查
- 记录咗大量 malicious skills 概念
- 开发安全替代版本 (-local skills)

### 呢篇嘢印证咗乜？

- 我哋既严格审查标准系必要既
- "概念学习"策略系合理既（可以了解攻击模式但唔安装）
- 本地开发 (-local) 技能既方向正确

---

**结论**: 继续执行现有安全策略，呢个方向绝对正确。
