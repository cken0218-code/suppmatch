// Supplement Product Data with Affiliate Links
// Affiliate IDs applied via affiliateConfig at read time

import { withAmazonAffiliate, withIherbAffiliate } from '@/data/affiliateConfig';

export interface Product {
  id: string;
  name: string;
  nameZh: string;
  brand: string;
  iherbUrl: string;
  amazonUrl: string;
  priceRange: string;
  /** Internal only — never display to users */
  commission: string;
  tags: string[];
}

function p(
  partial: Omit<Product, 'commission'> & { commission?: string },
): Product {
  return { ...partial, commission: partial.commission || '8%' };
}

/** Search-style fallbacks that still work with affiliate params */
function iherbSearch(kw: string) {
  return `https://www.iherb.com/search?kw=${encodeURIComponent(kw)}`;
}
function amazonSearch(kw: string) {
  return `https://www.amazon.com/s?k=${encodeURIComponent(kw)}`;
}

export const supplementProducts: Record<string, Product[]> = {
  'vitamin-b-complex': [
    p({
      id: 'now-b-complex',
      name: 'NOW Foods Vitamin B-Complex',
      nameZh: 'NOW Foods 維他命B群',
      brand: 'NOW Foods',
      iherbUrl:
        'https://www.iherb.com/pr/now-foods-vitamin-b-complex-100-vegetarian-capsules-8149',
      amazonUrl: 'https://www.amazon.com/dp/B0019LHU0G',
      priceRange: '$10-15',
      tags: ['b-complex', 'energy', 'stress'],
    }),
    p({
      id: 'solgar-b-complex',
      name: 'Solgar Vitamin B-Complex',
      nameZh: 'Solgar 維他命B群',
      brand: 'Solgar',
      iherbUrl:
        'https://www.iherb.com/pr/solgar-vitamin-b-complex-100-vegetarian-capsules-17871',
      amazonUrl: 'https://www.amazon.com/dp/B000W2BGNK',
      priceRange: '$20-25',
      tags: ['b-complex', 'energy'],
    }),
  ],
  magnesium: [
    p({
      id: 'now-magnesium',
      name: 'NOW Foods Magnesium Citrate',
      nameZh: 'NOW Foods 鎂檸檬酸鹽',
      brand: 'NOW Foods',
      iherbUrl:
        'https://www.iherb.com/pr/now-foods-magnesium-citrate-250-capsules-58381',
      amazonUrl: 'https://www.amazon.com/dp/B0014PR1UQ',
      priceRange: '$12-18',
      tags: ['magnesium', 'sleep', 'muscle'],
    }),
    p({
      id: 'natural-vitality-magnesium',
      name: 'Natural Vitality Magnesium',
      nameZh: 'Natural Vitality 鎂',
      brand: 'Natural Vitality',
      iherbUrl:
        'https://www.iherb.com/pr/natural-vitality-natural-calm-magnesium-citrate-16-oz-58117',
      amazonUrl: 'https://www.amazon.com/dp/B0001YJ25W',
      priceRange: '$20-25',
      tags: ['magnesium', 'sleep', 'stress'],
    }),
  ],
  'fish-oil-omega-3': [
    p({
      id: 'nordic-naturel-omega-3',
      name: 'Nordic Naturals Ultimate Omega',
      nameZh: 'Nordic Naturals 終極魚油',
      brand: 'Nordic Naturals',
      iherbUrl:
        'https://www.iherb.com/pr/nordic-naturals-ultimate-omega-120-softgels-26233',
      amazonUrl: 'https://www.amazon.com/dp/B00KQXJS4W',
      priceRange: '$30-40',
      commission: '10%',
      tags: ['omega-3', 'heart', 'brain'],
    }),
    p({
      id: 'now-fish-oil',
      name: 'NOW Foods Ultra Omega-3',
      nameZh: 'NOW Foods 超級魚油',
      brand: 'NOW Foods',
      iherbUrl:
        'https://www.iherb.com/pr/now-foods-ultra-omega-3-900-mg-180-softgels-6023',
      amazonUrl: 'https://www.amazon.com/dp/B0013PWK2G',
      priceRange: '$25-30',
      tags: ['omega-3', 'heart'],
    }),
  ],
  'vitamin-d3': [
    p({
      id: 'now-vitamin-d3',
      name: 'NOW Foods Vitamin D3',
      nameZh: 'NOW Foods 維他命D3',
      brand: 'NOW Foods',
      iherbUrl:
        'https://www.iherb.com/pr/now-foods-vitamin-d3-10-000-iu-240-softgels-58336',
      amazonUrl: 'https://www.amazon.com/dp/B0014PR0A2',
      priceRange: '$10-15',
      tags: ['vitamin-d', 'immune', 'bone'],
    }),
    p({
      id: 'garden-of-life-d3',
      name: 'Garden of Life Vitamin D3',
      nameZh: 'Garden of Life 維他命D3',
      brand: 'Garden of Life',
      iherbUrl: 'https://www.iherb.com/pr/garden-of-life-vitamin-d3-90-veg-caps-59132',
      amazonUrl: 'https://www.amazon.com/dp/B00KIDBDU8',
      priceRange: '$15-20',
      commission: '10%',
      tags: ['vitamin-d', 'immune'],
    }),
  ],
  zinc: [
    p({
      id: 'now-zinc',
      name: 'NOW Foods Zinc',
      nameZh: 'NOW Foods 鋅',
      brand: 'NOW Foods',
      iherbUrl: 'https://www.iherb.com/pr/now-foods-zinc-50-mg-120-capsules-58242',
      amazonUrl: 'https://www.amazon.com/dp/B0014PR0G2',
      priceRange: '$8-12',
      tags: ['zinc', 'immune', 'skin'],
    }),
    p({
      id: 'solgar-zinc',
      name: 'Solgar Zinc Picolinate',
      nameZh: 'Solgar 吡啶甲酸鋅',
      brand: 'Solgar',
      iherbUrl: iherbSearch('Solgar Zinc Picolinate'),
      amazonUrl: amazonSearch('Solgar Zinc Picolinate'),
      priceRange: '$10-15',
      tags: ['zinc', 'immune'],
    }),
  ],
  probiotics: [
    p({
      id: 'seed-daily-probiotic',
      name: 'SEED Daily Synbiotic',
      nameZh: 'SEED 每日共生菌',
      brand: 'SEED',
      iherbUrl: 'https://www.iherb.com/pr/seed-daily-synbiotic-60-capsules-90096',
      amazonUrl: 'https://www.amazon.com/dp/B07X4D8V4G',
      priceRange: '$50-60',
      commission: '15%',
      tags: ['probiotic', 'gut', 'digestion'],
    }),
    p({
      id: 'now-probiotics',
      name: 'NOW Foods Probiotic-10',
      nameZh: 'NOW Foods 益生菌-10',
      brand: 'NOW Foods',
      iherbUrl:
        'https://www.iherb.com/pr/now-foods-probiotic-10-25-billion-50-vegetarian-capsules-58354',
      amazonUrl: 'https://www.amazon.com/dp/B0014PR1UW',
      priceRange: '$20-25',
      tags: ['probiotic', 'gut'],
    }),
  ],
  coq10: [
    p({
      id: 'now-coq10',
      name: 'NOW Foods CoQ10',
      nameZh: 'NOW Foods 輔酶Q10',
      brand: 'NOW Foods',
      iherbUrl: 'https://www.iherb.com/pr/now-foods-coq10-200-mg-60-softgels-58041',
      amazonUrl: 'https://www.amazon.com/dp/B0014P2028',
      priceRange: '$25-30',
      tags: ['coq10', 'heart', 'energy'],
    }),
    p({
      id: 'doctor-best-coq10',
      name: "Doctor's Best High Absorption CoQ10",
      nameZh: "Doctor's Best 高吸收 CoQ10",
      brand: "Doctor's Best",
      iherbUrl: iherbSearch("Doctor's Best CoQ10"),
      amazonUrl: amazonSearch("Doctor's Best CoQ10"),
      priceRange: '$20-30',
      tags: ['coq10', 'heart'],
    }),
  ],
  ashwagandha: [
    p({
      id: 'now-ashwagandha',
      name: 'NOW Foods Ashwagandha',
      nameZh: 'NOW Foods 南非醉茄',
      brand: 'NOW Foods',
      iherbUrl:
        'https://www.iherb.com/pr/now-foods-ashwagandha-600-mg-120-vegetarian-capsules-58058',
      amazonUrl: 'https://www.amazon.com/dp/B0014PR1PA',
      priceRange: '$15-20',
      tags: ['ashwagandha', 'stress', 'sleep'],
    }),
    p({
      id: 'ksm66-ashwagandha',
      name: 'KSM-66 Ashwagandha',
      nameZh: 'KSM-66 南非醉茄',
      brand: 'KSM-66',
      iherbUrl: iherbSearch('KSM-66 Ashwagandha'),
      amazonUrl: amazonSearch('KSM-66 Ashwagandha'),
      priceRange: '$18-28',
      tags: ['ashwagandha', 'stress'],
    }),
  ],
  collagen: [
    p({
      id: 'vital-proteins-collagen',
      name: 'Vital Proteins Collagen',
      nameZh: 'Vital Proteins 膠原蛋白',
      brand: 'Vital Proteins',
      iherbUrl:
        'https://www.iherb.com/pr/vital-proteins-collagen-peptides-unflavored-221-oz-71769',
      amazonUrl: 'https://www.amazon.com/dp/B01N31WCWP',
      priceRange: '$25-35',
      commission: '12%',
      tags: ['collagen', 'skin', 'hair'],
    }),
    p({
      id: 'youtheory-collagen',
      name: 'Youtheory Collagen',
      nameZh: 'Youtheory 膠原蛋白',
      brand: 'Youtheory',
      iherbUrl: iherbSearch('Youtheory Collagen'),
      amazonUrl: amazonSearch('Youtheory Collagen'),
      priceRange: '$18-28',
      tags: ['collagen', 'skin'],
    }),
  ],
  multivitamin: [
    p({
      id: 'rainbow-light-multivitamin',
      name: 'Rainbow Light Multivitamin',
      nameZh: 'Rainbow Light 綜合維他命',
      brand: 'Rainbow Light',
      iherbUrl:
        'https://www.iherb.com/pr/rainbow-light-one-daily-multivitamin-150-tablets-38108',
      amazonUrl: 'https://www.amazon.com/dp/B0011E5M46',
      priceRange: '$20-25',
      commission: '10%',
      tags: ['multivitamin', 'daily', 'energy'],
    }),
    p({
      id: 'garden-of-life-multi',
      name: 'Garden of Life Multivitamin',
      nameZh: 'Garden of Life 綜合維他命',
      brand: 'Garden of Life',
      iherbUrl: iherbSearch('Garden of Life Multivitamin'),
      amazonUrl: amazonSearch('Garden of Life Multivitamin'),
      priceRange: '$25-35',
      tags: ['multivitamin', 'daily'],
    }),
  ],
  melatonin: [
    p({
      id: 'now-melatonin',
      name: 'NOW Foods Melatonin 3 mg',
      nameZh: 'NOW Foods 褪黑激素 3mg',
      brand: 'NOW Foods',
      iherbUrl: iherbSearch('NOW Melatonin 3 mg'),
      amazonUrl: amazonSearch('NOW Melatonin 3mg'),
      priceRange: '$6-12',
      tags: ['melatonin', 'sleep'],
    }),
    p({
      id: 'natrol-melatonin',
      name: 'Natrol Melatonin',
      nameZh: 'Natrol 褪黑激素',
      brand: 'Natrol',
      iherbUrl: iherbSearch('Natrol Melatonin'),
      amazonUrl: amazonSearch('Natrol Melatonin'),
      priceRange: '$8-14',
      tags: ['melatonin', 'sleep'],
    }),
  ],
  iron: [
    p({
      id: 'solgar-iron',
      name: 'Solgar Gentle Iron',
      nameZh: 'Solgar 溫和鐵',
      brand: 'Solgar',
      iherbUrl: iherbSearch('Solgar Gentle Iron'),
      amazonUrl: amazonSearch('Solgar Gentle Iron'),
      priceRange: '$10-16',
      tags: ['iron', 'energy', 'women'],
    }),
    p({
      id: 'nature-made-iron',
      name: 'Nature Made Iron',
      nameZh: 'Nature Made 鐵',
      brand: 'Nature Made',
      iherbUrl: iherbSearch('Nature Made Iron'),
      amazonUrl: amazonSearch('Nature Made Iron'),
      priceRange: '$8-14',
      tags: ['iron', 'energy'],
    }),
  ],
  biotin: [
    p({
      id: 'now-biotin',
      name: 'NOW Foods Biotin 5000 mcg',
      nameZh: 'NOW Foods 生物素 5000mcg',
      brand: 'NOW Foods',
      iherbUrl: iherbSearch('NOW Biotin 5000'),
      amazonUrl: amazonSearch('NOW Biotin 5000'),
      priceRange: '$8-14',
      tags: ['biotin', 'hair', 'skin'],
    }),
    p({
      id: 'natrol-biotin',
      name: 'Natrol Biotin',
      nameZh: 'Natrol 生物素',
      brand: 'Natrol',
      iherbUrl: iherbSearch('Natrol Biotin'),
      amazonUrl: amazonSearch('Natrol Biotin'),
      priceRange: '$8-15',
      tags: ['biotin', 'hair'],
    }),
  ],
  calcium: [
    p({
      id: 'now-calcium',
      name: 'NOW Foods Calcium Citrate',
      nameZh: 'NOW Foods 檸檬酸鈣',
      brand: 'NOW Foods',
      iherbUrl: iherbSearch('NOW Calcium Citrate'),
      amazonUrl: amazonSearch('NOW Calcium Citrate'),
      priceRange: '$10-16',
      tags: ['calcium', 'bone'],
    }),
    p({
      id: 'citracal-calcium',
      name: 'Citracal Calcium',
      nameZh: 'Citracal 鈣',
      brand: 'Citracal',
      iherbUrl: iherbSearch('Citracal Calcium'),
      amazonUrl: amazonSearch('Citracal Calcium'),
      priceRange: '$12-20',
      tags: ['calcium', 'bone'],
    }),
  ],
  lutein: [
    p({
      id: 'now-lutein',
      name: 'NOW Foods Lutein',
      nameZh: 'NOW Foods 葉黃素',
      brand: 'NOW Foods',
      iherbUrl: iherbSearch('NOW Lutein'),
      amazonUrl: amazonSearch('NOW Lutein'),
      priceRange: '$12-18',
      tags: ['lutein', 'eye'],
    }),
    p({
      id: 'bausch-ocuvite',
      name: 'Bausch + Lomb Ocuvite',
      nameZh: 'Bausch + Lomb Ocuvite 護眼',
      brand: 'Bausch + Lomb',
      iherbUrl: iherbSearch('Ocuvite Lutein'),
      amazonUrl: amazonSearch('Ocuvite Lutein'),
      priceRange: '$15-25',
      tags: ['lutein', 'eye'],
    }),
  ],
  'vitamin-c': [
    p({
      id: 'now-vitamin-c',
      name: 'NOW Foods Vitamin C-1000',
      nameZh: 'NOW Foods 維他命C 1000',
      brand: 'NOW Foods',
      iherbUrl: iherbSearch('NOW Vitamin C 1000'),
      amazonUrl: amazonSearch('NOW Vitamin C 1000'),
      priceRange: '$10-16',
      tags: ['vitamin-c', 'immune'],
    }),
    p({
      id: 'ester-c',
      name: 'Ester-C Vitamin C',
      nameZh: 'Ester-C 維他命C',
      brand: 'Ester-C',
      iherbUrl: iherbSearch('Ester-C'),
      amazonUrl: amazonSearch('Ester-C Vitamin C'),
      priceRange: '$12-20',
      tags: ['vitamin-c', 'immune'],
    }),
  ],
  'valerian-root': [
    p({
      id: 'now-valerian',
      name: 'NOW Foods Valerian Root',
      nameZh: 'NOW Foods 纈草根',
      brand: 'NOW Foods',
      iherbUrl: iherbSearch('NOW Valerian Root'),
      amazonUrl: amazonSearch('NOW Valerian Root'),
      priceRange: '$8-14',
      tags: ['valerian', 'sleep'],
    }),
    p({
      id: 'natures-way-valerian',
      name: "Nature's Way Valerian",
      nameZh: "Nature's Way 纈草",
      brand: "Nature's Way",
      iherbUrl: iherbSearch("Nature's Way Valerian"),
      amazonUrl: amazonSearch("Nature's Way Valerian"),
      priceRange: '$8-15',
      tags: ['valerian', 'sleep'],
    }),
  ],
  'digestive-enzymes': [
    p({
      id: 'now-digestive-enzymes',
      name: 'NOW Foods Super Enzymes',
      nameZh: 'NOW Foods 超級消化酶',
      brand: 'NOW Foods',
      iherbUrl: iherbSearch('NOW Super Enzymes'),
      amazonUrl: amazonSearch('NOW Super Enzymes'),
      priceRange: '$12-18',
      tags: ['enzymes', 'digestion'],
    }),
    p({
      id: 'enzymedica-digest',
      name: 'Enzymedica Digest Gold',
      nameZh: 'Enzymedica Digest Gold',
      brand: 'Enzymedica',
      iherbUrl: iherbSearch('Enzymedica Digest Gold'),
      amazonUrl: amazonSearch('Enzymedica Digest Gold'),
      priceRange: '$20-30',
      tags: ['enzymes', 'digestion'],
    }),
  ],
  'aloe-vera': [
    p({
      id: 'now-aloe',
      name: 'NOW Foods Aloe Vera',
      nameZh: 'NOW Foods 蘆薈',
      brand: 'NOW Foods',
      iherbUrl: iherbSearch('NOW Aloe Vera gel'),
      amazonUrl: amazonSearch('NOW Aloe Vera supplement'),
      priceRange: '$8-14',
      tags: ['aloe', 'digestion'],
    }),
    p({
      id: 'lily-aloe',
      name: 'Lily of the Desert Aloe',
      nameZh: 'Lily of the Desert 蘆薈',
      brand: 'Lily of the Desert',
      iherbUrl: iherbSearch('Lily of the Desert Aloe'),
      amazonUrl: amazonSearch('Lily of the Desert Aloe'),
      priceRange: '$10-16',
      tags: ['aloe', 'digestion'],
    }),
  ],
  keratin: [
    p({
      id: 'youtheory-keratin',
      name: 'Youtheory Keratin',
      nameZh: 'Youtheory 角蛋白',
      brand: 'Youtheory',
      iherbUrl: iherbSearch('Youtheory Keratin'),
      amazonUrl: amazonSearch('Youtheory Keratin'),
      priceRange: '$15-22',
      tags: ['keratin', 'hair'],
    }),
    p({
      id: 'sports-research-keratin',
      name: 'Sports Research Keratin',
      nameZh: 'Sports Research 角蛋白',
      brand: 'Sports Research',
      iherbUrl: iherbSearch('Sports Research Keratin'),
      amazonUrl: amazonSearch('Sports Research Keratin'),
      priceRange: '$18-25',
      tags: ['keratin', 'hair'],
    }),
  ],
  bilberry: [
    p({
      id: 'now-bilberry',
      name: 'NOW Foods Bilberry',
      nameZh: 'NOW Foods 山桑子',
      brand: 'NOW Foods',
      iherbUrl: iherbSearch('NOW Bilberry'),
      amazonUrl: amazonSearch('NOW Bilberry'),
      priceRange: '$12-18',
      tags: ['bilberry', 'eye'],
    }),
    p({
      id: 'natures-way-bilberry',
      name: "Nature's Way Bilberry",
      nameZh: "Nature's Way 山桑子",
      brand: "Nature's Way",
      iherbUrl: iherbSearch("Nature's Way Bilberry"),
      amazonUrl: amazonSearch("Nature's Way Bilberry"),
      priceRange: '$10-16',
      tags: ['bilberry', 'eye'],
    }),
  ],
  'vitamin-a': [
    p({
      id: 'now-vitamin-a',
      name: 'NOW Foods Vitamin A',
      nameZh: 'NOW Foods 維他命A',
      brand: 'NOW Foods',
      iherbUrl: iherbSearch('NOW Vitamin A'),
      amazonUrl: amazonSearch('NOW Vitamin A'),
      priceRange: '$6-12',
      tags: ['vitamin-a', 'eye'],
    }),
    p({
      id: 'solgar-vitamin-a',
      name: 'Solgar Vitamin A',
      nameZh: 'Solgar 維他命A',
      brand: 'Solgar',
      iherbUrl: iherbSearch('Solgar Vitamin A'),
      amazonUrl: amazonSearch('Solgar Vitamin A'),
      priceRange: '$8-14',
      tags: ['vitamin-a', 'eye'],
    }),
  ],
};

