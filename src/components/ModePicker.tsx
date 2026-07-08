'use client';

import Link from 'next/link';
import { useLocale } from '@/contexts/LocaleContext';
import { ArrowRightIcon, SparklesIcon } from '@/components/icons';
import type { AppLocale } from '@/lib/i18n-routing';

export type EntryMode = 'quick' | 'guided' | 'chat';

interface ModePickerProps {
  onSelect: (mode: EntryMode) => void;
  onOpenFavorites: () => void;
  onOpenPriceWatch: () => void;
  onOpenContent: () => void;
  favoritesCount: number;
}

export function ModePicker({
  onSelect,
  onOpenFavorites,
  onOpenPriceWatch,
  onOpenContent,
  favoritesCount,
}: ModePickerProps) {
  const { locale, t } = useLocale();

  return (
    <div className="space-y-5">
      <div className="text-center space-y-2">
        <p className="text-sm text-zinc-500">{t('mode.intro')}</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <button
          type="button"
          onClick={() => onSelect('quick')}
          className="group text-left p-5 rounded-3xl border border-surface-border bg-surface-elevated hover:border-accent-purple/60 hover:bg-accent-purple/5 transition-all"
        >
          <div className="w-11 h-11 rounded-2xl bg-accent-purple/20 text-accent-purple flex items-center justify-center mb-4">
            ⚡
          </div>
          <h3 className="text-lg font-bold text-white mb-1">{t('mode.quick.title')}</h3>
          <p className="text-sm text-zinc-400 leading-relaxed mb-4">{t('mode.quick.desc')}</p>
          <span className="inline-flex items-center gap-1 text-sm font-medium text-accent-purple group-hover:gap-2 transition-all">
            {t('mode.quick.cta')} <ArrowRightIcon className="w-4 h-4" />
          </span>
        </button>

        <button
          type="button"
          onClick={() => onSelect('guided')}
          className="group text-left p-5 rounded-3xl border border-surface-border bg-gradient-to-br from-accent-purple/15 to-accent-blue/10 hover:border-accent-purple/60 transition-all"
        >
          <div className="w-11 h-11 rounded-2xl bg-gradient-to-br from-accent-purple to-accent-blue text-white flex items-center justify-center mb-4 shadow-lg shadow-purple-500/20">
            <SparklesIcon className="w-5 h-5" />
          </div>
          <h3 className="text-lg font-bold text-white mb-1">{t('mode.guided.title')}</h3>
          <p className="text-sm text-zinc-400 leading-relaxed mb-4">{t('mode.guided.desc')}</p>
          <span className="inline-flex items-center gap-1 text-sm font-medium text-white group-hover:gap-2 transition-all">
            {t('mode.guided.cta')} <ArrowRightIcon className="w-4 h-4" />
          </span>
        </button>

        <button
          type="button"
          onClick={() => onSelect('chat')}
          className="group text-left p-5 rounded-3xl border border-surface-border bg-surface-elevated hover:border-accent-blue/60 sm:col-span-2 transition-all"
        >
          <div className="w-11 h-11 rounded-2xl bg-accent-blue/20 text-sky-300 flex items-center justify-center mb-4">
            💬
          </div>
          <h3 className="text-lg font-bold text-white mb-1">{t('mode.chat.title')}</h3>
          <p className="text-sm text-zinc-400 leading-relaxed mb-4">{t('mode.chat.desc')}</p>
          <span className="inline-flex items-center gap-1 text-sm font-medium text-sky-300 group-hover:gap-2 transition-all">
            {t('mode.chat.cta')} <ArrowRightIcon className="w-4 h-4" />
          </span>
        </button>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <button
          type="button"
          onClick={onOpenFavorites}
          className="w-full flex items-center justify-between px-4 py-3 rounded-2xl border border-surface-border bg-surface-elevated text-zinc-300 hover:text-white hover:border-zinc-500 transition-colors"
        >
          <span className="inline-flex items-center gap-2 text-sm font-medium">
            ⭐ {t('favorites.open')}
          </span>
          <span className="text-xs tabular-nums text-zinc-500">
            {favoritesCount > 0
              ? t('favorites.count', { count: String(favoritesCount) })
              : t('favorites.emptyShort')}
          </span>
        </button>

        <button
          type="button"
          onClick={onOpenPriceWatch}
          className="w-full flex items-center justify-between px-4 py-3 rounded-2xl border border-surface-border bg-surface-elevated text-zinc-300 hover:text-white hover:border-zinc-500 transition-colors"
        >
          <span className="inline-flex items-center gap-2 text-sm font-medium">
            💰 {t('price.open')}
          </span>
          <span className="text-xs text-zinc-500">{t('price.hint')}</span>
        </button>

        <Link
          href={`/${locale as AppLocale}/`}
          className="w-full flex items-center justify-between px-4 py-3 rounded-2xl border border-surface-border bg-surface-elevated text-zinc-300 hover:text-white hover:border-zinc-500 transition-colors"
        >
          <span className="inline-flex items-center gap-2 text-sm font-medium">
            📚 {t('guides.open')}
          </span>
          <span className="text-xs text-zinc-500">{t('guides.hint')}</span>
        </Link>

        <button
          type="button"
          onClick={onOpenContent}
          className="w-full flex items-center justify-between px-4 py-3 rounded-2xl border border-surface-border bg-surface-elevated text-zinc-300 hover:text-white hover:border-zinc-500 transition-colors"
        >
          <span className="inline-flex items-center gap-2 text-sm font-medium">
            📣 {t('content.open')}
          </span>
          <span className="text-xs text-zinc-500">{t('content.hint')}</span>
        </button>
      </div>
    </div>
  );
}
