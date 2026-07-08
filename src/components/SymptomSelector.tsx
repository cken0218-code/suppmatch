'use client';

import { useCallback, useEffect, useMemo, useState } from 'react';
import Fuse from 'fuse.js';
import { useLocale } from '@/contexts/LocaleContext';
import { ALL_CATEGORY_ID } from '@/data/categories';
import { symptoms, type Symptom } from '@/data/symptoms';
import {
  addToHistory,
  clearHistory,
  getSearchHistory,
  getUserProfile,
  incrementPopular,
  saveUserProfile,
  type UserProfile,
} from '@/lib/storage';
import { SearchBar } from '@/components/SearchBar';
import { SymptomCard } from '@/components/SymptomCard';
import { PopularSymptoms } from '@/components/PopularSymptoms';
import { ProfileSetup } from '@/components/ProfileSetup';
import { CategoryTabs } from '@/components/CategoryTabs';
import { ArrowRightIcon, SparklesIcon } from '@/components/icons';

interface SymptomSelectorProps {
  onRecommend: (symptoms: Symptom[]) => void;
}

export function SymptomSelector({ onRecommend }: SymptomSelectorProps) {
  const { t } = useLocale();
  const [selected, setSelected] = useState<Symptom[]>([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [categoryId, setCategoryId] = useState(ALL_CATEGORY_ID);
  const [searchHistory, setSearchHistory] = useState<string[]>([]);
  const [profile, setProfile] = useState<UserProfile>({});
  const [showProfile, setShowProfile] = useState(false);

  useEffect(() => {
    setSearchHistory(getSearchHistory());
    const saved = getUserProfile();
    setProfile(saved);
    if (!saved.age && !saved.gender) {
      setShowProfile(true);
    }
  }, []);

  const categoryCounts = useMemo(() => {
    const counts: Record<string, number> = { [ALL_CATEGORY_ID]: symptoms.length };
    for (const s of symptoms) {
      counts[s.category_id] = (counts[s.category_id] || 0) + 1;
    }
    return counts;
  }, []);

  const filteredSymptoms = useMemo(() => {
    let pool =
      categoryId === ALL_CATEGORY_ID
        ? symptoms
        : symptoms.filter((s) => s.category_id === categoryId);

    if (!searchQuery.trim()) return pool;

    const fuse = new Fuse(pool, {
      keys: [
        { name: 'names.zh-HK', weight: 3 },
        { name: 'names.zh-CN', weight: 3 },
        { name: 'names.en', weight: 2 },
        { name: 'id', weight: 1 },
        { name: 'recommendations.name.zh-HK', weight: 0.5 },
        { name: 'recommendations.name.zh-CN', weight: 0.5 },
        { name: 'recommendations.name.en', weight: 0.5 },
        { name: 'iherb_category.name', weight: 0.3 },
      ],
      threshold: 0.3,
      includeScore: true,
      minMatchCharLength: 1,
      ignoreLocation: true,
    });

    return fuse.search(searchQuery).map((r) => r.item);
  }, [searchQuery, categoryId]);

  useEffect(() => {
    if (!searchQuery.trim()) return;
    addToHistory(searchQuery);
    setSearchHistory(getSearchHistory());
  }, [searchQuery]);

  const toggleSymptom = useCallback((symptom: Symptom) => {
    incrementPopular(symptom.id);
    setSelected((prev) => {
      const exists = prev.find((s) => s.id === symptom.id);
      if (exists) return prev.filter((s) => s.id !== symptom.id);
      return [...prev, symptom];
    });
  }, []);

  const handlePopularSelect = useCallback(
    (id: string) => {
      const symptom = symptoms.find((s) => s.id === id);
      if (symptom) toggleSymptom(symptom);
    },
    [toggleSymptom],
  );

  const handleProfileChange = (next: UserProfile) => {
    setProfile(next);
    saveUserProfile(next);
  };

  return (
    <div className="space-y-6">
      {showProfile && (
        <ProfileSetup
          profile={profile}
          onChange={handleProfileChange}
          onClose={() => setShowProfile(false)}
        />
      )}

      {!showProfile && (profile.age || profile.gender) && (
        <button
          type="button"
          onClick={() => setShowProfile(true)}
          className="text-xs text-zinc-500 hover:text-accent-purple transition-colors"
        >
          {t('profile.edit')}
        </button>
      )}

      <SearchBar
        onSearch={setSearchQuery}
        showHistory={searchHistory}
        onClearHistory={() => {
          clearHistory();
          setSearchHistory([]);
        }}
        onPickCategory={(id) => {
          setCategoryId(id);
          setSearchQuery('');
        }}
      />

      <CategoryTabs
        activeId={categoryId}
        onChange={setCategoryId}
        counts={categoryCounts}
      />

      {searchQuery ? (
        <p className="text-sm text-zinc-500">
          {t('search.results', { count: String(filteredSymptoms.length) })}
        </p>
      ) : (
        <PopularSymptoms onSelect={handlePopularSelect} />
      )}

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
        {filteredSymptoms.map((symptom) => (
          <SymptomCard
            key={symptom.id}
            symptom={symptom}
            isSelected={selected.some((s) => s.id === symptom.id)}
            onClick={() => toggleSymptom(symptom)}
          />
        ))}
      </div>

      {filteredSymptoms.length === 0 && (
        <p className="text-center text-zinc-500 py-10">{t('search.noResults')}</p>
      )}

      {selected.length > 0 && (
        <div className="sticky bottom-4 z-10 pt-2">
          <button
            type="button"
            onClick={() => onRecommend(selected)}
            className="w-full py-4 bg-gradient-to-r from-accent-purple to-accent-blue text-white rounded-2xl font-bold text-lg shadow-xl shadow-purple-500/25 hover:shadow-purple-500/40 transition-all flex items-center justify-center gap-2"
          >
            <SparklesIcon className="w-5 h-5" />
            <span>{t('button.recommend', { count: String(selected.length) })}</span>
            <ArrowRightIcon />
          </button>
        </div>
      )}
    </div>
  );
}
