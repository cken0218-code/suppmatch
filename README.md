# SuppMatch - 營養補充品推薦網站

## 📱 簡介
選擇您的症狀/身體情況，獲取iHerb營養補充品推薦。

## 🌐 支援語言
- 🇭🇰 繁體中文 (香港)
- 🇨🇳 簡體中文
- 🇺🇸 English

## 🚀 快速開始

### 1. 安裝依賴
```bash
npm install
```

### 2. 運行開發服務器
```bash
npm run dev
```

### 3. 打開瀏覽器
訪問 [http://localhost:3000](http://localhost:3000)

## 📁 項目結構
```
suppmatch/
├── src/
│   ├── app/
│   │   ├── page.tsx          # 主頁面
│   │   ├── layout.tsx        # Layout
│   │   └── globals.css       # 全局樣式
│   ├── contexts/
│   │   └── LocaleContext.tsx # 多語言上下文
│   └── data/
│       └── symptoms.json      # 症狀數據
├── data/
│   └── symptoms.json          # 症狀數據
├── public/
├── package.json
└── README.md
```

## 🛠️ 技術堆疊
- **Framework:** Next.js 14 (App Router)
- **Styling:** Tailwind CSS
- **Language:** TypeScript
- **Data:** JSON (無需數據庫)

## 📝 添加新症狀

編輯 `data/symptoms.json`：

```json
{
  "id": "new-symptom",
  "names": {
    "zh-HK": "新症狀名稱",
    "zh-CN": "新症状名称",
    "en": "New Symptom Name"
  },
  "iherb_category": {
    "name": "iHerb Category Name",
    "url": "https://www.iherb.com/c/category"
  },
  "recommendations": [
    {
      "name": {
        "zh-HK": "推薦補充品1",
        "zh-CN": "推荐补充品1",
        "en": "Supplement 1"
      }
    }
  ]
}
```

## 🚀 部署到 Vercel

1. Push代碼到GitHub
2. 訪問 [Vercel](https://vercel.com)
3. Import項目
4. 自動部署

## ⚠️ 免責聲明
本網站提供的信息僅供參考，不構成醫療建議。使用前請諮詢醫生。
