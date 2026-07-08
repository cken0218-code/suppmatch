import type { Metadata } from 'next';
import Link from 'next/link';
import { notFound } from 'next/navigation';
import { symptoms } from '@/data/symptoms';
import { getSymptomPageContent } from '@/data/symptomContent';
import { getProductsForSupplement } from '@/data/supplementProducts';
import { getReasonForSupplement } from '@/data/supplementReasons';
import {
  generateBreadcrumbSchema,
  generateSymptomFAQSchema,
  generateSymptomItemListSchema,
  generateSymptomMedicalWebPageSchema,
  siteConfig,
} from '@/data/seo';
import { isAppLocale, LOCALES, type AppLocale, symptomPath } from '@/lib/i18n-routing';
import { JsonLd } from '@/components/JsonLd';
import { SiteShell } from '@/components/SiteShell';
import { EvidenceBlock } from '@/components/EvidenceBlock';
import { ProductCard } from '@/components/ProductCard';

export const dynamicParams = false;

export function generateStaticParams() {
  return LOCALES.flatMap((locale) =>
    symptoms.map((s) => ({
      locale,
      id: s.id,
    })),
  );
}

function getSymptom(id: string) {
  return symptoms.find((s) => s.id === id);
}

export function generateMetadata({
  params,
}: {
  params: { locale: string; id: string };
}): Metadata {
  if (!isAppLocale(params.locale)) return {};
  const locale = params.locale as AppLocale;
  const symptom = getSymptom(params.id);
  if (!symptom) return {};

  const name = symptom.names[locale];
  const content = getSymptomPageContent(symptom);
  const title =
    locale === 'en'
      ? `${name}: supplements often discussed`
      : locale === 'zh-CN'
        ? `${name}：常被讨论的营养补充品`
        : `${name}：常被討論嘅營養補充品`;
  const description = content.intro[locale].slice(0, 155);
  const path = symptomPath(locale, symptom.id);
  const url = `${siteConfig.url}${path}`;

  return {
    title,
    description,
    alternates: {
      canonical: url,
      languages: Object.fromEntries(
        LOCALES.map((l) => [l, `${siteConfig.url}${symptomPath(l, symptom.id)}`]),
      ),
    },
    openGraph: {
      title,
      description,
      url,
      locale: locale === 'zh-HK' ? 'zh_HK' : locale === 'zh-CN' ? 'zh_CN' : 'en_US',
      type: 'article',
    },
  };
}

