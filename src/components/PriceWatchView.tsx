'use client';

import { useEffect, useState } from 'react';
import { useLocale } from '@/contexts/LocaleContext';
import {
  buildPriceAlertMailto,
  buildTelegramShareUrl,
  getWatchlist,
  removeFromWatchlist,
  updateWatchNote,
  type WatchedProduct,
} from '@/data/priceWatch';
import { ChevronLeftIcon } from '@/components/icons';

interface PriceWatchViewProps {
  onBack: () => void;
}

export function PriceWatchView({ onBack }: PriceWatchViewProps) {
  const { locale, t } = useLocale();
  const [items, setItems] = useState<WatchedProduct[]>([]);

  const refresh = () => setItems(getWatchlist());
  useEffect(() => {
    refresh();
  }, []);

  const shareText =
    locale === 'en'
      ? `My SuppMatch price watch (${items.length} items)`
      : locale === 'zh-CN'
        ? `我的 SuppMatch 价格关注（${items.length} 项）`
        : `我嘅 SuppMatch 價格關注（${items.length} 項）`;

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between gap-3">
        <button
          type="button"
          onClick={onBack}
          className="inline-flex items-center gap-2 text-accent-purple hover:text-white font-medium"
        >
          <ChevronLeftIcon />
          {t('price.back')}
        </button>
      </div>

      <div>
        <h2 className="text-xl font-bold text-white mb-1">💰 {t('price.title')}</h2>
        <p className="text-sm text-zinc-500">{t('price.subtitle')}</p>
      </div>

      {items.length === 0 ? (
        <p className="text-center text-zinc-500 py-10 text-sm">{t('price.empty')}</p>
      ) : (
        <>
          <div className="flex flex-wrap gap-2">
            <a
              href={buildPriceAlertMailto(items, locale)}
              className="px-3 py-2 rounded-xl border border-surface-border text-sm text-zinc-300 hover:text-white"
            >
              ✉️ {t('price.email')}
            </a>
            <a
              href={buildTelegramShareUrl(`${shareText}\n${items.map((i) => i.iherbUrl).join('\n')}`)}
              target="_blank"
              rel="noopener noreferrer"
              className="px-3 py-2 rounded-xl border border-surface-border text-sm text-zinc-300 hover:text-white"
            >
              ✈️ {t('price.telegram')}
            </a>
          </div>

          <ul className="space-y-4">
            {items.map((item) => (
              <li
                key={item.id}
                className="rounded-2xl border border-surface-border bg-surface-elevated p-4 space-y-3"
              >
                <div className="flex justify-between gap-3">
                  <div>
                    <h3 className="font-semibold text-white">{item.nameZh || item.name}</h3>
                    <p className="text-xs text-zinc-500 mt-0.5">
                      {item.brand} · {item.priceRange}
                    </p>
                  </div>
                  <button
                    type="button"
                    onClick={() => {
                      removeFromWatchlist(item.id);
                      refresh();
                    }}
                    className="text-xs text-zinc-500 hover:text-red-400 shrink-0"
                  >
                    {t('price.remove')}
                  </button>
                </div>
                <input
                  type="text"
                  value={item.targetPrice || ''}
                  onChange={(e) => {
                    updateWatchNote(item.id, item.note || '', e.target.value);
                    refresh();
                  }}
                  placeholder={t('price.targetPlaceholder')}
                  className="w-full bg-surface border border-surface-border rounded-xl px-3 py-2 text-sm text-white placeholder:text-zinc-600 focus:border-accent-purple focus:outline-none"
                />
                <div className="grid grid-cols-2 gap-2">
                  <a
                    href={item.iherbUrl}
                    target="_blank"
                    rel="noopener noreferrer sponsored"
                    className="text-center py-2 rounded-xl bg-emerald-600 text-white text-sm font-medium"
                  >
                    iHerb
                  </a>
                  <a
                    href={item.amazonUrl}
                    target="_blank"
                    rel="noopener noreferrer sponsored"
                    className="text-center py-2 rounded-xl bg-zinc-700 text-white text-sm font-medium"
                  >
                    Amazon
                  </a>
                </div>
              </li>
            ))}
          </ul>
        </>
      )}
    </div>
  );
}
