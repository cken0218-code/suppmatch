'use client';

import { useEffect, useMemo, useState } from 'react';
import { useLocale } from '@/contexts/LocaleContext';
import { getProductsForSupplement } from '@/data/supplementProducts';
import { getReasonForSupplement } from '@/data/supplementReasons';
import { isFavorite, toggleFavorite } from '@/data/favorites';
import type { Symptom } from '@/data/symptoms';
import { getUserProfile, type UserProfile } from '@/lib/storage';
import { scoreSupplementForProfile, sortRecommendations } from '@/lib/personalize';
import {
  buildShareText,
  buildShareUrl,
  copyText,
  shareResults,
} from '@/lib/share';
import { ProductCard } from '@/components/ProductCard';
import { EvidenceBlock } from '@/components/EvidenceBlock';
import { InteractionAlerts } from '@/components/InteractionAlerts';
import { FeedbackPanel } from '@/components/FeedbackPanel';
import {
  ArrowRightIcon,
  ChevronLeftIcon,
  ClipboardIcon,
  ShareIcon,
  SparklesIcon,
  StarIcon,
} from '@/components/icons';
import type { AppLocale } from '@/lib/i18n-routing';
import Link from 'next/link';
import { symptomPath } from '@/lib/i18n-routing';

interface RecommendationViewProps {
  symptoms: Symptom[];
  onBack: () => void;
}

type Rec = {
  name: { 'zh-HK': string; 'zh-CN': string; en: string };
  products: ReturnType<typeof getProductsForSupplement>;
  symptomCount: number;
  boost: number;
  boostReasonKey?: string;
  reason: string | null;
  fromSymptoms: string[];
  relatedSymptomIds: string[];
};

