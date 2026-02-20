---
name: api-security-check
description: API 安全检查 skill - 检查 API keys 和敏感信息泄露
version: 1.0.0
author: local
license: MIT
---

# API Security Check Skill

## 功能
- 检查代码中的 API keys 泄露
- 验证环境变量配置
- 检查 .gitignore 设置
- 审查敏感文件权限

## 检查清单

### 1. 搜索敏感信息
```bash
# 搜索可能的 API keys
grep -r "api_key\|apikey\|API_KEY" --include="*.js" --include="*.py" .

# 搜索密码
grep -r "password\|passwd\|pwd" --include="*.js" --include="*.py" .

# 搜索 tokens
grep -r "token\|secret\|auth" --include="*.js" --include="*.py" .
```

### 2. 检查 .gitignore
```bash
cat .gitignore | grep -E "env|key|secret|config"
```

### 3. 文件权限检查
```bash
# 检查敏感文件权限
ls -la ~/.openclaw/openclaw.json
ls -la ~/.ssh/
ls -la ~/.env*
```

### 4. 环境变量
```bash
# 列出环境变量（不显示值）
env | grep -E "API|KEY|TOKEN|SECRET" | cut -d= -f1
```

## 安全建议

✅ 使用环境变量存储敏感信息
✅ 将敏感文件加入 .gitignore
✅ 设置正确的文件权限（600）
✅ 定期轮换 API keys
✅ 使用加密存储

## 风险等级

🔴 高风险：明文 API keys 在代码中
🟡 中风险：敏感文件权限过宽
🟢 低风险：环境变量配置正确

## 修复建议

如果发现泄露：
1. 立即撤销/重置 API key
2. 从 Git 历史中删除
3. 更新所有使用该 key 的地方
4. 加强代码审查流程