export default function SymptomPage({
  params,
}: {
  params: { locale: string; id: string };
}) {
  if (!isAppLocale(params.locale)) notFound();
  const locale = params.locale as AppLocale;
  const symptom = getSymptom(params.id);
  if (!symptom) notFound();

  const content = getSymptomPageContent(symptom);
  const name = symptom.names[locale];
  const path = symptomPath(locale, symptom.id);
  const url = `${siteConfig.url}${path}`;

  const pageTitle =
    locale === 'en'
      ? `${name} — supplement reference`
      : locale === 'zh-CN'
        ? `${name} — 补充品参考`
        : `${name} — 補充品參考`;

  const schemas = [
    generateSymptomMedicalWebPageSchema({
      locale,
      name: pageTitle,
      description: content.intro[locale],
      url,
    }),
    generateSymptomFAQSchema(
      content.faqs.map((f) => ({
        question: f.q[locale],
        answer: f.a[locale],
      })),
    ),
    generateSymptomItemListSchema({
      name: pageTitle,
      url,
      items: symptom.recommendations.map((r, i) => ({
        name: r.name[locale],
        position: i + 1,
      })),
    }),
    generateBreadcrumbSchema([
      { name: 'SuppMatch', url: siteConfig.url },
      {
        name: locale === 'en' ? 'Symptoms' : locale === 'zh-CN' ? '症状' : '症狀',
        url: `${siteConfig.url}/${locale}/`,
      },
      { name, url },
    ]),
  ];

  const labels = {
    back: locale === 'en' ? 'Open recommender' : locale === 'zh-CN' ? '打开推荐工具' : '打開推薦工具',
    intro: locale === 'en' ? 'Overview' : locale === 'zh-CN' ? '概述' : '概述',
    recs: locale === 'en' ? 'Supplements often discussed' : locale === 'zh-CN' ? '常被讨论的补充品' : '常被討論嘅補充品',
    lifestyle: locale === 'en' ? 'Lifestyle first' : locale === 'zh-CN' ? '生活方式优先' : '生活方式優先',
    doctor: locale === 'en' ? 'When to see a doctor' : locale === 'zh-CN' ? '何时就医' : '幾時求醫',
    faq: locale === 'en' ? 'FAQ' : '常見問題',
    products: locale === 'en' ? 'Example products' : locale === 'zh-CN' ? '产品示例' : '產品示例',
    more: locale === 'en' ? 'Browse iHerb category' : locale === 'zh-CN' ? '浏览 iHerb 分类' : '瀏覽 iHerb 分類',
    related: locale === 'en' ? 'Related symptoms' : locale === 'zh-CN' ? '相关症状' : '相關症狀',
    tryApp: locale === 'en' ? 'Get a multi-symptom plan in the app' : locale === 'zh-CN' ? '在工具里做多症状推荐' : '喺工具入面做多症狀推薦',
  };

  const related = symptoms
    .filter((s) => s.category_id === symptom.category_id && s.id !== symptom.id)
    .slice(0, 6);

  return (
    <SiteShell locale={locale} pathSuffix={`/symptom/${symptom.id}/`}>
      <JsonLd data={schemas} />

      <article className="space-y-8">
        <nav className="text-xs text-zinc-500 flex flex-wrap gap-1">
          <Link href="/" className="hover:text-white">
            SuppMatch
          </Link>
          <span>/</span>
          <span className="text-zinc-400">{name}</span>
        </nav>

        <header className="space-y-3">
          <p className="text-sm text-accent-purple font-medium">
            {symptom.iherb_category.name}
          </p>
          <h1 className="text-3xl sm:text-4xl font-bold text-white leading-tight">{name}</h1>
          <p className="text-zinc-400 leading-relaxed">{content.intro[locale]}</p>
          <div className="flex flex-wrap gap-2 pt-2">
            <Link
              href={`/?s=${symptom.id}`}
              className="inline-flex items-center px-4 py-2.5 rounded-xl bg-gradient-to-r from-accent-purple to-accent-blue text-white text-sm font-semibold shadow-lg shadow-purple-500/20"
            >
              {labels.back}
            </Link>
            <a
              href={symptom.iherb_category.url}
              target="_blank"
              rel="noopener noreferrer sponsored"
              className="inline-flex items-center px-4 py-2.5 rounded-xl border border-surface-border text-sm text-zinc-300 hover:text-white hover:border-zinc-500"
            >
              🌿 {labels.more}
            </a>
          </div>
        </header>

        <section className="rounded-3xl border border-surface-border bg-surface-card p-5 sm:p-6 space-y-3">
          <h2 className="text-lg font-bold text-white">{labels.lifestyle}</h2>
          <p className="text-sm text-zinc-400 leading-relaxed">{content.lifestyle[locale]}</p>
        </section>

        <section className="space-y-4">
          <h2 className="text-xl font-bold text-white">{labels.recs}</h2>
          <div className="space-y-4">
            {symptom.recommendations.map((rec) => {
              const products = getProductsForSupplement(rec.name.en);
              const reason = getReasonForSupplement(rec.name.en, locale);
              return (
                <div
                  key={rec.name.en}
                  className="rounded-3xl border border-surface-border bg-surface-card overflow-hidden"
                >
                  <div className="px-5 py-4 border-b border-surface-border space-y-2">
                    <h3 className="text-lg font-bold text-white">💊 {rec.name[locale]}</h3>
                    {reason && <p className="text-sm text-zinc-400">{reason}</p>}
                    <EvidenceBlock nameEn={rec.name.en} locale={locale} />
                  </div>
                  {products.length > 0 && (
                    <div className="p-5">
                      <p className="text-xs text-zinc-500 mb-3">{labels.products}</p>
                      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                        {products.slice(0, 2).map((p) => (
                          <ProductCard key={p.id} product={p} />
                        ))}
                      </div>
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </section>

        <section className="rounded-3xl border border-amber-500/25 bg-amber-500/10 p-5 sm:p-6 space-y-2">
          <h2 className="text-lg font-bold text-amber-100">{labels.doctor}</h2>
          <p className="text-sm text-amber-50/90 leading-relaxed">
            {content.whenToSeeDoctor[locale]}
          </p>
        </section>

        <section className="space-y-4">
          <h2 className="text-xl font-bold text-white">{labels.faq}</h2>
          <div className="space-y-3">
            {content.faqs.map((faq, i) => (
              <details
                key={i}
                className="group rounded-2xl border border-surface-border bg-surface-card open:bg-surface-elevated"
              >
                <summary className="cursor-pointer list-none px-5 py-4 font-medium text-white flex items-center justify-between gap-3">
                  <span>{faq.q[locale]}</span>
                  <span className="text-zinc-500 group-open:rotate-45 transition-transform text-xl leading-none">
                    +
                  </span>
                </summary>
                <div className="px-5 pb-4 text-sm text-zinc-400 leading-relaxed">
                  {faq.a[locale]}
                </div>
              </details>
            ))}
          </div>
        </section>

        {related.length > 0 && (
          <section className="space-y-3">
            <h2 className="text-lg font-bold text-white">{labels.related}</h2>
            <div className="flex flex-wrap gap-2">
              {related.map((s) => (
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
        )}

        <div className="rounded-3xl bg-gradient-to-r from-accent-purple to-accent-blue p-6 text-center text-white">
          <p className="font-semibold mb-3">{labels.tryApp}</p>
          <Link
            href={`/?s=${symptom.id}`}
            className="inline-flex px-5 py-2.5 rounded-xl bg-white text-zinc-900 font-bold text-sm hover:bg-zinc-100"
          >
            {labels.back}
          </Link>
        </div>
      </article>
    </SiteShell>
  );
}
