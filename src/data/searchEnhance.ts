// Search Enhancement - Additional search features
// Added: 2026-02-21

export interface SearchSuggestion {
  text: string;
  category: string;
  type: 'symptom' | 'supplement' | 'category';
}

// Common search queries to suggest
export const searchSuggestions: SearchSuggestion[] = [
  // Symptoms
  { text: '頭痛', category: 'brain-cognitive', type: 'symptom' },
  { text: '失眠', category: 'sleep-mood', type: 'symptom' },
  { text: '疲勞', category: 'energy', type: 'symptom' },
  { text: '脫髮', category: 'hair-skin-nails', type: 'symptom' },
  { text: '壓力', category: 'stress', type: 'symptom' },
  { text: '前列腺', category: 'mens-health', type: 'symptom' },
  { text: '甲狀腺', category: 'thyroid', type: 'symptom' },
  { text: '肝臟', category: 'liver-detox', type: 'symptom' },
  { text: '眼睛', category: 'eye-vision', type: 'symptom' },
  { text: '體重', category: 'weight-management', type: 'symptom' },
  
  // Supplements
  { text: '維他命B', category: 'all', type: 'supplement' },
  { text: '魚油', category: 'all', type: 'supplement' },
  { text: '鋅', category: 'all', type: 'supplement' },
  { text: '鎂', category: 'all', type: 'supplement' },
  { text: '維他命D', category: 'all', type: 'supplement' },
  { text: '奶薊', category: 'all', type: 'supplement' },
  { text: '南非醉茄', category: 'all', type: 'supplement' },
  
  // Categories
  { text: '男士健康', category: 'mens-health', type: 'category' },
  { text: '抗衰老', category: 'anti-aging', type: 'category' },
  { text: '能量', category: 'energy', type: 'category' },
];

export function getSuggestions(query: string, limit: number = 5): SearchSuggestion[] {
  if (!query.trim()) return [];
  
  const q = query.toLowerCase();
  return searchSuggestions
    .filter(s => s.text.toLowerCase().includes(q))
    .slice(0, limit);
}
