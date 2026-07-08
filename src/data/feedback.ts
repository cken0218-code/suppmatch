export interface FeedbackEntry {
  /** supplement EN key or combo id */
  key: string;
  label: string;
  /** 1 = not helpful, 2 = ok, 3 = helpful — experience only, not medical efficacy */
  rating: 1 | 2 | 3;
  comment?: string;
  createdAt: number;
}

const KEY = 'suppmatch_feedback';

export function getFeedback(): FeedbackEntry[] {
  if (typeof window === 'undefined') return [];
  try {
    return JSON.parse(localStorage.getItem(KEY) || '[]');
  } catch {
    return [];
  }
}

function persist(items: FeedbackEntry[]) {
  localStorage.setItem(KEY, JSON.stringify(items.slice(0, 200)));
}

export function addFeedback(entry: Omit<FeedbackEntry, 'createdAt'>): void {
  const list = getFeedback().filter((f) => f.key !== entry.key);
  list.unshift({ ...entry, createdAt: Date.now() });
  persist(list);
}

export function getFeedbackFor(key: string): FeedbackEntry | undefined {
  return getFeedback().find((f) => f.key === key.toLowerCase());
}

export function feedbackSummary(key: string): { count: number; avg: number } {
  const items = getFeedback().filter((f) => f.key === key.toLowerCase());
  if (items.length === 0) return { count: 0, avg: 0 };
  const avg = items.reduce((s, i) => s + i.rating, 0) / items.length;
  return { count: items.length, avg };
}
