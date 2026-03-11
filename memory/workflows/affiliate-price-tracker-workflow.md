# Workflow 2: Affiliate 产品价格追踪

## 🎯 目标
监控 Amazon/ClickBank 产品价格，降价时自动通知，并生成推广文案

---

## 📊 流程图

```
┌─────────────────────────────────────────────────┐
│          价格监控流程 (每小时运行)                  │
└─────────────────────────────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   n8n 触发器 (Schedule)   │
        │   时间: 每 1 小时         │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   读取产品列表           │
        │   MCP Filesystem:       │
        │   ~/affiliate-products/  │
        │   products.json         │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   循环处理每个产品        │
        │   For Each Product:     │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   MCP Server: Fetch     │
        │   抓取 Amazon 产品页     │
        │   或 ClickBank API      │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   提取价格信息           │
        │   • 原价                │
        │   • 现价                │
        │   • 折扣率              │
        │   • 库存状态            │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   比较历史价格           │
        │   MCP Memory:           │
        │   查询上次价格          │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   价格变化？            │
        └─────────────────────────┘
              ↓Yes        ↓No
    ┌──────────────┐   ┌──────────┐
    │ 降价 > 10%？  │   │ 跳过     │
    └──────────────┘   └──────────┘
         ↓Yes    ↓No
    ┌─────────┐ ┌──────────┐
    │ 触发通知 │ │ 记录变化  │
    └─────────┘ └──────────┘
         ↓
    ┌─────────────────────────┐
    │   AI 生成推广文案         │
    │   OpenClaw:             │
    │   "写个吸引的推广文案     │
    │    强调降价优势"         │
    └─────────────────────────┘
         ↓
    ┌─────────────────────────┐
    │   保存到文件             │
    │   MCP Filesystem:       │
    │   price-alerts/         │
    │   {{product-id}}.md     │
    └─────────────────────────┘
         ↓
    ┌─────────────────────────┐
    │   多渠道通知             │
    │   • Discord (即时)      │
    │   • Email (详细)        │
    │   • Telegram (手机)     │
    └─────────────────────────┘
         ↓
    ┌─────────────────────────┐
    │   更新价格历史           │
    │   MCP Memory:           │
    │   保存新价格            │
    └─────────────────────────┘
         ↓
              [下一个产品 ↓]
```

---

## 🔧 详细步骤

### Step 1: 读取产品列表
**工具**: MCP Server - filesystem
**文件**: `~/affiliate-products/products.json`
**格式**:
```json
{
  "products": [
    {
      "id": "B08N5KWB9H",
      "platform": "amazon",
      "name": "Sony WH-1000XM4",
      "category": "electronics",
      "targetPrice": 300,
      "affiliateLink": "https://amzn.to/xxx",
      "priority": "high"
    },
    {
      "id": "clickbank-12345",
      "platform": "clickbank",
      "name": "Course XYZ",
      "category": "education",
      "targetPrice": 50,
      "affiliateLink": "https://xxx.clickbank.net",
      "priority": "medium"
    }
  ]
}
```

---

### Step 2: 抓取价格
**工具**: MCP Server - fetch
**Amazon 示例**:
```javascript
// 使用 Amazon Product Advertising API
const response = await fetch('https://api.amazon.com/products', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_TOKEN'
  },
  body: JSON.stringify({
    productIds: [productId]
  })
});

const data = await response.json();
return {
  currentPrice: data.price,
  originalPrice: data.listPrice,
  discount: ((data.listPrice - data.price) / data.listPrice * 100),
  inStock: data.availability === 'In Stock'
};
```

---

### Step 3: 比较历史价格
**工具**: MCP Server - memory
**查询**:
```javascript
// 查询上次价格
const lastPrice = await mcp.memory.query({
  key: `price_${productId}`,
  limit: 1
});

if (lastPrice) {
  const priceChange = ((currentPrice - lastPrice.value) / lastPrice.value * 100);
  
  if (priceChange < -10) {
    // 降价超过 10%，触发通知
    return { alert: true, change: priceChange };
  }
}
```

---

### Step 4: AI 生成推广文案
**工具**: OpenClaw
**Prompt**:
```
你是联盟行销文案专家。

产品信息：
- 名称: {{product.name}}
- 原价: ${{originalPrice}}
- 现价: ${{currentPrice}}
- 折扣: {{discount}}%
- 分类: {{category}}

任务：
1. 写一个吸引的标题（不超过 20 字）
2. 写一段推广文案（50-100 字）
3. 强调降价优势
4. 制造紧迫感
5. 包含 CTA（行动呼吁）

输出格式：
【标题】
【文案】
【CTA】
```

