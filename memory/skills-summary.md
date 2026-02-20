# Skills 总览 - 2026-02-18

**最后更新**: 2026-02-18 11:35
**总数量**: 12 个 skills

---

## ✅ 已安装 Skills（12 个）

### 🛡️ 安全类（3 个）
1. **clawsec-suite** - 官方安全套件
   - 文件完整性保护
   - 自动安全审计
   - CVE 监控

2. **security-audit** - 系统安全审计
   - 配置安全检查
   - 权限审查
   - 风险评估

3. **api-security-check** - API 安全检查
   - 检测 API keys 泄露
   - 环境变量验证
   - 敏感信息扫描

### 🔧 系统管理类（2 个）
4. **system-monitor** - 系统监控
   - CPU/内存/磁盘监控
   - 进程状态
   - 网络连接

5. **backup-manager** - 备份管理
   - 自动备份配置
   - 备份 skills
   - 恢复功能

### 💻 开发工具类（2 个）
6. **github** - GitHub CLI 集成
   - 官方验证
   - GitHub 操作

7. **git-automation** - Git 自动化
   - 快速 Git 操作
   - Commit 规范
   - 分支管理

### 📊 数据处理类（1 个）
8. **data-analyzer-local** - 数据分析
   - CSV/Excel 分析
   - 统计报告
   - 数据可视化

### ⏰ 任务管理类（1 个）
9. **cron-manager** - Cron 任务管理
   - 管理定时任务
   - 查看任务历史
   - 故障排查

### 🔍 监控查询类（2 个）
10. **skill-scanner** - 自动 Skills 扫描器
    - 白天轻量扫描（09:00, 12:00, 15:00, 18:00, 21:00）
    - 深夜深度分析（23:00, 02:00, 05:00）
    - 安全审查
    - 概念记录

11. **skill-history** - Skills 历史查询
    - 查询所有扫描记录
    - 查看安全 skills 列表
    - 历史记录查询

### 🔄 工作流类（1 个）✨ 新增
12. **workflow-trigger-local** - 工作流触发器
    - **替代**: n8n-dispatch（不安全）
    - 触发 N8N/Slack/自定义 webhook
    - 用户自行配置 endpoints
    - 完全透明

### 🚀 应用开发类（1 个）✨ 新增
13. **app-scaffold-local** - 应用脚手架
    - **替代**: app-builder（不安全）
    - 快速创建应用脚手架
    - 支持 Node.js/Python/静态网站
    - 完全本地

---

## 🆕 新开发 Skills（2 个）

### workflow-trigger-local
**开发原因**: n8n-dispatch 被 VirusTotal 标记为可疑
**安全特性**:
- ✅ 不包含硬编码外部 API
- ✅ 用户自行配置所有 endpoints
- ✅ 代码清晰可审查

**使用场景**:
- 触发 N8N 工作流
- 发送 Slack 通知
- 调用自定义 webhook

### app-scaffold-local
**开发原因**: app-builder 被 VirusTotal 标记为可疑
**安全特性**:
- ✅ 完全本地运行
- ✅ 使用标准工具（npm, pip, git）
- ✅ 用户完全控制

**支持类型**:
- Node.js: Express, Next.js, React, Vue
- Python: Flask, FastAPI, Django
- 静态网站

---

## 📊 统计

### 分类统计
- 安全类: 3 个
- 系统管理: 2 个
- 开发工具: 2 个
- 数据处理: 1 个
- 任务管理: 1 个
- 监控查询: 2 个
- 工作流: 1 个
- 应用开发: 1 个

### 来源统计
- ClawHub 官方: 1 个（github）
- 自行开发: 11 个（全部以 -local 结尾）

### 安全状态
- ✅ 全部安全: 12 个
- ⚠️ 可疑: 0 个
- ❌ 不安全: 0 个

---

## 🎯 使用方式

### 安全审计
```
"帮我进行安全审计"
"检查 API keys 有冇泄露"
```

### 系统管理
```
"检查系统状态"
"创建备份"
```

### 开发工具
```
"帮我 commit 同 push"
"检查 GitHub 状态"
```

### 数据分析
```
"分析呢个 CSV 文件"
"生成数据报告"
```

### 任务管理
```
"列出所有定时任务"
"查看任务历史"
```

### Skills 监控
```
"有冇新嘅 skills？"
"上次发现咩？"
"帮我睇下 X 月 X 日嘅记录"
```

### 工作流 ✨ 新增
```
"触发 N8N 工作流"
"发送 Slack 通知"
```

### 应用开发 ✨ 新增
```
"帮我创建一个 Express API"
"我想开发一个 FastAPI 项目"
"创建一个 Next.js 应用"
```

---

## 📂 文件位置

**Skills 目录**: `/Users/cken0218/.openclaw/workspace/skills/`

**相关记录**:
- 安装列表: `memory/skills-safe-to-install.md`
- 概念记录: `memory/skills-concepts-to-develop.md`
- 扫描历史: `memory/skill-scans/`
- 开发记录: `memory/2026-02-18-skills-developed.md`

---

## 🔄 下次扫描

**轻量扫描**: 12:00（约 25 分钟后）
**深度分析**: 今晚 23:00

---

## 💡 开发原则

所有自开发的 skills 都遵循：
1. ✅ 不包含硬编码的外部 API
2. ✅ 用户可以自行配置所有参数
3. ✅ 代码清晰可读，可以审查
4. ✅ 使用标准工具和库
5. ✅ 完全本地运行（除非用户明确需要）

---

**备注**: 所有自开发的 skills 都以 `-local` 结尾，确保与 ClawHub 的 skills 区分，并且用户可以随时审查代码。

---

**更新记录**:
- 2026-02-18 11:00 - 初始安装 9 个 skills
- 2026-02-18 11:15 - 增加扫描系统（skill-scanner, skill-history）
- 2026-02-18 11:35 - 开发 2 个安全替代 skills（workflow-trigger-local, app-scaffold-local）
