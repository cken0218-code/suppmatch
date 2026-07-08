export type ReasonLocale = 'zh-HK' | 'zh-CN' | 'en';

export type LocalizedText = Record<ReasonLocale, string>;

/**
 * Why we recommend a supplement — keyed by English name (case-insensitive match).
 * Keep wording supportive, not medical claims.
 */
export const supplementReasons: Record<string, LocalizedText> = {
  'vitamin b complex': {
    'zh-HK': '支持能量代謝同神經系統，常見用於疲勞同壓力相關狀態。',
    'zh-CN': '支持能量代谢和神经系统，常见用于疲劳与压力相关状态。',
    en: 'Supports energy metabolism and the nervous system; often used for fatigue and stress.',
  },
  magnesium: {
    'zh-HK': '有助肌肉放鬆同神經平穩，常被用於睡眠同壓力管理。',
    'zh-CN': '有助于肌肉放松与神经平稳，常用于睡眠和压力管理。',
    en: 'May help muscle relaxation and calm nerves; commonly used for sleep and stress.',
  },
  'fish oil (omega-3)': {
    'zh-HK': 'Omega-3 支持心血管同腦部健康，日常營養常見選擇。',
    'zh-CN': 'Omega-3 支持心血管与脑部健康，日常营养常见选择。',
    en: 'Omega-3 supports heart and brain health; a common daily nutrition choice.',
  },
  'fish oil': {
    'zh-HK': 'Omega-3 支持心血管同腦部健康。',
    'zh-CN': 'Omega-3 支持心血管与脑部健康。',
    en: 'Omega-3 supports heart and brain health.',
  },
  melatonin: {
    'zh-HK': '有助調節睡眠週期，適合偶爾難以入睡嘅情況（短期使用較常見）。',
    'zh-CN': '有助于调节睡眠周期，适合偶尔难以入睡的情况（多为短期使用）。',
    en: 'Helps regulate sleep cycles; often used short-term for occasional sleep difficulty.',
  },
  'valerian root': {
    'zh-HK': '傳統用於放鬆同改善入睡，屬草本鎮靜取向。',
    'zh-CN': '传统用于放松与改善入睡，属草本镇静取向。',
    en: 'Traditionally used for relaxation and falling asleep; a herbal calm option.',
  },
  iron: {
    'zh-HK': '支持紅血球同氧氣運送；缺鐵時較常被考慮（女性更常見）。',
    'zh-CN': '支持红细胞与氧气运送；缺铁时较常被考虑（女性更常见）。',
    en: 'Supports red blood cells and oxygen transport; often considered when iron is low (more common in women).',
  },
  coq10: {
    'zh-HK': '參與細胞能量生產，常見於疲勞同心臟健康相關討論。',
    'zh-CN': '参与细胞能量生产，常见于疲劳与心脏健康相关讨论。',
    en: 'Involved in cellular energy production; often discussed for fatigue and heart health.',
  },
  biotin: {
    'zh-HK': '支持頭髮、皮膚同指甲健康，係美容營養常見成分。',
    'zh-CN': '支持头发、皮肤与指甲健康，是美容营养常见成分。',
    en: 'Supports hair, skin, and nail health; a common beauty-nutrition ingredient.',
  },
  zinc: {
    'zh-HK': '支持免疫同皮膚健康，亦常見於男士健康相關補充。',
    'zh-CN': '支持免疫与皮肤健康，也常见于男士健康相关补充。',
    en: 'Supports immune and skin health; also common in men’s health formulas.',
  },
  keratin: {
    'zh-HK': '頭髮同指甲結構相關蛋白質，常見於護髮補充配方。',
    'zh-CN': '头发与指甲结构相关蛋白质，常见于护发补充配方。',
    en: 'A structural protein for hair and nails; common in hair-support formulas.',
  },
  probiotics: {
    'zh-HK': '支持腸道菌群平衡，常見用於消化不適同腸胃調理。',
    'zh-CN': '支持肠道菌群平衡，常见用于消化不适与肠胃调理。',
    en: 'Supports gut microbiome balance; often used for digestive comfort.',
  },
  'digestive enzymes': {
    'zh-HK': '有助分解食物中嘅營養素，適合餐後脹氣或消化慢。',
    'zh-CN': '有助于分解食物中的营养素，适合餐后胀气或消化慢。',
    en: 'Helps break down nutrients in food; useful for bloating or slow digestion after meals.',
  },
  'aloe vera': {
    'zh-HK': '傳統用於舒緩腸胃不適，屬溫和消化道支持。',
    'zh-CN': '传统用于舒缓肠胃不适，属温和消化道支持。',
    en: 'Traditionally used to soothe digestive discomfort; gentle GI support.',
  },
  ashwagandha: {
    'zh-HK': '適應原草本，常見於壓力管理同放鬆相關用途。',
    'zh-CN': '适应原草本，常见于压力管理与放松相关用途。',
    en: 'An adaptogenic herb often used for stress management and relaxation.',
  },
  lutein: {
    'zh-HK': '黃斑區常見類胡蘿蔔素，支持眼睛健康同藍光相關護眼。',
    'zh-CN': '黄斑区常见类胡萝卜素，支持眼睛健康与蓝光相关护眼。',
    en: 'A carotenoid concentrated in the macula; supports eye health and screen-related care.',
  },
  bilberry: {
    'zh-HK': '富含花青素，傳統用於視力同眼部循環支持。',
    'zh-CN': '富含花青素，传统用于视力与眼部循环支持。',
    en: 'Rich in anthocyanins; traditionally used for vision and eye circulation support.',
  },
  'vitamin a': {
    'zh-HK': '支持視力同黏膜健康，係眼睛營養基礎成分之一。',
    'zh-CN': '支持视力与粘膜健康，是眼睛营养基础成分之一。',
    en: 'Supports vision and mucosal health; a foundational nutrient for eye care.',
  },
  'vitamin d': {
    'zh-HK': '支持骨骼同免疫健康；室內生活或日照不足時較常補充。',
    'zh-CN': '支持骨骼与免疫健康；室内生活或日照不足时较常补充。',
    en: 'Supports bone and immune health; often supplemented with low sun exposure.',
  },
  'vitamin d3': {
    'zh-HK': '支持骨骼同免疫健康；室內生活或日照不足時較常補充。',
    'zh-CN': '支持骨骼与免疫健康；室内生活或日照不足时较常补充。',
    en: 'Supports bone and immune health; often supplemented with low sun exposure.',
  },
  calcium: {
    'zh-HK': '骨骼同牙齒主要礦物質，年齡增長後更常被關注。',
    'zh-CN': '骨骼与牙齿主要矿物质，年龄增长后更常被关注。',
    en: 'Primary mineral for bones and teeth; often a focus with age.',
  },
  collagen: {
    'zh-HK': '支持皮膚彈性同關節結締組織，常見於抗衰老配方。',
    'zh-CN': '支持皮肤弹性与关节结缔组织，常见于抗衰老配方。',
    en: 'Supports skin elasticity and connective tissue; common in anti-aging formulas.',
  },
  multivitamin: {
    'zh-HK': '日常微量營養素底盤，適合飲食唔均衡時作基礎補充。',
    'zh-CN': '日常微量营养素底盘，适合饮食不均衡时作基础补充。',
    en: 'A daily micronutrient base for uneven diets.',
  },
  'vitamin c': {
    'zh-HK': '支持免疫同抗氧化，日常補充常見選擇。',
    'zh-CN': '支持免疫与抗氧化，日常补充常见选择。',
    en: 'Supports immune function and antioxidant status; a common daily choice.',
  },
};

/** Fuzzy lookup: match by full EN name or contained keyword */
export function getReasonForSupplement(nameEn: string, locale: ReasonLocale): string | null {
  const key = nameEn.toLowerCase().trim();
  if (supplementReasons[key]) return supplementReasons[key][locale];

  for (const [k, v] of Object.entries(supplementReasons)) {
    if (key.includes(k) || k.includes(key)) return v[locale];
  }
  return null;
}
