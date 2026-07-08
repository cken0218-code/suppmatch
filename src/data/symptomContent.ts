import type { Symptom } from '@/data/symptoms';
import type { LocaleText } from '@/data/evidence';

export interface SymptomFAQ {
  q: LocaleText;
  a: LocaleText;
}

export interface SymptomPageContent {
  intro: LocaleText;
  lifestyle: LocaleText;
  whenToSeeDoctor: LocaleText;
  faqs: SymptomFAQ[];
}

/** Curated intros for high-traffic symptoms; others use a safe template */
const curated: Record<string, Partial<SymptomPageContent>> = {
  insomnia: {
    intro: {
      'zh-HK': '睡眠質素差可以由壓力、作息、咖啡因、環境光或多種因素引起。部分營養素同草本會被用嚟支持放鬆同入睡，但唔能取代規律作息同必要時嘅醫療評估。',
      'zh-CN': '睡眠质量差可以由压力、作息、咖啡因、环境光或多种因素引起。部分营养素和草本会被用来支持放松与入睡，但不能取代规律作息和必要时的医疗评估。',
      en: 'Poor sleep can stem from stress, schedule, caffeine, light exposure, and more. Some nutrients and herbs are used to support relaxation and sleep onset — they do not replace sleep hygiene or medical care when needed.',
    },
  },
  'stress-anxiety': {
    intro: {
      'zh-HK': '壓力同焦慮感受好常見。生活方式（運動、睡眠、社交支持）通常係基礎；部分補充品可能作為輔助討論，但持續情緒困擾應尋求專業協助。',
      'zh-CN': '压力与焦虑感受很常见。生活方式（运动、睡眠、社交支持）通常是基础；部分补充品可能作为辅助讨论，但持续情绪困扰应寻求专业协助。',
      en: 'Stress and anxious feelings are common. Lifestyle foundations matter most; supplements may be discussed as adjuncts, but persistent distress deserves professional care.',
    },
  },
  fatigue: {
    intro: {
      'zh-HK': '持續疲勞可能同睡眠、壓力、缺鐵、甲狀腺或其他健康問題有關。補充品只係其中一個討論方向，長期疲勞應先排查原因。',
      'zh-CN': '持续疲劳可能与睡眠、压力、缺铁、甲状腺或其他健康问题有关。补充品只是其中一个讨论方向，长期疲劳应先排查原因。',
      en: 'Ongoing fatigue may relate to sleep, stress, iron status, thyroid, or other conditions. Supplements are only one discussion track — investigate causes of chronic fatigue.',
    },
  },
  'hair-loss': {
    intro: {
      'zh-HK': '脫髮原因包括遺傳、壓力、營養、荷爾蒙同皮膚狀況。生物素等補充品在缺乏以外證據有限；明顯脫髮建議咨詢醫生或皮膚科。',
      'zh-CN': '脱发原因包括遗传、压力、营养、荷尔蒙与皮肤状况。生物素等补充品在缺乏以外证据有限；明显脱发建议咨询医生或皮肤科。',
      en: 'Hair loss has many drivers (genetics, stress, nutrition, hormones, scalp conditions). Biotin and similar options have limited evidence beyond deficiency; see a clinician for significant loss.',
    },
  },
  'digestive-issues': {
    intro: {
      'zh-HK': '消化不適可能同飲食、菌群、壓力或疾病有關。益生菌同消化酶係常見討論方向，但紅旗症狀（出血、消瘦、持續劇痛）需盡快求醫。',
      'zh-CN': '消化不适可能与饮食、菌群、压力或疾病有关。益生菌和消化酶是常见讨论方向，但红旗症状（出血、消瘦、持续剧痛）需尽快求医。',
      en: 'Digestive discomfort may relate to diet, microbiome, stress, or disease. Probiotics and enzymes are common discussion points — red-flag symptoms need prompt care.',
    },
  },
  headache: {
    intro: {
      'zh-HK': '頭痛類型好多（緊張型、偏頭痛等）。水分、睡眠、姿勢同壓力管理好重要；補充品只屬輔助資訊，突然劇烈頭痛應緊急求醫。',
      'zh-CN': '头痛类型很多（紧张型、偏头痛等）。水分、睡眠、姿势与压力管理很重要；补充品只属辅助信息，突然剧烈头痛应紧急求医。',
      en: 'Headaches vary widely. Hydration, sleep, posture, and stress matter; supplements are supportive info only. Sudden severe headache needs emergency care.',
    },
  },
  'weak-immunity': {
    intro: {
      'zh-HK': '「免疫力」係複雜系統，睡眠、營養、接種同衛生習慣係基礎。維他命 D、C、鋅等常被討論，但唔能取代醫療建議同疫苗。',
      'zh-CN': '“免疫力”是复杂系统，睡眠、营养、接种与卫生习惯是基础。维生素 D、C、锌等常被讨论，但不能取代医疗建议与疫苗。',
      en: 'Immune function is complex. Sleep, nutrition, vaccines, and hygiene are foundations. D, C, and zinc are often discussed — they do not replace medical care or immunization.',
    },
  },
  'eye-strain': {
    intro: {
      'zh-HK': '長時間屏幕可致眼睛疲勞。20-20-20 法則、光線同休息係首要；葉黃素等營養素多作為護眼飲食討論。',
      'zh-CN': '长时间屏幕可致眼睛疲劳。20-20-20 法则、光线与休息是首要；叶黄素等营养素多作为护眼饮食讨论。',
      en: 'Screen time can drive eye strain. Breaks, lighting, and the 20-20-20 rule come first; lutein is often discussed as part of eye-supportive nutrition.',
    },
  },
};

