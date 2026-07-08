'use client';

import { useMemo, useState } from 'react';
import { useLocale } from '@/contexts/LocaleContext';
import { CATEGORIES } from '@/data/categories';
import { symptoms, type Symptom } from '@/data/symptoms';
import {
  getUserProfile,
  saveUserProfile,
  type UserProfile,
} from '@/lib/storage';
import { ArrowRightIcon, CheckIcon, ChevronLeftIcon, SparklesIcon } from '@/components/icons';

type Step = 1 | 2 | 3;

interface GuidedWizardProps {
  onComplete: (selected: Symptom[], profile: UserProfile) => void;
  onCancel: () => void;
}

export function GuidedWizard({ onComplete, onCancel }: GuidedWizardProps) {
  const { locale, t } = useLocale();
  const [step, setStep] = useState<Step>(1);
  const [focusIds, setFocusIds] = useState<string[]>([]);
  const [selected, setSelected] = useState<Symptom[]>([]);
  const [profile, setProfile] = useState<UserProfile>(() =>
    typeof window !== 'undefined' ? getUserProfile() : {},
  );

  const focusSymptoms = useMemo(() => {
    if (focusIds.length === 0) return symptoms;
    return symptoms.filter((s) => focusIds.includes(s.category_id));
  }, [focusIds]);

  const progress = (step / 3) * 100;

  const toggleFocus = (id: string) => {
    setFocusIds((prev) => (prev.includes(id) ? prev.filter((x) => x !== id) : [...prev, id]));
  };

  const toggleSymptom = (s: Symptom) => {
    setSelected((prev) => {
      const exists = prev.some((x) => x.id === s.id);
      if (exists) return prev.filter((x) => x.id !== s.id);
      return [...prev, s];
    });
  };

  const updateProfile = (next: UserProfile) => {
    setProfile(next);
    saveUserProfile(next);
  };

  const canNext =
    step === 1 ? focusIds.length > 0 : step === 2 ? selected.length > 0 : true;

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between gap-3">
        <button
          type="button"
          onClick={() => {
            if (step === 1) onCancel();
            else setStep((s) => (s - 1) as Step);
          }}
          className="inline-flex items-center gap-1 text-sm text-zinc-400 hover:text-white transition-colors"
        >
          <ChevronLeftIcon className="w-4 h-4" />
          {step === 1 ? t('wizard.cancel') : t('wizard.back')}
        </button>
        <span className="text-xs text-zinc-500 tabular-nums">
          {t('wizard.step', { current: String(step), total: '3' })}
        </span>
      </div>

      <div className="h-1.5 rounded-full bg-surface-elevated overflow-hidden">
        <div
          className="h-full rounded-full bg-gradient-to-r from-accent-purple to-accent-blue transition-all duration-300"
          style={{ width: `${progress}%` }}
        />
      </div>

      {step === 1 && (
        <section className="space-y-4">
          <div>
            <h3 className="text-xl font-bold text-white mb-1">{t('wizard.step1.title')}</h3>
            <p className="text-sm text-zinc-500">{t('wizard.step1.desc')}</p>
          </div>
          <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
            {CATEGORIES.map((cat) => {
              const active = focusIds.includes(cat.id);
              return (
                <button
                  key={cat.id}
                  type="button"
                  onClick={() => toggleFocus(cat.id)}
                  className={`relative text-left p-4 rounded-2xl border transition-all ${
                    active
                      ? 'border-accent-purple bg-accent-purple/15 text-white'
                      : 'border-surface-border bg-surface-elevated text-zinc-300 hover:border-zinc-500'
                  }`}
                >
                  {active && (
                    <span className="absolute top-2 right-2 text-accent-purple">
                      <CheckIcon className="w-4 h-4" />
                    </span>
                  )}
                  <span className="text-xl block mb-2" aria-hidden="true">
                    {cat.emoji}
                  </span>
                  <span className="text-sm font-semibold leading-snug">{cat.names[locale]}</span>
                </button>
              );
            })}
          </div>
        </section>
      )}

      {step === 2 && (
        <section className="space-y-4">
          <div>
            <h3 className="text-xl font-bold text-white mb-1">{t('wizard.step2.title')}</h3>
            <p className="text-sm text-zinc-500">
              {t('wizard.step2.desc', { count: String(focusSymptoms.length) })}
            </p>
          </div>
          <div className="max-h-[50vh] overflow-y-auto space-y-2 pr-1">
            {focusSymptoms.map((s) => {
              const active = selected.some((x) => x.id === s.id);
              return (
                <button
                  key={s.id}
                  type="button"
                  onClick={() => toggleSymptom(s)}
                  className={`w-full flex items-center justify-between gap-3 px-4 py-3 rounded-xl border text-left transition-all ${
                    active
                      ? 'border-accent-purple bg-accent-purple/15 text-white'
                      : 'border-surface-border bg-surface-elevated text-zinc-300 hover:border-zinc-500'
                  }`}
                >
                  <span className="text-sm font-medium">{s.names[locale]}</span>
                  {active && <CheckIcon className="w-4 h-4 text-accent-purple shrink-0" />}
                </button>
              );
            })}
          </div>
          {selected.length > 0 && (
            <p className="text-xs text-zinc-500">
              {t('wizard.step2.selected', { count: String(selected.length) })}
            </p>
          )}
        </section>
      )}

      {step === 3 && (
        <section className="space-y-4">
          <div>
            <h3 className="text-xl font-bold text-white mb-1">{t('wizard.step3.title')}</h3>
            <p className="text-sm text-zinc-500">{t('wizard.step3.desc')}</p>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label className="block text-sm text-zinc-400 mb-2">{t('profile.age')}</label>
              <select
                value={profile.age || ''}
                onChange={(e) => updateProfile({ ...profile, age: e.target.value })}
                className="w-full bg-surface border border-surface-border rounded-xl px-4 py-3 text-white focus:border-accent-purple focus:outline-none"
              >
                <option value="">{t('profile.selectAge')}</option>
                <option value="18-25">18-25</option>
                <option value="26-35">26-35</option>
                <option value="36-45">36-45</option>
                <option value="46-55">46-55</option>
                <option value="55+">55+</option>
              </select>
            </div>
            <div>
              <label className="block text-sm text-zinc-400 mb-2">{t('profile.gender')}</label>
              <select
                value={profile.gender || ''}
                onChange={(e) => updateProfile({ ...profile, gender: e.target.value })}
                className="w-full bg-surface border border-surface-border rounded-xl px-4 py-3 text-white focus:border-accent-purple focus:outline-none"
              >
                <option value="">{t('profile.selectGender')}</option>
                <option value="male">{t('profile.male')}</option>
                <option value="female">{t('profile.female')}</option>
                <option value="other">{t('profile.other')}</option>
              </select>
            </div>
          </div>

          <label className="flex items-start gap-3 p-4 rounded-2xl border border-surface-border bg-surface-elevated cursor-pointer">
            <input
              type="checkbox"
              checked={Boolean(profile.onMedication)}
              onChange={(e) => updateProfile({ ...profile, onMedication: e.target.checked })}
              className="mt-1 rounded border-zinc-600 bg-surface text-accent-purple focus:ring-accent-purple"
            />
            <span>
              <span className="block text-sm font-medium text-white">{t('wizard.meds.label')}</span>
              <span className="block text-xs text-zinc-500 mt-1">{t('wizard.meds.hint')}</span>
            </span>
          </label>

          {profile.onMedication && (
            <div className="bg-amber-500/10 border border-amber-500/25 rounded-2xl p-4 text-sm text-amber-100/90">
              {t('wizard.meds.warning')}
            </div>
          )}
        </section>
      )}

      <div className="pt-2">
        {step < 3 ? (
          <button
            type="button"
            disabled={!canNext}
            onClick={() => setStep((s) => (s + 1) as Step)}
            className="w-full py-4 rounded-2xl font-bold text-lg flex items-center justify-center gap-2 transition-all disabled:opacity-40 disabled:cursor-not-allowed bg-gradient-to-r from-accent-purple to-accent-blue text-white shadow-xl shadow-purple-500/20"
          >
            {t('wizard.next')}
            <ArrowRightIcon />
          </button>
        ) : (
          <button
            type="button"
            disabled={selected.length === 0}
            onClick={() => {
              saveUserProfile(profile);
              onComplete(selected, profile);
            }}
            className="w-full py-4 rounded-2xl font-bold text-lg flex items-center justify-center gap-2 transition-all disabled:opacity-40 bg-gradient-to-r from-accent-purple to-accent-blue text-white shadow-xl shadow-purple-500/25"
          >
            <SparklesIcon className="w-5 h-5" />
            {t('wizard.finish', { count: String(selected.length) })}
          </button>
        )}
      </div>
    </div>
  );
}
