// Favorites feature - save and manage favorite supplements
// Added: 2026-02-21

export interface FavoriteItem {
  symptomId: string;
  supplementName: string;
  addedAt: number;
}

const FAVORITES_KEY = 'suppmatch_favorites';

export function getFavorites(): FavoriteItem[] {
  if (typeof window === 'undefined') return [];
  try {
    return JSON.parse(localStorage.getItem(FAVORITES_KEY) || '[]');
  } catch {
    return [];
  }
}

export function addFavorite(symptomId: string, supplementName: string): void {
  const favorites = getFavorites();
  const exists = favorites.some(
    f => f.symptomId === symptomId && f.supplementName === supplementName
  );
  if (!exists) {
    favorites.push({ symptomId, supplementName, addedAt: Date.now() });
    localStorage.setItem(FAVORITES_KEY, JSON.stringify(favorites));
  }
}

export function removeFavorite(symptomId: string, supplementName: string): void {
  const favorites = getFavorites().filter(
    f => !(f.symptomId === symptomId && f.supplementName === supplementName)
  );
  localStorage.setItem(FAVORITES_KEY, JSON.stringify(favorites));
}

export function clearFavorites(): void {
  localStorage.removeItem(FAVORITES_KEY);
}

export function isFavorite(symptomId: string, supplementName: string): boolean {
  return getFavorites().some(
    f => f.symptomId === symptomId && f.supplementName === supplementName
  );
}
