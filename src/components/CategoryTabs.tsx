'use client';

import { useLocale } from '@/contexts/LocaleContext';
import { ALL_CATEGORY_ID, CATEGORIES } from '@/data/categories';

interface CategoryTabsProps {
  activeId: string;
  onChange: (categoryId: string) => void;
  counts?: Record<string, number>;
}

export function CategoryTabs({ activeId, onChange, counts }: CategoryTabsProps) {
  const { locale, t } = useLocale();

  const tabs = [
    { id: ALL_CATEGORY_ID, label: t('category.all'), emoji: '📋' },
    ...CATEGORIES.map((c) => ({
      id: c.id,
      label: c.names[locale],
      emoji: c.emoji,
    })),
  ];

  return (
    <div className="-mx-1">
      <div
        className="flex gap-2 overflow-x-auto pb-2 px-1 scrollbar-thin"
        role="tablist"
        aria-label={t('category.label')}
      >
        {tabs.map((tab) => {
          const isActive = activeId === tab.id;
          const count = counts?.[tab.id];
          return (
            <button
              key={tab.id}
              type="button"
              role="tab"
              aria-selected={isActive}
              onClick={() => onChange(tab.id)}
              className={`shrink-0 inline-flex items-center gap-1.5 px-3.5 py-2 rounded-full text-sm font-medium border transition-all ${
                isActive
                  ? 'bg-accent-purple/20 border-accent-purple text-white shadow-sm shadow-purple-500/20'
                  : 'bg-surface-elevated border-surface-border text-zinc-400 hover:text-white hover:border-zinc-500'
              }`}
            >
              <span aria-hidden="true">{tab.emoji}</span>
              <span>{tab.label}</span>
              {typeof count === 'number' && count > 0 && (
                <span
                  className={`text-xs tabular-nums ${
                    isActive ? 'text-purple-200' : 'text-zinc-600'
                  }`}
                >
                  {count}
                </span>
              )}
            </button>
          );
        })}
      </div>
    </div>
  );
}
