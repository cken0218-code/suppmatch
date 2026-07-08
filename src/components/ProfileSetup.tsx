'use client';

import { useLocale } from '@/contexts/LocaleContext';
import type { UserProfile } from '@/lib/storage';

interface ProfileSetupProps {
  profile: UserProfile;
  onChange: (profile: UserProfile) => void;
  onClose: () => void;
}

export function ProfileSetup({ profile, onChange, onClose }: ProfileSetupProps) {
  const { t } = useLocale();

  return (
    <div className="bg-surface-card border border-surface-border rounded-2xl p-5">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-white flex items-center gap-2">
          <span className="w-8 h-8 bg-gradient-to-br from-accent-purple to-accent-blue rounded-xl flex items-center justify-center text-sm">
            ✨
          </span>
          {t('profile.title')}
        </h3>
        <button
          type="button"
          onClick={onClose}
          className="text-zinc-500 hover:text-white transition-colors p-1"
          aria-label={t('profile.close')}
        >
          ✕
        </button>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div>
          <label className="block text-sm text-zinc-400 mb-2">{t('profile.age')}</label>
          <select
            value={profile.age || ''}
            onChange={(e) => onChange({ ...profile, age: e.target.value })}
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
            onChange={(e) => onChange({ ...profile, gender: e.target.value })}
            className="w-full bg-surface border border-surface-border rounded-xl px-4 py-3 text-white focus:border-accent-purple focus:outline-none"
          >
            <option value="">{t('profile.selectGender')}</option>
            <option value="male">{t('profile.male')}</option>
            <option value="female">{t('profile.female')}</option>
            <option value="other">{t('profile.other')}</option>
          </select>
        </div>
      </div>

      <label className="mt-4 flex items-start gap-3 p-3 rounded-xl border border-surface-border bg-surface cursor-pointer">
        <input
          type="checkbox"
          checked={Boolean(profile.onMedication)}
          onChange={(e) => onChange({ ...profile, onMedication: e.target.checked })}
          className="mt-1 rounded border-zinc-600 bg-surface text-accent-purple focus:ring-accent-purple"
        />
        <span>
          <span className="block text-sm text-white">{t('wizard.meds.label')}</span>
          <span className="block text-xs text-zinc-500 mt-0.5">{t('wizard.meds.hint')}</span>
        </span>
      </label>

      {profile.age && profile.gender && (
        <p className="text-sm text-accent-purple mt-3">{t('profile.saved')}</p>
      )}
    </div>
  );
}