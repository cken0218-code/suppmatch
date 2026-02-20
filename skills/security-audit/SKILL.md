---
name: security-audit
description: 系统安全审计 skill - 检查配置、权限、潜在风险
version: 1.0.0
author: local
license: MIT
---

# Security Audit Skill

## 功能
- 检查 OpenClaw 配置安全性
- 审查文件权限
- 检测潜在安全风险
- 生成安全报告

## 使用方式

当用户要求进行安全审计时：
1. 检查 `~/.openclaw/openclaw.json` 中的敏感配置
2. 审查 skills 目录权限
3. 检查是否有明文存储的 API keys
4. 生成审计报告

## 安全检查清单

- [ ] API keys 是否加密存储
- [ ] 文件权限是否正确（600/700）
- [ ] 是否有可疑的外部请求
- [ ] Skills 是否来自可信来源
- [ ] Gateway 配置是否安全

## 输出格式

```markdown
# 安全审计报告

**日期**: YYYY-MM-DD
**风险等级**: 低/中/高

## 发现的问题
- 问题1
- 问题2

## 建议修复
- 建议1
- 建议2

## 总体评分
X/10
```
