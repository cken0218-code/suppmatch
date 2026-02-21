# SuppMatch 項目結構文檔

## 📁 項目資訊

| 項目 | 內容 |
|------|------|
| **項目名稱** | SuppMatch |
| **GitHub** | https://github.com/cken0218-code/suppmatch |
| **Vercel** | https://suppmatch.vercel.app |
| **主要功能** | 症狀揀選 → 營養補充品推薦 + 聯盟行銷 |

---

## 📂 目錄結構

```
suppmatch/
├── .github/
│   └── workflows/           # CI/CD 配置
├── data/
│   └── symptoms.json        # 症狀數據（原有）
│   └── symptoms.json       # 症狀數據 + Affiliate 結構（新版）
├── public/                  # 靜態資源
├── src/
│   ├── app/
│   │   ├── page.tsx        # 主頁面（UI）
│   │   ├── page_updated.tsx # 🆕 新版 UI（含「邊度買」按鈕）
│   │   └── layout.tsx      # Layout + SEO
│   ├── contexts/
│   │   └── LocaleContext.tsx # 多語言上下文
│   └── data/
│       ├── affiliateConfig.ts  # 🆕 Affiliate 配置
│       ├── symptoms.ts       # 症狀數據（TypeScript）
│       └── seo.ts           # 🆕 SEO 結構化數據
├── package.json
├── next.config.ts
├── tsconfig.json
└── README.md
```

---

## 📊 數據存放位置

| 類型 | 路徑 | 說明 |
|------|------|------|
| **主數據** | `/workspace/suppmatch-project/data/` | 症狀、配置數據 |
| **源代碼** | `/workspace/suppmatch-project/src/` | React 組件、邏輯 |
| **部署** | Vercel | https://suppmatch.vercel.app |
| **備份** | GitHub | https://github.com/cken0218-code/suppmatch |

---

## 🔗 重要連結

### 核心連結
- **GitHub Repo**: https://github.com/cken0218-code/suppmatch
- **Vercel Deploy**: https://suppmatch.vercel.app
- **Demo Site**: https://suppmatch.vercel.app

### Affiliate 平台
- **iHerb**: https://www.iherb.com/partners/affiliate
- **Amazon**: https://affiliate-program.amazon.com

---

## 🛠️ 技術棧

| 技術 | 版本 | 用途 |
|------|------|------|
| Next.js | 14.2.3 | React Framework |
| React | 18.2.0 | UI Library |
| TypeScript | 5.x | 類型安全 |
| Tailwind CSS | 3.x | 樣式 |
| Fuse.js | 7.1.0 | 搜索功能 |
| Vercel | - | 部署平台 |

---

## 📝 數據結構

### 症狀數據 (symptoms.json)

```typescript
interface Symptom {
  id: string;                    // 症狀 ID (如: "headache")
  category_id: string;           // 分類 ID (如: "brain-cognitive")
  names: {
    'zh-HK': string;            // 繁體中文
    'zh-CN': string;            // 簡體中文
    'en': string;               // 英文
  };
  description?: {                // 🆕 症狀描述
    'zh-HK': string;
    'zh-CN': string;
    'en': string;
  };
  seo_keywords?: {               // 🆕 SEO 關鍵詞
    'zh-HK': string[];
    'zh-CN': string[];
    'en': string[];
  };
  iherb_category: {
    name: string;               // iHerb 分類名稱
    url: string;               // 🆕 Affiliate URL
  };
  amazon_category?: {           // 🆕 Amazon 分類
    name: string;
    url: string;               // Affiliate URL
  };
  recommendations: {
    name: {
      'zh-HK': string;
      'zh-CN': string;
      'en': string;
    };
    iherb_url?: string;        // 🆕 產品連結
    amazon_url?: string;       // 🆕 產品連結
    price_range?: string;      // 🆕 價格範圍
    commission?: string;       # 🆕 佣金比例
  }[];
}
```

### Affiliate 配置 (affiliateConfig.ts)

```typescript
interface AffiliatePlatform {
  name: string;
  affiliateId: string;          // 環境變數控制
  baseUrl: string;
  commission: string;
  color: string;
  logo: string;
}
```

---

## 🚀 部署資訊

### 本地開發
```bash
cd /workspace/suppmatch-project
npm install
npm run dev
# 訪問 http://localhost:3000
```

### 部署到 Vercel
```bash
cd /workspace/suppmatch-project
vercel --prod
```

### 環境變數 (.env.local)
```bash
IHERB_AFF_ID=你的rcode
AMAZON_AFF_ID=你的AssociateID
```

---

## 📈 監控指標

| 指標 | 工具 | 位置 |
|------|------|------|
| **訪問量** | Vercel Analytics | Vercel Dashboard |
| **點擊追蹤** | localStorage | 瀏覽器本地 |
| **GitHub 活動** | GitHub API | github.com/cken0218-code/suppmatch |
| **錯誤監控** | Vercel | Vercel Dashboard |

---

## 🔧 維護任務

### 每日
- [ ] 檢查 Vercel 錯誤日志
- [ ] 監控點擊數據

### 每週
- [ ] 更新症狀數據（如需要）
- [ ] 檢查 affiliate links 有效性
- [ ] Review GitHub commits

### 每月
- [ ] 性能優化
- [ ] SEO 審計
- [ ] 市場趨勢更新

---

## 📅 更新日誌

| 日期 | 更新內容 |
|------|----------|
| 2026-02-20 | 新增「邊度買」UI + Affiliate 功能 |
| 2026-02-20 | 建立項目結構文檔 |

