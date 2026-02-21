// SEO Configuration and Structured Data for SuppMatch
// Health-related SEO best practices for supplement recommendations

import { Symptom } from './symptoms';

// Site-wide SEO configuration
export const siteConfig = {
  name: 'SuppMatch',
  nameEn: 'SuppMatch - Supplement Recommendation Engine',
  description: {
    'zh-HK': '揀選症狀 → 推薦最適合既營養補充品。iHerb、Amazon熱門保健品推薦。',
    'zh-CN': '选择症状 → 推荐最适合的营养补充品。iHerb、Amazon热门保健品推荐。',
    'en': 'Select your symptoms → Get personalized supplement recommendations. Top supplements from iHerb and Amazon.'
  },
  url: 'https://suppmatch.vercel.app',
  locale: 'zh-HK',
  image: 'https://suppmatch.vercel.app/og-image.png',
  keywords: {
    'zh-HK': ['保健品推薦', '營養補充品', 'iHerb推薦', 'Amazon保健品', '維他命推薦', '保健品邊度買'],
    'zh-CN': ['保健品推荐', '营养补充品', 'iHerb推荐', 'Amazon保健品', '维生素推荐', '保健品哪里买'],
    'en': ['supplement recommendations', 'health supplements', 'iHerb supplements', 'Amazon vitamins', 'natural supplements', 'vitamin guide']
  }
};

// Generate WebSite structured data
export function generateWebsiteSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    name: siteConfig.name,
    url: siteConfig.url,
    potentialAction: {
      '@type': 'SearchAction',
      target: {
        '@type': 'EntryPoint',
        urlTemplate: `${siteConfig.url}/search?q={search_term_string}`
      },
      'query-input': 'required name=search_term_string'
    }
  };
}

// Generate WebApplication structured data
export function generateWebApplicationSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebApplication',
    name: siteConfig.name,
    applicationCategory: 'HealthApplication',
    operatingSystem: 'Web',
    url: siteConfig.url,
    offers: {
      '@type': 'Offer',
      price: '0',
      priceCurrency: 'USD'
    },
    description: siteConfig.description['zh-HK']
  };
}

// Generate FAQPage structured data for common supplement questions
export function generateFAQSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: [
      {
        '@type': 'Question',
        name: '保健品幾時食最好？',
        acceptedAnswer: {
          '@type': 'Answer',
          text: '大多數保健品建議係朝早食早餐嗰陣，或者跟隨產品說明書既指示。脂溶性維他命(A、D、E、K)最好同脂肪含量高既食物一齊食。'
        }
      },
      {
        '@type': 'Question',
        name: '可以同時食幾種保健品嗎？',
        acceptedAnswer: {
          '@type': 'Answer',
          text: '一般情況下，多種保健品可以一齊食，但係要注意每日建議攝取量唔好超标。有啲營養素會相互影響吸收，建議相隔2-3小時服用。'
        }
      },
      {
        '@type': 'Question',
        name: '邊度買保健品最正？',
        acceptedAnswer: {
          '@type': 'Answer',
          text: '我地推薦iHerb同Amazon。iHerb係專門賣保健品既平台，種類齊全而且價錢合理。Amazon就選擇多而且送貨方便。記得睇清楚產品評價同成分說明。'
        }
      },
      {
        '@type': 'Question',
        name: '保健品要食幾耐先見效？',
        acceptedAnswer: {
          '@type': 'Answer',
          text: '見效時間因人而異，亦取決於補充品既類型。一般維他命同礦物質需要連續食4-12個禮拜先會見到明顯效果。有啲產品如魚油、益生菌可能需要更長時間。'
        }
      },
      {
        '@type': 'Question',
        name: '食保健品有副作用嗎？',
        acceptedAnswer: {
          '@type': 'Answer',
          text: '適量服用既話，大多數保健品係安全既。但係過量攝取可能會有副作用，亦有可能同藥物產生相互作用。建議服用前咨询醫生意見。'
        }
      }
    ]
  };
}

// Generate MedicalWebPage structured data for health content
export function generateMedicalWebPageSchema(locale: string = 'zh-HK') {
  return {
    '@context': 'https://schema.org',
    '@type': 'MedicalWebPage',
    name: siteConfig.name,
    about: {
      '@type': 'Thing',
      name: 'Dietary Supplements',
      description: 'Nutritional supplements and vitamins for health maintenance'
    },
    audience: {
      '@type': 'Audience',
      audienceType: 'health consumers'
    },
    medicalSpecialty: ['Nutrition', 'Dietary Supplements'],
    url: siteConfig.url,
    description: siteConfig.description[locale] || siteConfig.description['zh-HK']
  };
}

// Generate BreadcrumbList structured data
export function generateBreadcrumbSchema(breadcrumbs: Array<{ name: string; url: string }>) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: breadcrumbs.map((crumb, index) => ({
      '@type': 'ListItem',
      position: index + 1,
      name: crumb.name,
      item: crumb.url
    }))
  };
}

// Generate HowTo structured data for supplement guides
export function generateHowToSchema(steps: Array<{ name: string; text: string }>) {
  return {
    '@context': 'https://schema.org',
    '@type': 'HowTo',
    name: '點樣選擇保健品',
    step: steps.map((step, index) => ({
      '@type': 'HowToStep',
      position: index + 1,
      name: step.name,
      text: step.text
    }))
  };
}

// Generate all structured data as JSON-LD script tags
export function generateAllSchemaScripts(): string {
  const schemas = [
    generateWebsiteSchema(),
    generateWebApplicationSchema(),
    generateFAQSchema(),
    generateMedicalWebPageSchema()
  ];

  return schemas
    .map(schema => `<script type="application/ld+json">${JSON.stringify(schema)}</script>`)
    .join('\n');
}

// Export site config for use in components
export { siteConfig };
