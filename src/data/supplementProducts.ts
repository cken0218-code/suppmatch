// Supplement Product Data with Affiliate Links
// Add your affiliate IDs in .env or here directly

export interface Product {
  id: string;
  name: string;
  nameZh: string;
  brand: string;
  iherbUrl: string;
  amazonUrl: string;
  priceRange: string; // USD
  commission: string;
  tags: string[];
}

export const supplementProducts: Record<string, Product[]> = {
  'vitamin-b-complex': [
    {
      id: 'now-b-complex',
      name: 'NOW Foods Vitamin B-Complex',
      nameZh: 'NOW Foods 維他命B群',
      brand: 'NOW Foods',
      iherbUrl: 'https://www.iherb.com/pr/now-foods-vitamin-b-complex-100-vegetarian-capsules-8149?utm_campaign=t1g9e4&utm_medium=cpc&utm_source=google&rcode=MLG10',
      amazonUrl: 'https://www.amazon.com/dp/B0019LHU0G?tag=YOUR_AMAZON_TAG',
      priceRange: '$10-15',
      commission: '8%',
      tags: ['b-complex', 'energy', 'stress']
    },
    {
      id: 'solgar-b-complex',
      name: 'Solgar Vitamin B-Complex',
      nameZh: 'Solgar 維他命B群',
      brand: 'Solgar',
      iherbUrl: 'https://www.iherb.com/pr/solgar-vitamin-b-complex-100-vegetarian-capsules-17871?utm_campaign=t1g9e4&utm_medium=cpc&utm_source=google&rcode=MLG10',
      amazonUrl: 'https://www.amazon.com/dp/B000W2BGNK?tag=YOUR_AMAZON_TAG',
      priceRange: '$20-25',
      commission: '8%',
      tags: ['b-complex', 'energy']
    }
  ],
  'magnesium': [
    {
      id: 'now-magnesium',
      name: 'NOW Foods Magnesium Citrate',
      nameZh: 'NOW Foods 鎂檸檬酸鹽',
      brand: 'NOW Foods',
      iherbUrl: 'https://www.iherb.com/pr/now-foods-magnesium-citrate-250-capsules-58381?utm_campaign=t1g9e4&utm_medium=cpc&utm_source=google&rcode=MLG10',
      amazonUrl: 'https://www.amazon.com/dp/B0014PR1UQ?tag=YOUR_AMAZON_TAG',
      priceRange: '$12-18',
      commission: '8%',
      tags: ['magnesium', 'sleep', 'muscle']
    },
    {
      id: 'natural-vitality-magnesium',
      name: 'Natural Vitality Magnesium',
      nameZh: 'Natural Vitality 鎂',
      brand: 'Natural Vitality',
      iherbUrl: 'https://www.iherb.com/pr/natural-vitality-natural-calm-magnesium-citrate-16-oz-58117?utm_campaign=t1g9e4&utm_medium=cpc&utm_source=google&rcode=MLG10',
      amazonUrl: 'https://www.amazon.com/dp/B0001YJ25W?tag=YOUR_AMAZON_TAG',
      priceRange: '$20-25',
      commission: '8%',
      tags: ['magnesium', 'sleep', 'stress']
    }
  ],
  'fish-oil-omega-3': [
    {
      id: 'nordic-naturel-omega-3',
      name: 'Nordic Naturals Ultimate Omega',
      nameZh: 'Nordic Naturals 終極魚油',
      brand: 'Nordic Naturals',
      iherbUrl: 'https://www.iherb.com/pr/nordic-naturals-ultimate-omega-120-softgels-26233?utm_campaign=t1g9e4&utm_medium=cpc&utm_source=google&rcode=MLG10',
      amazonUrl: 'https://www.amazon.com/dp/B00KQXJS4W?tag=YOUR_AMAZON_TAG',
      priceRange: '$30-40',
      commission: '10%',
      tags: ['omega-3', 'heart', 'brain']
    },
    {
      id: 'now-fish-oil',
      name: 'NOW Foods Ultra Omega-3',
      nameZh: 'NOW Foods 超級魚油',
      brand: 'NOW Foods',
      iherbUrl: 'https://www.iherb.com/pr/now-foods-ultra-omega-3-900-mg-180-softgels-6023?utm_campaign=t1g9e4&utm_medium=cpc&utm_source=google&rcode=MLG10',
      amazonUrl: 'https://www.amazon.com/dp/B0013PWK2G?tag=YOUR_AMAZON_TAG',
      priceRange: '$25-30',
      commission: '8%',
      tags: ['omega-3', 'heart']
    }
  ],
  'vitamin-d3': [
    {
      id: 'now-vitamin-d3',
      name: 'NOW Foods Vitamin D3',
      nameZh: 'NOW Foods 維他命D3',
      brand: 'NOW Foods',
      iherbUrl: 'https://www.iherb.com/pr/now-foods-vitamin-d3-10-000-iu-240-softgels-58336?utm_campaign=t1g9e4&utm_medium=cpc&utm_source=google&rcode=MLG10',
      amazonUrl: 'https://www.amazon.com/dp/B0014PR0A2?tag=YOUR_AMAZON_TAG',
      priceRange: '$10-15',
      commission: '8%',
      tags: ['vitamin-d', 'immune', 'bone']
    },
    {
      id: 'garden-of-life-d3',
      name: 'Garden of Life Vitamin D3',
      nameZh: 'Garden of Life 維他命D3',
      brand: 'Garden of Life',
      iherbUrl: 'https://www.iherb.com/pr/garden-of-life-vitamin-d3-90-veg-caps-59132?utm_campaign=t1g9e4&utm_medium=cpc&utm_source=google&rcode=MLG10',
      amazonUrl: 'https://www.amazon.com/dp/B00KIDBDU8?tag=YOUR_AMAZON_TAG',
      priceRange: '$15-20',
      commission: '10%',
      tags: ['vitamin-d', 'immune']
    }
  ],
  'zinc': [
    {
      id: 'now-zinc',
      name: 'NOW Foods Zinc',
      nameZh: 'NOW Foods 鋅',
      brand: 'NOW Foods',
      iherbUrl: 'https://www.iherb.com/pr/now-foods-zinc-50-mg-120-capsules-58242?utm_campaign=t1g9e4&utm_medium=cpc&utm_source=google&rcode=MLG10',
      amazonUrl: 'https://www.amazon.com/dp/B0014PR0G2?tag=YOUR_AMAZON_TAG',
      priceRange: '$8-12',
      commission: '8%',
      tags: ['zinc', 'immune', 'skin']
    }
  ],
  'probiotics': [
    {
      id: 'seed-daily-probiotic',
      name: 'SEED Daily Synbiotic',
      nameZh: 'SEED 每日共生菌',
      brand: 'SEED',
      iherbUrl: 'https://www.iherb.com/pr/seed-daily-synbiotic-60-capsules-90096?utm_campaign=t1g9e4&utm_medium=cpc&utm_source=google&rcode=MLG10',
      amazonUrl: 'https://www.amazon.com/dp/B07X4D8V4G?tag=YOUR_AMAZON_TAG',
      priceRange: '$50-60',
      commission: '15%',
      tags: ['probiotic', 'gut', 'digestion']
    },
    {
      id: 'now-probiotics',
      name: 'NOW Foods Probiotic-10',
      nameZh: 'NOW Foods 益生菌-10',
      brand: 'NOW Foods',
      iherbUrl: 'https://www.iherb.com/pr/now-foods-probiotic-10-25-billion-50-vegetarian-capsules-58354?utm_campaign=t1g9e4&utm_medium=cpc&utm_source=google&rcode=MLG10',
      amazonUrl: 'https://www.amazon.com/dp/B0014PR1UW?tag=YOUR_AMAZON_TAG',
      priceRange: '$20-25',
      commission: '8%',
      tags: ['probiotic', 'gut']
    }
  ],
  'coq10': [
    {
      id: 'now-coq10',
      name: 'NOW Foods CoQ10',
      nameZh: 'NOW Foods 輔酶Q10',
      brand: 'NOW Foods',
      iherbUrl: 'https://www.iherb.com/pr/now-foods-coq10-200-mg-60-softgels-58041?utm_campaign=t1g9e4&utm_medium=cpc&utm_source=google&rcode=MLG10',
      amazonUrl: 'https://www.amazon.com/dp/B0014P2028?tag=YOUR_AMAZON_TAG',
      priceRange: '$25-30',
      commission: '8%',
      tags: ['coq10', 'heart', 'energy']
    }
  ],
  'ashwagandha': [
    {
      id: 'now-ashwagandha',
      name: 'NOW Foods Ashwagandha',
      nameZh: 'NOW Foods 南非醉茄',
      brand: 'NOW Foods',
      iherbUrl: 'https://www.iherb.com/pr/now-foods-ashwagandha-600-mg-120-vegetarian-capsules-58058?utm_campaign=t1g9e4&utm_medium=cpc&utm_source=google&rcode=MLG10',
      amazonUrl: 'https://www.amazon.com/B0014PR1PA?tag=YOUR_AMAZON_TAG',
      priceRange: '$15-20',
      commission: '8%',
      tags: ['ashwagandha', 'stress', 'sleep']
    }
  ],
  'collagen': [
    {
      id: 'vital-proteins-collagen',
      name: 'Vital Proteins Collagen',
      nameZh: 'Vital Proteins 膠原蛋白',
      brand: 'Vital Proteins',
      iherbUrl: 'https://www.iherb.com/pr/vital-proteins-collagen-peptides-unflavored-221-oz-71769?utm_campaign=t1g9e4&utm_medium=cpc&utm_source=google&rcode=MLG10',
      amazonUrl: 'https://www.amazon.com/dp/B01N31WCWP?tag=YOUR_AMAZON_TAG',
      priceRange: '$25-35',
      commission: '12%',
      tags: ['collagen', 'skin', 'hair']
    }
  ],
  'multivitamin': [
    {
      id: 'rainbow-light-multivitamin',
      name: 'Rainbow Light Multivitamin',
      nameZh: 'Rainbow Light 綜合維他命',
      brand: 'Rainbow Light',
      iherbUrl: 'https://www.iherb.com/pr/rainbow-light-one-daily-multivitamin-150-tablets-38108?utm_campaign=t1g9e4&utm_medium=cpc&utm_source=google&rcode=MLG10',
      amazonUrl: 'https://www.amazon.com/dp/B0011E5M46?tag=YOUR_AMAZON_TAG',
      priceRange: '$20-25',
      commission: '10%',
      tags: ['multivitamin', 'daily', 'energy']
    }
  ]
};

