'use client';

import { useEffect, useState } from 'react';
import type { Product } from '@/data/supplementProducts';
import { addToWatchlist, isWatched, removeFromWatchlist } from '@/data/priceWatch';

interface ProductCardProps {
  product: Product;
  /** Enable price watch button (client app only) */
  enableWatch?: boolean;
  watchLabel?: string;
  watchingLabel?: string;
}

export function ProductCard({
  product,
  enableWatch = false,
  watchLabel = 'Watch price',
  watchingLabel = 'Watching',
}: ProductCardProps) {
  const [watching, setWatching] = useState(false);

  useEffect(() => {
    if (enableWatch) setWatching(isWatched(product.id));
  }, [enableWatch, product.id]);

  const toggleWatch = () => {
    if (watching) {
      removeFromWatchlist(product.id);
      setWatching(false);
    } else {
      addToWatchlist({
        id: product.id,
        name: product.name,
        nameZh: product.nameZh,
        brand: product.brand,
        priceRange: product.priceRange,
        iherbUrl: product.iherbUrl,
        amazonUrl: product.amazonUrl,
      });
      setWatching(true);
    }
  };

  return (
    <div className="bg-surface-elevated rounded-2xl border border-surface-border overflow-hidden hover:border-zinc-500 transition-colors">
      <div className="p-4">
        <div className="flex justify-between items-start gap-3 mb-4">
          <div className="min-w-0">
            <h4 className="font-semibold text-white leading-snug">{product.nameZh}</h4>
            <p className="text-xs text-zinc-500 mt-1">{product.brand}</p>
          </div>
          <span className="shrink-0 text-base font-bold text-emerald-400">{product.priceRange}</span>
        </div>

        <div className="grid grid-cols-2 gap-2">
          <a
            href={product.iherbUrl}
            target="_blank"
            rel="noopener noreferrer sponsored"
            className="flex items-center justify-center gap-1.5 py-2.5 bg-emerald-600 text-white rounded-xl font-medium hover:bg-emerald-500 transition-colors text-sm"
          >
            <span aria-hidden="true">🌿</span> iHerb
          </a>
          <a
            href={product.amazonUrl}
            target="_blank"
            rel="noopener noreferrer sponsored"
            className="flex items-center justify-center gap-1.5 py-2.5 bg-zinc-700 text-white rounded-xl font-medium hover:bg-zinc-600 transition-colors text-sm"
          >
            <span aria-hidden="true">📦</span> Amazon
          </a>
        </div>

        {enableWatch && (
          <button
            type="button"
            onClick={toggleWatch}
            className={`mt-2 w-full py-2 rounded-xl text-xs font-medium border transition-colors ${
              watching
                ? 'border-amber-400/40 text-amber-200 bg-amber-400/10'
                : 'border-surface-border text-zinc-400 hover:text-white'
            }`}
          >
            {watching ? `✓ ${watchingLabel}` : `💰 ${watchLabel}`}
          </button>
        )}
      </div>
    </div>
  );
}
