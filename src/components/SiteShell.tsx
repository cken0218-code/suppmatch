import Link from 'next/link';
import type { AppLocale } from '@/lib/i18n-routing';
import { LOCALES } from '@/lib/i18n-routing';

const labels: Record<AppLocale, { tagline: string; home: string; disclaimer: string }> = {
  'zh-HK': {
    tagline: '症狀資訊 → 補充品參考',
    home: '返回工具',
    disclaimer: '本頁資訊僅供參考，不構成醫療建議。',
  },
  'zh-CN': {
    tagline: '症状信息 → 补充品参考',
    home: '返回工具',
    disclaimer: '本页信息仅供参考，不构成医疗建议。',
  },
  en: {
    tagline: 'Symptom info → supplement reference',
    home: 'Open app',
    disclaimer: 'For reference only — not medical advice.',
  },
};

export function SiteShell({
  locale,
  children,
  pathSuffix = '',
}: {
  locale: AppLocale;
  children: React.ReactNode;
  /** e.g. /symptom/insomnia/ for language switcher */
  pathSuffix?: string;
}) {
  const t = labels[locale];

  return (
    <div className="min-h-screen bg-surface text-zinc-200 flex flex-col">
      <header className="sticky top-0 z-50 bg-surface/90 backdrop-blur-xl border-b border-surface-border">
        <div className="max-w-3xl mx-auto px-4 py-4 flex justify-between items-center gap-3">
          <Link href="/" className="flex items-center gap-3 min-w-0 group">
            <div className="shrink-0 w-10 h-10 bg-gradient-to-br from-accent-purple to-accent-blue rounded-2xl flex items-center justify-center text-white text-sm font-bold shadow-lg shadow-purple-500/30">
              S
            </div>
            <div className="min-w-0">
              <div className="text-xl font-bold text-white group-hover:text-zinc-200">SuppMatch</div>
              <p className="text-xs text-zinc-500 truncate">{t.tagline}</p>
            </div>
          </Link>
          <div className="flex items-center gap-2 shrink-0">
            <div className="flex gap-1">
              {LOCALES.map((l) => (
                <Link
                  key={l}
                  href={`/${l}${pathSuffix}`}
                  className={`px-2.5 py-1 rounded-lg text-xs font-medium border transition-colors ${
                    l === locale
                      ? 'bg-accent-purple/20 border-accent-purple text-white'
                      : 'border-surface-border text-zinc-500 hover:text-white'
                  }`}
                >
                  {l === 'zh-HK' ? '繁' : l === 'zh-CN' ? '简' : 'EN'}
                </Link>
              ))}
            </div>
            <Link
              href="/"
              className="hidden sm:inline-flex text-xs px-3 py-1.5 rounded-lg bg-white text-zinc-900 font-semibold hover:bg-zinc-100"
            >
              {t.home}
            </Link>
          </div>
        </div>
      </header>

      <main className="flex-1 max-w-3xl w-full mx-auto px-4 py-8">{children}</main>

      <footer className="text-center py-8 text-zinc-500 text-sm border-t border-surface-border">
        <p>© 2026 SuppMatch. {t.disclaimer}</p>
      </footer>
    </div>
  );
}