export function RecommendationView({ symptoms: selectedSymptoms, onBack }: RecommendationViewProps) {
  const { locale, t } = useLocale();
  const [profile, setProfile] = useState<UserProfile>({});
  const [favKeys, setFavKeys] = useState<Set<string>>(new Set());
  const [shareMsg, setShareMsg] = useState<string | null>(null);

  useEffect(() => {
    setProfile(getUserProfile());
  }, []);

  const recommendations = useMemo(() => {
    const recs = new Map<string, Rec>();

    for (const symptom of selectedSymptoms) {
      for (const rec of symptom.recommendations) {
        const key = rec.name.en.toLowerCase();
        const existing = recs.get(key);
        if (existing) {
          existing.symptomCount += 1;
          if (!existing.fromSymptoms.includes(symptom.names[locale])) {
            existing.fromSymptoms.push(symptom.names[locale]);
          }
          if (!existing.relatedSymptomIds.includes(symptom.id)) {
            existing.relatedSymptomIds.push(symptom.id);
          }
        } else {
          const { boost, reasonKey } = scoreSupplementForProfile(rec.name.en, profile);
          recs.set(key, {
            name: rec.name,
            products: getProductsForSupplement(rec.name.en),
            symptomCount: 1,
            boost,
            boostReasonKey: reasonKey,
            reason: getReasonForSupplement(rec.name.en, locale),
            fromSymptoms: [symptom.names[locale]],
            relatedSymptomIds: [symptom.id],
          });
        }
      }
    }

    return sortRecommendations(Array.from(recs.values()));
  }, [selectedSymptoms, locale, profile]);

  useEffect(() => {
    setFavKeys(
      new Set(recommendations.filter((r) => isFavorite(r.name.en)).map((r) => r.name.en.toLowerCase())),
    );
  }, [recommendations]);

  const priorityRecs = recommendations.filter((r) => r.symptomCount > 1);
  const hasProfile = Boolean(profile.age || profile.gender);

  const handleToggleFav = (rec: Rec) => {
    const nowFav = toggleFavorite({
      name: rec.name,
      relatedSymptomIds: rec.relatedSymptomIds,
    });
    setFavKeys((prev) => {
      const next = new Set(prev);
      const key = rec.name.en.toLowerCase();
      if (nowFav) next.add(key);
      else next.delete(key);
      return next;
    });
  };

  const handleShare = async () => {
    const url = buildShareUrl(selectedSymptoms.map((s) => s.id));
    const text = buildShareText(
      selectedSymptoms,
      recommendations.map((r) => r.name[locale]),
      locale,
    );
    const result = await shareResults({
      title: 'SuppMatch',
      text,
      url,
    });
    if (result === 'shared') setShareMsg(t('share.done'));
    else if (result === 'copied') setShareMsg(t('share.copied'));
    else setShareMsg(t('share.failed'));
    setTimeout(() => setShareMsg(null), 2500);
  };

  const handleCopyLink = async () => {
    const url = buildShareUrl(selectedSymptoms.map((s) => s.id));
    const ok = await copyText(url);
    setShareMsg(ok ? t('share.linkCopied') : t('share.failed'));
    setTimeout(() => setShareMsg(null), 2500);
  };

  return (
    <div className="space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-3">
        <button
          type="button"
          onClick={onBack}
          className="inline-flex items-center gap-2 text-accent-purple hover:text-white font-medium transition-colors"
        >
          <ChevronLeftIcon />
          {t('button.back')}
        </button>

        <div className="flex items-center gap-2">
          <button
            type="button"
            onClick={handleCopyLink}
            className="inline-flex items-center gap-1.5 px-3 py-2 rounded-xl border border-surface-border text-sm text-zinc-300 hover:text-white hover:border-zinc-500 transition-colors"
          >
            <ClipboardIcon className="w-4 h-4" />
            {t('share.copyLink')}
          </button>
          <button
            type="button"
            onClick={handleShare}
            className="inline-flex items-center gap-1.5 px-3 py-2 rounded-xl bg-accent-purple/20 border border-accent-purple/40 text-sm text-white hover:bg-accent-purple/30 transition-colors"
          >
            <ShareIcon className="w-4 h-4" />
            {t('share.button')}
          </button>
        </div>
      </div>

      {shareMsg && (
        <div className="text-center text-sm text-emerald-300 bg-emerald-500/10 border border-emerald-500/20 rounded-xl py-2">
          {shareMsg}
        </div>
      )}

      <div className="bg-gradient-to-r from-accent-purple to-accent-blue rounded-3xl p-6 text-white">
        <div className="flex items-center gap-2 mb-3">
          <SparklesIcon className="w-5 h-5" />
          <span className="font-bold">
            {t('recommendation.selected', { count: String(selectedSymptoms.length) })}
          </span>
        </div>
        <div className="flex flex-wrap gap-2">
          {selectedSymptoms.map((s) => (
            <Link
              key={s.id}
              href={symptomPath(locale as AppLocale, s.id)}
              className="px-3 py-1.5 bg-white/20 backdrop-blur-sm rounded-full text-sm font-medium hover:bg-white/30 transition-colors"
              title={t('symptom.guide')}
            >
              {s.names[locale]}
            </Link>
          ))}
        </div>
        {hasProfile && (
          <p className="mt-3 text-sm text-white/80">
            {t('recommendation.personalized', {
              age: profile.age || '—',
              gender:
                profile.gender === 'male'
                  ? t('profile.male')
                  : profile.gender === 'female'
                    ? t('profile.female')
                    : profile.gender === 'other'
                      ? t('profile.other')
                      : '—',
            })}
          </p>
        )}
      </div>

      {profile.onMedication && (
        <div className="bg-amber-500/10 border border-amber-500/25 rounded-2xl p-4 text-sm text-amber-100/90">
          {t('wizard.meds.warning')}
        </div>
      )}

      <InteractionAlerts supplementNamesEn={recommendations.map((r) => r.name.en)} />

      {/* Multi-symptom priority merge banner */}
      {priorityRecs.length > 0 && (
        <div className="rounded-3xl border border-emerald-500/30 bg-emerald-500/10 p-5 space-y-3">
          <h3 className="font-bold text-emerald-200 flex items-center gap-2">
            <span aria-hidden="true">🎯</span>
            {t('recommendation.priorityTitle')}
          </h3>
          <p className="text-sm text-emerald-100/80">{t('recommendation.priorityDesc')}</p>
          <ul className="space-y-2">
            {priorityRecs.map((rec) => (
              <li
                key={rec.name.en}
                className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-1 text-sm bg-surface/40 rounded-xl px-3 py-2"
              >
                <span className="font-semibold text-white">{rec.name[locale]}</span>
                <span className="text-emerald-200/90 text-xs sm:text-sm">
                  {t('recommendation.priorityItem', {
                    count: String(rec.symptomCount),
                    symptoms: rec.fromSymptoms.join(locale === 'en' ? ', ' : '、'),
                  })}
                </span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {recommendations.map((rec) => {
        const key = rec.name.en.toLowerCase();
        const fav = favKeys.has(key);
        return (
          <section
            key={key}
            className="bg-surface-card rounded-3xl border border-surface-border overflow-hidden"
          >
            <div className="px-5 py-4 border-b border-surface-border space-y-2">
              <div className="flex flex-wrap items-center gap-2">
                <h3 className="text-lg font-bold text-white flex items-center gap-2 min-w-0 flex-1">
                  <span className="w-8 h-8 bg-accent-purple/20 rounded-xl flex items-center justify-center shrink-0">
                    💊
                  </span>
                  <span className="truncate">{rec.name[locale]}</span>
                </h3>
                <button
                  type="button"
                  onClick={() => handleToggleFav(rec)}
                  className={`shrink-0 p-2 rounded-xl border transition-colors ${
                    fav
                      ? 'border-amber-400/50 text-amber-300 bg-amber-400/10'
                      : 'border-surface-border text-zinc-500 hover:text-amber-300 hover:border-amber-400/40'
                  }`}
                  aria-label={fav ? t('favorites.remove') : t('favorites.add')}
                  title={fav ? t('favorites.remove') : t('favorites.add')}
                >
                  <StarIcon className="w-5 h-5" filled={fav} />
                </button>
              </div>
              <div className="flex flex-wrap gap-2 pl-10">
                {rec.symptomCount > 1 && (
                  <span className="text-xs px-2 py-0.5 rounded-full bg-emerald-500/15 text-emerald-300 border border-emerald-500/30">
                    {t('recommendation.multiMatch', { count: String(rec.symptomCount) })}
                  </span>
                )}
                {rec.boost > 0 && rec.boostReasonKey && (
                  <span className="text-xs px-2 py-0.5 rounded-full bg-accent-purple/15 text-purple-200 border border-accent-purple/30">
                    {t(rec.boostReasonKey)}
                  </span>
                )}
              </div>
              {rec.reason && (
                <p className="text-sm text-zinc-400 leading-relaxed pl-10">{rec.reason}</p>
              )}
              <div className="pl-10">
                <EvidenceBlock nameEn={rec.name.en} locale={locale as AppLocale} compact />
              </div>
              {rec.symptomCount > 1 && (
                <p className="text-xs text-zinc-500 pl-10">
                  {t('recommendation.covers', {
                    symptoms: rec.fromSymptoms.join(locale === 'en' ? ', ' : '、'),
                  })}
                </p>
              )}
            </div>

            <div className="p-5">
              {rec.products.length > 0 ? (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {rec.products.map((product) => (
                    <ProductCard
                      key={product.id}
                      product={product}
                      enableWatch
                      watchLabel={t('price.watch')}
                      watchingLabel={t('price.watching')}
                    />
                  ))}
                </div>
              ) : (
                <p className="text-zinc-500 text-sm text-center py-6">{t('recommendation.noProducts')}</p>
              )}
            </div>
          </section>
        );
      })}

      <a
        href={selectedSymptoms[0]?.iherb_category.url || 'https://www.iherb.com/c/supplements'}
        target="_blank"
        rel="noopener noreferrer sponsored"
        className="flex items-center justify-center gap-2 py-4 bg-white text-zinc-900 rounded-2xl font-bold text-lg hover:bg-zinc-100 transition-colors"
      >
        <span aria-hidden="true">🌿</span>
        {t('iherb.more')}
        <ArrowRightIcon />
      </a>

      <FeedbackPanel
        feedbackKey={`combo:${selectedSymptoms
          .map((s) => s.id)
          .sort()
          .join('+')}`}
        label={selectedSymptoms.map((s) => s.names.en).join(', ')}
      />

      <div className="bg-amber-500/10 border border-amber-500/20 rounded-2xl p-4">
        <p className="text-sm text-amber-200/90">{t('disclaimer.full')}</p>
      </div>
    </div>
  );
}
