'use client';

import { useEffect, useState } from 'react';
import { useLocale } from '@/contexts/LocaleContext';
import { symptoms } from '@/data/symptoms';
import { getPopularSymptoms } from '@/lib/storage';
import { TrendUpIcon } from '@/components/icons';

interface PopularSymptomsProps {
  onSelect: (id: string) => void;
}

export function PopularSymptoms({ onSelect }: PopularSymptomsProps) {
  const { locale, t } = useLocale();
  const [popular, setPopular] = useState<{ id: string; count: number }[]>([]);

  useEffect(() => {
    const pop = getPopularSymptoms();
    const sorted = Object.entries(pop)
      .map(([id, count]) => ({ id, count }))
      .sort((a, b) => b.count - a.count)
      .slice(0, 6);
    setPopular(sorted);
  }, []);

  if (popular.length === 0) return null;

  return (
    <section>
      <div className="flex items-center gap-2 mb-3">
        <TrendUpIcon className="text-zinc-500" />
        <span className="text-sm font-medium text-zinc-400">{t('popular.title')}</span>
      </div>
      <div className="flex flex-wrap gap-2">
        {popular.map((item) => {
          const symptom = symptoms.find((s) => s.id === item.id);
          if (!symptom) return null;
          return (
            <button
              key={item.id}
              type="button"
              onClick={() => onSelect(item.id)}
              className="px-4 py-2 bg-surface-card border border-surface-border rounded-full text-sm font-medium text-zinc-300 hover:border-accent-purple hover:text-white transition-all"
            >
              {symptom.names[locale]}
            </button>
          );
        })}
      </div>
    </section>
  );
}