---
name: git-automation
description: Git 自动化 skill - 常用 Git 操作和工作流
version: 1.0.0
author: local
license: MIT
requires:
  bins:
    - git
---

# Git Automation Skill

## 功能
- 快速 Git 操作
- 分支管理
- Commit 规范
- 自动 push

## 常用操作

### 状态检查
```bash
git status
git log --oneline -10
git branch -a
```

### 快速提交
```bash
git add .
git commit -m "type: description"
git push origin $(git branch --show-current)
```

### Commit 消息规范
使用 Conventional Commits：
- feat: 新功能
- fix: 修复 bug
- docs: 文档更新
- style: 代码格式
- refactor: 重构
- test: 测试
- chore: 构建/工具

### 分支管理
```bash
# 创建新分支
git checkout -b feature/description

# 合并分支
git checkout main
git merge feature/description

# 删除已合并分支
git branch -d feature/description
```

### 同步远程
```bash
git fetch origin
git pull origin $(git branch --show-current)
```

## 工作流程

1. 开始工作前：`git pull`
2. 工作中：定期 `git commit`
3. 完成后：`git push`
4. 重要更改：创建 PR

## 安全提示

⚠️ 提交前检查：
- 不要提交敏感信息（API keys, passwords）
- 检查 .gitignore 配置
- 确认要提交的文件
