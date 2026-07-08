// Search Enhancement - autocomplete seeds + helpers

export interface SearchSuggestion {
  text: string;
  category: string;
  type: 'symptom' | 'supplement' | 'category';
}

/** Static seeds (zh-HK / en mixed) — live symptom names are merged in SearchBar */
export const searchSuggestions: SearchSuggestion[] = [
  // Symptoms
  { text: '頭痛', category: 'brain-cognitive', type: 'symptom' },
  { text: '失眠', category: 'sleep-mood', type: 'symptom' },
  { text: '疲勞', category: 'heart-health', type: 'symptom' },
  { text: '脫髮', category: 'hair-skin-nails', type: 'symptom' },
  { text: '壓力', category: 'sleep-mood', type: 'symptom' },
  { text: '焦慮', category: 'sleep-mood', type: 'symptom' },
  { text: '眼睛', category: 'eye-vision', type: 'symptom' },
  { text: '體重', category: 'weight-management', type: 'symptom' },
  { text: '消化', category: 'digestive-support', type: 'symptom' },
  { text: '關節', category: 'bone-joint', type: 'symptom' },
  { text: '免疫', category: 'immune', type: 'symptom' },
  { text: 'headache', category: 'brain-cognitive', type: 'symptom' },
  { text: 'insomnia', category: 'sleep-mood', type: 'symptom' },
  { text: 'fatigue', category: 'heart-health', type: 'symptom' },

  // Supplements
  { text: '維他命B', category: 'all', type: 'supplement' },
  { text: '魚油', category: 'all', type: 'supplement' },
  { text: '鋅', category: 'all', type: 'supplement' },
  { text: '鎂', category: 'all', type: 'supplement' },
  { text: '維他命D', category: 'all', type: 'supplement' },
  { text: '益生菌', category: 'all', type: 'supplement' },
  { text: '南非醉茄', category: 'all', type: 'supplement' },
  { text: '膠原蛋白', category: 'all', type: 'supplement' },
  { text: 'magnesium', category: 'all', type: 'supplement' },
  { text: 'probiotics', category: 'all', type: 'supplement' },

  // Categories (ids must match symptoms.category_id)
  { text: '睡眠情緒', category: 'sleep-mood', type: 'category' },
  { text: '消化腸胃', category: 'digestive-support', type: 'category' },
  { text: '頭髮皮膚', category: 'hair-skin-nails', type: 'category' },
  { text: '女性健康', category: 'womens-health', type: 'category' },
  { text: '免疫力', category: 'immune', type: 'category' },
  { text: '骨骼關節', category: 'bone-joint', type: 'category' },
];

export function getSuggestions(query: string, limit: number = 5): SearchSuggestion[] {
  if (!query.trim()) return [];

  const q = query.toLowerCase();
  return searchSuggestions.filter((s) => s.text.toLowerCase().includes(q)).slice(0, limit);
}
