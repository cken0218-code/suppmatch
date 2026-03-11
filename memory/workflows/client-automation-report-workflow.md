# Workflow 3: 客户自动化报表

## 🎯 目标
为 Local Business 客户自动生成周报/月报，包括数据分析、趋势、建议

---

## 📊 流程图

```
┌─────────────────────────────────────────────────┐
│       客户报表自动化流程 (每周五 18:00)             │
└─────────────────────────────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   n8n 触发器 (Schedule)   │
        │   时间: 周五 18:00       │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   读取客户列表           │
        │   MCP Filesystem:       │
        │   ~/clients/clients.json │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   循环处理每个客户        │
        │   For Each Client:      │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   收集数据               │
        │   • Google Analytics    │
        │   • 社交媒体数据         │
        │   • 销售数据            │
        │   • 客户反馈            │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   数据处理与分析         │
        │   JavaScript/Python:    │
        │   • 计算增长率           │
        │   • 识别趋势            │
        │   • 对比上周            │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   AI 生成洞察           │
        │   OpenClaw:             │
        │   "分析数据，提供        │
        │    可行动建议"           │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   生成 PDF 报表          │
        │   工具: HTML → PDF      │
        │   • 图表               │
        │   • 表格               │
        │   • 建议               │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   发送 Email            │
        │   • 附件: PDF 报表      │
        │   • 正文: 摘要          │
        │   • CTA: 预约咨询       │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   保存记录              │
        │   MCP Memory:           │
        │   • 发送状态            │
        │   • 客户反馈            │
        │   • 下次提醒            │
        └─────────────────────────┘
                      ↓
        ┌─────────────────────────┐
        │   Discord 通知 (内部)    │
        │   "✅ 客户 X 报表已发送"  │
        └─────────────────────────┘
                      ↓
                  [下一个客户 ↓]
```

---

## 🔧 详细步骤

### Step 1: 读取客户列表
**工具**: MCP Server - filesystem
**文件**: `~/clients/clients.json`
**格式**:
```json
{
  "clients": [
    {
      "id": "client-001",
      "name": "ABC Restaurant",
      "email": "owner@abc-restaurant.com",
      "services": ["social-media", "seo", "email-marketing"],
      "reportFrequency": "weekly",
      "nextReport": "2026-03-13",
      "googleAnalyticsId": "UA-123456",
      "socialAccounts": {
        "facebook": "abcrestaurant",
        "instagram": "@abc_restaurant"
      }
    }
  ]
}
```

---

### Step 2: 收集数据
**工具**: MCP Server - fetch + API calls

**2.1 Google Analytics**
```javascript
const gaData = await fetch('https://analyticsreporting.googleapis.com/v4/reports:batchGet', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_TOKEN'
  },
  body: JSON.stringify({
    reportRequests: [{
      viewId: clientId,
      dateRanges: [
        { startDate: '7daysAgo', endDate: 'today' }
      ],
      metrics: [
        { expression: 'ga:sessions' },
        { expression: 'ga:users' },
        { expression: 'ga:pageviews' },
        { expression: 'ga:bounceRate' }
      ]
    }]
  })
});
```

**2.2 社交媒体**
```javascript
// Facebook Insights
const fbData = await fetch(`https://graph.facebook.com/v18.0/${pageId}/insights`, {
  params: {
    metric: 'page_impressions,page_engaged_users',
    period: 'week'
  }
});

// Instagram Insights
const igData = await fetch(`https://graph.facebook.com/v18.0/${igId}/insights`, {
  params: {
    metric: 'impressions,reach,profile_views',
    period: 'week'
  }
});
```

**2.3 销售数据**
```javascript
// 从客户提供的 CSV 或 API
const salesData = await mcp.filesystem.readFile(`~/clients/${clientId}/sales.csv`);
```

---

### Step 3: 数据分析
**工具**: JavaScript (in n8n Function Node)
**代码**:
```javascript
// 计算增长率
const calculateGrowth = (current, previous) => {
  if (previous === 0) return 0;
  return ((current - previous) / previous * 100).toFixed(2);
};

