// Favorites — save supplements for later

export interface FavoriteItem {
  /** English name (canonical key) */
  supplementKey: string;
  name: {
    'zh-HK': string;
    'zh-CN': string;
    en: string;
  };
  addedAt: number;
  relatedSymptomIds: string[];
}

const FAVORITES_KEY = 'suppmatch_favorites';

export function getFavorites(): FavoriteItem[] {
  if (typeof window === 'undefined') return [];
  try {
    const raw = JSON.parse(localStorage.getItem(FAVORITES_KEY) || '[]') as FavoriteItem[];
    // Migrate legacy { symptomId, supplementName } shape if present
    return raw.map((f) => {
      if ('supplementKey' in f && f.supplementKey) return f;
      const legacy = f as unknown as { symptomId?: string; supplementName?: string; addedAt?: number };
      const key = (legacy.supplementName || '').toLowerCase();
      return {
        supplementKey: key,
        name: { 'zh-HK': legacy.supplementName || '', 'zh-CN': legacy.supplementName || '', en: legacy.supplementName || '' },
        addedAt: legacy.addedAt || Date.now(),
        relatedSymptomIds: legacy.symptomId ? [legacy.symptomId] : [],
      };
    });
  } catch {
    return [];
  }
}

function persist(items: FavoriteItem[]) {
  localStorage.setItem(FAVORITES_KEY, JSON.stringify(items));
}

export function isFavorite(supplementKey: string): boolean {
  const key = supplementKey.toLowerCase();
  return getFavorites().some((f) => f.supplementKey === key);
}

export function toggleFavorite(item: {
  name: { 'zh-HK': string; 'zh-CN': string; en: string };
  relatedSymptomIds?: string[];
}): boolean {
  const key = item.name.en.toLowerCase();
  const favorites = getFavorites();
  const idx = favorites.findIndex((f) => f.supplementKey === key);
  if (idx >= 0) {
    favorites.splice(idx, 1);
    persist(favorites);
    return false;
  }
  favorites.unshift({
    supplementKey: key,
    name: item.name,
    addedAt: Date.now(),
    relatedSymptomIds: item.relatedSymptomIds || [],
  });
  persist(favorites);
  return true;
}

export function removeFavorite(supplementKey: string): void {
  const key = supplementKey.toLowerCase();
  persist(getFavorites().filter((f) => f.supplementKey !== key));
}

export function clearFavorites(): void {
  localStorage.removeItem(FAVORITES_KEY);
}

export function favoritesCount(): number {
  return getFavorites().length;
}
