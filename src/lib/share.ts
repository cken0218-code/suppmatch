import type { Symptom } from '@/data/symptoms';

export function buildShareQuery(symptomIds: string[]): string {
  if (symptomIds.length === 0) return '';
  const params = new URLSearchParams();
  params.set('s', symptomIds.join(','));
  return `?${params.toString()}`;
}

export function parseShareQuery(search: string): string[] {
  try {
    const q = search.startsWith('?') ? search.slice(1) : search;
    const params = new URLSearchParams(q);
    const raw = params.get('s');
    if (!raw) return [];
    return raw
      .split(',')
      .map((id) => id.trim())
      .filter(Boolean);
  } catch {
    return [];
  }
}

export function buildShareUrl(symptomIds: string[]): string {
  if (typeof window === 'undefined') return '';
  const base = `${window.location.origin}${window.location.pathname}`;
  return `${base}${buildShareQuery(symptomIds)}`;
}

export function buildShareText(
  symptoms: Symptom[],
  supplementNames: string[],
  locale: 'zh-HK' | 'zh-CN' | 'en',
): string {
  const symptomLine = symptoms.map((s) => s.names[locale]).join(locale === 'en' ? ', ' : '、');
  const suppLine = supplementNames.join(locale === 'en' ? ', ' : '、');
  if (locale === 'en') {
    return `My SuppMatch picks\nSymptoms: ${symptomLine}\nSupplements to consider: ${suppLine}\n(For reference only — not medical advice)`;
  }
  if (locale === 'zh-CN') {
    return `我的 SuppMatch 推荐\n症状：${symptomLine}\n建议关注的补充品：${suppLine}\n（仅供参考，不构成医疗建议）`;
  }
  return `我嘅 SuppMatch 推薦\n症狀：${symptomLine}\n建議關注嘅補充品：${suppLine}\n（僅供參考，不構成醫療建議）`;
}

export async function shareResults(opts: {
  title: string;
  text: string;
  url: string;
}): Promise<'shared' | 'copied' | 'failed'> {
  try {
    if (typeof navigator !== 'undefined' && navigator.share) {
      await navigator.share({
        title: opts.title,
        text: opts.text,
        url: opts.url,
      });
      return 'shared';
    }
  } catch (err) {
    // User cancelled share sheet
    if (err instanceof Error && err.name === 'AbortError') return 'failed';
  }

  try {
    const payload = `${opts.text}\n${opts.url}`;
    await navigator.clipboard.writeText(payload);
    return 'copied';
  } catch {
    return 'failed';
  }
}

export async function copyText(text: string): Promise<boolean> {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch {
    return false;
  }
}
