'use client';
// Updated: 2026-02-13 - Added search history, popular symptoms, dark mode, keyboard shortcuts

import { useState, useMemo, useEffect, useCallback } from 'react';
import Fuse from 'fuse.js';
import { LocaleProvider, useLocale, type Locale } from '@/contexts/LocaleContext';
import { symptoms, type Symptom } from '@/data/symptoms';

// Stats storage
const POPULAR_KEY = 'suppmatch_popular';
const HISTORY_KEY = 'suppmatch_history';
const THEME_KEY = 'suppmatch_dark';

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
    <div className="flex gap-2">
      {(['zh-HK', 'zh-CN', 'en'] as Locale[]).map((l) => (
        <button
          key={l}
          onClick={() => setLocale(l)}
          className={`px-2 py-1 rounded text-sm transition-colors ${
            locale === l 
              ? 'bg-emerald-600 text-white' 
              : 'bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-600'
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
      className="p-2 rounded-lg bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 transition-colors"
      title={dark ? 'Switch to Light Mode' : 'Switch to Dark Mode'}
    >
      {dark ? '☀️' : '🌙'}
    </button>
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
  const name = symptom.names[locale];

  return (
    <button
      onClick={onClick}
      className={`p-4 rounded-lg border-2 text-left transition-all ${
        isSelected
          ? 'border-emerald-500 bg-emerald-50 dark:bg-emerald-900/30'
          : 'border-gray-200 dark:border-gray-700 hover:border-emerald-300 dark:hover:border-emerald-600 hover:bg-gray-50 dark:hover:bg-gray-800'
      }`}
    >
      <span className="text-lg font-medium text-gray-800 dark:text-gray-200">{name}</span>
    </button>
  );
}

function SearchBar({ 
  onSearch,
  showHistory,
  onClearHistory
}: { 
  onSearch: (query: string) => void;
  showHistory: string[];
  onClearHistory: () => void;
}) {
  const [focused, setFocused] = useState(false);

  return (
    <div className="relative">
      <input
        type="text"
        placeholder="搜尋症狀... (輸入關鍵字)"
        onChange={(e) => onSearch(e.target.value)}
        onFocus={() => setFocused(true)}
        onBlur={() => setTimeout(() => setFocused(false), 200)}
        className="w-full px-4 py-3 pl-10 border-2 border-gray-200 dark:border-gray-600 rounded-lg 
                   focus:border-emerald-500 focus:outline-none text-lg
                   bg-white dark:bg-gray-800 text-gray-800 dark:text-gray-200
                   placeholder-gray-400 dark:placeholder-gray-500"
      />
      <svg 
        className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400"
        fill="none" 
        stroke="currentColor" 
        viewBox="0 0 24 24"
      >
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
      </svg>
      
      {focused && showHistory.length > 0 && (
        <div className="absolute top-full left-0 right-0 mt-1 bg-white dark:bg-gray-800 border-2 border-gray-200 dark:border-gray-700 rounded-lg shadow-lg z-20 max-h-48 overflow-auto">
          <div className="flex justify-between items-center p-2 border-b border-gray-200 dark:border-gray-700">
            <span className="text-sm text-gray-500">搜尋記錄</span>
            <button onClick={onClearHistory} className="text-sm text-red-500 hover:text-red-600">清除</button>
          </div>
          {showHistory.map((h, i) => (
            <button
              key={i}
              onClick={() => onSearch(h)}
              className="w-full text-left px-4 py-2 hover:bg-gray-100 dark:hover:bg-gray-700 text-gray-700 dark:text-gray-300"
            >
              {h}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}

function PopularSymptoms({ onSelect }: { onSelect: (id: string) => void }) {
  const [popular, setPopular] = useState<{id: string, count: number}[]>([]);
  const [locale] = useLocale();

  useEffect(() => {
    const pop = getPopularSymptoms();
    const sorted = Object.entries(pop)
      .map(([id, count]) => ({ id, count: count as number }))
      .sort((a, b) => b.count - a.count)
      .slice(0, 5);
    setPopular(sorted);
  }, []);

  if (popular.length === 0) return null;

  return (
    <div className="mb-4 p-4 bg-amber-50 dark:bg-amber-900/20 rounded-lg border border-amber-200 dark:border-amber-800">
      <h3 className="text-sm font-medium text-amber-800 dark:text-amber-300 mb-2">🔥 熱門症狀</h3>
      <div className="flex flex-wrap gap-2">
        {popular.map(({ id }) => {
          const symptom = symptoms.find(s => s.id === id);
          if (!symptom) return null;
          return (
            <button
              key={id}
              onClick={() => onSelect(id)}
              className="px-3 py-1 bg-amber-100 dark:bg-amber-900/40 text-amber-800 dark:text-amber-200 rounded-full text-sm hover:bg-amber-200 dark:hover:bg-amber-900/60 transition-colors"
            >
              {symptom.names[locale]}
            </button>
          );
        })}
      </div>
    </div>
  );
}

function RecommendationView({ 
  symptom, 
  onBack 
}: { 
  symptom: Symptom; 
  onBack: () => void;
}) {
  const { locale } = useLocale();

  return (
    <div className="space-y-6">
      <button
        onClick={onBack}
        className="text-emerald-600 dark:text-emerald-400 hover:text-emerald-700 dark:hover:text-emerald-300 font-medium"
      >
        ← 返回
      </button>

      <div className="bg-white dark:bg-gray-800 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 p-6">
        <h2 className="text-xl font-semibold mb-2 text-gray-800 dark:text-gray-200">
          {symptom.names[locale]}
        </h2>
        <p className="text-gray-600 dark:text-gray-400 mb-4">推薦補充品</p>

        <div className="space-y-3">
          {symptom.recommendations.map((rec, idx) => (
            <div 
              key={idx}
              className="flex items-center gap-3 p-3 bg-emerald-50 dark:bg-emerald-900/30 rounded-lg"
            >
              <span className="text-emerald-600 dark:text-emerald-400">✓</span>
              <span className="font-medium text-gray-800 dark:text-gray-200">{rec.name[locale]}</span>
            </div>
          ))}
        </div>

        <a
          href={symptom.iherb_category.url}
          target="_blank"
          rel="noopener noreferrer"
          className="block mt-6 text-center py-3 bg-emerald-600 text-white rounded-lg font-medium hover:bg-emerald-700 transition-colors"
        >
          去iHerb睇 →
        </a>
      </div>

      <p className="text-sm text-gray-500 dark:text-gray-400 bg-yellow-50 dark:bg-yellow-900/20 p-3 rounded-lg">
        ⚠️ 本網站提供資訊僅供參考，不構成醫療建議。使用前請諮詢醫生。
      </p>
    </div>
  );
}

function MainContent() {
  const { locale } = useLocale();
  const [selectedSymptoms, setSelectedSymptoms] = useState<Symptom[]>([]);
  const [view, setView] = useState<'select' | 'recommend'>('select');
  const [searchQuery, setSearchQuery] = useState('');
  const [searchHistory, setSearchHistory] = useState<string[]>([]);

  // Load search history
  useEffect(() => {
    setSearchHistory(getSearchHistory());
  }, []);

  const filteredSymptoms = useMemo(() => {
    if (!searchQuery.trim()) return symptoms;
    
    const fuse = new Fuse(symptoms, {
      keys: [
        { name: 'names.zh-HK', weight: 2 },
        { name: 'names.zh-CN', weight: 2 },
        { name: 'names.en', weight: 1 },
        { name: 'id', weight: 0.5 }
      ],
      threshold: 0.4,
      includeScore: true,
      minMatchCharLength: 1,
    });
    
    const results = fuse.search(searchQuery);
    addToHistory(searchQuery);
    setSearchHistory(getSearchHistory());
    return results.map(r => r.item);
  }, [searchQuery]);

  const handleSymptomClick = useCallback((symptom: Symptom) => {
    incrementPopular(symptom.id);
    setSelectedSymptoms([symptom]);
    setView('recommend');
  }, []);

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
    return <RecommendationView symptom={selectedSymptoms[0]} onBack={handleBack} />;
  }

  return (
    <div className="space-y-6">
      <SearchBar 
        onSearch={setSearchQuery} 
        showHistory={searchHistory}
        onClearHistory={handleClearHistory}
      />
      
      {searchQuery && (
        <p className="text-sm text-gray-500 dark:text-gray-400">
          搵到 {filteredSymptoms.length} 個症狀
        </p>
      )}

      {!searchQuery && <PopularSymptoms onSelect={handleSelectFromPopular} />}

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3">
        {filteredSymptoms.map((symptom) => (
          <SymptomCard
            key={symptom.id}
            symptom={symptom}
            isSelected={selectedSymptoms.includes(symptom)}
            onClick={() => handleSymptomClick(symptom)}
          />
        ))}
      </div>

      {filteredSymptoms.length === 0 && (
        <p className="text-center text-gray-500 dark:text-gray-400 py-8">
          搵唔到相關症狀
        </p>
      )}

      <p className="text-sm text-gray-500 dark:text-gray-400 bg-yellow-50 dark:bg-yellow-900/20 p-3 rounded-lg">
        ⚠️ 本網站提供資訊僅供參考，不構成醫療建議。使用前請諮詢醫生。
      </p>
    </div>
  );
}

function AppContent() {
  // Initialize dark mode
  useEffect(() => {
    document.documentElement.classList.toggle('dark', isDarkMode());
  }, []);

  const [locale] = useState<Locale>('zh-HK');

  return (
    <LocaleProvider locale={locale}>
      <div className="min-h-screen bg-gradient-to-br from-emerald-50 to-teal-50 dark:from-gray-900 dark:to-gray-800 transition-colors">
        <header className="bg-white dark:bg-gray-900 shadow-sm sticky top-0 z-10">
          <div className="max-w-4xl mx-auto px-4 py-4 flex justify-between items-center">
            <h1 className="text-2xl font-bold text-emerald-700 dark:text-emerald-400">
              SuppMatch
            </h1>
            <div className="flex gap-2 items-center">
              <ThemeToggle />
              <LanguageSelector />
            </div>
          </div>
        </header>

        <main className="max-w-4xl mx-auto px-4 py-8">
          <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-lg p-6 md:p-8">
            <h2 className="text-3xl font-semibold text-gray-800 dark:text-gray-200 mb-2">
              SuppMatch
            </h2>
            <p className="text-gray-600 dark:text-gray-400 mb-8 text-lg">
              症狀揀選 → 營養補充品推薦
            </p>

            <MainContent />
          </div>
        </main>

        <footer className="text-center py-6 text-gray-500 dark:text-gray-400 text-sm">
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
