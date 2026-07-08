import type { AppLocale } from '@/lib/i18n-routing';
import {
  evidenceLevelLabels,
  getEvidence,
  type EvidenceLevel,
} from '@/data/evidence';
import { getWarnings } from '@/data/contraindications';

const levelStyles: Record<EvidenceLevel, string> = {
  strong: 'bg-emerald-500/15 text-emerald-300 border-emerald-500/30',
  moderate: 'bg-sky-500/15 text-sky-300 border-sky-500/30',
  limited: 'bg-amber-500/15 text-amber-200 border-amber-500/30',
  traditional: 'bg-violet-500/15 text-violet-200 border-violet-500/30',
};

interface EvidenceBlockProps {
  nameEn: string;
  locale: AppLocale;
  compact?: boolean;
}

export function EvidenceBlock({ nameEn, locale, compact = false }: EvidenceBlockProps) {
  const evidence = getEvidence(nameEn);
  const warnings = getWarnings(nameEn);

  if (!evidence && warnings.length === 0) return null;

  return (
    <div className={compact ? 'space-y-2' : 'space-y-3'}>
      {evidence && (
        <div className="space-y-1.5">
          <div className="flex flex-wrap items-center gap-2">
            <span
              className={`text-xs px-2 py-0.5 rounded-full border font-medium ${levelStyles[evidence.level]}`}
            >
              {evidenceLevelLabels[evidence.level][locale]}
            </span>
            {!compact && (
              <span className="text-xs text-zinc-500">{evidence.uses[locale]}</span>
            )}
          </div>
          {!compact && (
            <>
              <p className="text-sm text-zinc-400 leading-relaxed">{evidence.summary[locale]}</p>
              {evidence.sources.length > 0 && (
                <div className="flex flex-wrap gap-2 pt-1">
                  {evidence.sources.map((s) => (
                    <a
                      key={s.url}
                      href={s.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-xs text-accent-purple hover:text-white underline-offset-2 hover:underline"
                    >
                      {s.label} ↗
                    </a>
                  ))}
                </div>
              )}
            </>
          )}
        </div>
      )}

      {warnings.length > 0 && (
        <ul className="space-y-1.5">
          {warnings.map((w, i) => (
            <li
              key={`${w.tag}-${i}`}
              className={`text-xs leading-relaxed rounded-lg px-2.5 py-2 border ${
                w.severity === 'avoid_unless_advised'
                  ? 'bg-red-500/10 border-red-500/25 text-red-200/90'
                  : 'bg-amber-500/10 border-amber-500/25 text-amber-100/90'
              }`}
            >
              <span className="font-semibold mr-1">
                {w.severity === 'avoid_unless_advised' ? '⛔' : '⚠️'}
              </span>
              {w.text[locale]}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
