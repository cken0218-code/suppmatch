export const LOCALES = ['zh-HK', 'zh-CN', 'en'] as const;
export type AppLocale = (typeof LOCALES)[number];

export function isAppLocale(value: string): value is AppLocale {
  return (LOCALES as readonly string[]).includes(value);
}

export function symptomPath(locale: AppLocale, symptomId: string): string {
  return `/${locale}/symptom/${symptomId}/`;
}

export function homePath(locale?: AppLocale): string {
  // Main interactive app stays at root; locale only used for SEO pages
  return locale ? `/${locale}/` : '/';
}
