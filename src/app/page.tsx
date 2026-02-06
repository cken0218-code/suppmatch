'use client';

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
  const { locale, t } = useLocale();
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

function RecommendationView({ 
  symptom, 
  onBack 
}: { 
  symptom: Symptom; 
  onBack: () => void;
}) {
  const { locale, t } = useLocale();

  return (
    <div className="space-y-6">
      <button
        onClick={onBack}
        className="text-emerald-600 hover:text-emerald-700 font-medium"
      >
        ← {t('button.back')}
      </button>

      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
        <h2 className="text-xl font-semibold mb-2">
          {symptom.names[locale]}
        </h2>
        <p className="text-gray-600 mb-4">{t('recommendation.description')}</p>

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
          {t('iherb.link')} → 
        </a>
      </div>

      <p className="text-sm text-gray-500 bg-yellow-50 p-3 rounded-lg">
        {t('disclaimer')}
      </p>
    </div>
  );
}

function MainContent() {
  const { locale, t } = useLocale();
  const [selectedSymptoms, setSelectedSymptoms] = useState<Symptom[]>([]);
  const [view, setView] = useState<'select' | 'recommend'>('select');

  const groupedSymptoms = useMemo(() => 
    groupSymptomsByCategory(symptoms), 
  []);

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
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3">
        {symptoms.map((symptom) => (
          <SymptomCard
            key={symptom.id}
            symptom={symptom}
            isSelected={selectedSymptoms.includes(symptom)}
            onClick={() => handleSymptomClick(symptom)}
          />
        ))}
      </div>

      <p className="text-sm text-gray-500 bg-yellow-50 p-3 rounded-lg">
        {t('disclaimer')}
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
          <p>© 2025 SuppMatch. {useLocale().t('disclaimer')}</p>
        </footer>
      </div>
    </LocaleProvider>
  );
}

export default function Home() {
  return <AppContent />;
}
