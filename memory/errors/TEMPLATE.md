# 错误记录模板

## 如何记录错误

每次遇到错误时，记录以下信息：

```
## [时间]

### 任务
[描述]

### 错误信息
[完整的错误输出]

### 尝试的解决方案
1. [方案1]
2. [方案2]

### 最终结果
- [x] 成功解决 / [ ] 放弃 / [ ] 需要用户决定
```

---

## 示例

### 2026-02-23 - Git Push 失败

**任务**: 推送 AGENTS.md 更新到 GitHub

**错误信息**:
```
fatal: could not read Username for 'https://github.com': Device not configured
```

**尝试的解决方案**:
1. 检查 git remote 配置
2. 尝试 SSH 方式

**最终结果**:
- [x] 本地 commit 成功，等待用户配置 remote
