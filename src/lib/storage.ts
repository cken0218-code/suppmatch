export const STORAGE_KEYS = {
  POPULAR: 'suppmatch_popular',
  HISTORY: 'suppmatch_history',
  LOCALE: 'suppmatch-locale',
  PROFILE: 'suppmatch_profile',
} as const;

export interface UserProfile {
  age?: string;
  gender?: string;
  /** User is currently on medication — show caution only, never medical advice */
  onMedication?: boolean;
}

export function getPopularSymptoms(): Record<string, number> {
  if (typeof window === 'undefined') return {};
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEYS.POPULAR) || '{}');
  } catch {
    return {};
  }
}

export function incrementPopular(symptomId: string) {
  const popular = getPopularSymptoms();
  popular[symptomId] = (popular[symptomId] || 0) + 1;
  localStorage.setItem(STORAGE_KEYS.POPULAR, JSON.stringify(popular));
}

export function getSearchHistory(): string[] {
  if (typeof window === 'undefined') return [];
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEYS.HISTORY) || '[]');
  } catch {
    return [];
  }
}

export function addToHistory(query: string) {
  if (!query.trim()) return;
  const history = getSearchHistory();
  const newHistory = [query, ...history.filter((h) => h !== query)].slice(0, 10);
  localStorage.setItem(STORAGE_KEYS.HISTORY, JSON.stringify(newHistory));
}

export function clearHistory() {
  localStorage.removeItem(STORAGE_KEYS.HISTORY);
}

export function getUserProfile(): UserProfile {
  if (typeof window === 'undefined') return {};
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEYS.PROFILE) || '{}');
  } catch {
    return {};
  }
}

export function saveUserProfile(profile: UserProfile) {
  localStorage.setItem(STORAGE_KEYS.PROFILE, JSON.stringify(profile));
}