export type EvidenceLevel = 'strong' | 'moderate' | 'limited' | 'traditional';

export type LocaleText = { 'zh-HK': string; 'zh-CN': string; en: string };

export interface EvidenceSource {
  label: string;
  url: string;
}

export interface SupplementEvidence {
  level: EvidenceLevel;
  /** Common uses (supportive language, not medical claims) */
  uses: LocaleText;
  summary: LocaleText;
  sources: EvidenceSource[];
}

export const evidenceLevelLabels: Record<EvidenceLevel, LocaleText> = {
  strong: {
    'zh-HK': '證據較充分',
    'zh-CN': '证据较充分',
    en: 'Stronger evidence',
  },
  moderate: {
    'zh-HK': '證據中等',
    'zh-CN': '证据中等',
    en: 'Moderate evidence',
  },
  limited: {
    'zh-HK': '證據有限',
    'zh-CN': '证据有限',
    en: 'Limited evidence',
  },
  traditional: {
    'zh-HK': '傳統使用為主',
    'zh-CN': '传统使用为主',
    en: 'Traditional use',
  },
};

const NIH = (path: string, label = 'NIH ODS') => ({
  label,
  url: `https://ods.od.nih.gov/factsheets/${path}`,
});

/**
 * Evidence notes for common supplements.
 * Language is intentionally cautious — informational only.
 */
