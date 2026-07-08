export type CategoryLocale = 'zh-HK' | 'zh-CN' | 'en';

export interface CategoryMeta {
  id: string;
  names: Record<CategoryLocale, string>;
  emoji: string;
}

/** All symptom category_ids used in symptoms.ts */
export const CATEGORIES: CategoryMeta[] = [
  { id: 'sleep-mood', names: { 'zh-HK': '睡眠情緒', 'zh-CN': '睡眠情绪', en: 'Sleep & Mood' }, emoji: '😴' },
  { id: 'brain-cognitive', names: { 'zh-HK': '腦部認知', 'zh-CN': '脑部认知', en: 'Brain & Cognitive' }, emoji: '🧠' },
  { id: 'digestive-support', names: { 'zh-HK': '消化腸胃', 'zh-CN': '消化肠胃', en: 'Digestive' }, emoji: '🫙' },
  { id: 'immune', names: { 'zh-HK': '免疫力', 'zh-CN': '免疫力', en: 'Immune' }, emoji: '🛡️' },
  { id: 'heart-health', names: { 'zh-HK': '心臟能量', 'zh-CN': '心脏能量', en: 'Heart & Energy' }, emoji: '❤️' },
  { id: 'hair-skin-nails', names: { 'zh-HK': '頭髮皮膚', 'zh-CN': '头发皮肤', en: 'Hair & Skin' }, emoji: '✨' },
  { id: 'bone-joint', names: { 'zh-HK': '骨骼關節', 'zh-CN': '骨骼关节', en: 'Bone & Joint' }, emoji: '🦴' },
  { id: 'eye-vision', names: { 'zh-HK': '眼睛視力', 'zh-CN': '眼睛视力', en: 'Eye & Vision' }, emoji: '👁️' },
  { id: 'womens-health', names: { 'zh-HK': '女性健康', 'zh-CN': '女性健康', en: "Women's Health" }, emoji: '🌸' },
  { id: 'weight-management', names: { 'zh-HK': '體重管理', 'zh-CN': '体重管理', en: 'Weight' }, emoji: '⚖️' },
  { id: 'seasonal-allergies', names: { 'zh-HK': '季節過敏', 'zh-CN': '季节过敏', en: 'Allergies' }, emoji: '🤧' },
];

export const ALL_CATEGORY_ID = 'all';
