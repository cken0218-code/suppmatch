'use client';

import { useLocale } from '@/contexts/LocaleContext';
import { findInteractions } from '@/data/interactions';

interface InteractionAlertsProps {
  supplementNamesEn: string[];
}

export function InteractionAlerts({ supplementNamesEn }: InteractionAlertsProps) {
  const { locale, t } = useLocale();
  const items = findInteractions(supplementNamesEn);
  if (items.length === 0) return null;

  return (
    <div className="rounded-3xl border border-orange-500/30 bg-orange-500/10 p-5 space-y-3">
      <h3 className="font-bold text-orange-100 flex items-center gap-2">
        <span aria-hidden="true">⚗️</span>
        {t('interactions.title')}
      </h3>
      <p className="text-sm text-orange-100/80">{t('interactions.desc')}</p>
      <ul className="space-y-3">
        {items.map((item, i) => (
          <li
            key={i}
            className={`rounded-xl border px-3 py-2.5 text-sm ${
              item.severity === 'important'
                ? 'border-red-500/40 bg-red-500/10'
                : item.severity === 'caution'
                  ? 'border-orange-400/40 bg-orange-500/10'
                  : 'border-zinc-600/50 bg-surface/40'
            }`}
          >
            <p className="font-medium text-white">{item.message[locale]}</p>
            <p className="text-xs text-zinc-400 mt-1">{item.tip[locale]}</p>
          </li>
        ))}
      </ul>
      <p className="text-xs text-zinc-500">{t('interactions.footer')}</p>
    </div>
  );
}
