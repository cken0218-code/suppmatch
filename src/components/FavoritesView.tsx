'use client';

import { useEffect, useState } from 'react';
import { useLocale } from '@/contexts/LocaleContext';
import {
  clearFavorites,
  getFavorites,
  removeFavorite,
  type FavoriteItem,
} from '@/data/favorites';
import { getProductsForSupplement } from '@/data/supplementProducts';
import { getReasonForSupplement } from '@/data/supplementReasons';
import { ProductCard } from '@/components/ProductCard';
import { ChevronLeftIcon } from '@/components/icons';

interface FavoritesViewProps {
  onBack: () => void;
}

export function FavoritesView({ onBack }: FavoritesViewProps) {
  const { locale, t } = useLocale();
  const [items, setItems] = useState<FavoriteItem[]>([]);

  const refresh = () => setItems(getFavorites());

  useEffect(() => {
    refresh();
  }, []);

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between gap-3">
        <button
          type="button"
          onClick={onBack}
          className="inline-flex items-center gap-2 text-accent-purple hover:text-white font-medium transition-colors"
        >
          <ChevronLeftIcon />
          {t('favorites.back')}
        </button>
        {items.length > 0 && (
          <button
            type="button"
            onClick={() => {
              clearFavorites();
              refresh();
            }}
            className="text-xs text-zinc-500 hover:text-red-400 transition-colors"
          >
            {t('favorites.clear')}
          </button>
        )}
      </div>

      <div>
        <h2 className="text-xl font-bold text-white mb-1">⭐ {t('favorites.title')}</h2>
        <p className="text-sm text-zinc-500">{t('favorites.subtitle')}</p>
      </div>

      {items.length === 0 ? (
        <div className="text-center py-12 text-zinc-500 text-sm">{t('favorites.empty')}</div>
      ) : (
        <div className="space-y-5">
          {items.map((item) => {
            const products = getProductsForSupplement(item.name.en);
            const reason = getReasonForSupplement(item.name.en, locale);
            return (
              <section
                key={item.supplementKey}
                className="bg-surface-elevated border border-surface-border rounded-3xl overflow-hidden"
              >
                <div className="px-5 py-4 border-b border-surface-border flex items-start justify-between gap-3">
                  <div>
                    <h3 className="font-bold text-white">{item.name[locale] || item.name.en}</h3>
                    {reason && <p className="text-sm text-zinc-400 mt-1">{reason}</p>}
                  </div>
                  <button
                    type="button"
                    onClick={() => {
                      removeFavorite(item.supplementKey);
                      refresh();
                    }}
                    className="shrink-0 text-xs text-zinc-500 hover:text-red-400 transition-colors px-2 py-1"
                  >
                    {t('favorites.remove')}
                  </button>
                </div>
                <div className="p-5">
                  {products.length > 0 ? (
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      {products.map((p) => (
                        <ProductCard key={p.id} product={p} />
                      ))}
                    </div>
                  ) : (
                    <p className="text-sm text-zinc-500 text-center py-4">
                      {t('recommendation.noProducts')}
                    </p>
                  )}
                </div>
              </section>
            );
          })}
        </div>
      )}
    </div>
  );
}
