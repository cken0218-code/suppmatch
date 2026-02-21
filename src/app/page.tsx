'use client';
// Updated: 2026-02-22 - Google AI Studio style redesign v2

import { useState, useMemo, useEffect, useCallback } from 'react';
import Fuse from 'fuse.js';
import { LocaleProvider, useLocale, type Locale } from '@/contexts/LocaleContext';
import { symptoms, type Symptom } from '@/data/symptoms';
import { getProductsForSupplement, type Product } from '@/data/supplementProducts';

// Stats storage
const POPULAR_KEY = 'suppmatch_popular';
const HISTORY_KEY = 'suppmatch_history';
const THEME_KEY = 'suppmatch_dark';
const PROFILE_KEY = 'suppmatch_profile';

// User profile for personalization
interface UserProfile {
  age?: string;
  gender?: string;
}

function getUserProfile(): UserProfile {
  if (typeof window === 'undefined') return {};
  try {
    return JSON.parse(localStorage.getItem(PROFILE_KEY) || '{}');
  } catch {
    return {};
  }
}

function saveUserProfile(profile: UserProfile) {
  localStorage.setItem(PROFILE_KEY, JSON.stringify(profile));
}

// Icons as simple SVG components
const SearchIcon = () => (
  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
  </svg>
);

const XIcon = () => (
  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
  </svg>
);

const SunIcon = () => (
  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
  </svg>
);

const MoonIcon = () => (
  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
  </svg>
);

const SparklesIcon = () => (
  <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
  </svg>
);

const TrendUpIcon = () => (
  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
  </svg>
);

function getPopularSymptoms(): Record<string, number> {
  if (typeof window === 'undefined') return {};
  try {
    return JSON.parse(localStorage.getItem(POPULAR_KEY) || '{}');
  } catch {
    return {};
  }
}

function incrementPopular(symptomId: string) {
  const popular = getPopularSymptoms();
  popular[symptomId] = (popular[symptomId] || 0) + 1;
  localStorage.setItem(POPULAR_KEY, JSON.stringify(popular));
}

function getSearchHistory(): string[] {
  if (typeof window === 'undefined') return [];
  try {
    return JSON.parse(localStorage.getItem(HISTORY_KEY) || '[]');
  } catch {
    return [];
  }
}

function addToHistory(query: string) {
  if (!query.trim()) return;
  const history = getSearchHistory();
  const newHistory = [query, ...history.filter(h => h !== query)].slice(0, 10);
  localStorage.setItem(HISTORY_KEY, JSON.stringify(newHistory));
}

function clearHistory() {
  localStorage.removeItem(HISTORY_KEY);
}

function isDarkMode(): boolean {
  if (typeof window === 'undefined') return false;
  return localStorage.getItem(THEME_KEY) === 'dark' || 
    window.matchMedia('(prefers-color-scheme: dark)').matches;
}

function toggleDarkMode() {
  const dark = !isDarkMode();
  localStorage.setItem(THEME_KEY, dark ? 'dark' : 'light');
  document.documentElement.classList.toggle('dark', dark);
}

