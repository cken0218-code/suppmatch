export interface WatchedProduct {
  id: string;
  name: string;
  nameZh: string;
  brand: string;
  priceRange: string;
  iherbUrl: string;
  amazonUrl: string;
  note?: string;
  addedAt: number;
  /** User's target "want under" note (free text, e.g. "$15") */
  targetPrice?: string;
}

const KEY = 'suppmatch_price_watch';

export function getWatchlist(): WatchedProduct[] {
  if (typeof window === 'undefined') return [];
  try {
    return JSON.parse(localStorage.getItem(KEY) || '[]');
  } catch {
    return [];
  }
}

function persist(items: WatchedProduct[]) {
  localStorage.setItem(KEY, JSON.stringify(items));
}

export function isWatched(productId: string): boolean {
  return getWatchlist().some((w) => w.id === productId);
}

export function addToWatchlist(item: Omit<WatchedProduct, 'addedAt'>): void {
  const list = getWatchlist().filter((w) => w.id !== item.id);
  list.unshift({ ...item, addedAt: Date.now() });
  persist(list.slice(0, 50));
}

export function removeFromWatchlist(productId: string): void {
  persist(getWatchlist().filter((w) => w.id !== productId));
}

export function updateWatchNote(productId: string, note: string, targetPrice?: string): void {
  const list = getWatchlist().map((w) =>
    w.id === productId ? { ...w, note, targetPrice: targetPrice ?? w.targetPrice } : w,
  );
  persist(list);
}

export function buildPriceAlertMailto(items: WatchedProduct[], locale: string): string {
  const subject =
    locale === 'en'
      ? 'SuppMatch price watch list'
      : locale === 'zh-CN'
        ? 'SuppMatch 价格关注列表'
        : 'SuppMatch 價格關注列表';
  const lines = items.map(
    (w, i) =>
      `${i + 1}. ${w.nameZh || w.name} (${w.brand}) — ${w.priceRange}${w.targetPrice ? ` · target ${w.targetPrice}` : ''}\n   iHerb: ${w.iherbUrl}`,
  );
  const body =
    locale === 'en'
      ? `My watched products:\n\n${lines.join('\n\n')}\n\nOpen iHerb to check current prices.`
      : locale === 'zh-CN'
        ? `我关注的产品：\n\n${lines.join('\n\n')}\n\n请打开 iHerb 核对现价。`
        : `我關注嘅產品：\n\n${lines.join('\n\n')}\n\n請打開 iHerb 核對現價。`;
  return `mailto:?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
}

export function buildTelegramShareUrl(text: string): string {
  return `https://t.me/share/url?url=${encodeURIComponent('https://suppmatch.vercel.app')}&text=${encodeURIComponent(text)}`;
}
