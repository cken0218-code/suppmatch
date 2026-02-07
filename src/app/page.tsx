'use client';
// Updated: 2026-02-08 - Added search functionality

import { useState, useMemo } from 'react';
import { LocaleProvider, useLocale, type Locale } from '@/contexts/LocaleContext';
import { symptoms, type Symptom } from '@/data/symptoms';

// Group symptoms by first letter for easier display
function groupSymptomsByCategory(symptoms: Symptom[]) {
  const categories: Record<string, Symptom[]> = {};
  symptoms.forEach(symptom => {
    // Simple categorization based on id prefix
    const category = symptom.id.split('-')[0];
    if (!categories[category]) {
      categories[category] = [];
    }
    categories[category].push(symptom);
  });
  return categories;
}

function LanguageSelector() {
  const { locale, setLocale, t } = useLocale();
  
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
          className={`px-2 py-1 rounded text-sm ${
            locale === l 
              ? 'bg-emerald-600 text-white' 
              : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
          }`}
        >
          {flags[l]}
        </button>
      ))}
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
  const name = symptom.names[locale];

  return (
    <button
      onClick={onClick}
      className={`p-4 rounded-lg border-2 text-left transition-all ${
        isSelected
          ? 'border-emerald-500 bg-emerald-50'
          : 'border-gray-200 hover:border-emerald-300 hover:bg-gray-50'
      }`}
    >
      <span className="text-lg font-medium">{name}</span>
    </button>
  );
}

function SearchBar({ 
  onSearch 
}: { 
  onSearch: (query: string) => void 
}) {
  return (
    <div className="relative">
      <input
        type="text"
        placeholder="搜尋症狀..."
        onChange={(e) => onSearch(e.target.value)}
        className="w-full px-4 py-3 pl-10 border-2 border-gray-200 rounded-lg focus:border-emerald-500 focus:outline-none text-lg"
      />
      <svg 
        className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400"
        fill="none" 
        stroke="currentColor" 
        viewBox="0 0 24 24"
      >
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
      </svg>
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
        className="text-emerald-600 hover:text-emerald-700 font-medium"
      >
        ← 返回
      </button>

      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
        <h2 className="text-xl font-semibold mb-2">
          {symptom.names[locale]}
        </h2>
        <p className="text-gray-600 mb-4">推薦補充品</p>

        <div className="space-y-3">
          {symptom.recommendations.map((rec, idx) => (
            <div 
              key={idx}
              className="flex items-center gap-3 p-3 bg-emerald-50 rounded-lg"
            >
              <span className="text-emerald-600">✓</span>
              <span className="font-medium">{rec.name[locale]}</span>
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

      <p className="text-sm text-gray-500 bg-yellow-50 p-3 rounded-lg">
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

  const filteredSymptoms = useMemo(() => {
    if (!searchQuery.trim()) return symptoms;
    const query = searchQuery.toLowerCase();
    return symptoms.filter(s => 
      s.names[locale]?.toLowerCase().includes(query) ||
      s.names['zh-HK']?.toLowerCase().includes(query) ||
      s.names['zh-CN']?.toLowerCase().includes(query) ||
      s.names['en']?.toLowerCase().includes(query) ||
      s.id.toLowerCase().includes(query)
    );
  }, [searchQuery, locale]);

  const handleSymptomClick = (symptom: Symptom) => {
    setSelectedSymptoms([symptom]);
    setView('recommend');
  };

  const handleBack = () => {
    setView('select');
    setSelectedSymptoms([]);
  };

  if (view === 'recommend' && selectedSymptoms.length > 0) {
    return (
      <RecommendationView 
        symptom={selectedSymptoms[0]} 
        onBack={handleBack}
      />
    );
  }

  return (
    <div className="space-y-6">
      <SearchBar onSearch={setSearchQuery} />
      
      {searchQuery && (
        <p className="text-sm text-gray-500">
          搵到 {filteredSymptoms.length} 個症狀
        </p>
      )}

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
        <p className="text-center text-gray-500 py-8">
          搵唔到相關症狀
        </p>
      )}

      <p className="text-sm text-gray-500 bg-yellow-50 p-3 rounded-lg">
        ⚠️ 本網站提供資訊僅供參考，不構成醫療建議。使用前請諮詢醫生。
      </p>
    </div>
  );
}

function AppContent() {
  const [locale] = useState<Locale>('zh-HK');

  return (
    <LocaleProvider locale={locale}>
      <div className="min-h-screen bg-gradient-to-br from-emerald-50 to-teal-50">
        <header className="bg-white shadow-sm sticky top-0 z-10">
          <div className="max-w-4xl mx-auto px-4 py-4 flex justify-between items-center">
            <h1 className="text-2xl font-bold text-emerald-700">
              SuppMatch
            </h1>
            <LanguageSelector />
          </div>
        </header>

        <main className="max-w-4xl mx-auto px-4 py-8">
          <div className="bg-white rounded-2xl shadow-lg p-6 md:p-8">
            <h2 className="text-3xl font-semibold text-gray-800 mb-2">
              SuppMatch
            </h2>
            <p className="text-gray-600 mb-8 text-lg">
              症狀揀選 → 營養補充品推薦
            </p>

            <MainContent />
          </div>
        </main>

        <footer className="text-center py-6 text-gray-500 text-sm">
          <p>© 2025 SuppMatch. ⚠️ 本網站提供資訊僅供參考，不構成醫療建議。使用前請諮詢醫生。</p>
        </footer>
      </div>
    </LocaleProvider>
  );
}

export default function Home() {
  return <AppContent />;
}
