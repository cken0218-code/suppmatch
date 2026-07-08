import { symptoms, type Symptom } from '@/data/symptoms';

/** Keyword → symptom id boosts for natural-language matching */
const KEYWORD_MAP: Array<{ keys: string[]; symptomIds: string[]; weight?: number }> = [
  { keys: ['失眠', '瞓唔着', '睡不着', '睡不好', '睡眠', 'insomnia', 'sleep', "can't sleep", 'cant sleep'], symptomIds: ['insomnia'] },
  { keys: ['攰', '疲劳', '疲勞', '冇精神', '没精神', '累', 'fatigue', 'tired', 'exhausted', 'low energy'], symptomIds: ['fatigue'] },
  { keys: ['頭痛', '头疼', '偏頭痛', 'headache', 'migraine'], symptomIds: ['headache'] },
  { keys: ['壓力', '压力', '焦慮', '焦虑', '緊張', 'stress', 'anxiety', 'anxious'], symptomIds: ['stress-anxiety'] },
  { keys: ['脫髮', '脱发', '甩頭髮', '掉发', 'hair loss', 'hair fall', 'bald'], symptomIds: ['hair-loss'] },
  { keys: ['消化', '腸胃', '肠胃', '肚痛', '胃胀', '脹氣', 'digest', 'bloating', 'stomach', 'gut'], symptomIds: ['digestive-issues'] },
  { keys: ['眼睛', '視力', '视力', '眼乾', 'eye', 'vision', 'screen'], symptomIds: ['eye-strain'] },
  { keys: ['免疫', '成日病', '容易病', '感冒', 'immune', 'immunity', 'catch cold'], symptomIds: ['weak-immunity'] },
  { keys: ['關節', '关节', '骨痛', '膝', 'joint', 'bone pain', 'arthritis'], symptomIds: ['bone-joint-pain'] },
  { keys: ['皮膚', '皮肤', '暗瘡', 'acne', 'skin'], symptomIds: ['skin-problems'] },
  { keys: ['經期', '经期', '生理痛', '月經', 'menstrual', 'period pain', 'pms'], symptomIds: ['menstrual-issues'] },
  { keys: ['過敏', '过敏', '花粉', 'allerg', 'hay fever'], symptomIds: ['allergies'] },
  { keys: ['減肥', '减重', '體重', 'weight', 'lose weight'], symptomIds: ['weight-management'] },
  { keys: ['記性', '记忆', '腦霧', 'memory', 'brain fog', 'focus', 'concentrat'], symptomIds: ['memory-issues'] },
  { keys: ['心臟', '心脏', '心悸', 'heart', 'cardio'], symptomIds: ['heart-health'] },
];

export interface ChatMatch {
  symptom: Symptom;
  score: number;
  matchedKeys: string[];
}

export interface ChatParseResult {
  matches: ChatMatch[];
  /** Symptoms ordered for recommendation */
  symptoms: Symptom[];
  /** Short explanation keys for UI */
  notes: string[];
}

function normalize(text: string): string {
  return text.toLowerCase().replace(/\s+/g, ' ').trim();
}

/**
 * Rule-based NL parser (no external AI API).
 * Works offline for common Cantonese / Chinese / English phrases.
 */
export function parseNaturalLanguage(input: string): ChatParseResult {
  const text = normalize(input);
  if (!text) return { matches: [], symptoms: [], notes: ['empty'] };

  const scores = new Map<string, { score: number; keys: string[] }>();

  for (const row of KEYWORD_MAP) {
    const weight = row.weight ?? 1;
    for (const key of row.keys) {
      const k = key.toLowerCase();
      if (text.includes(k)) {
        for (const id of row.symptomIds) {
          const cur = scores.get(id) || { score: 0, keys: [] };
          cur.score += weight * (k.length >= 4 ? 2 : 1);
          if (!cur.keys.includes(key)) cur.keys.push(key);
          scores.set(id, cur);
        }
      }
    }
  }

  // Also fuzzy-match symptom names directly
  for (const s of symptoms) {
    const names = [s.names['zh-HK'], s.names['zh-CN'], s.names.en, s.id.replace(/-/g, ' ')];
    for (const n of names) {
      const nn = n.toLowerCase();
      if (nn.length >= 2 && text.includes(nn)) {
        const cur = scores.get(s.id) || { score: 0, keys: [] };
        cur.score += 3;
        if (!cur.keys.includes(n)) cur.keys.push(n);
        scores.set(s.id, cur);
      }
    }
  }

  // Multi-complaint boost: "又" / "and" / "同埋"
  if (/又|同埋|而且|and | also |,|，|、/.test(text) && scores.size >= 2) {
    for (const [id, v] of scores) {
      scores.set(id, { ...v, score: v.score + 0.5 });
    }
  }

  const matches: ChatMatch[] = [...scores.entries()]
    .map(([id, v]) => {
      const symptom = symptoms.find((s) => s.id === id);
      if (!symptom) return null;
      return { symptom, score: v.score, matchedKeys: v.keys };
    })
    .filter((m): m is ChatMatch => Boolean(m))
    .sort((a, b) => b.score - a.score)
    .slice(0, 8);

  const notes: string[] = [];
  if (matches.length === 0) notes.push('no_match');
  else notes.push('matched');
  if (matches.length >= 2) notes.push('multi');

  return {
    matches,
    symptoms: matches.map((m) => m.symptom),
    notes,
  };
}

export const CHAT_EXAMPLES = [
  { 'zh-HK': '我近排好攰，又失眠', 'zh-CN': '我最近很累，又失眠', en: "I've been tired and can't sleep" },
  { 'zh-HK': '成日頭痛同壓力好大', 'zh-CN': '经常头痛而且压力很大', en: 'Frequent headaches and high stress' },
  { 'zh-HK': '脫髮同腸胃唔舒服', 'zh-CN': '脱发和肠胃不舒服', en: 'Hair loss and stomach discomfort' },
];
