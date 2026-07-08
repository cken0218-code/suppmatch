import type { MetadataRoute } from 'next';
import { siteConfig } from '@/data/seo';

export default function robots(): MetadataRoute.Robots {
  const base = siteConfig.url.replace(/\/$/, '');
  return {
    rules: {
      userAgent: '*',
      allow: '/',
    },
    sitemap: `${base}/sitemap.xml`,
  };
}