**示例输出**:
```
【标题】🎧 Sony 耳机暴跌 30%！限时优惠
【文案】Sony WH-1000XM4 顶级降噪耳机，原价 $399，
而家只系 $279！降了足足 $120！主动降噪、
30 小时续航、舒适佩戴，强烈推荐！
【CTA】👉 立即抢购：[链接]
```

---

### Step 5: 多渠道通知
**Discord**:
```javascript
{
  "embeds": [{
    "title": "🔥 价格警报：{{product.name}}",
    "color": 16711680,
    "fields": [
      {
        "name": "原价",
        "value": "${{originalPrice}}",
        "inline": true
      },
      {
        "name": "现价",
        "value": "**${{currentPrice}}**",
        "inline": true
      },
      {
        "name": "折扣",
        "value": "{{discount}}% ⬇️",
        "inline": true
      },
      {
        "name": "推广文案",
        "value": "{{generatedCopy}}"
      }
    ],
    "url": "{{affiliateLink}}"
  }]
}
```

**Email**:
```html
<h2>🔥 价格警报：{{product.name}}</h2>
<p><strong>原价:</strong> <del>${{originalPrice}}</del></p>
<p><strong>现价:</strong> <span style="color: red; font-size: 24px;">${{currentPrice}}</span></p>
<p><strong>折扣:</strong> {{discount}}%</p>

<hr>

<h3>推广文案：</h3>
<div style="background: #f5f5f5; padding: 15px;">
  {{generatedCopy}}
</div>

<p>
  <a href="{{affiliateLink}}" style="background: #ff6600; color: white; padding: 10px 20px; text-decoration: none;">
    立即购买
  </a>
</p>
```

---

## 📊 数据流

```
输入: products.json (产品列表)
  ↓
处理:
  - 读取: 10-50 个产品
  - 抓取: 每个产品价格
  - 比较: 历史价格
  - 生成: AI 文案
  ↓
输出:
  - 通知: Discord/Email/Telegram
  - 文件: 推广文案
  - 数据库: 价格历史
```

---

## 💰 成本

**API 调用**:
- Amazon API: 免费（有 quota）
- ClickBank API: 免费
- OpenClaw AI: ~$0.05/次
- Discord/Email: 免费

**每小时成本**: ~$0.10（假设 10 个产品）
**每月成本**: ~$72（如果 24/7 运行）

**优化方案**:
- 减少频率到每 4 小时：$18/月
- 只监控 top 10 产品：$7/月
- 使用缓存：$5/月

---

## ⏱️ 执行时间

- 读取产品列表: ~1秒
- 抓取价格（每个产品）: ~2秒
- 比较历史: ~1秒
- 生成文案: ~5秒
- 发送通知: ~1秒

**总计**: ~10-30秒（取决于产品数量）

---

## 🎯 成功指标

- ✅ 成功监控 10-50 个产品
- ✅ 降价 > 10% 时 5 分钟内通知
- ✅ 自动生成高质量文案
- ✅ Affiliate link 点击率 > 5%

---

## 🔄 变体

### 变体 A: 库存监控
- 触发: 每 30 分钟
- 监控: 库存状态
- 通知: "返货啦！"

### 变体 B: 竞争对手监控
- 监控: 其他 affiliate 的价格
- 分析: 他们的策略
- 调整: 自己的定价

### 变体 C: 季节性产品
- 触发: 黑五、圣诞等
- 监控: 热门节日产品
- 通知: 最佳推广时机

---

## 🐛 故障排除

### 问题 1: Amazon API 被封
**解决**:
- 使用代理 IP
- 减少请求频率
- 或改用网页抓取（小心违规）

### 问题 2: 价格抓取失败
**解决**:
- 添加重试机制（3 次）
- 使用备用数据源
- 记录失败产品

### 问题 3: AI 文案质量差
**解决**:
- 优化 prompt
- 提供更多上下文
- 人工审核机制

---

## 🚀 扩展方向

1. **自动发布到社交平台**
   - Twitter
   - Facebook
   - Instagram

2. **A/B 测试文案**
   - 生成 3 个版本
   - 追踪转化率
   - 自动优化

3. **价格预测**
   - ML 预测价格趋势
   - 建议"等还是买"

4. **整合到网站**
   - 自动更新价格
   - 动态 banner
   - 倒计时功能

---

**下一步**: 
- ✅ 理解这个 workflow
- 📝 继续 Workflow 3
- 🎯 然后进入 Option 3（试用）
