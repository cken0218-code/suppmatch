'use client';

import { useEffect, useState } from 'react';
import { useLocale } from '@/contexts/LocaleContext';
import { addFeedback, getFeedbackFor, type FeedbackEntry } from '@/data/feedback';

interface FeedbackPanelProps {
  /** Unique key e.g. combo of symptom ids or supplement en */
  feedbackKey: string;
  label: string;
}

export function FeedbackPanel({ feedbackKey, label }: FeedbackPanelProps) {
  const { t } = useLocale();
  const key = feedbackKey.toLowerCase();
  const [saved, setSaved] = useState<FeedbackEntry | undefined>();
  const [comment, setComment] = useState('');

  useEffect(() => {
    setSaved(getFeedbackFor(key));
  }, [key]);

  const submit = (rating: 1 | 2 | 3) => {
    addFeedback({ key, label, rating, comment: comment.trim() || undefined });
    setSaved(getFeedbackFor(key));
  };

  return (
    <div className="rounded-2xl border border-surface-border bg-surface-elevated p-4 space-y-3">
      <div>
        <h4 className="text-sm font-semibold text-white">{t('feedback.title')}</h4>
        <p className="text-xs text-zinc-500 mt-1">{t('feedback.desc')}</p>
      </div>

      {saved ? (
        <p className="text-sm text-emerald-300">{t('feedback.thanks')}</p>
      ) : (
        <>
          <div className="flex flex-wrap gap-2">
            <button
              type="button"
              onClick={() => submit(3)}
              className="px-3 py-2 rounded-xl text-sm border border-emerald-500/40 text-emerald-200 hover:bg-emerald-500/10"
            >
              👍 {t('feedback.helpful')}
            </button>
            <button
              type="button"
              onClick={() => submit(2)}
              className="px-3 py-2 rounded-xl text-sm border border-surface-border text-zinc-300 hover:bg-surface-card"
            >
              😐 {t('feedback.ok')}
            </button>
            <button
              type="button"
              onClick={() => submit(1)}
              className="px-3 py-2 rounded-xl text-sm border border-surface-border text-zinc-400 hover:bg-surface-card"
            >
              👎 {t('feedback.not')}
            </button>
          </div>
          <input
            type="text"
            value={comment}
            onChange={(e) => setComment(e.target.value)}
            placeholder={t('feedback.commentPlaceholder')}
            maxLength={200}
            className="w-full bg-surface border border-surface-border rounded-xl px-3 py-2 text-sm text-white placeholder:text-zinc-600 focus:border-accent-purple focus:outline-none"
          />
        </>
      )}
    </div>
  );
}