function templateIntro(symptom: Symptom): LocaleText {
  return {
    'zh-HK': `「${symptom.names['zh-HK']}」係用家常見關注嘅不適方向。以下整理咗一啲可能被討論嘅營養補充品資訊，僅供參考，唔構成診斷或治療建議。`,
    'zh-CN': `「${symptom.names['zh-CN']}」是用户常见关注的不适方向。以下整理了一些可能被讨论的营养补充品信息，仅供参考，不构成诊断或治疗建议。`,
    en: `"${symptom.names.en}" is a commonly searched concern. Below is educational information about supplements often discussed in this context — not a diagnosis or treatment plan.`,
  };
}

function defaultLifestyle(): LocaleText {
  return {
    'zh-HK': '優先考慮睡眠規律、均衡飲食、適量運動、減少煙酒同管理壓力。補充品無法取代健康生活習慣。',
    'zh-CN': '优先考虑睡眠规律、均衡饮食、适量运动、减少烟酒与管理压力。补充品无法取代健康生活习惯。',
    en: 'Prioritize sleep, balanced meals, movement, less smoking/alcohol, and stress management. Supplements do not replace healthy habits.',
  };
}

function defaultWhenToSeeDoctor(symptom: Symptom): LocaleText {
  return {
    'zh-HK': `如果「${symptom.names['zh-HK']}」突然加重、持續超過兩週、伴隨發燒/胸痛/呼吸困難/神智改變，或影響日常生活，請盡快咨詢醫生。`,
    'zh-CN': `如果「${symptom.names['zh-CN']}」突然加重、持续超过两周、伴随发烧/胸痛/呼吸困难/神智改变，或影响日常生活，请尽快咨询医生。`,
    en: `Seek care promptly if "${symptom.names.en}" suddenly worsens, lasts more than two weeks, comes with fever/chest pain/breathing trouble/confusion, or disrupts daily life.`,
  };
}

function defaultFaqs(symptom: Symptom): SymptomFAQ[] {
  const nameHK = symptom.names['zh-HK'];
  const nameCN = symptom.names['zh-CN'];
  const nameEN = symptom.names.en;
  const first = symptom.recommendations[0]?.name;

  return [
    {
      q: {
        'zh-HK': `${nameHK}可以靠保健品解決嗎？`,
        'zh-CN': `${nameCN}可以靠保健品解决吗？`,
        en: `Can supplements fix ${nameEN}?`,
      },
      a: {
        'zh-HK': '通常唔可以單靠保健品「解決」。佢哋最多係營養支持或輔助討論，真正原因需要生活調整甚至醫療評估。',
        'zh-CN': '通常不可以单靠保健品“解决”。它们最多是营养支持或辅助讨论，真正原因需要生活调整甚至医疗评估。',
        en: 'Rarely by themselves. At best they are supportive nutrition topics; root causes need lifestyle change and sometimes medical evaluation.',
      },
    },
    {
      q: {
        'zh-HK': first ? `點解會提到${first['zh-HK']}？` : '點樣揀補充品？',
        'zh-CN': first ? `为什么会提到${first['zh-CN']}？` : '怎么选补充品？',
        en: first ? `Why is ${first.en} mentioned?` : 'How should I choose?',
      },
      a: {
        'zh-HK': first
          ? `${first['zh-HK']}喺公開健康資訊同用家搜尋中，較常同「${nameHK}」一齊被討論。是否適合你要睇個人狀況同醫囑。`
          : '應先了解成分、劑量、相互作用同自己身體狀況，必要時咨詢藥劑師或醫生。',
        'zh-CN': first
          ? `${first['zh-CN']}在公开健康信息与用户搜索中，较常与「${nameCN}」一起被讨论。是否适合你要看个人状况与医嘱。`
          : '应先了解成分、剂量、相互作用与自己身体状况，必要时咨询药师或医生。',
        en: first
          ? `${first.en} often appears in public health info and searches related to ${nameEN}. Suitability depends on your situation and clinician advice.`
          : 'Review ingredients, dose, interactions, and your health history; ask a pharmacist or doctor when unsure.',
      },
    },
    {
      q: {
        'zh-HK': '幾耐會見效？',
        'zh-CN': '多久会见效？',
        en: 'How long until I notice anything?',
      },
      a: {
        'zh-HK': '因人而異。部分人幾日內主觀感受有變化，多數營養素需要數週持續觀察；若惡化請停用並求醫。',
        'zh-CN': '因人而异。部分人几天内主观感受有变化，多数营养素需要数周持续观察；若恶化请停用并求医。',
        en: 'It varies. Some notice subjective changes in days; many nutrients need weeks. Worsening means stop and seek care.',
      },
    },
  ];
}

export function getSymptomPageContent(symptom: Symptom): SymptomPageContent {
  const c = curated[symptom.id] || {};
  return {
    intro: c.intro || templateIntro(symptom),
    lifestyle: c.lifestyle || defaultLifestyle(),
    whenToSeeDoctor: c.whenToSeeDoctor || defaultWhenToSeeDoctor(symptom),
    faqs: c.faqs || defaultFaqs(symptom),
  };
}
