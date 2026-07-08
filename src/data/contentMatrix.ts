import type { LocaleText } from '@/data/evidence';
import { symptoms } from '@/data/symptoms';
import { siteConfig } from '@/data/seo';
import { symptomPath, type AppLocale } from '@/lib/i18n-routing';

export type ContentChannel = 'xiaohongshu' | 'youtube' | 'threads' | 'ig';

export interface ContentIdea {
  id: string;
  channel: ContentChannel;
  symptomId: string;
  title: LocaleText;
  caption: LocaleText;
  hooks: LocaleText[];
  cta: LocaleText;
}

const TOP_SYMPTOMS = [
  'insomnia',
  'fatigue',
  'stress-anxiety',
  'hair-loss',
  'digestive-issues',
  'headache',
  'weak-immunity',
  'eye-strain',
  'bone-joint-pain',
  'skin-problems',
];

function ideaFor(
  symptomId: string,
  channel: ContentChannel,
  extra?: Partial<ContentIdea>,
): ContentIdea | null {
  const s = symptoms.find((x) => x.id === symptomId);
  if (!s) return null;
  const recs = s.recommendations
    .slice(0, 3)
    .map((r) => r.name['zh-HK'])
    .join('、');
  const recsCN = s.recommendations
    .slice(0, 3)
    .map((r) => r.name['zh-CN'])
    .join('、');
  const recsEN = s.recommendations
    .slice(0, 3)
    .map((r) => r.name.en)
    .join(', ');

  const base: ContentIdea = {
    id: `${channel}-${symptomId}`,
    channel,
    symptomId,
    title: {
      'zh-HK': `${s.names['zh-HK']}食咩保健品？`,
      'zh-CN': `${s.names['zh-CN']}吃什么保健品？`,
      en: `Supplements people discuss for ${s.names.en}`,
    },
    caption: {
      'zh-HK': `最近好多人都會搜「${s.names['zh-HK']}」……\n\n常見會被提到：${recs}\n\n⚠️ 唔係醫療建議，只係整理公開資訊同購物參考。\n有長期症狀請睇醫生。\n\n🔗 完整對照：`,
      'zh-CN': `最近很多人会搜「${s.names['zh-CN']}」……\n\n常见会提到：${recsCN}\n\n⚠️ 不是医疗建议，只是整理公开信息与购物参考。\n有长期症状请看医生。\n\n🔗 完整对照：`,
      en: `People often search about ${s.names.en}…\n\nCommonly discussed: ${recsEN}\n\n⚠️ Not medical advice — educational shopping reference only.\nSee a clinician for ongoing symptoms.\n\n🔗 Full guide:`,
    },
    hooks: [
      {
        'zh-HK': `3 個關於「${s.names['zh-HK']}」成日被問嘅補充品`,
        'zh-CN': `3 个关于「${s.names['zh-CN']}」常被问的补充品`,
        en: `3 supplements often asked about for ${s.names.en}`,
      },
      {
        'zh-HK': `唔好亂堆！先了解呢幾個方向`,
        'zh-CN': `不要乱堆！先了解这几个方向`,
        en: `Don’t stack randomly — start with these angles`,
      },
    ],
    cta: {
      'zh-HK': '留言「指南」送你對照連結（或直接點 bio）',
      'zh-CN': '留言「指南」获取对照链接（或点主页）',
      en: 'Comment GUIDE or tap the link in bio',
    },
    ...extra,
  };
  return base;
}

export function getContentMatrix(): ContentIdea[] {
  const channels: ContentChannel[] = ['xiaohongshu', 'youtube', 'threads', 'ig'];
  const out: ContentIdea[] = [];
  for (const id of TOP_SYMPTOMS) {
    for (const ch of channels) {
      const idea = ideaFor(id, ch);
      if (idea) out.push(idea);
    }
  }
  return out;
}

export function contentLandingUrl(locale: AppLocale, symptomId: string): string {
  return `${siteConfig.url}${symptomPath(locale, symptomId)}`;
}

export const channelLabels: Record<ContentChannel, LocaleText> = {
  xiaohongshu: { 'zh-HK': '小紅書', 'zh-CN': '小红书', en: 'Xiaohongshu' },
  youtube: { 'zh-HK': 'YouTube', 'zh-CN': 'YouTube', en: 'YouTube' },
  threads: { 'zh-HK': 'Threads', 'zh-CN': 'Threads', en: 'Threads' },
  ig: { 'zh-HK': 'Instagram', 'zh-CN': 'Instagram', en: 'Instagram' },
};
