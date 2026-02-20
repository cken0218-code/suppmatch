---
name: skill-history
description: 查询 Skills 扫描历史记录
version: 1.0.0
author: local
license: MIT
---

# Skill History - Skills 历史查询

## 功能
- 查询所有扫描记录
- 查看安全 skills 列表
- 查看概念记录
- 查看每日总结

## 使用方式

### 查询最新发现
```bash
# 查看今日记录
cat memory/2026-02-18.md

# 查看最新扫描
ls -lt memory/skill-scans/ | head -n 5
```

### 查询安全 Skills
```bash
# 查看所有可以安装的 skills
cat memory/skills-safe-to-install.md
```

### 查询概念记录
```bash
# 查看所有概念和开发计划
cat memory/skills-concepts-to-develop.md
```

### 查询特定日期
```bash
# 查看特定日期的扫描记录
cat memory/skill-scans/2026-02-18-summary.md
```

## 用户查询示例

当用户问：
- "有冇新嘅 skills？" → 显示 skills-safe-to-install.md 最新几条
- "上次发现咩？" → 显示最新的 summary.md
- "帮我睇下 X 月 X 日嘅记录" → 显示对应日期的文件
- "有冇关于数据分析嘅 skills？" → 搜索相关记录
- "点解唔记得？" → **显示所有历史记录**

## 记录保证

### ✅ 永久保存
所有记录都保存在：
- `memory/` 目录下
- 每日文件永久保存
- 不会删除历史记录

### ✅ 不会遗漏
每次扫描都会：
- 记录到对应日期的文件
- 更新总列表
- 同步到 MEMORY.md

### ✅ 随时可查
用户可以随时查询：
- 今天的记录
- 昨天的记录
- 任何历史记录
- 特定类型的 skills

## 文件结构

```
memory/
├── skills-safe-to-install.md       # 总列表（随时更新）
├── skills-concepts-to-develop.md   # 概念记录（随时更新）
├── skill-scans/
│   ├── 2026-02-18-light.md        # 白天轻量扫描
│   ├── 2026-02-18-deep.md         # 深夜深度分析
│   └── 2026-02-18-summary.md      # 每日总结
├── 2026-02-18.md                   # 今日完整记录
├── 2026-02-17.md                   # 昨日记录
└── ...                             # 历史记录
```

## 查询命令

### 快速查询
```bash
# 最新发现的安全 skills
tail -n 20 memory/skills-safe-to-install.md

# 最新概念记录
tail -n 20 memory/skills-concepts-to-develop.md

# 今日扫描记录
cat memory/2026-02-18.md | grep -A 5 "Skills"
```

### 搜索特定内容
```bash
# 搜索数据分析相关
grep -r "数据分析" memory/skill-scans/

# 搜索安全 skills
grep -r "✅ 安全" memory/skill-scans/

# 搜索特定日期
cat memory/skill-scans/2026-02-18-*.md
```

## 响应格式

当用户查询时，返回：

```markdown
📊 **Skills 扫描记录查询**

**查询内容**: [用户问题]
**查询结果**: [显示相关记录]

---

**记录来源**: memory/skill-scans/[文件名]
**记录时间**: YYYY-MM-DD HH:MM
**记录状态**: ✅ 完整保存

**备注**: 所有记录永久保存，不会遗漏
```

## 重要承诺

### 🔒 永不丢失
- ✅ 所有记录保存到文件
- ✅ 定期备份
- ✅ 多重备份（memory/ + MEMORY.md）

### 🔍 随时可查
- ✅ 支持任意时间查询
- ✅ 支持关键词搜索
- ✅ 支持分类查询

### 📝 完整记录
- ✅ 每次 scanning 都记录
- ✅ 包含所有发现
- ✅ 包含安全评估
- ✅ 包含建议行动

---

**承诺**: **绝不遗漏任何记录，随时可查询历史**
