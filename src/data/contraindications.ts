import type { LocaleText } from '@/data/evidence';

export type WarningTag =
  | 'pregnancy'
  | 'breastfeeding'
  | 'blood_thinners'
  | 'blood_pressure'
  | 'thyroid'
  | 'iron_overload'
  | 'surgery'
  | 'kids'
  | 'sedatives'
  | 'autoimmune'
  | 'kidney'
  | 'general';

export interface Contraindication {
  tag: WarningTag;
  severity: 'caution' | 'avoid_unless_advised';
  text: LocaleText;
}

/** Warnings keyed by English supplement name (fuzzy match like evidence) */
export const supplementWarnings: Record<string, Contraindication[]> = {
  melatonin: [
    {
      tag: 'pregnancy',
      severity: 'avoid_unless_advised',
      text: {
        'zh-HK': '孕婦／計劃懷孕：使用前請咨詢醫生。',
        'zh-CN': '孕妇／计划怀孕：使用前请咨询医生。',
        en: 'Pregnancy / trying to conceive: ask a clinician before use.',
      },
    },
    {
      tag: 'sedatives',
      severity: 'caution',
      text: {
        'zh-HK': '可能加強鎮靜／安眠藥效果，開車或操作機械前慎用。',
        'zh-CN': '可能加强镇静／安眠药效果，开车或操作机械前慎用。',
        en: 'May add to sedative effects; caution before driving or machinery.',
      },
    },
    {
      tag: 'kids',
      severity: 'avoid_unless_advised',
      text: {
        'zh-HK': '兒童使用應由兒科醫生指導。',
        'zh-CN': '儿童使用应由儿科医生指导。',
        en: 'Pediatric use only under clinician guidance.',
      },
    },
  ],
  'valerian root': [
    {
      tag: 'sedatives',
      severity: 'caution',
      text: {
        'zh-HK': '可能有鎮靜作用，避免同酒精或其他鎮靜物同時濫用。',
        'zh-CN': '可能有镇静作用，避免与酒精或其他镇静物同时滥用。',
        en: 'May be sedating; avoid stacking with alcohol or other sedatives.',
      },
    },
    {
      tag: 'surgery',
      severity: 'caution',
      text: {
        'zh-HK': '手術前可能需要停用（麻醉相關風險，遵醫囑）。',
        'zh-CN': '手术前可能需要停用（麻醉相关风险，遵医嘱）。',
        en: 'May need to stop before surgery (anesthesia-related; follow clinician advice).',
      },
    },
  ],
  iron: [
    {
      tag: 'iron_overload',
      severity: 'avoid_unless_advised',
      text: {
        'zh-HK': '血色病或鐵過載者勿自行補鐵。',
        'zh-CN': '血色病或铁过载者勿自行补铁。',
        en: 'Do not self-supplement if you have hemochromatosis / iron overload.',
      },
    },
    {
      tag: 'general',
      severity: 'caution',
      text: {
        'zh-HK': '無缺鐵時長期補鐵可能有害；建議先驗血。',
        'zh-CN': '无缺铁时长期补铁可能有害；建议先验血。',
        en: 'Long-term iron without deficiency can be harmful; test first.',
      },
    },
    {
      tag: 'kids',
      severity: 'avoid_unless_advised',
      text: {
        'zh-HK': '鐵劑對兒童過量可致嚴重中毒，務必妥善存放。',
        'zh-CN': '铁剂对儿童过量可致严重中毒，务必妥善存放。',
        en: 'Iron overdose is dangerous for children — store securely.',
      },
    },
  ],
  ashwagandha: [
    {
      tag: 'pregnancy',
      severity: 'avoid_unless_advised',
      text: {
        'zh-HK': '孕期通常建議避免，使用前咨詢醫生。',
        'zh-CN': '孕期通常建议避免，使用前咨询医生。',
        en: 'Often advised to avoid in pregnancy; check with a clinician.',
      },
    },
    {
      tag: 'thyroid',
      severity: 'caution',
      text: {
        'zh-HK': '可能影響甲狀腺相關指標，甲狀腺疾病患者應咨詢醫生。',
        'zh-CN': '可能影响甲状腺相关指标，甲状腺疾病患者应咨询医生。',
        en: 'May affect thyroid markers; thyroid patients should seek advice.',
      },
    },
    {
      tag: 'autoimmune',
      severity: 'caution',
      text: {
        'zh-HK': '自體免疫疾病患者使用前應咨詢專科。',
        'zh-CN': '自体免疫疾病患者使用前应咨询专科。',
        en: 'People with autoimmune conditions should ask a specialist first.',
      },
    },
  ],
  'fish oil (omega-3)': [
    {
      tag: 'blood_thinners',
      severity: 'caution',
      text: {
        'zh-HK': '高劑量可能影響凝血，服用抗凝血藥者需咨詢醫生。',
        'zh-CN': '高剂量可能影响凝血，服用抗凝血药者需咨询医生。',
        en: 'High doses may affect clotting; check if you take anticoagulants.',
      },
    },
    {
      tag: 'surgery',
      severity: 'caution',
      text: {
        'zh-HK': '手術前可能需調整劑量（遵醫囑）。',
        'zh-CN': '手术前可能需调整剂量（遵医嘱）。',
        en: 'Dose may need adjustment before surgery (clinician advice).',
      },
    },
  ],
  'fish oil': [
    {
      tag: 'blood_thinners',
      severity: 'caution',
      text: {
        'zh-HK': '高劑量可能影響凝血。',
        'zh-CN': '高剂量可能影响凝血。',
        en: 'High doses may affect clotting.',
      },
    },
  ],
  magnesium: [
    {
      tag: 'kidney',
      severity: 'caution',
      text: {
        'zh-HK': '腎功能不全者補鎂需醫生指導。',
        'zh-CN': '肾功能不全者补镁需医生指导。',
        en: 'Impaired kidney function: use magnesium only with medical guidance.',
      },
    },
    {
      tag: 'general',
      severity: 'caution',
      text: {
        'zh-HK': '過量可能引起腹瀉或不適。',
        'zh-CN': '过量可能引起腹泻或不适。',
        en: 'Excess may cause diarrhea or GI discomfort.',
      },
    },
  ],
  zinc: [
    {
      tag: 'general',
      severity: 'caution',
      text: {
        'zh-HK': '長期高劑量可能干擾銅吸收，並可能引起噁心。',
        'zh-CN': '长期高剂量可能干扰铜吸收，并可能引起恶心。',
        en: 'Chronic high doses may impair copper status and cause nausea.',
      },
    },
  ],
  calcium: [
    {
      tag: 'kidney',
      severity: 'caution',
      text: {
        'zh-HK': '腎結石病史者應咨詢醫生再補鈣。',
        'zh-CN': '肾结石病史者应咨询医生再补钙。',
        en: 'History of kidney stones: ask a clinician before supplementing calcium.',
      },
    },
    {
      tag: 'general',
      severity: 'caution',
      text: {
        'zh-HK': '可能影響某些藥物（如甲狀腺素、部分抗生素）吸收，注意間隔。',
        'zh-CN': '可能影响某些药物（如甲状腺素、部分抗生素）吸收，注意间隔。',
        en: 'May reduce absorption of some drugs (e.g. thyroid hormone, some antibiotics); space doses.',
      },
    },
  ],
  'vitamin d': [
    {
      tag: 'general',
      severity: 'caution',
      text: {
        'zh-HK': '脂溶性維他命可蓄積，長期超高劑量有中毒風險。',
        'zh-CN': '脂溶性维生素可蓄积，长期超高剂量有中毒风险。',
        en: 'Fat-soluble; chronic very high doses risk toxicity.',
      },
    },
  ],
  'vitamin d3': [
    {
      tag: 'general',
      severity: 'caution',
      text: {
        'zh-HK': '長期超高劑量有中毒風險，宜按驗血調整。',
        'zh-CN': '长期超高剂量有中毒风险，宜按验血调整。',
        en: 'Chronic mega-doses risk toxicity; prefer lab-guided dosing.',
      },
    },
  ],
  biotin: [
    {
      tag: 'general',
      severity: 'caution',
      text: {
        'zh-HK': '高劑量生物素可能干擾甲狀腺及 troponin 等化驗。',
        'zh-CN': '高剂量生物素可能干扰甲状腺及 troponin 等化验。',
        en: 'High-dose biotin can interfere with thyroid and troponin lab tests.',
      },
    },
  ],
  'vitamin a': [
    {
      tag: 'pregnancy',
      severity: 'avoid_unless_advised',
      text: {
        'zh-HK': '孕期過量維他命 A（視黃醇）可能有風險，勿自行高劑量補充。',
        'zh-CN': '孕期过量维生素 A（视黄醇）可能有风险，勿自行高剂量补充。',
        en: 'Excess retinol vitamin A in pregnancy can be risky — avoid high-dose self-supplementation.',
      },
    },
  ],
  coq10: [
    {
      tag: 'blood_pressure',
      severity: 'caution',
      text: {
        'zh-HK': '可能輕微影響血壓，服降壓藥者應監察。',
        'zh-CN': '可能轻微影响血压，服降压药者应监察。',
        en: 'May mildly affect blood pressure; monitor if on antihypertensives.',
      },
    },
    {
      tag: 'blood_thinners',
      severity: 'caution',
      text: {
        'zh-HK': '與華法林等抗凝血藥可能有相互作用報告。',
        'zh-CN': '与华法林等抗凝血药可能有相互作用报告。',
        en: 'Possible interactions reported with warfarin-type anticoagulants.',
      },
    },
  ],
  probiotics: [
    {
      tag: 'general',
      severity: 'caution',
      text: {
        'zh-HK': '嚴重免疫低下或中央導管患者使用前必須咨詢醫生。',
        'zh-CN': '严重免疫低下或中央导管患者使用前必须咨询医生。',
        en: 'Severely immunocompromised patients or those with central lines need medical advice first.',
      },
    },
  ],
};

export function getWarnings(nameEn: string): Contraindication[] {
  const key = nameEn.toLowerCase().trim();
  if (supplementWarnings[key]) return supplementWarnings[key];
  for (const [k, v] of Object.entries(supplementWarnings)) {
    if (key.includes(k) || k.includes(key)) return v;
  }
  return [];
}