// 分析数据
const analysis = {
  website: {
    sessions: currentWeek.sessions,
    growth: calculateGrowth(currentWeek.sessions, lastWeek.sessions),
    trend: currentWeek.sessions > lastWeek.sessions ? '📈' : '📉'
  },
  social: {
    facebook: {
      impressions: fbData.impressions,
      engagement: fbData.engagement,
      growth: calculateGrowth(fbData.impressions, lastWeekFb.impressions)
    },
    instagram: {
      reach: igData.reach,
      profileViews: igData.profileViews,
      growth: calculateGrowth(igData.reach, lastWeekIg.reach)
    }
  }
};

return { json: analysis };
```

---

### Step 4: AI 生成洞察
**工具**: OpenClaw
**Prompt**:
```
你是数字营销分析师。

客户：{{client.name}}
行业：餐厅
本周数据：
- 网站访问：{{sessions}} ({{growth}}%)
- Facebook 触及：{{fb.impressions}}
- Instagram 触及：{{ig.reach}}
- 销售额：${{sales}}

任务：
1. 分析本周表现（3-5 点）
2. 识别机会与问题
3. 提供具体可行动建议（3-5 条）
4. 预测下周趋势

输出格式：
## 📊 本周表现
[分析内容]

## 💡 行动建议
[建议列表]

## 🔮 下周预测
[预测内容]

语气：专业、实用、鼓励
```

**示例输出**:
```markdown
## 📊 本周表现
✅ **网站流量增长 15%** - 主要来自 Instagram 
⚠️ **Facebook 互动下降 8%** - 内容发布时间需调整
✅ **销售额提升 12%** - 新菜单推广有效

## 💡 行动建议
1. **增加 Instagram Stories** - 每日 2-3 条，展示菜品制作过程
2. **优化 Facebook 发布时间** - 改为晚上 7-9 点（用餐时间）
3. **推出周末优惠** - 针对新客户，提升转化率

