# Blog Agent - 博客内容

## 用途
管理 WordPress/Ghost 博客，生成 SEO 优化内容，进行关键词研究，分析流量数据。

## 触发条件
- 每周一、三、五发布（cron）
- Google Search Console 异常
- 用户要求「写 blog post」

## 使用方式

### 1. 生成 Blog Post
```bash
# 生成文章
python3 scripts/generate-post.py --topic "[topic]" --keywords "[keywords]"

# 输出位置
# blog-posts/YYYY-MM-DD-[title].md
```

### 2. SEO 优化
```bash
# SEO 检查
python3 scripts/seo-check.py --file [file]

# 输出位置
# memory/reports/seo-YYYY-MM-DD.md
```

### 3. 流量分析
```bash
# 获取流量数据
python3 scripts/fetch-traffic.py

# 输出位置
# memory/reports/blog-YYYY-MM-DD.md
```

## 范例

**用户**：「写一篇关于 AI tools 的 blog post」

**Blog Agent**：
1. 研究 trending AI tools
2. 进行关键词研究
3. 生成 SEO 优化文章
4. 发布到 WordPress
5. 追踪流量数据

## 报告格式

```markdown
# Blog Report - YYYY-MM-DD

## 📊 流量概览
- 总访问: XXX
- 新访客: XX%
- 跳出率: XX%
- 平均停留时间: XX 秒

## 📝 发布文章
| 标题 | 字数 | 关键词 | 排名 |
|------|------|--------|------|
| [标题 1] | XXX | [关键词] | #X |
| [标题 2] | XXX | [关键词] | #X |

## 🔍 SEO 表现
- 索引页面: XX
- 平均排名: XX
- 点击率: XX%

## 💡 发现
- [洞察 1]
- [洞察 2]

## 🎯 下周计划
- [ ] [任务 1]
- [ ] [任务 2]
```

## SEO 检查清单

- [ ] 标题包含关键词
- [ ] Meta description 优化
- [ ] H1/H2 标签正确
- [ ] 内链/外链
- [ ] 图片 alt text
- [ ] URL 简洁
- [ ] 字数 > 1000

## 重点关键词

1. **AI tools 2026**
2. **AI automation**
3. **Passive income AI**
4. **YouTube automation**
5. **Affiliate marketing**

## 相关文件
- 文章：`blog-posts/`
- 报告：`memory/reports/blog-*.md`
- SEO 数据：`data/seo-*.csv`

## 模型
- **内容创作**：GLM-5
- **数据分析**：MiniMax

## 依赖
- WordPress/Ghost API（待配置）
- Google Search Console API
- SEO 工具（Ahrefs/SEMrush）

## 状态
- ⏳ 框架设计中
- ⏳ WordPress 整合待开发
