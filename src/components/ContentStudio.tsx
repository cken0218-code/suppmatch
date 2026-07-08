'use client';

import { useMemo, useState } from 'react';
import { useLocale } from '@/contexts/LocaleContext';
import {
  channelLabels,
  contentLandingUrl,
  getContentMatrix,
  type ContentChannel,
  type ContentIdea,
} from '@/data/contentMatrix';
import type { AppLocale } from '@/lib/i18n-routing';
import { copyText } from '@/lib/share';
import { ChevronLeftIcon, ClipboardIcon } from '@/components/icons';

interface ContentStudioProps {
  onBack: () => void;
}

const CHANNELS: ContentChannel[] = ['xiaohongshu', 'youtube', 'threads', 'ig'];

export function ContentStudio({ onBack }: ContentStudioProps) {
  const { locale, t } = useLocale();
  const [channel, setChannel] = useState<ContentChannel>('xiaohongshu');
  const [msg, setMsg] = useState<string | null>(null);

  const ideas = useMemo(
    () => getContentMatrix().filter((i) => i.channel === channel),
    [channel],
  );

  const copyIdea = async (idea: ContentIdea) => {
    const url = contentLandingUrl(locale as AppLocale, idea.symptomId);
    const full = `${idea.title[locale]}\n\n${idea.caption[locale]}\n${url}\n\n${idea.cta[locale]}`;
    const ok = await copyText(full);
    setMsg(ok ? t('content.copied') : t('share.failed'));
    setTimeout(() => setMsg(null), 2000);
  };

  return (
    <div className="space-y-6">
      <button
        type="button"
        onClick={onBack}
        className="inline-flex items-center gap-2 text-accent-purple hover:text-white font-medium"
      >
        <ChevronLeftIcon />
        {t('content.back')}
      </button>

      <div>
        <h2 className="text-xl font-bold text-white mb-1">📣 {t('content.title')}</h2>
        <p className="text-sm text-zinc-500">{t('content.subtitle')}</p>
      </div>

      <div className="flex flex-wrap gap-2">
        {CHANNELS.map((ch) => (
          <button
            key={ch}
            type="button"
            onClick={() => setChannel(ch)}
            className={`px-3 py-1.5 rounded-full text-sm border transition-colors ${
              channel === ch
                ? 'border-accent-purple bg-accent-purple/20 text-white'
                : 'border-surface-border text-zinc-400 hover:text-white'
            }`}
          >
            {channelLabels[ch][locale]}
          </button>
        ))}
      </div>

      {msg && (
        <p className="text-center text-sm text-emerald-300 bg-emerald-500/10 border border-emerald-500/20 rounded-xl py-2">
          {msg}
        </p>
      )}

      <ul className="space-y-4">
        {ideas.map((idea) => (
          <li
            key={idea.id}
            className="rounded-2xl border border-surface-border bg-surface-elevated p-4 space-y-3"
          >
            <h3 className="font-semibold text-white">{idea.title[locale]}</h3>
            <p className="text-xs text-zinc-500">{idea.hooks[0]?.[locale]}</p>
            <pre className="text-xs text-zinc-400 whitespace-pre-wrap font-sans bg-surface rounded-xl p-3 border border-surface-border max-h-40 overflow-y-auto">
              {idea.caption[locale]}
              {'\n'}
              {contentLandingUrl(locale as AppLocale, idea.symptomId)}
            </pre>
            <button
              type="button"
              onClick={() => copyIdea(idea)}
              className="inline-flex items-center gap-1.5 px-3 py-2 rounded-xl bg-accent-purple/20 border border-accent-purple/40 text-sm text-white"
            >
              <ClipboardIcon className="w-4 h-4" />
              {t('content.copy')}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