/** Map display / EN names → product catalog keys */
export const supplementMap: Record<string, string[]> = {
  '維他命B群': ['vitamin-b-complex'],
  'vitamin b complex': ['vitamin-b-complex'],
  '維他命B': ['vitamin-b-complex'],
  鎂: ['magnesium'],
  magnesium: ['magnesium'],
  魚油: ['fish-oil-omega-3'],
  'omega-3': ['fish-oil-omega-3'],
  'fish oil': ['fish-oil-omega-3'],
  'fish oil (omega-3)': ['fish-oil-omega-3'],
  維他命D: ['vitamin-d3'],
  'vitamin d': ['vitamin-d3'],
  維他命D3: ['vitamin-d3'],
  'vitamin d3': ['vitamin-d3'],
  鋅: ['zinc'],
  zinc: ['zinc'],
  益生菌: ['probiotics'],
  probiotic: ['probiotics'],
  probiotics: ['probiotics'],
  輔酶Q10: ['coq10'],
  coq10: ['coq10'],
  南非醉茄: ['ashwagandha'],
  ashwagandha: ['ashwagandha'],
  膠原蛋白: ['collagen'],
  collagen: ['collagen'],
  綜合維他命: ['multivitamin'],
  multivitamin: ['multivitamin'],
  褪黑激素: ['melatonin'],
  melatonin: ['melatonin'],
  鐵: ['iron'],
  iron: ['iron'],
  生物素: ['biotin'],
  biotin: ['biotin'],
  鈣: ['calcium'],
  calcium: ['calcium'],
  葉黃素: ['lutein'],
  lutein: ['lutein'],
  維他命C: ['vitamin-c'],
  'vitamin c': ['vitamin-c'],
  纈草: ['valerian-root'],
  'valerian root': ['valerian-root'],
  valerian: ['valerian-root'],
  消化酶: ['digestive-enzymes'],
  'digestive enzymes': ['digestive-enzymes'],
  蘆薈: ['aloe-vera'],
  'aloe vera': ['aloe-vera'],
  角蛋白: ['keratin'],
  keratin: ['keratin'],
  山桑子: ['bilberry'],
  bilberry: ['bilberry'],
  維他命A: ['vitamin-a'],
  'vitamin a': ['vitamin-a'],
};

function applyAffiliateLinks(product: Product): Product {
  return {
    ...product,
    iherbUrl: withIherbAffiliate(product.iherbUrl),
    amazonUrl: withAmazonAffiliate(product.amazonUrl),
  };
}

export function getProductsForSupplement(nameEn: string): Product[] {
  const key = nameEn.toLowerCase();
  let productKeys = supplementMap[key] || [];
  if (productKeys.length === 0) {
    for (const [mapKey, keys] of Object.entries(supplementMap)) {
      if (key.includes(mapKey) || mapKey.includes(key)) {
        productKeys = keys;
        break;
      }
    }
  }

  const products: Product[] = [];
  for (const pk of productKeys) {
    if (supplementProducts[pk]) {
      products.push(...supplementProducts[pk].map(applyAffiliateLinks));
    }
  }
  return products;
}
