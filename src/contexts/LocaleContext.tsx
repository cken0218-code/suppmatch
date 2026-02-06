import { useState, createContext, useContext, ReactNode } from 'react';

export type Locale = 'zh-HK' | 'zh-CN' | 'en';

interface LocaleContextType {
  locale: Locale;
  setLocale: (locale: Locale) => void;
  t: (key: string) => string;
}

const translations: Record<string, Record<Locale, string>> = {
  'app.title': {
    'zh-HK': 'SuppMatch',
    'zh-CN': 'SuppMatch',
    'en': 'SuppMatch'
  },
  'app.subtitle': {
    'zh-HK': '症狀揀選 → 營養補充品推薦',
    'zh-CN': '症状选取 → 营养补充品推荐',
    'en': 'Select Symptoms → Get Supplement Recommendations'
  },
  'select.symptom': {
    'zh-HK': '邊度唔舒服？',
    'zh-CN': '哪里不舒服？',
    'en': 'What\'s bothering you?'
  },
  'select.category': {
    'zh-HK': '選擇身體部位/情況',
    'zh-CN': '选择身体部位/情况',
    'en': 'Select body area / condition'
  },
  'button.recommend': {
    'zh-HK': '睇推薦',
    'zh-CN': '看推荐',
    'en': 'See Recommendations'
  },
  'button.back': {
    'zh-HK': '返去',
    'zh-CN': '返回',
    'en': 'Back'
  },
  'recommendation.title': {
    'zh-HK': '建議補充品',
    'zh-CN': '建议补充品',
    'en': 'Recommended Supplements'
  },
  'recommendation.description': {
    'zh-HK': '以下係基於您揀選嘅症狀建議：',
    'zh-CN': '以下是基于您选取的症状建议：',
    'en': 'Based on your selected symptoms:'
  },
  'iherb.link': {
    'zh-HK': '去iHerb睇呢類產品',
    'zh-CN': '去iHerb看这类产品',
    'en': 'View products on iHerb'
  },
  'disclaimer': {
    'zh-HK': '⚠️ 本網站提供嘅資訊僅供參考，不構成醫療建議。使用前請諮詢醫生。',
    'zh-CN': '⚠️ 本网站提供的信息仅供参考，不构成医疗建议。使用前请咨询医生。',
    'en': '⚠️ This website provides information for reference only and does not constitute medical advice. Please consult a doctor before use.'
  },
  'language': {
    'zh-HK': '語言',
    'zh-CN': '语言',
    'en': 'Language'
  },
  'view.all': {
    'zh-HK': '睇全部症狀',
    'zh-CN': '看全部症状',
    'en': 'View all symptoms'
  },
  'popular': {
    'zh-HK': '熱門',
    'zh-CN': '热门',
    'en': 'Popular'
  },
  'all': {
    'zh-HK': '全部',
    'zh-CN': '全部',
    'en': 'All'
  }
};

const LocaleContext = createContext<LocaleContextType | null>(null);

export function LocaleProvider({ children, locale: initialLocale }: { children: ReactNode; locale: Locale }) {
  const [locale, setLocale] = useState<Locale>(initialLocale);

  const t = (key: string): string => {
    return translations[key]?.[locale] || key;
  };

  return (
    <LocaleContext.Provider value={{ locale, setLocale, t }}>
      {children}
    </LocaleContext.Provider>
  );
}

export function useLocale() {
  const context = useContext(LocaleContext);
  if (!context) {
    throw new Error('useLocale must be used within LocaleProvider');
  }
  return context;
}