// Map supplement names to product keys
export const supplementMap: Record<string, string[]> = {
  '維他命B群': ['vitamin-b-complex'],
  'vitamin b complex': ['vitamin-b-complex'],
  '維他命B': ['vitamin-b-complex'],
  '鎂': ['magnesium'],
  'magnesium': ['magnesium'],
  '魚油': ['fish-oil-omega-3'],
  'omega-3': ['fish-oil-omega-3'],
  'fish oil': ['fish-oil-omega-3'],
  '維他命D': ['vitamin-d3'],
  'vitamin d': ['vitamin-d3'],
  '維他命D3': ['vitamin-d3'],
  '鋅': ['zinc'],
  'zinc': ['zinc'],
  '益生菌': ['probiotics'],
  'probiotic': ['probiotics'],
  '輔酶Q10': ['coq10'],
  'coq10': ['coq10'],
  '南非醉茄': ['ashwagandha'],
  'ashwagandha': ['ashwagandha'],
  '膠原蛋白': ['collagen'],
  'collagen': ['collagen'],
  '綜合維他命': ['multivitamin'],
  'multivitamin': ['multivitamin']
};

export function getProductsForSupplement(nameEn: string): Product[] {
  const key = nameEn.toLowerCase();
  const productKeys = supplementMap[key] || [];
  
  const products: Product[] = [];
  for (const pk of productKeys) {
    if (supplementProducts[pk]) {
      products.push(...supplementProducts[pk]);
    }
  }
  return products;
}
