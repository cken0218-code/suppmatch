import type { Metadata } from 'next';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { symptoms } from '@/data/symptoms';
import { CATEGORIES } from '@/data/categories';
import { siteConfig } from '@/data/seo';
import { isAppLocale, LOCALES, type AppLocale, symptomPath } from '@/lib/i18n-routing';
import { SiteShell } from '@/components/SiteShell';

export function generateStaticParams() {
  return LOCALES.map((locale) => ({ locale }));
}

export function generateMetadata({
  params,
}: {
  params: { locale: string };
}): Metadata {
  if (!isAppLocale(params.locale)) return {};
  const locale = params.locale as AppLocale;
  const title =
    locale === 'en'
      ? 'Symptom guides — SuppMatch'
      : locale === 'zh-CN'
        ? '症状指南 — SuppMatch'
        : '症狀指南 — SuppMatch';
  const description = siteConfig.description[locale];
  return {
    title,
    description,
    alternates: {
      canonical: `${siteConfig.url}/${locale}/`,
      languages: Object.fromEntries(LOCALES.map((l) => [l, `${siteConfig.url}/${l}/`])),
    },
  };
}

export default function LocaleHubPage({ params }: { params: { locale: string } }) {
  if (!isAppLocale(params.locale)) notFound();
  const locale = params.locale as AppLocale;

  const copy = {
    title:
      locale === 'en'
        ? 'Symptom guides'
        : locale === 'zh-CN'
          ? '症状指南'
          : '症狀指南',
    desc:
      locale === 'en'
        ? 'SEO-friendly pages for common concerns. Open any guide, or use the free recommender tool.'
        : locale === 'zh-CN'
          ? '面向常见不适的参考页面。可打开任一指南，或使用免费推荐工具。'
          : '面向常見不適嘅參考頁。可以打開任一指南，或使用免費推薦工具。',
    app: locale === 'en' ? 'Open recommender' : locale === 'zh-CN' ? '打开推荐工具' : '打開推薦工具',
    all: locale === 'en' ? 'All symptoms' : locale === 'zh-CN' ? '全部症状' : '全部症狀',
  };

  return (
    <SiteShell locale={locale} pathSuffix="/">
      <div className="space-y-8">
        <header className="space-y-3">
          <h1 className="text-3xl font-bold text-white">{copy.title}</h1>
          <p className="text-zinc-400">{copy.desc}</p>
          <Link
            href="/"
            className="inline-flex px-4 py-2.5 rounded-xl bg-gradient-to-r from-accent-purple to-accent-blue text-white text-sm font-semibold"
          >
            {copy.app}
          </Link>
        </header>

        {CATEGORIES.map((cat) => {
          const items = symptoms.filter((s) => s.category_id === cat.id);
          if (items.length === 0) return null;
          return (
            <section key={cat.id} className="space-y-3">
              <h2 className="text-lg font-bold text-white flex items-center gap-2">
                <span>{cat.emoji}</span>
                {cat.names[locale]}
              </h2>
              <div className="flex flex-wrap gap-2">
                {items.map((s) => (
                  <Link
                    key={s.id}
                    href={symptomPath(locale, s.id)}
                    className="px-3 py-1.5 rounded-full text-sm border border-surface-border text-zinc-300 hover:border-accent-purple hover:text-white transition-colors"
                  >
                    {s.names[locale]}
                  </Link>
                ))}
              </div>
            </section>
          );
        })}

        <section className="space-y-3">
          <h2 className="text-lg font-bold text-white">{copy.all}</h2>
          <ul className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-sm">
            {symptoms.map((s) => (
              <li key={s.id}>
                <Link
                  href={symptomPath(locale, s.id)}
                  className="text-zinc-400 hover:text-white underline-offset-2 hover:underline"
                >
                  {s.names[locale]}
                </Link>
              </li>
            ))}
          </ul>
        </section>
      </div>
    </SiteShell>
  );
}