function LanguageSelector() {
  const { locale, setLocale } = useLocale();
  
  const flags: Record<Locale, string> = {
    'zh-HK': '🇭🇰',
    'zh-CN': '🇨🇳',
    'en': '🇺🇸'
  };

  return (
    <div className="flex gap-1">
      {(['zh-HK', 'zh-CN', 'en'] as Locale[]).map((l) => (
        <button
          key={l}
          onClick={() => setLocale(l)}
          className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
            locale === l 
              ? 'bg-gradient-to-r from-[#8b5cf6] to-[#3b82f6] text-white shadow-lg shadow-purple-500/25' 
              : 'bg-[#1a1a1f] text-zinc-400 hover:text-white hover:bg-[#2d2d35] border border-[#2d2d35]'
          }`}
        >
          {flags[l]}
        </button>
      ))}
    </div>
  );
}

function ThemeToggle() {
  const [dark, setDark] = useState(isDarkMode());

  useEffect(() => {
    setDark(isDarkMode());
  }, []);

  return (
    <button
      onClick={() => {
        toggleDarkMode();
        setDark(!dark);
      }}
      className="p-2 rounded-xl bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-400 hover:bg-zinc-200 dark:hover:bg-zinc-700 transition-all"
    >
      {dark ? <SunIcon /> : <MoonIcon />}
    </button>
  );
}

function SearchBar({ 
  onSearch, 
  showHistory, 
  onClearHistory 
}: { 
  onSearch: (q: string) => void;
  showHistory: string[];
  onClearHistory: () => void;
}) {
  const [value, setValue] = useState('');

  return (
    <div className="relative">
      <div className="relative">
        <SearchIcon />
        <input
          type="text"
          value={value}
          onChange={(e) => {
            setValue(e.target.value);
            onSearch(e.target.value);
          }}
          placeholder="邊度唔舒服？"
          className="w-full px-4 py-4 pl-12 text-lg bg-white dark:bg-zinc-800 border-2 border-zinc-200 dark:border-zinc-700 rounded-2xl focus:border-emerald-500 focus:ring-4 focus:ring-emerald-500/20 outline-none transition-all placeholder:text-zinc-400"
        />
        {value && (
          <button
            onClick={() => {
              setValue('');
              onSearch('');
            }}
            className="absolute right-4 top-1/2 -translate-y-1/2 p-1 hover:bg-zinc-100 dark:hover:bg-zinc-700 rounded-lg"
          >
            <XIcon />
          </button>
        )}
      </div>
      
      {showHistory.length > 0 && !value && (
        <div className="mt-3 flex items-center gap-2 flex-wrap">
          <span className="text-xs text-zinc-400">最近搜尋：</span>
          {showHistory.slice(0, 5).map((h, i) => (
            <button
              key={i}
              onClick={() => {
                setValue(h);
                onSearch(h);
              }}
              className="px-2 py-1 text-xs bg-zinc-100 dark:bg-zinc-800 text-zinc-600 dark:text-zinc-400 rounded-lg hover:bg-zinc-200 dark:hover:bg-zinc-700 transition-colors"
            >
              {h}
            </button>
          ))}
          <button
            onClick={onClearHistory}
            className="text-xs text-zinc-400 hover:text-red-500 transition-colors"
          >
            清除
          </button>
        </div>
      )}
    </div>
  );
}

function SymptomCard({ 
  symptom, 
  isSelected, 
  onClick 
}: { 
  symptom: Symptom; 
  isSelected: boolean;
  onClick: () => void;
}) {
  const { locale } = useLocale();
  
  return (
    <button
      onClick={onClick}
      className={`w-full text-left p-4 rounded-2xl border-2 transition-all duration-200 hover:shadow-lg ${
        isSelected 
          ? 'border-emerald-500 bg-emerald-50 dark:bg-emerald-900/30 shadow-lg shadow-emerald-500/20' 
          : 'border-zinc-200 dark:border-zinc-700 bg-white dark:bg-zinc-800 hover:border-emerald-300 hover:shadow-md'
      }`}
    >
      <div className="flex items-start justify-between">
        <div className="flex-1">
          <h3 className="font-semibold text-zinc-800 dark:text-zinc-200">
            {symptom.names[locale]}
          </h3>
          <p className="text-xs text-zinc-500 dark:text-zinc-400 mt-1">
            {symptom.recommendations.slice(0, 2).map(r => r.name[locale]).join('、')}
            {symptom.recommendations.length > 2 && '...'}
          </p>
        </div>
        <div className={`w-6 h-6 rounded-full border-2 flex items-center justify-center transition-all ${
          isSelected 
            ? 'border-emerald-500 bg-emerald-500' 
            : 'border-zinc-300 dark:border-zinc-600'
        }`}>
          {isSelected && (
            <svg className="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
            </svg>
          )}
        </div>
      </div>
    </button>
  );
}

function PopularSymptoms({ onSelect }: { onSelect: (id: string) => void }) {
  const [popular, setPopular] = useState<{id: string, count: number}[]>([]);
  const { locale } = useLocale();

  useEffect(() => {
    const pop = getPopularSymptoms();
    const sorted = Object.entries(pop)
      .map(([id, count]) => ({ id, count: count as number }))
      .sort((a, b) => b.count - a.count)
      .slice(0, 6);
    setPopular(sorted);
  }, []);

  if (popular.length === 0) return null;

  return (
    <div className="mt-6">
      <div className="flex items-center gap-2 mb-3">
        <TrendUpIcon />
        <span className="text-sm font-medium text-zinc-600 dark:text-zinc-400">熱門症狀</span>
      </div>
      <div className="flex flex-wrap gap-2">
        {popular.map(p => {
          const symptom = symptoms.find(s => s.id === p.id);
          if (!symptom) return null;
          return (
            <button
              key={p.id}
              onClick={() => onSelect(p.id)}
              className="px-4 py-2 bg-white dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700 rounded-full text-sm font-medium text-zinc-700 dark:text-zinc-300 hover:border-emerald-500 hover:text-emerald-600 dark:hover:text-emerald-400 transition-all"
            >
              {symptom.names[locale]}
            </button>
          );
        })}
      </div>
    </div>
  );
}

// Product Card - Modern Style
function ProductCard({ product }: { product: Product }) {
  return (
    <div className="bg-white dark:bg-zinc-800 rounded-2xl shadow-md border border-zinc-200 dark:border-zinc-700 overflow-hidden hover:shadow-lg transition-shadow">
      <div className="p-4">
        <div className="flex justify-between items-start mb-2">
          <div>
            <h4 className="font-semibold text-zinc-800 dark:text-zinc-200">{product.nameZh}</h4>
            <p className="text-xs text-zinc-500 dark:text-zinc-400">{product.brand}</p>
          </div>
          <span className="text-lg font-bold text-emerald-600 dark:text-emerald-400">
            {product.priceRange}
          </span>
        </div>

        <div className="flex gap-2 mt-4">
          <a
            href={product.iherbUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="flex-1 flex items-center justify-center gap-1 py-2.5 bg-emerald-500 text-white rounded-xl font-medium hover:bg-emerald-600 transition-colors text-sm"
          >
            <span>🌿</span> iHerb
          </a>
          <a
            href={product.amazonUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="flex-1 flex items-center justify-center gap-1 py-2.5 bg-zinc-800 text-white rounded-xl font-medium hover:bg-zinc-700 transition-colors text-sm"
          >
            <span>📦</span> Amazon
          </a>
        </div>
        
        <p className="text-xs text-zinc-400 dark:text-zinc-500 mt-2 text-center">
          預計佣金: {product.commission}
        </p>
      </div>
    </div>
  );
}

// Multi-symptom Recommendation View - Google AI Studio Style
function RecommendationView({ 
  symptoms: selectedSymptoms, 
  onBack 
}: { 
  symptoms: Symptom[]; 
  onBack: () => void;
}) {
  const { locale } = useLocale();

  const allRecommendations = useMemo(() => {
    const recs = new Map<string, { name: { [key: string]: string }; products: Product[] }>();
    
    for (const symptom of selectedSymptoms) {
      for (const rec of symptom.recommendations) {
        const key = rec.name.en.toLowerCase();
        if (!recs.has(key)) {
          const products = getProductsForSupplement(rec.name.en);
          recs.set(key, { name: rec.name, products });
        }
      }
    }
    return Array.from(recs.values());
  }, [selectedSymptoms]);

  return (
    <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-300">
      {/* Back Button */}
      <button
        onClick={onBack}
        className="flex items-center gap-2 text-emerald-600 dark:text-emerald-400 hover:text-emerald-700 dark:hover:text-emerald-300 font-medium transition-colors"
      >
        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
        </svg>
        返回揀症狀
      </button>

      {/* Selected Symptoms Summary - Modern Card */}
      <div className="bg-gradient-to-r from-emerald-500 to-teal-500 rounded-3xl p-6 text-white">
        <div className="flex items-center gap-2 mb-3">
          <SparklesIcon />
          <span className="font-bold">你揀咗 {selectedSymptoms.length} 個症狀</span>
        </div>
        <div className="flex flex-wrap gap-2">
          {selectedSymptoms.map(s => (
            <span 
              key={s.id}
              className="px-3 py-1.5 bg-white/20 backdrop-blur-sm rounded-full text-sm font-medium"
            >
              {s.names[locale]}
            </span>
          ))}
        </div>
      </div>

      {/* Recommendations with Products */}
      {allRecommendations.map((rec, idx) => (
        <div key={idx} className="bg-white dark:bg-zinc-800 rounded-3xl shadow-lg border border-zinc-200 dark:border-zinc-700 overflow-hidden">
          <div className="p-5 border-b border-zinc-100 dark:border-zinc-700">
            <h3 className="text-lg font-bold text-zinc-800 dark:text-zinc-200 flex items-center gap-2">
              <span className="w-8 h-8 bg-emerald-100 dark:bg-emerald-900/30 rounded-xl flex items-center justify-center text-emerald-600">
                💊
              </span>
              {rec.name[locale]}
            </h3>
          </div>
          
          <div className="p-5">
            {rec.products.length > 0 ? (
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {rec.products.map(product => (
                  <ProductCard key={product.id} product={product} />
                ))}
              </div>
            ) : (
              <p className="text-zinc-500 dark:text-zinc-400 text-sm text-center py-4">
                暫時未有產品資料
              </p>
            )}
          </div>
        </div>
      ))}

      {/* General iHerb Link - Prominent CTA */}
      <a
        href={selectedSymptoms[0]?.iherb_category.url || 'https://www.iherb.com/c/supplements'}
        target="_blank"
        rel="noopener noreferrer"
        className="flex items-center justify-center gap-2 py-5 bg-zinc-900 dark:bg-zinc-100 text-white dark:text-zinc-900 rounded-3xl font-bold text-lg hover:bg-zinc-800 dark:hover:bg-zinc-200 transition-colors shadow-xl"
      >
        <span>🌿</span>
        去 iHerb 睇更多產品
        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 8l4 4m0 0l-4 4m4-4H3" />
        </svg>
      </a>

      {/* Disclaimer */}
      <div className="bg-amber-50 dark:bg-amber-900/20 rounded-2xl p-4">
        <p className="text-sm text-amber-800 dark:text-amber-200">
          <strong>⚠️ 聲明：</strong>本網站提供資訊僅供參考，不構成醫療建議。使用任何補充品前請諮詢醫生。本網站包含附屬連結，透過購買我們可能獲得佣金。
        </p>
      </div>
    </div>
  );
}

function MainContent() {
  const { locale } = useLocale();
  const [selectedSymptoms, setSelectedSymptoms] = useState<Symptom[]>([]);
  const [view, setView] = useState<'select' | 'recommend'>('select');
  const [searchQuery, setSearchQuery] = useState('');
  const [searchHistory, setSearchHistory] = useState<string[]>([]);
  const [userProfile, setUserProfile] = useState<UserProfile>({});
  const [showProfileSetup, setShowProfileSetup] = useState(false);

  useEffect(() => {
    setSearchHistory(getSearchHistory());
    setUserProfile(getUserProfile());
  }, []);

  // Show profile setup on first visit
  useEffect(() => {
    if (!userProfile.age && !userProfile.gender) {
      setShowProfileSetup(true);
    }
  }, [userProfile]);

  const filteredSymptoms = useMemo(() => {
    if (!searchQuery.trim()) return symptoms;
    
    const fuse = new Fuse(symptoms, {
      keys: [
        { name: 'names.zh-HK', weight: 3 },
        { name: 'names.zh-CN', weight: 3 },
        { name: 'names.en', weight: 2 },
        { name: 'id', weight: 1 },
        { name: 'recommendations.name.zh-HK', weight: 0.5 },
        { name: 'recommendations.name.zh-CN', weight: 0.5 },
        { name: 'recommendations.name.en', weight: 0.5 },
        { name: 'iherb_category.name', weight: 0.3 }
      ],
      threshold: 0.3,
      includeScore: true,
      includeMatches: true,
      minMatchCharLength: 1,
      ignoreLocation: true,
      useExtendedSearch: true,
    });
    
    const results = fuse.search(searchQuery);
    addToHistory(searchQuery);
    setSearchHistory(getSearchHistory());
    return results.map(r => r.item);
  }, [searchQuery]);

  // Toggle symptom selection
  const handleSymptomClick = useCallback((symptom: Symptom) => {
    incrementPopular(symptom.id);
    setSelectedSymptoms(prev => {
      const exists = prev.find(s => s.id === symptom.id);
      if (exists) {
        return prev.filter(s => s.id !== symptom.id);
      }
      return [...prev, symptom];
    });
  }, []);

  const handleGetRecommendations = useCallback(() => {
    if (selectedSymptoms.length > 0) {
      setView('recommend');
    }
  }, [selectedSymptoms]);

  const handleBack = useCallback(() => {
    setView('select');
    setSelectedSymptoms([]);
  }, []);

  const handleClearHistory = useCallback(() => {
    clearHistory();
    setSearchHistory([]);
  }, []);

  const handleSelectFromPopular = useCallback((id: string) => {
    const symptom = symptoms.find(s => s.id === id);
    if (symptom) handleSymptomClick(symptom);
  }, [handleSymptomClick]);

  // Keyboard shortcuts
  useEffect(() => {
    function handleKeyDown(e: KeyboardEvent) {
      if (e.key === 'Escape' && view === 'recommend') {
        handleBack();
      }
      if (e.key === '/' && document.activeElement?.tagName !== 'INPUT') {
        e.preventDefault();
        document.querySelector<HTMLInputElement>('input[type="text"]')?.focus();
      }
    }
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [view, handleBack]);

  if (view === 'recommend' && selectedSymptoms.length > 0) {
    return <RecommendationView symptoms={selectedSymptoms} onBack={handleBack} />;
  }

  return (
    <div className="space-y-6">
      {/* Personalization Setup - Google AI Studio Style */}
      {showProfileSetup && (
        <div className="bg-[#1a1a1f] border border-[#2d2d35] rounded-2xl p-5 animate-in slide-in-from-top-4">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-lg font-semibold text-white flex items-center gap-2">
              <span className="w-8 h-8 bg-gradient-to-br from-[#8b5cf6] to-[#3b82f6] rounded-xl flex items-center justify-center text-white text-sm">✨</span>
              個人化設定
            </h3>
            <button 
              onClick={() => setShowProfileSetup(false)}
              className="text-zinc-400 hover:text-white transition-colors"
            >
              ✕
            </button>
          </div>
          
          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm text-zinc-400 mb-2">年齡</label>
              <select
                value={userProfile.age || ''}
                onChange={(e) => {
                  const newProfile = { ...userProfile, age: e.target.value };
                  setUserProfile(newProfile);
                  saveUserProfile(newProfile);
                }}
                className="w-full bg-[#0f0f12] border border-[#2d2d35] rounded-xl px-4 py-3 text-white focus:border-[#8b5cf6] focus:outline-none"
              >
                <option value="">選擇年齡</option>
                <option value="18-25">18-25歲</option>
                <option value="26-35">26-35歲</option>
                <option value="36-45">36-45歲</option>
                <option value="46-55">46-55歲</option>
                <option value="55+">55歲以上</option>
              </select>
            </div>
            
            <div>
              <label className="block text-sm text-zinc-400 mb-2">性別</label>
              <select
                value={userProfile.gender || ''}
                onChange={(e) => {
                  const newProfile = { ...userProfile, gender: e.target.value };
                  setUserProfile(newProfile);
                  saveUserProfile(newProfile);
                }}
                className="w-full bg-[#0f0f12] border border-[#2d2d35] rounded-xl px-4 py-3 text-white focus:border-[#8b5cf6] focus:outline-none"
              >
                <option value="">選擇性別</option>
                <option value="male">男性</option>
                <option value="female">女性</option>
                <option value="other">其他</option>
              </select>
            </div>
          </div>
          
          {userProfile.age && userProfile.gender && (
            <p className="text-sm text-[#8b5cf6] mt-3">
              ✅ 已保存！我地會根據你既設定推薦最適合既補充品
            </p>
          )}
        </div>
      )}

      <SearchBar 
        onSearch={setSearchQuery} 
        showHistory={searchHistory}
        onClearHistory={handleClearHistory}
      />
      
      {searchQuery && (
        <p className="text-sm text-zinc-500 dark:text-zinc-400">
          搵到 {filteredSymptoms.length} 個症狀
        </p>
      )}

      {!searchQuery && <PopularSymptoms onSelect={handleSelectFromPopular} />}

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3">
        {filteredSymptoms.map((symptom) => (
          <SymptomCard
            key={symptom.id}
            symptom={symptom}
            isSelected={selectedSymptoms.some(s => s.id === symptom.id)}
            onClick={() => handleSymptomClick(symptom)}
          />
        ))}
      </div>

      {filteredSymptoms.length === 0 && (
        <p className="text-center text-zinc-500 dark:text-zinc-400 py-8">
          搵唔到相關症狀
        </p>
      )}

      {/* Multi-select floating button */}
      {selectedSymptoms.length > 0 && (
        <div className="sticky bottom-4 z-10 animate-in slide-in-from-bottom-4">
          <button
            onClick={handleGetRecommendations}
            className="w-full py-4 bg-gradient-to-r from-[#8b5cf6] to-[#3b82f6] text-white rounded-2xl font-bold text-lg shadow-xl shadow-purple-500/30 hover:shadow-2xl hover:shadow-purple-500/40 transition-all flex items-center justify-center gap-2"
          >
            <SparklesIcon />
            <span>獲取推薦 ({selectedSymptoms.length} 個症狀)</span>
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17 8l4 4m0 0l-4 4m4-4H3" />
            </svg>
          </button>
        </div>
      )}

      <p className="text-xs text-zinc-400 dark:text-zinc-500 text-center pt-4">
        ⚠️ 本網站提供資訊僅供參考，不構成醫療建議。使用前請諮詢醫生。
      </p>
    </div>
  );
}

function AppContent() {
  useEffect(() => {
    document.documentElement.classList.toggle('dark', isDarkMode());
  }, []);

  const [locale] = useState<Locale>(() => {
    if (typeof window !== 'undefined') {
      const saved = localStorage.getItem('suppmatch-locale') as Locale;
      if (saved && ['zh-HK', 'zh-CN', 'en'].includes(saved)) {
        return saved;
      }
    }
    return 'zh-HK';
  });

  return (
    <LocaleProvider locale={locale}>
      <div className="min-h-screen bg-[#0f0f12]">
        {/* Navigation */}
        <header className="sticky top-0 z-50 bg-[#0f0f12]/90 backdrop-blur-xl border-b border-[#2d2d35]">
          <div className="max-w-4xl mx-auto px-4 py-4 flex justify-between items-center">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-gradient-to-br from-[#8b5cf6] to-[#3b82f6] rounded-2xl flex items-center justify-center text-white shadow-lg shadow-purple-500/30">
                <SparklesIcon />
              </div>
              <div>
                <h1 className="text-xl font-bold bg-gradient-to-r from-white to-zinc-400 bg-clip-text text-transparent">
                  SuppMatch
                </h1>
                <p className="text-xs text-zinc-500">AI 營養補充品推薦</p>
              </div>
            </div>
            <div className="flex gap-2 items-center">
              <ThemeToggle />
              <LanguageSelector />
            </div>
          </div>
        </header>

        <main className="max-w-4xl mx-auto px-4 py-8">
          {/* Hero Section */}
          <div className="text-center mb-8">
            <h2 className="text-3xl md:text-4xl font-bold text-white mb-3">
              症狀揀選 → <span className="bg-gradient-to-r from-[#8b5cf6] to-[#3b82f6] bg-clip-text text-transparent">營養補充品推薦</span>
            </h2>
            <p className="text-zinc-500 dark:text-zinc-400">
              揀選你嘅症狀，獲取個性化 supplement 建議
            </p>
          </div>

          {/* Main Card */}
          <div className="bg-white dark:bg-zinc-800 rounded-3xl shadow-xl border border-zinc-200 dark:border-zinc-700 p-6 md:p-8">
            <MainContent />
          </div>
        </main>

        <footer className="text-center py-6 text-zinc-400 dark:text-zinc-500 text-sm">
          <p>© 2025 SuppMatch. ⚠️ 本網站提供資訊僅供參考，不構成醫療建議。使用前請諮詢醫生。</p>
          <p className="mt-1 text-xs">⌨️ 按 / 搜尋 | 按 ESC 返回</p>
        </footer>
      </div>
    </LocaleProvider>
  );
}

export default function Home() {
  return <AppContent />;
}
