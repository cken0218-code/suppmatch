'use client';

import { useLocale, type Locale } from '@/contexts/LocaleContext';
import { HeartIcon, SparklesIcon } from '@/components/icons';

function LanguageSelector() {
  const { locale, setLocale } = useLocale();

  const flags: Record<Locale, string> = {
    'zh-HK': '🇭🇰',
    'zh-CN': '🇨🇳',
    en: '🇺🇸',
  };

  return (
    <div className="flex gap-1" role="group" aria-label="Language">
      {(['zh-HK', 'zh-CN', 'en'] as Locale[]).map((l) => (
        <button
          key={l}
          type="button"
          onClick={() => setLocale(l)}
          className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
            locale === l
              ? 'bg-gradient-to-r from-accent-purple to-accent-blue text-white shadow-lg shadow-purple-500/25'
              : 'bg-surface-card text-zinc-400 hover:text-white hover:bg-surface-elevated border border-surface-border'
          }`}
        >
          {flags[l]}
        </button>
      ))}
    </div>
  );
}

interface HeaderProps {
  onOpenFavorites?: () => void;
  favoritesCount?: number;
}

export function Header({ onOpenFavorites, favoritesCount = 0 }: HeaderProps) {
  const { t } = useLocale();

  return (
    <header className="sticky top-0 z-50 bg-surface/90 backdrop-blur-xl border-b border-surface-border">
      <div className="max-w-4xl mx-auto px-4 py-4 flex justify-between items-center gap-3">
        <div className="flex items-center gap-3 min-w-0">
          <div className="shrink-0 w-10 h-10 bg-gradient-to-br from-accent-purple to-accent-blue rounded-2xl flex items-center justify-center text-white shadow-lg shadow-purple-500/30">
            <SparklesIcon className="w-5 h-5" />
          </div>
          <div className="min-w-0">
            <h1 className="text-xl font-bold bg-gradient-to-r from-white to-zinc-400 bg-clip-text text-transparent truncate">
              {t('app.title')}
            </h1>
            <p className="text-xs text-zinc-500 truncate">{t('app.tagline')}</p>
          </div>
        </div>
        <div className="flex items-center gap-2 shrink-0">
          {onOpenFavorites && (
            <button
              type="button"
              onClick={onOpenFavorites}
              className="relative p-2 rounded-xl border border-surface-border text-zinc-400 hover:text-pink-300 hover:border-pink-400/40 transition-colors"
              aria-label={t('favorites.open')}
              title={t('favorites.open')}
            >
              <HeartIcon className="w-5 h-5" filled={favoritesCount > 0} />
              {favoritesCount > 0 && (
                <span className="absolute -top-1 -right-1 min-w-[1.1rem] h-[1.1rem] px-1 rounded-full bg-pink-500 text-[10px] font-bold text-white flex items-center justify-center">
                  {favoritesCount > 9 ? '9+' : favoritesCount}
                </span>
              )}
            </button>
          )}
          <LanguageSelector />
        </div>
      </div>
    </header>
  );
}
