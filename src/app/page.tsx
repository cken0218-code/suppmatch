'use client';

import { useCallback, useEffect, useState } from 'react';
import { LocaleProvider, useLocale } from '@/contexts/LocaleContext';
import { Header } from '@/components/Header';
import { ModePicker, type EntryMode } from '@/components/ModePicker';
import { SymptomSelector } from '@/components/SymptomSelector';
import { GuidedWizard } from '@/components/GuidedWizard';
import { ChatRecommend } from '@/components/ChatRecommend';
import { RecommendationView } from '@/components/RecommendationView';
import { FavoritesView } from '@/components/FavoritesView';
import { PriceWatchView } from '@/components/PriceWatchView';
import { ContentStudio } from '@/components/ContentStudio';
import { symptoms, type Symptom } from '@/data/symptoms';
import { favoritesCount } from '@/data/favorites';
import { parseShareQuery } from '@/lib/share';

type View =
  | 'home'
  | 'quick'
  | 'guided'
  | 'chat'
  | 'recommend'
  | 'favorites'
  | 'price'
  | 'content';

function AppShell() {
  const { t } = useLocale();
  const [view, setView] = useState<View>('home');
  const [selectedSymptoms, setSelectedSymptoms] = useState<Symptom[]>([]);
  const [favCount, setFavCount] = useState(0);

  const refreshFavCount = useCallback(() => {
    setFavCount(favoritesCount());
  }, []);

  const goRecommend = useCallback((list: Symptom[]) => {
    setSelectedSymptoms(list);
    setView('recommend');
  }, []);

  useEffect(() => {
    const ids = parseShareQuery(window.location.search);
    if (ids.length === 0) return;
    const matched = ids
      .map((id) => symptoms.find((s) => s.id === id))
      .filter((s): s is Symptom => Boolean(s));
    if (matched.length > 0) {
      setSelectedSymptoms(matched);
      setView('recommend');
    }
  }, []);

  useEffect(() => {
    refreshFavCount();
  }, [view, refreshFavCount]);

  const handleBackHome = useCallback(() => {
    setView('home');
    setSelectedSymptoms([]);
    if (window.location.search) {
      window.history.replaceState({}, '', window.location.pathname);
    }
  }, []);

  const handleMode = (mode: EntryMode) => {
    if (mode === 'quick') setView('quick');
    else if (mode === 'guided') setView('guided');
    else setView('chat');
  };

  useEffect(() => {
    function handleKeyDown(e: KeyboardEvent) {
      if (e.key === 'Escape' && view !== 'home') {
        handleBackHome();
      }
      if (e.key === '/' && document.activeElement?.tagName !== 'INPUT' && view === 'quick') {
        e.preventDefault();
        document.querySelector<HTMLInputElement>('input[type="text"]')?.focus();
      }
    }
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [view, handleBackHome]);

  const showHero = view === 'home';

  return (
    <div className="min-h-screen bg-surface text-zinc-200 flex flex-col">
      <Header
        onOpenFavorites={() => {
          refreshFavCount();
          setView('favorites');
        }}
        favoritesCount={favCount}
      />

      <main className="flex-1 max-w-4xl w-full mx-auto px-4 py-8">
        {showHero && (
          <div className="text-center mb-8 px-2">
            <h2 className="text-2xl sm:text-3xl md:text-4xl font-bold mb-3 leading-tight bg-gradient-to-r from-white via-zinc-200 to-accent-purple bg-clip-text text-transparent">
              {t('app.subtitle')}
            </h2>
            <p className="text-zinc-500 text-sm sm:text-base max-w-xl mx-auto">{t('app.description')}</p>
          </div>
        )}

        <div className="bg-surface-card rounded-3xl border border-surface-border p-5 sm:p-6 md:p-8 shadow-2xl shadow-black/20">
          {view === 'home' && (
            <ModePicker
              onSelect={handleMode}
              onOpenFavorites={() => setView('favorites')}
              onOpenPriceWatch={() => setView('price')}
              onOpenContent={() => setView('content')}
              favoritesCount={favCount}
            />
          )}

          {view === 'quick' && (
            <div className="space-y-4">
              <button
                type="button"
                onClick={handleBackHome}
                className="text-sm text-zinc-500 hover:text-white transition-colors"
              >
                ← {t('mode.backHome')}
              </button>
              <SymptomSelector onRecommend={goRecommend} />
            </div>
          )}

          {view === 'guided' && (
            <GuidedWizard onCancel={handleBackHome} onComplete={(list) => goRecommend(list)} />
          )}

          {view === 'chat' && (
            <ChatRecommend onCancel={handleBackHome} onComplete={goRecommend} />
          )}

          {view === 'recommend' && selectedSymptoms.length > 0 && (
            <RecommendationView
              symptoms={selectedSymptoms}
              onBack={() => {
                refreshFavCount();
                handleBackHome();
              }}
            />
          )}

          {view === 'favorites' && (
            <FavoritesView
              onBack={() => {
                refreshFavCount();
                setView('home');
              }}
            />
          )}

          {view === 'price' && <PriceWatchView onBack={() => setView('home')} />}

          {view === 'content' && <ContentStudio onBack={() => setView('home')} />}
        </div>
      </main>

      <footer className="text-center py-6 text-zinc-500 text-sm space-y-1">
        <p>© 2026 SuppMatch. {t('disclaimer')}</p>
        <p className="text-xs">{t('footer.shortcuts')}</p>
      </footer>
    </div>
  );
}

export default function Home() {
  return (
    <LocaleProvider locale="zh-HK">
      <AppShell />
    </LocaleProvider>
  );
}