export const supplementEvidence: Record<string, SupplementEvidence> = {
  magnesium: {
    level: 'moderate',
    uses: {
      'zh-HK': '肌肉放鬆、睡眠與壓力相關討論中常見',
      'zh-CN': '肌肉放松、睡眠与压力相关讨论中常见',
      en: 'Often discussed for muscle relaxation, sleep, and stress support',
    },
    summary: {
      'zh-HK': '鎂係人體必需礦物質；不足時可能影響肌肉同睡眠質素，但補充效果因人而異。',
      'zh-CN': '镁是人体必需矿物质；不足时可能影响肌肉与睡眠质量，但补充效果因人而异。',
      en: 'Magnesium is an essential mineral; low levels may affect muscle and sleep, but responses to supplements vary.',
    },
    sources: [NIH('Magnesium-HealthProfessional/', 'NIH — Magnesium'), { label: 'PubMed search', url: 'https://pubmed.ncbi.nlm.nih.gov/?term=magnesium+sleep' }],
  },
  'vitamin b complex': {
    level: 'moderate',
    uses: {
      'zh-HK': '能量代謝、神經系統支持',
      'zh-CN': '能量代谢、神经系统支持',
      en: 'Energy metabolism and nervous-system support',
    },
    summary: {
      'zh-HK': 'B 群參與能量代謝；飲食不均時較常被討論，但「即時提神」未必適用於所有人。',
      'zh-CN': 'B 族参与能量代谢；饮食不均时较常被讨论，但“即时提神”未必适用于所有人。',
      en: 'B vitamins support energy metabolism; more relevant with poor diet than as a universal energy boost.',
    },
    sources: [NIH('VitaminB6-HealthProfessional/', 'NIH — Vitamin B6'), NIH('VitaminB12-HealthProfessional/', 'NIH — B12')],
  },
  'fish oil (omega-3)': {
    level: 'strong',
    uses: {
      'zh-HK': '心血管與腦部健康相關營養支持',
      'zh-CN': '心血管与脑部健康相关营养支持',
      en: 'Heart and brain nutrition support',
    },
    summary: {
      'zh-HK': 'EPA/DHA 研究相對多，尤其係血脂同整體心血管風險因素相關討論。',
      'zh-CN': 'EPA/DHA 研究相对多，尤其是血脂与整体心血管风险因素相关讨论。',
      en: 'EPA/DHA have a relatively large research base, especially around lipids and heart-risk factors.',
    },
    sources: [NIH('Omega3FattyAcids-HealthProfessional/', 'NIH — Omega-3'), { label: 'AHA resources', url: 'https://www.heart.org' }],
  },
  'fish oil': {
    level: 'strong',
    uses: {
      'zh-HK': '心血管與腦部健康',
      'zh-CN': '心血管与脑部健康',
      en: 'Heart and brain health',
    },
    summary: {
      'zh-HK': '魚油（Omega-3）係證據基礎較厚嘅常見補充品之一。',
      'zh-CN': '鱼油（Omega-3）是证据基础较厚的常见补充品之一。',
      en: 'Fish oil (omega-3) is among the better-studied common supplements.',
    },
    sources: [NIH('Omega3FattyAcids-HealthProfessional/', 'NIH — Omega-3')],
  },
  melatonin: {
    level: 'moderate',
    uses: {
      'zh-HK': '調節睡眠週期、短暫入睡困難',
      'zh-CN': '调节睡眠周期、短暂入睡困难',
      en: 'Sleep-cycle timing and occasional sleep onset difficulty',
    },
    summary: {
      'zh-HK': '對時差或入睡時間調節有一定研究支持；長期高劑量使用應謹慎。',
      'zh-CN': '对时差或入睡时间调节有一定研究支持；长期高剂量使用应谨慎。',
      en: 'Some support for circadian/jet-lag related sleep timing; long-term high doses warrant caution.',
    },
    sources: [{ label: 'NCCIH — Melatonin', url: 'https://www.nccih.nih.gov/health/melatonin-what-you-need-to-know' }],
  },
  'valerian root': {
    level: 'traditional',
    uses: {
      'zh-HK': '放鬆、傳統助眠草本',
      'zh-CN': '放松、传统助眠草本',
      en: 'Relaxation; traditional sleep herb',
    },
    summary: {
      'zh-HK': '傳統使用多，現代臨床證據質量參差，效果因人而異。',
      'zh-CN': '传统使用多，现代临床证据质量参差，效果因人而异。',
      en: 'Long traditional use; modern trial quality is mixed and responses vary.',
    },
    sources: [{ label: 'NCCIH — Valerian', url: 'https://www.nccih.nih.gov/health/valerian' }],
  },
  iron: {
    level: 'strong',
    uses: {
      'zh-HK': '缺鐵相關疲勞、紅血球生成',
      'zh-CN': '缺铁相关疲劳、红细胞生成',
      en: 'Iron-deficiency related fatigue; red blood cell production',
    },
    summary: {
      'zh-HK': '對確診缺鐵非常重要；無缺鐵時長期補鐵可能有害，應先檢測。',
      'zh-CN': '对确诊缺铁非常重要；无缺铁时长期补铁可能有害，应先检测。',
      en: 'Critical when deficiency is confirmed; unnecessary long-term iron can be harmful — test first.',
    },
    sources: [NIH('Iron-HealthProfessional/', 'NIH — Iron')],
  },
  coq10: {
    level: 'moderate',
    uses: {
      'zh-HK': '細胞能量、他汀使用者相關討論',
      'zh-CN': '细胞能量、他汀使用者相关讨论',
      en: 'Cellular energy; often discussed with statin use',
    },
    summary: {
      'zh-HK': '有研究探討疲勞同心臟相關指標，但唔係所有適應症都有一致結論。',
      'zh-CN': '有研究探讨疲劳与心脏相关指标，但不是所有适应症都有一致结论。',
      en: 'Studied for energy/heart-related outcomes, but findings are not uniform across all uses.',
    },
    sources: [{ label: 'PubMed — CoQ10', url: 'https://pubmed.ncbi.nlm.nih.gov/?term=coenzyme+Q10' }],
  },
  zinc: {
    level: 'moderate',
    uses: {
      'zh-HK': '免疫、皮膚、傷口癒合相關',
      'zh-CN': '免疫、皮肤、伤口愈合相关',
      en: 'Immune function, skin, wound healing',
    },
    summary: {
      'zh-HK': '鋅係必需微量元素；感冒相關使用有研究但結果不完全一致，過量可致副作用。',
      'zh-CN': '锌是必需微量元素；感冒相关使用有研究但结果不完全一致，过量可致副作用。',
      en: 'Essential micronutrient; cold-related research is mixed; excess can cause side effects.',
    },
    sources: [NIH('Zinc-HealthProfessional/', 'NIH — Zinc')],
  },
  biotin: {
    level: 'limited',
    uses: {
      'zh-HK': '頭髮、皮膚、指甲美容營養',
      'zh-CN': '头发、皮肤、指甲美容营养',
      en: 'Hair, skin, and nail beauty nutrition',
    },
    summary: {
      'zh-HK': '對嚴重缺乏以外嘅「生髮」證據有限；高劑量可能干擾某些驗血結果。',
      'zh-CN': '对严重缺乏以外的“生发”证据有限；高剂量可能干扰某些验血结果。',
      en: 'Limited evidence for hair growth beyond true deficiency; high doses may interfere with some lab tests.',
    },
    sources: [NIH('Biotin-HealthProfessional/', 'NIH — Biotin')],
  },
  probiotics: {
    level: 'moderate',
    uses: {
      'zh-HK': '腸道菌群、消化舒適',
      'zh-CN': '肠道菌群、消化舒适',
      en: 'Gut microbiome and digestive comfort',
    },
    summary: {
      'zh-HK': '效果高度取決於菌株同用途；唔係所有益生菌產品都一樣。',
      'zh-CN': '效果高度取决于菌株与用途；不是所有益生菌产品都一样。',
      en: 'Effects are strain- and use-specific; products are not interchangeable.',
    },
    sources: [{ label: 'NCCIH — Probiotics', url: 'https://www.nccih.nih.gov/health/probiotics-what-you-need-to-know' }],
  },
  'vitamin d': {
    level: 'strong',
    uses: {
      'zh-HK': '骨骼健康、免疫相關營養',
      'zh-CN': '骨骼健康、免疫相关营养',
      en: 'Bone health and immune-related nutrition',
    },
    summary: {
      'zh-HK': '證據較充分於骨骼同維他命 D 狀態；補充劑量應按驗血同醫囑調整。',
      'zh-CN': '证据较充分于骨骼与维生素 D 状态；补充剂量应按验血与医嘱调整。',
      en: 'Stronger evidence for bone health and vitamin D status; dose should follow labs/clinical advice.',
    },
    sources: [NIH('VitaminD-HealthProfessional/', 'NIH — Vitamin D')],
  },
  'vitamin d3': {
    level: 'strong',
    uses: {
      'zh-HK': '骨骼健康、日照不足時補充',
      'zh-CN': '骨骼健康、日照不足时补充',
      en: 'Bone health; low sun-exposure contexts',
    },
    summary: {
      'zh-HK': 'D3 係常見補充形式；應避免長期過量。',
      'zh-CN': 'D3 是常见补充形式；应避免长期过量。',
      en: 'D3 is a common supplemental form; avoid chronic excess.',
    },
    sources: [NIH('VitaminD-HealthProfessional/', 'NIH — Vitamin D')],
  },
  calcium: {
    level: 'strong',
    uses: {
      'zh-HK': '骨骼與牙齒礦物化',
      'zh-CN': '骨骼与牙齿矿物化',
      en: 'Bone and tooth mineralization',
    },
    summary: {
      'zh-HK': '飲食攝取優先；補充時注意總量同與其他礦物質嘅吸收互動。',
      'zh-CN': '饮食摄入优先；补充时注意总量以及与其他矿物质的吸收互动。',
      en: 'Food first; when supplementing, watch total intake and mineral interactions.',
    },
    sources: [NIH('Calcium-HealthProfessional/', 'NIH — Calcium')],
  },
  ashwagandha: {
    level: 'limited',
    uses: {
      'zh-HK': '壓力、適應原草本',
      'zh-CN': '压力、适应原草本',
      en: 'Stress support; adaptogenic herb',
    },
    summary: {
      'zh-HK': '有初步研究探討壓力相關指標，但證據仍發展中，肝功能異常者應特別謹慎。',
      'zh-CN': '有初步研究探讨压力相关指标，但证据仍发展中，肝功能异常者应特别谨慎。',
      en: 'Early research on stress markers; evidence still evolving; extra caution with liver issues.',
    },
    sources: [{ label: 'NCCIH — Ashwagandha', url: 'https://www.nccih.nih.gov/health/ashwagandha' }],
  },
  collagen: {
    level: 'limited',
    uses: {
      'zh-HK': '皮膚彈性、關節舒適相關',
      'zh-CN': '皮肤弹性、关节舒适相关',
      en: 'Skin elasticity and joint comfort discussions',
    },
    summary: {
      'zh-HK': '部分小型研究顯示皮膚指標改善可能，但整體證據仍有限。',
      'zh-CN': '部分小型研究显示皮肤指标改善可能，但整体证据仍有限。',
      en: 'Some small studies suggest possible skin outcomes; overall evidence remains limited.',
    },
    sources: [{ label: 'PubMed — collagen skin', url: 'https://pubmed.ncbi.nlm.nih.gov/?term=collagen+peptides+skin' }],
  },
  lutein: {
    level: 'moderate',
    uses: {
      'zh-HK': '黃斑區營養、護眼相關',
      'zh-CN': '黄斑区营养、护眼相关',
      en: 'Macular nutrition; eye-health support',
    },
    summary: {
      'zh-HK': '葉黃素/玉米黃素於眼睛健康研究中較常見，尤其係飲食攝取。',
      'zh-CN': '叶黄素/玉米黄素于眼睛健康研究中较常见，尤其是饮食摄入。',
      en: 'Lutein/zeaxanthin appear frequently in eye-health research, especially dietary intake.',
    },
    sources: [NIH('VitaminA-HealthProfessional/', 'NIH — related carotenoids context')],
  },
  'vitamin c': {
    level: 'strong',
    uses: {
      'zh-HK': '免疫支持、抗氧化',
      'zh-CN': '免疫支持、抗氧化',
      en: 'Immune support and antioxidant status',
    },
    summary: {
      'zh-HK': '必需營養素；一般飲食可攝取，高劑量「預防感冒」證據有限。',
      'zh-CN': '必需营养素；一般饮食可摄取，高剂量“预防感冒”证据有限。',
      en: 'Essential nutrient; high-dose cold prevention evidence is limited for most people.',
    },
    sources: [NIH('VitaminC-HealthProfessional/', 'NIH — Vitamin C')],
  },
  'digestive enzymes': {
    level: 'limited',
    uses: {
      'zh-HK': '餐後消化、脹氣相關',
      'zh-CN': '餐后消化、胀气相关',
      en: 'Post-meal digestion and bloating discussions',
    },
    summary: {
      'zh-HK': '對特定酶缺乏可能有幫助；一般健康人證據較參差。',
      'zh-CN': '对特定酶缺乏可能有帮助；一般健康人证据较参差。',
      en: 'May help specific enzyme insufficiencies; mixed evidence for otherwise healthy people.',
    },
    sources: [{ label: 'PubMed — digestive enzymes', url: 'https://pubmed.ncbi.nlm.nih.gov/?term=digestive+enzymes+supplement' }],
  },
  multivitamin: {
    level: 'moderate',
    uses: {
      'zh-HK': '日常微量營養素底盤',
      'zh-CN': '日常微量营养素底盘',
      en: 'Daily micronutrient baseline',
    },
    summary: {
      'zh-HK': '可填補飲食空隙，但唔等於可取代均衡飲食；亦唔保證預防慢性病。',
      'zh-CN': '可填补饮食空隙，但不等于可取代均衡饮食；也不保证预防慢性病。',
      en: 'Can fill dietary gaps; not a substitute for diet and not a proven chronic-disease shield.',
    },
    sources: [{ label: 'NIH — Multivitamin/mineral', url: 'https://ods.od.nih.gov/factsheets/MVMS-HealthProfessional/' }],
  },
};

export function getEvidence(nameEn: string): SupplementEvidence | null {
  const key = nameEn.toLowerCase().trim();
  if (supplementEvidence[key]) return supplementEvidence[key];
  for (const [k, v] of Object.entries(supplementEvidence)) {
    if (key.includes(k) || k.includes(key)) return v;
  }
  return null;
}
