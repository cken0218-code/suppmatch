import type { LocaleText } from '@/data/evidence';

export type InteractionSeverity = 'info' | 'caution' | 'important';

export interface SupplementInteraction {
  /** Match against English names (case-insensitive, substring) */
  a: string;
  b: string;
  severity: InteractionSeverity;
  message: LocaleText;
  tip: LocaleText;
}

/**
 * Educational interaction notes only — not clinical decision support.
 * Matched when BOTH supplements appear in the current recommendation set.
 */
export const interactions: SupplementInteraction[] = [
  {
    a: 'calcium',
    b: 'iron',
    severity: 'caution',
    message: {
      'zh-HK': '鈣同鐵可能互相影響吸收。',
      'zh-CN': '钙与铁可能互相影响吸收。',
      en: 'Calcium and iron may compete for absorption.',
    },
    tip: {
      'zh-HK': '建議唔好同一時間空腹一齊食，可相隔 2 小時。',
      'zh-CN': '建议不要同一时间空腹一起吃，可相隔 2 小时。',
      en: 'Avoid taking together on an empty stomach; space by ~2 hours.',
    },
  },
  {
    a: 'calcium',
    b: 'zinc',
    severity: 'info',
    message: {
      'zh-HK': '高劑量鈣可能影響鋅吸收。',
      'zh-CN': '高剂量钙可能影响锌吸收。',
      en: 'High calcium intake may reduce zinc absorption.',
    },
    tip: {
      'zh-HK': '可分開時段服用，或跟餐按產品說明。',
      'zh-CN': '可分时段服用，或跟餐按产品说明。',
      en: 'Consider separate timing or follow label with meals.',
    },
  },
  {
    a: 'zinc',
    b: 'iron',
    severity: 'info',
    message: {
      'zh-HK': '鋅同鐵同時空腹高劑量可能互相干擾。',
      'zh-CN': '锌与铁同时空腹高剂量可能互相干扰。',
      en: 'High doses of zinc and iron together may interfere with absorption.',
    },
    tip: {
      'zh-HK': '可分餐或分時段。',
      'zh-CN': '可分餐或分时段。',
      en: 'Take at different meals or times when possible.',
    },
  },
  {
    a: 'magnesium',
    b: 'calcium',
    severity: 'info',
    message: {
      'zh-HK': '高劑量鎂同鈣一齊食可能影響彼此吸收。',
      'zh-CN': '高剂量镁与钙一起吃可能影响彼此吸收。',
      en: 'High-dose magnesium and calcium together may reduce absorption of either.',
    },
    tip: {
      'zh-HK': '可早晚分開；劑量不高時多數人可接受。',
      'zh-CN': '可早晚分开；剂量不高时多数人可接受。',
      en: 'Split morning/evening if doses are high; modest doses are often fine together.',
    },
  },
  {
    a: 'fish oil',
    b: 'vitamin e',
    severity: 'info',
    message: {
      'zh-HK': '魚油同高劑量維他命 E 都可能影響凝血。',
      'zh-CN': '鱼油与高剂量维生素 E 都可能影响凝血。',
      en: 'Fish oil and high-dose vitamin E may both affect clotting.',
    },
    tip: {
      'zh-HK': '服用抗凝血藥或手術前請咨詢醫生。',
      'zh-CN': '服用抗凝血药或手术前请咨询医生。',
      en: 'Ask a clinician if on blood thinners or before surgery.',
    },
  },
  {
    a: 'omega',
    b: 'vitamin e',
    severity: 'info',
    message: {
      'zh-HK': 'Omega-3 同高劑量維他命 E 需注意凝血相關風險。',
      'zh-CN': 'Omega-3 与高剂量维生素 E 需注意凝血相关风险。',
      en: 'Omega-3 plus high-dose vitamin E: watch clotting-related risk.',
    },
    tip: {
      'zh-HK': '有相關藥物或手術計劃時先咨詢專業人士。',
      'zh-CN': '有相关药物或手术计划时先咨询专业人士。',
      en: 'Check with a professional if you take related meds or have surgery planned.',
    },
  },
  {
    a: 'melatonin',
    b: 'valerian',
    severity: 'caution',
    message: {
      'zh-HK': '褪黑激素同纈草都可能有鎮靜作用。',
      'zh-CN': '褪黑激素与缬草都可能有镇静作用。',
      en: 'Melatonin and valerian may both have sedating effects.',
    },
    tip: {
      'zh-HK': '唔好一齊加量；首次使用避免開車或操作機械。',
      'zh-CN': '不要一起加量；首次使用避免开车或操作机械。',
      en: 'Don’t stack high doses; avoid driving until you know your response.',
    },
  },
  {
    a: 'melatonin',
    b: 'ashwagandha',
    severity: 'info',
    message: {
      'zh-HK': '兩者都常用於放鬆／睡眠，疊加可能令你更睏。',
      'zh-CN': '两者都常用于放松／睡眠，叠加可能令你更困。',
      en: 'Both are used for calm/sleep; stacking may increase drowsiness.',
    },
    tip: {
      'zh-HK': '可先試其中一種，觀察反應。',
      'zh-CN': '可先试其中一种，观察反应。',
      en: 'Consider trying one first and observe response.',
    },
  },
  {
    a: 'vitamin d',
    b: 'calcium',
    severity: 'info',
    message: {
      'zh-HK': '維他命 D 有助鈣吸收，常一齊討論。',
      'zh-CN': '维生素 D 有助钙吸收，常一起讨论。',
      en: 'Vitamin D supports calcium absorption — often discussed together.',
    },
    tip: {
      'zh-HK': '呢個係協同多過衝突；仍需注意總鈣攝取量。',
      'zh-CN': '这是协同多于冲突；仍需注意总钙摄入量。',
      en: 'More synergy than conflict; still watch total calcium intake.',
    },
  },
  {
    a: 'iron',
    b: 'calcium',
    severity: 'caution',
    message: {
      'zh-HK': '鐵劑同鈣補充唔宜同時空腹。',
      'zh-CN': '铁剂与钙补充不宜同时空腹。',
      en: 'Iron and calcium supplements are best not taken together fasting.',
    },
    tip: {
      'zh-HK': '鐵可空腹或少鈣餐；鈣可另一餐。',
      'zh-CN': '铁可空腹或少钙餐；钙可另一餐。',
      en: 'Iron with a low-calcium meal or empty stomach; calcium at another meal.',
    },
  },
];

function matchesName(nameEn: string, token: string): boolean {
  return nameEn.toLowerCase().includes(token.toLowerCase());
}

export function findInteractions(
  supplementNamesEn: string[],
): Array<SupplementInteraction & { nameA: string; nameB: string }> {
  const names = [...new Set(supplementNamesEn.map((n) => n.trim()).filter(Boolean))];
  const found: Array<SupplementInteraction & { nameA: string; nameB: string }> = [];
  const seen = new Set<string>();

  for (const rule of interactions) {
    for (let i = 0; i < names.length; i++) {
      for (let j = i + 1; j < names.length; j++) {
        const n1 = names[i];
        const n2 = names[j];
        const hit =
          (matchesName(n1, rule.a) && matchesName(n2, rule.b)) ||
          (matchesName(n1, rule.b) && matchesName(n2, rule.a));
        if (!hit) continue;
        const key = [rule.a, rule.b, n1.toLowerCase(), n2.toLowerCase()].sort().join('|');
        if (seen.has(key)) continue;
        seen.add(key);
        found.push({ ...rule, nameA: n1, nameB: n2 });
      }
    }
  }

  const order = { important: 0, caution: 1, info: 2 };
  return found.sort((a, b) => order[a.severity] - order[b.severity]);
}
