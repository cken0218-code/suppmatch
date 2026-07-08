'use client';

import Link from 'next/link';
import { useLocale } from '@/contexts/LocaleContext';
import { CheckIcon } from '@/components/icons';
import type { Symptom } from '@/data/symptoms';
import { symptomPath, type AppLocale } from '@/lib/i18n-routing';

interface SymptomCardProps {
  symptom: Symptom;
  isSelected: boolean;
  onClick: () => void;
}

export function SymptomCard({ symptom, isSelected, onClick }: SymptomCardProps) {
  const { locale, t } = useLocale();
  const preview = symptom.recommendations
    .slice(0, 2)
    .map((r) => r.name[locale])
    .join('、');

  return (
    <div
      className={`rounded-2xl border transition-all duration-200 ${
        isSelected
          ? 'border-accent-purple bg-accent-purple/10 shadow-lg shadow-purple-500/10'
          : 'border-surface-border bg-surface-card hover:border-zinc-500 hover:bg-surface-elevated'
      }`}
    >
      <button type="button" onClick={onClick} className="w-full text-left p-4">
        <div className="flex items-start gap-3">
          <div className="flex-1 min-w-0">
            <h3 className="font-semibold text-white leading-snug">{symptom.names[locale]}</h3>
            <p className="text-xs text-zinc-500 mt-1.5 line-clamp-2">
              {preview}
              {symptom.recommendations.length > 2 && '...'}
            </p>
          </div>
          <div
            className={`shrink-0 w-6 h-6 rounded-full border-2 flex items-center justify-center transition-all ${
              isSelected ? 'border-accent-purple bg-accent-purple' : 'border-zinc-600'
            }`}
          >
            {isSelected && <CheckIcon className="w-3.5 h-3.5 text-white" />}
          </div>
        </div>
      </button>
      <div className="px-4 pb-3 -mt-1">
        <Link
          href={symptomPath(locale as AppLocale, symptom.id)}
          className="text-xs text-accent-purple hover:text-white transition-colors"
          onClick={(e) => e.stopPropagation()}
        >
          {t('symptom.guide')} →
        </Link>
      </div>
    </div>
  );
}
