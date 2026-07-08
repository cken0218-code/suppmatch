import type { UserProfile } from '@/lib/storage';

export interface RankableRecommendation {
  name: { 'zh-HK': string; 'zh-CN': string; en: string };
  /** How many selected symptoms mentioned this supplement */
  symptomCount: number;
  /** Personalization boost score */
  boost: number;
  /** Short label why it was boosted (optional UI) */
  boostReasonKey?: string;
}

/** Keywords that get a boost for certain profiles (matched against EN name, lowercased) */
const FEMALE_BOOST = ['iron', 'folate', 'folic', 'calcium', 'biotin', 'collagen', 'iron'];
const MALE_BOOST = ['zinc', 'magnesium', 'ashwagandha', 'omega', 'fish oil'];
const AGE_55_BOOST = ['vitamin d', 'calcium', 'coq10', 'omega', 'fish oil', 'collagen', 'magnesium'];
const AGE_YOUNG_BOOST = ['vitamin b', 'probiotic', 'zinc', 'magnesium'];

function nameMatches(nameEn: string, keywords: string[]): boolean {
  const n = nameEn.toLowerCase();
  return keywords.some((k) => n.includes(k));
}

/**
 * Score a supplement name against the user profile.
 * Higher boost = show earlier in the list.
 */
export function scoreSupplementForProfile(
  nameEn: string,
  profile: UserProfile,
): { boost: number; reasonKey?: string } {
  let boost = 0;
  let reasonKey: string | undefined;

  if (profile.gender === 'female' && nameMatches(nameEn, FEMALE_BOOST)) {
    boost += 3;
    reasonKey = 'personalize.female';
  }
  if (profile.gender === 'male' && nameMatches(nameEn, MALE_BOOST)) {
    boost += 2;
    reasonKey = reasonKey || 'personalize.male';
  }
  if (profile.age === '55+' && nameMatches(nameEn, AGE_55_BOOST)) {
    boost += 3;
    reasonKey = 'personalize.senior';
  }
  if (
    (profile.age === '18-25' || profile.age === '26-35') &&
    nameMatches(nameEn, AGE_YOUNG_BOOST)
  ) {
    boost += 1;
    reasonKey = reasonKey || 'personalize.young';
  }

  return { boost, reasonKey };
}

/** Sort recommendations: personalization boost first, then multi-symptom frequency */
export function sortRecommendations<T extends RankableRecommendation>(items: T[]): T[] {
  return [...items].sort((a, b) => {
    const scoreA = a.boost * 10 + a.symptomCount;
    const scoreB = b.boost * 10 + b.symptomCount;
    return scoreB - scoreA;
  });
}