## 🔮 下周预测
- 网站流量预计增长 10-15%
- 社交媒体互动稳定
- 建议加大周末推广力度
```

---

### Step 5: 生成 PDF 报表
**工具**: n8n HTML to PDF Node
**HTML 模板**:
```html
<!DOCTYPE html>
<html>
<head>
  <style>
    body { font-family: Arial, sans-serif; }
    .header { background: #4A90E2; color: white; padding: 20px; }
    .section { margin: 20px 0; padding: 15px; background: #f5f5f5; }
    .metric { display: inline-block; margin: 10px; }
    .chart { width: 100%; height: 300px; }
    .recommendation { border-left: 4px solid #4A90E2; padding-left: 10px; }
  </style>
</head>
<body>
  <div class="header">
    <h1>{{client.name}} - 周报</h1>
    <p>日期：{{date}}</p>
  </div>

  <div class="section">
    <h2>📊 关键指标</h2>
    <div class="metric">
      <h3>网站访问</h3>
      <p>{{sessions}} ({{growth}}%) {{trend}}</p>
    </div>
    <div class="metric">
      <h3>社交媒体触及</h3>
      <p>FB: {{fb.impressions}} | IG: {{ig.reach}}</p>
    </div>
  </div>

  <div class="section">
    <h2>📈 数据趋势</h2>
    <img src="{{chartUrl}}" class="chart" />
  </div>

  <div class="section">
    <h2>💡 AI 洞察与建议</h2>
    {{aiInsights}}
  </div>

  <div class="section">
    <h2>📅 下周计划</h2>
    <ul>
      {{#each nextSteps}}
      <li>{{this}}</li>
      {{/each}}
    </ul>
  </div>

  <footer>
    <p>如有疑问，请回复此邮件或预约咨询：[链接]</p>
    <p>Powered by OpenClaw AI</p>
  </footer>
</body>
</html>
```

---

### Step 6: 发送 Email
**工具**: n8n Email Node (SMTP)
**配置**:
```javascript
{
  "from": "reports@yourbusiness.com",
  "to": "{{client.email}}",
  "subject": "📊 {{client.name}} 周报 - {{date}}",
  "text": `
Hi {{client.name}},

你嘅本周数字营销报告已生成！

📊 **亮点**：
- 网站流量：{{sessions}} ({{growth}}%)
- 社交触及：{{socialReach}}
- 销售额：${{sales}}

详细报告请见附件。

有问题？回复此邮件或预约咨询：
[预约链接]

Best,
Your Name
  `,
  "attachments": [{
    "filename": "{{client.name}}-report-{{date}}.pdf",
    "content": "{{pdfData}}"
  }]
}
```

---

### Step 7: 保存记录
**工具**: MCP Server - memory
**数据**:
```json
{
  "clientId": "client-001",
  "reportDate": "2026-03-06",
  "sent": true,
  "openRate": null,
  "feedback": null,
  "nextReport": "2026-03-13",
  "metrics": {
    "sessions": 1250,
    "growth": 15.2,
    "sales": 8500
  }
}
```

---

## 📊 数据流

```
输入: 
  - 客户列表 (JSON)
  - API tokens
  - 历史数据
  
处理:
  - 收集: 5-10 个数据源
  - 分析: 趋势、增长率
  - 生成: AI 洞察
  - 渲染: PDF 报表
  
输出:
  - Email: PDF 附件
  - 通知: Discord (内部)
  - 记录: Memory server
```

---

## 💰 成本

**API 调用**:
- Google Analytics API: 免费
- Facebook/Instagram API: 免费
- OpenClaw AI: ~$0.10-0.20/客户
- Email (Gmail SMTP): 免费

**每个客户成本**: ~$0.15
**10 个客户/周**: ~$1.50/周 = ~$6/月

---

## ⏱️ 执行时间

- 收集数据: ~5-10秒/客户
- 数据分析: ~2秒
- AI 生成: ~10秒
- PDF 渲染: ~5秒
- 发送 Email: ~2秒

**总计**: ~25-30秒/客户

**10 个客户**: ~5分钟

---

## 🎯 成功指标

- ✅ 每周五准时发送
- ✅ Email 打开率 > 60%
- ✅ 客户满意度 > 4.5/5
- ✅ 节省人工时间 > 2 小时/周

---

## 🔄 变体

### 变体 A: 月报
- 触发: 每月 1 号
- 内容: 更详细的分析
- 格式: 20-30 页 PDF

### 变体 B: 实时仪表板
- 工具: n8n + Google Data Studio
- 功能: 实时数据展示
- 访问: 客户可随时查看

### 变体 C: 自动跟进
- 触发: 报表发送 3 天后
- 动作: 询问客户反馈
- 记录: 满意度调查

---

## 🐛 故障排除

### 问题 1: API token 过期
**解决**:
- 自动刷新 token
- 提前 7 天通知
- 备用手动数据输入

### 问题 2: Email 进入垃圾箱
**解决**:
- 设置 SPF/DKIM
- 使用专业 email 服务
- 客户加白名单

### 问题 3: 客户数据缺失
**解决**:
- 标注缺失部分
- 使用历史数据估算
- 通知客户补充

---

## 🚀 扩展方向

1. **客户仪表板**
   - 实时查看数据
   - 自定义报表
   - 下载历史报告

2. **自动优化建议**
   - 基于历史数据
   - ML 预测
   - 自动调整策略

3. **多语言支持**
   - 根据客户语言
   - 自动翻译报告
   - 本地化建议

4. **整合 CRM**
   - Salesforce
   - HubSpot
   - 自动同步数据

---

## 📈 收费建议

**基础服务**:
- 周报: $300-500/月/客户
- 月报: $200-300/月/客户

**增值服务**:
- 实时仪表板: +$100/月
- AI 优化建议: +$150/月
- 24/7 支持: +$200/月

**潜在收入**: 
- 10 个客户 × $400 = **$4,000/月**
- 20 个客户 = **$8,000/月**

---

**下一步**: 
- ✅ 3 个 Workflows 设计完成
- 📝 总结对比
- 🎯 进入 Option 3（快速试用）
