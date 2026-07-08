'use client';

import { useMemo, useState } from 'react';
import { useLocale } from '@/contexts/LocaleContext';
import { CHAT_EXAMPLES, parseNaturalLanguage } from '@/lib/chatRecommend';
import type { Symptom } from '@/data/symptoms';
import { ArrowRightIcon, SparklesIcon } from '@/components/icons';

interface ChatRecommendProps {
  onComplete: (symptoms: Symptom[]) => void;
  onCancel: () => void;
}

export function ChatRecommend({ onComplete, onCancel }: ChatRecommendProps) {
  const { locale, t } = useLocale();
  const [text, setText] = useState('');
  const [submitted, setSubmitted] = useState(false);

  const result = useMemo(() => parseNaturalLanguage(text), [text]);

  const run = () => setSubmitted(true);

  return (
    <div className="space-y-6">
      <button
        type="button"
        onClick={onCancel}
        className="text-sm text-zinc-500 hover:text-white transition-colors"
      >
        ← {t('mode.backHome')}
      </button>

      <div className="space-y-2">
        <h3 className="text-xl font-bold text-white flex items-center gap-2">
          <SparklesIcon className="w-5 h-5 text-accent-purple" />
          {t('chat.title')}
        </h3>
        <p className="text-sm text-zinc-500">{t('chat.desc')}</p>
      </div>

      <div className="rounded-3xl border border-surface-border bg-surface-elevated p-4 space-y-3">
        <textarea
          value={text}
          onChange={(e) => {
            setText(e.target.value);
            setSubmitted(false);
          }}
          rows={4}
          placeholder={t('chat.placeholder')}
          className="w-full bg-surface border border-surface-border rounded-2xl px-4 py-3 text-white placeholder:text-zinc-600 focus:border-accent-purple focus:outline-none resize-y min-h-[100px]"
        />
        <div className="flex flex-wrap gap-2">
          {CHAT_EXAMPLES.map((ex, i) => (
            <button
              key={i}
              type="button"
              onClick={() => {
                setText(ex[locale]);
                setSubmitted(false);
              }}
              className="text-xs px-3 py-1.5 rounded-full border border-surface-border text-zinc-400 hover:text-white hover:border-zinc-500"
            >
              {ex[locale]}
            </button>
          ))}
        </div>
        <button
          type="button"
          onClick={run}
          disabled={!text.trim()}
          className="w-full py-3.5 rounded-2xl font-bold bg-gradient-to-r from-accent-purple to-accent-blue text-white disabled:opacity-40 flex items-center justify-center gap-2"
        >
          {t('chat.analyze')}
          <ArrowRightIcon />
        </button>
      </div>

      {submitted && (
        <div className="space-y-4">
          {result.symptoms.length === 0 ? (
            <div className="rounded-2xl border border-amber-500/25 bg-amber-500/10 p-4 text-sm text-amber-100">
              {t('chat.noMatch')}
            </div>
          ) : (
            <>
              <p className="text-sm text-zinc-400">{t('chat.matched', { count: String(result.symptoms.length) })}</p>
              <ul className="space-y-2">
                {result.matches.map((m) => (
                  <li
                    key={m.symptom.id}
                    className="flex items-center justify-between gap-3 px-4 py-3 rounded-xl border border-surface-border bg-surface-card"
                  >
                    <span className="font-medium text-white">{m.symptom.names[locale]}</span>
                    <span className="text-xs text-zinc-500 truncate max-w-[40%]">
                      {m.matchedKeys.slice(0, 3).join(' · ')}
                    </span>
                  </li>
                ))}
              </ul>
              <p className="text-xs text-zinc-500">{t('chat.disclaimer')}</p>
              <button
                type="button"
                onClick={() => onComplete(result.symptoms)}
                className="w-full py-4 rounded-2xl font-bold text-lg bg-white text-zinc-900 hover:bg-zinc-100 flex items-center justify-center gap-2"
              >
                <SparklesIcon className="w-5 h-5" />
                {t('chat.toRecs', { count: String(result.symptoms.length) })}
              </button>
            </>
          )}
        </div>
      )}
    </div>
  );
}
