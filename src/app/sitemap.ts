import type { MetadataRoute } from 'next';
import { symptoms } from '@/data/symptoms';
import { siteConfig } from '@/data/seo';
import { LOCALES, symptomPath } from '@/lib/i18n-routing';

export default function sitemap(): MetadataRoute.Sitemap {
  const base = siteConfig.url.replace(/\/$/, '');
  const now = new Date();

  const entries: MetadataRoute.Sitemap = [
    {
      url: `${base}/`,
      lastModified: now,
      changeFrequency: 'weekly',
      priority: 1,
    },
  ];

  for (const locale of LOCALES) {
    entries.push({
      url: `${base}/${locale}/`,
      lastModified: now,
      changeFrequency: 'weekly',
      priority: 0.8,
    });
    for (const s of symptoms) {
      entries.push({
        url: `${base}${symptomPath(locale, s.id)}`,
        lastModified: now,
        changeFrequency: 'monthly',
        priority: 0.7,
      });
    }
  }

  return entries;
}
