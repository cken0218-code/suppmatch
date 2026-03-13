# Affiliate Agent - 联盟行销管理

## 用途
管理 affiliate marketing，包括产品研究、landing page 创建、conversion rate 追踪和佣金收入分析。

## 触发条件
- 新 affiliate program 发布
- Conversion rate < 1% 警报
- 用户要求「整 landing page」
- 每月 1 号收入报告

## 使用方式

### 1. 研究 Affiliate 产品
```bash
# 搜寻高潜力产品
python3 scripts/research-products.py --niche "AI tools"

# 输出位置
# memory/reports/affiliate-products-YYYY-MM.md
```

### 2. 创建 Landing Page
```bash
# 生成 landing page
python3 scripts/create-landing-page.py --product "CustomGPT"

# 输出位置
# landing-pages/[product]/index.html
```

### 3. 追踪 Conversion
```bash
# 获取 conversion 数据
python3 scripts/fetch-conversion.py

# 输出位置
# memory/reports/affiliate-YYYY-MM-DD.md
```

## 范例

**用户**：「整一个 CustomGPT landing page」

**Affiliate Agent**：
1. 研究 CustomGPT affiliate program
2. 生成 landing page HTML
3. 整合 affiliate links
4. 追踪 conversion rate
5. 输出报告

## 报告格式

```markdown
# Affiliate Report - YYYY-MM-DD

## 💰 收入概览
- 总收入: $XXX
- Recurring: $XXX/month
- One-time: $XXX

## 📊 产品表现
| 产品 | 点击 | 转换 | 收入 | CTR |
|------|------|------|------|-----|
| CustomGPT | XXX | XX | $XXX | X.X% |

## 💡 优化建议
- [建议 1]
- [建议 2]

## 🎯 下月计划
- [ ] [任务 1]
- [ ] [任务 2]
```

## 重点产品
1. **CustomGPT** - 20% recurring ⭐⭐⭐⭐⭐
2. **Shopify** - $150-3,000 per sale
3. **ClickBank** - 高佣金数位产品

## 相关文件
- Landing Pages：`landing-pages/`
- 报告：`memory/reports/affiliate-*.md`
- 收入追踪：`memory/income-tracking.md`

## 模型
- **策略**：GLM-5
- **数据分析**：MiniMax

## 状态
- ✅ CustomGPT Landing Page 已创建（2026-03-13）
- ⏳ Conversion 追踪开发中
