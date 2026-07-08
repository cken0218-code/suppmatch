import type { Metadata } from 'next';
import './globals.css';
import { siteConfig, getHomeSchemas } from '@/data/seo';
import { JsonLd } from '@/components/JsonLd';

export const metadata: Metadata = {
  title: {
    default: 'SuppMatch - 症狀揀選 → 營養補充品推薦',
    template: '%s | SuppMatch',
  },
  description:
    '揀選症狀 → 推薦最適合既營養補充品。iHerb、Amazon熱門保健品推薦。免費症狀對照保健品建議。',
  keywords: [
    '保健品推薦',
    '營養補充品',
    'iHerb推薦',
    'Amazon保健品',
    '維他命推薦',
    '保健品邊度買',
    '補充品建議',
    '健康保健品',
    '香港保健品',
    '台灣保健品',
  ],
  authors: [{ name: 'SuppMatch' }],
  creator: 'SuppMatch',
  publisher: 'SuppMatch',
  metadataBase: new URL(siteConfig.url),
  alternates: {
    canonical: siteConfig.url,
    languages: {
      'zh-HK': `${siteConfig.url}/zh-HK/`,
      'zh-CN': `${siteConfig.url}/zh-CN/`,
      en: `${siteConfig.url}/en/`,
    },
  },
  openGraph: {
    type: 'website',
    locale: 'zh_HK',
    alternateLocale: ['zh_CN', 'en_US'],
    url: siteConfig.url,
    siteName: 'SuppMatch',
    title: 'SuppMatch - 症狀揀選 → 營養補充品推薦',
    description: '揀選症狀 → 推薦最適合既營養補充品。iHerb、Amazon熱門保健品推薦。',
    images: [
      {
        url: `${siteConfig.url}/og-image.png`,
        width: 1200,
        height: 630,
        alt: 'SuppMatch - 保健品推薦',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'SuppMatch - 症狀揀選 → 營養補充品推薦',
    description: '揀選症狀 → 推薦最適合既營養補充品',
    images: [`${siteConfig.url}/og-image.png`],
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="zh-HK">
      <body>
        <JsonLd data={getHomeSchemas()} />
        {children}
      </body>
    </html>
  );
}
