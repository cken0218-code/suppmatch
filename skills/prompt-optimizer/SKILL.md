# Prompt Optimizer Skill

> **Version**: 1.0
> **Created**: 2026-02-23
> **Purpose**: Use Grok to optimize user prompts before executing with other models

---

## 概述

此技能使用 Grok 分析和优化用户的指令，然后传递给目标模型（如 GLM-5）执行。这样可以：

1. 补充缺少的参数
2. 明确输出格式
3. 添加执行步骤
4. 提高任务完成质量

---

## 使用方式

### 基本用法

```
优化后执行：[你的指令]
```

### 指定目标模型

```
优化后执行 (GLM-5)：[你的指令]
优化后执行 (MiniMax)：[你的指令]
```

### 只看优化结果（不执行）

```
优化指令：[你的指令]
```

---

## 工作流程

```
用户指令
    ↓
Grok 分析
    ├── 识别任务类型
    ├── 检查缺少的参数
    ├── 确定输出格式
    └── 添加执行步骤
    ↓
优化后的指令
    ↓
目标模型执行
    ↓
结果返回用户
```

---

## 优化规则

### 1. 任务类型识别

| 关键词 | 任务类型 | 需要补充 |
|--------|----------|----------|
| 分析、研究 | Research | 数据源、范围、时间 |
| 写、创作 | Content | 格式、长度、风格 |
| 整理、归档 | Organization | 目标位置、分类方式 |
| 检查、监控 | Monitoring | 频率、阈值、通知方式 |
| 开发、写代码 | Development | 语言、框架、依赖 |

### 2. 参数补充

- **时间范围**: 默认最近 7 天
- **数据源**: 优先使用已有 API
- **输出格式**: 表格 > 列表 > 纯文本
- **语言**: 繁体中文 + 广东话口语

### 3. 输出格式模板

```markdown
## 任务：[任务名称]

### 参数
- 参数1: 值1
- 参数2: 值2

### 输出格式
1. [项目1]
2. [项目2]

### 工具
- 使用 [skill名称]
- 输出到 [文件路径]
```

---

## 示例

### 示例 1：股票分析

**用户指令：**
```
优化后执行：帮我睇下 CBA 股票
```

**Grok 优化后：**
```
任务：分析 CBA (Commonwealth Bank) 股票

参数：
- 股票代码：CBA.AX
- 数据源：Yahoo Finance
- 技术指标：RSI, MACD, EMA(12/26), ADX, ATR
- 时间范围：最近 30 天

输出格式：
1. 当前价格 + 涨跌幅
2. 技术指标分析（表格）
3. 买入/卖出信号
4. 建议止损/止盈位

工具：
- 使用 stock-agent skill
- 获取实时数据
- 生成分析报告
```

---

### 示例 2：YouTube 趋势

**用户指令：**
```
优化后执行：YouTube 有咩 trending
```

**Grok 优化后：**
```
任务：分析 YouTube 趋势内容

参数：
- 地区：TW/HK（繁体中文市场）
- 分类：Tech/AI（高 CPM niche）
- 时间：最近 7 天
- 数量：Top 10

输出格式：
| 排名 | 标题 | 观看次数 | 增长率 | 分析 |
|------|------|----------|--------|------|

分析维度：
1. 为什么 trending
2. 目标受众
3. 我们可以借鉴的点

工具：
- 使用 youtube-agent skill
- 调用 YouTube Data API
- 输出到 memory/projects/youtube-trends.md
```

---

### 示例 3：代码开发

**用户指令：**
```
优化后执行：写个备份脚本
```

**Grok 优化后：**
```
任务：开发自动备份脚本

参数：
- 语言：Python 3 或 Bash
- 备份目标：~/.openclaw/workspace/
- 备份位置：~/backup/
- 文件类型：核心配置文件（.md, .json）
- 压缩格式：.tar.gz
- 命名规则：openclaw-backup-YYYYMMDD-HHMMSS.tar.gz

功能需求：
1. 自动创建备份目录
2. 压缩指定文件
3. 保留最近 7 个备份
4. 记录备份日志
5. 可配置 cron 定时执行

输出：
- 脚本文件：scripts/backup.sh
- 使用说明
- cron 配置示例
```

---

## 配置

### 环境变量

```bash
# Grok API Key（需要在 openclaw.json 中配置）
XAI_API_KEY=your_grok_api_key
```

### OpenClaw 配置

在 `~/.openclaw/openclaw.json` 中添加：

```json
{
  "providers": {
    "xai": {
      "apiKey": "your_grok_api_key",
      "baseUrl": "https://api.x.ai/v1"
    }
  }
}
```

---

## 依赖

- Grok API access（需要申请：https://console.x.ai/）
- OpenAI-compatible API client

---

## 错误处理

| 错误 | 原因 | 解决方案 |
|------|------|----------|
| "Grok API key not configured" | 未配置 API key | 在 openclaw.json 中添加 xai.apiKey |
| "Optimization failed" | Grok 无法理解指令 | 尝试更详细描述任务 |
| "Target model unavailable" | 目标模型不可用 | 检查模型配置 |

---

## 未来扩展

- [ ] 支持多个优化器（Grok, Claude, GPT-4）
- [ ] 学习用户偏好，自动优化
- [ ] 缓存优化结果，避免重复调用
- [ ] A/B 测试优化效果

---

*Created by Ken 🐱*
