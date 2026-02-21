# SuppMatch - Affiliate Marketing Deployment Guide

## ✅ 已完成項目

### 1. UI 更新
- 新增「邊度買」按鈕（每個產品獨立）
- 顯示 iHerb + Amazon 兩個平台選項
- 追蹤點擊次數（localStorage）
- Affiliate disclosure 聲明

### 2. Affiliate 配置
- `src/data/affiliateConfig.ts` - 統一管理 affiliate IDs
- 支援 iHerb 同 Amazon
- 自動生成 affiliate links

### 3. SEO 優化
- Structured data 準備

---

## 🚀 下一步：部署流程

### Step 1: 申請 Affiliate IDs

**iHerb:**
1. 前往 https://www.iherb.com/partners/affiliate
2. 註冊 account
3.拎到你既 `rcode` (如: `ken123`)

**Amazon:**
1. 前往 https://affiliate-program.amazon.com
2. 註冊 account  
3.拎到你既 `Associate ID` (如: `ken0218-20`)

### Step 2: 設定環境變數

建立 `.env.local` 檔案：

```bash
# .env.local
IHERB_AFF_ID=你的iHerb_rcode
AMAZON_AFF_ID=你的Amazon_AssociateID
```

Example:
```bash
IHERB_AFF_ID=ken123
AMAZON_AFF_ID=ken0218-20
```

### Step 3: 更新 symptoms.ts（可選）

如果你想每個產品有獨特 link，編輯 `src/data/symptoms.ts`：

```typescript
recommendations: [
  {
    name: { "zh-HK": "維他命B群", ... },
    // 新增呢啲欄位
    iherb_url: "https://www.iherb.com/r/vitamin-b-complex?rcode=ken123",
    amazon_url: "https://www.amazon.com/dp/B000VX2KMO?tag=ken0218-20"
  }
]
```

### Step 4: 部署到 Vercel

```bash
cd suppmatch-project
vercel --prod
```

確保喺 Vercel dashboard 設定環境變數：
- `IHERB_AFF_ID`
- `AMAZON_AFF_ID`

### Step 5: 追蹤收入

**本地追蹤（browser localStorage）:**
```javascript
// 睇 clicks
JSON.parse(localStorage.getItem('suppmatch_clicks'))
```

**Vercel Analytics:**
- 開啟 Vercel Analytics
- 追蹤 page views 同 conversions

---

## 📊 預期效果

| 指標 | 預期 |
|------|------|
| 轉化率 | 2-5% |
| 平均訂單 | $30-50 |
| 佣金比例 | 5-10% |
| 每月收入（5,000 visits） | $300-1,000 |

---

## 🛠️ 技術細節

### 新增檔案
- `src/data/affiliateConfig.ts` - Affiliate 設定
- `src/app/page_updated.tsx` - 新版 UI（建議 rename 為 page.tsx）

### 修改位置
- Line 8: Import affiliateConfig
- Line 280-340: WhereToBuyButton component
- Line 400-460: Enhanced RecommendationView
- Footer: Affiliate disclosure

### 使用既 feature
- localStorage 追蹤 clicks
- Affiliate link 自動生成
- 雙平台對比（iHerb vs Amazon）
- Responsive design

---

## ⚠️ 注意

1. **Affiliate disclosure**: 法律要求必須披露使用 affiliate links
2. **產品價格**: 可能變動，建議用 price range
3. **佣金比例**: 會因產品類別而唔同
4. **Cookie duration**: 
   - iHerb: 30 days
   - Amazon: 24 hours

---

## 📈 擴展建議

1. **添加更多產品數據** - 每個症狀多啲產品推薦
2. **價格比較功能** - 顯示邊個平台平啲
3. **用戶評論整合** - 顯示產品 rating
4. **Email list** - 建立 mailing list 做 remarketing
5. **Content marketing** - 寫 blog 文章引流

---

## 🔗 相關連結

- [iHerb Affiliate Program](https://www.iherb.com/partners/affiliate)
- [Amazon Associates](https://affiliate-program.amazon.com)
- [Vercel Deployment](https://vercel.com)

