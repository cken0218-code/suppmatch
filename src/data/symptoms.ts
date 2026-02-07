export interface Symptom {
  id: string;
  category_id: string;
  names: {
    'zh-HK': string;
    'zh-CN': string;
    'en': string;
  };
  iherb_category: {
    name: string;
    url: string;
  };
  recommendations: {
    name: {
      'zh-HK': string;
      'zh-CN': string;
      'en': string;
    };
  }[];
}

export const symptoms: Symptom[] = [
  {
    id: "headache",
    category_id: "brain-cognitive",
    names: {
      "zh-HK": "頭痛",
      "zh-CN": "头痛",
      "en": "Headache"
    },
    iherb_category: {
      name: "Brain & Cognitive",
      url: "https://www.iherb.com/c/brain-cognitive"
    },
    recommendations: [
      { name: { "zh-HK": "維他命B群", "zh-CN": "维生素B群", "en": "Vitamin B Complex" } },
      { name: { "zh-HK": "鎂(Magnesium)", "zh-CN": "镁(Magnesium)", "en": "Magnesium" } },
      { name: { "zh-HK": "魚油(Omega-3)", "zh-CN": "鱼油(Omega-3)", "en": "Fish Oil (Omega-3)" } }
    ]
  },
  {
    id: "insomnia",
    category_id: "sleep-mood",
    names: {
      "zh-HK": "失眠/睡眠質素差",
      "zh-CN": "失眠/睡眠质量差",
      "en": "Insomnia / Poor Sleep"
    },
    iherb_category: {
      name: "Sleep & Mood",
      url: "https://www.iherb.com/c/sleep-mood"
    },
    recommendations: [
      { name: { "zh-HK": "褪黑激素(Melatonin)", "zh-CN": "褪黑激素(Melatonin)", "en": "Melatonin" } },
      { name: { "zh-HK": "纈草(Valerian Root)", "zh-CN": "缬草(Valerian Root)", "en": "Valerian Root" } },
      { name: { "zh-HK": "鎂(Magnesium)", "zh-CN": "镁(Magnesium)", "en": "Magnesium" } }
    ]
  },
  {
    id: "fatigue",
    category_id: "heart-health",
    names: {
      "zh-HK": "疲勞/冇精神",
      "zh-CN": "疲劳/没精神",
      "en": "Fatigue / Low Energy"
    },
    iherb_category: {
      name: "Heart Health",
      url: "https://www.iherb.com/c/heart-health"
    },
    recommendations: [
      { name: { "zh-HK": "維他命B群", "zh-CN": "维生素B群", "en": "Vitamin B Complex" } },
      { name: { "zh-HK": "鐵(Iron)", "zh-CN": "铁(Iron)", "en": "Iron" } },
      { name: { "zh-HK": "CoQ10", "zh-CN": "CoQ10", "en": "CoQ10" } }
    ]
  },
  {
    id: "hair-loss",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "甩頭髮/頭髮脆弱",
      "zh-CN": "掉发/头发脆弱",
      "en": "Hair Loss / Brittle Hair"
    },
    iherb_category: {
      name: "Hair, Skin & Nails",
      url: "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations: [
      { name: { "zh-HK": "生物素(Biotin)", "zh-CN": "生物素(Biotin)", "en": "Biotin" } },
      { name: { "zh-HK": "鋅(Zinc)", "zh-CN": "锌(Zinc)", "en": "Zinc" } },
      { name: { "zh-HK": "角蛋白(Keratin)", "zh-CN": "角蛋白(Keratin)", "en": "Keratin" } }
    ]
  },
  {
    id: "digestive-issues",
    category_id: "digestive-support",
    names: {
      "zh-HK": "消化不良/腸胃問題",
      "zh-CN": "消化不良/肠胃问题",
      "en": "Digestive Issues"
    },
    iherb_category: {
      name: "Digestive Support",
      url: "https://www.iherb.com/c/digestive-support"
    },
    recommendations: [
      { name: { "zh-HK": "益生菌(Probiotics)", "zh-CN": "益生菌(Probiotics)", "en": "Probiotics" } },
      { name: { "zh-HK": "消化酶(Digestive Enzymes)", "zh-CN": "消化酶(Digestive Enzymes)", "en": "Digestive Enzymes" } },
      { name: { "zh-HK": "蘆薈(Aloe Vera)", "zh-CN": "芦荟(Aloe Vera)", "en": "Aloe Vera" } }
    ]
  },
  {
    id: "stress-anxiety",
    category_id: "sleep-mood",
    names: {
      "zh-HK": "壓力大/焦慮",
      "zh-CN": "压力大/焦虑",
      "en": "Stress / Anxiety"
    },
    iherb_category: {
      name: "Sleep & Mood",
      url: "https://www.iherb.com/c/sleep-mood"
    },
    recommendations: [
      { name: { "zh-HK": "南非醉茄(Ashwagandha)", "zh-CN": "南非醉茄(Ashwagandha)", "en": "Ashwagandha" } },
      { name: { "zh-HK": "鎂(Magnesium)", "zh-CN": "镁(Magnesium)", "en": "Magnesium" } },
      { name: { "zh-HK": "維他命B群", "zh-CN": "维生素B群", "en": "Vitamin B Complex" } }
    ]
  },
  {
    id: "eye-strain",
    category_id: "eye-vision",
    names: {
      "zh-HK": "眼睛疲勞/視力問題",
      "zh-CN": "眼睛疲劳/视力问题",
      "en": "Eye Strain / Vision Issues"
    },
    iherb_category: {
      name: "Eye Vision",
      url: "https://www.iherb.com/c/eye-vision"
    },
    recommendations: [
      { name: { "zh-HK": "葉黃素(Lutein)", "zh-CN": "叶黄素(Lutein)", "en": "Lutein" } },
      { name: { "zh-HK": "山桑子(Bilberry)", "zh-CN": "山桑子(Bilberry)", "en": "Bilberry" } },
      { name: { "zh-HK": "維他命A", "zh-CN": "维生素A", "en": "Vitamin A" } }
    ]
  },
  {
    id: "bone-joint-pain",
    category_id: "bone-joint",
    names: {
      "zh-HK": "骨頭/關節痛",
      "zh-CN": "骨头/关节痛",
      "en": "Bone / Joint Pain"
    },
    iherb_category: {
      name: "Bone, Joint & Cartilage",
      url: "https://www.iherb.com/c/bone-joint"
    },
    recommendations: [
      { name: { "zh-HK": "葡萄糖胺(Glucosamine)", "zh-CN": "葡萄糖胺(Glucosamine)", "en": "Glucosamine" } },
      { name: { "zh-HK": "軟骨素(Chondroitin)", "zh-CN": "软骨素(Chondroitin)", "en": "Chondroitin" } },
      { name: { "zh-HK": "維他命D3", "zh-CN": "维生素D3", "en": "Vitamin D3" } }
    ]
  },
  {
    id: "skin-problems",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "皮膚問題(暗瘡/乾燥)",
      "zh-CN": "皮肤问题(暗疮/干燥)",
      "en": "Skin Problems (Acne/Dryness)"
    },
    iherb_category: {
      name: "Hair, Skin & Nails",
      url: "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations: [
      { name: { "zh-HK": "維他命C", "zh-CN": "维生素C", "en": "Vitamin C" } },
      { name: { "zh-HK": "鋅(Zinc)", "zh-CN": "锌(Zinc)", "en": "Zinc" } },
      { name: { "zh-HK": "椰子油(Coconut Oil)", "zh-CN": "椰子油(Coconut Oil)", "en": "Coconut Oil" } }
    ]
  },
  {
    id: "weak-immunity",
    category_id: "immune",
    names: {
      "zh-HK": "免疫力低/成日病",
      "zh-CN": "免疫力低/成日病",
      "en": "Weak Immunity / Get Sick Easily"
    },
    iherb_category: {
      name: "Immune Support",
      url: "https://www.iherb.com/c/immune-support"
    },
    recommendations: [
      { name: { "zh-HK": "維他命C", "zh-CN": "维生素C", "en": "Vitamin C" } },
      { name: { "zh-HK": "維他命D3", "zh-CN": "维生素D3", "en": "Vitamin D3" } },
      { name: { "zh-HK": "鋅(Zinc)", "zh-CN": "锌(Zinc)", "en": "Zinc" } }
    ]
  },
  {
    id: "memory-issues",
    category_id: "brain-cognitive",
    names: {
      "zh-HK": "記憶力差/專注力不足",
      "zh-CN": "记忆力差/专注力不足",
      "en": "Poor Memory / Focus Issues"
    },
    iherb_category: {
      name: "Brain & Cognitive",
      url: "https://www.iherb.com/c/brain-cognitive"
    },
    recommendations: [
      { name: { "zh-HK": "磷脂酰絲氨酸(PS)", "zh-CN": "磷脂酰丝氨酸(PS)", "en": "Phosphatidylserine (PS)" } },
      { name: { "zh-HK": "銀杏(Ginkgo Biloba)", "zh-CN": "银杏(Ginkgo Biloba)", "en": "Ginkgo Biloba" } },
      { name: { "zh-HK": "Omega-3", "zh-CN": "Omega-3", "en": "Omega-3" } }
    ]
  },
  {
    id: "menstrual-issues",
    category_id: "womens-health",
    names: {
      "zh-HK": "經期問題",
      "zh-CN": "经期问题",
      "en": "Menstrual Issues"
    },
    iherb_category: {
      name: "Women's Health",
      url: "https://www.iherb.com/c/womens-health"
    },
    recommendations: [
      { name: { "zh-HK": "鐵(Iron)", "zh-CN": "铁(Iron)", "en": "Iron" } },
      { name: { "zh-HK": "月見草油(EPO)", "zh-CN": "月见草油(EPO)", "en": "Evening Primrose Oil" } },
      { name: { "zh-HK": "維他命B6", "zh-CN": "维生素B6", "en": "Vitamin B6" } }
    ]
  },
  {
    id: "allergies",
    category_id: "seasonal-allergies",
    names: {
      "zh-HK": "過敏/季節性敏感",
      "zh-CN": "过敏/季节性敏感",
      "en": "Allergies / Seasonal Sensitivities"
    },
    iherb_category: {
      name: "Seasonal Allergies",
      url: "https://www.iherb.com/c/seasonal-allergies"
    },
    recommendations: [
      { name: { "zh-HK": "維他命C", "zh-CN": "维生素C", "en": "Vitamin C" } },
      { name: { "zh-HK": "槲皮素(Quercetin)", "zh-CN": "槲皮素(Quercetin)", "en": "Quercetin" } },
      { name: { "zh-HK": "益生菌(Probiotics)", "zh-CN": "益生菌(Probiotics)", "en": "Probiotics" } }
    ]
  },
  {
    id: "weight-management",
    category_id: "weight-management",
    names: {
      "zh-HK": "體重管理",
      "zh-CN": "体重管理",
      "en": "Weight Management"
    },
    iherb_category: {
      name: "Weight Management",
      url: "https://www.iherb.com/c/weight-management"
    },
    recommendations: [
      { name: { "zh-HK": "綠茶萃取(Green Tea Extract)", "zh-CN": "绿茶萃取(Green Tea Extract)", "en": "Green Tea Extract" } },
      { name: { "zh-HK": "蛋白質粉(Protein Powder)", "zh-CN": "蛋白质粉(Protein Powder)", "en": "Protein Powder" } },
      { name: { "zh-HK": "CLA", "zh-CN": "CLA", "en": "CLA" } }
    ]
  },
  {
    id: "heart-health",
    category_id: "heart-health",
    names: {
      "zh-HK": "心血管健康",
      "zh-CN": "心血管健康",
      "en": "Heart Health"
    },
    iherb_category: {
      name: "Heart Health",
      url: "https://www.iherb.com/c/heart-health"
    },
    recommendations: [
      { name: { "zh-HK": "魚油(Omega-3)", "zh-CN": "鱼油(Omega-3)", "en": "Fish Oil (Omega-3)" } },
      { name: { "zh-HK": "CoQ10", "zh-CN": "CoQ10", "en": "CoQ10" } },
      { name: { "zh-HK": "植物固醇(Plant Sterols)", "zh-CN": "植物固醇(Plant Sterols)", "en": "Plant Sterols" } }
    ]
  },
  {
    id: "dull-hair",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "頭髮暗淡/無光澤",
      "zh-CN": "头发暗淡/无光泽",
      "en": "Dull Hair / Lack of Shine"
    },
    iherb_category: {
      name: "Hair, Skin & Nails",
      url: "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations: [
      { name: { "zh-HK": "生物素(Biotin)", "zh-CN": "生物素(Biotin)", "en": "Biotin" } },
      { name: { "zh-HK": "角蛋白(Keratin)", "zh-CN": "角蛋白(Keratin)", "en": "Keratin" } },
      { name: { "zh-HK": "維他命E", "zh-CN": "维生素E", "en": "Vitamin E" } }
    ]
  },
  {
    id: "brittle-nails",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "指甲脆弱/易斷",
      "zh-CN": "指甲脆弱/易断",
      "en": "Brittle Nails"
    },
    iherb_category: {
      name: "Hair, Skin & Nails",
      url: "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations: [
      { name: { "zh-HK": "生物素(Biotin)", "zh-CN": "生物素(Biotin)", "en": "Biotin" } },
      { name: { "zh-HK": "鋅(Zinc)", "zh-CN": "锌(Zinc)", "en": "Zinc" } },
      { name: { "zh-HK": "矽(Silica)", "zh-CN": "矽(Silica)", "en": "Silica" } }
    ]
  },
  {
    id: "muscle-pain",
    category_id: "bone-joint",
    names: {
      "zh-HK": "肌肉酸痛",
      "zh-CN": "肌肉酸痛",
      "en": "Muscle Soreness / Pain"
    },
    iherb_category: {
      name: "Bone, Joint & Cartilage",
      url: "https://www.iherb.com/c/bone-joint"
    },
    recommendations: [
      { name: { "zh-HK": "鎂(Magnesium)", "zh-CN": "镁(Magnesium)", "en": "Magnesium" } },
      { name: { "zh-HK": "薑黃素(Curcumin)", "zh-CN": "姜黄素(Curcumin)", "en": "Curcumin" } },
      { name: { "zh-HK": "蛋白質粉(Protein)", "zh-CN": "蛋白质粉(Protein)", "en": "Protein Powder" } }
    ]
  },
  {
    id: "bloating",
    category_id: "digestive-support",
    names: {
      "zh-HK": "腹脹/胃氣",
      "zh-CN": "腹胀/胃气",
      "en": "Bloating / Gas"
    },
    iherb_category: {
      name: "Digestive Support",
      url: "https://www.iherb.com/c/digestive-support"
    },
    recommendations: [
      { name: { "zh-HK": "益生菌(Probiotics)", "zh-CN": "益生菌(Probiotics)", "en": "Probiotics" } },
      { name: { "zh-HK": "消化酶(Digestive Enzymes)", "zh-CN": "消化酶(Digestive Enzymes)", "en": "Digestive Enzymes" } },
      { name: { "zh-HK": "洋車前子(Psyllium Husk)", "zh-CN": "洋车前子(Psyllium Husk)", "en": "Psyllium Husk" } }
    ]
  },
  {
    id: "constipation",
    category_id: "digestive-support",
    names: {
      "zh-HK": "便秘",
      "zh-CN": "便秘",
      "en": "Constipation"
    },
    iherb_category: {
      name: "Digestive Support",
      url: "https://www.iherb.com/c/digestive-support"
    },
    recommendations: [
      { name: { "zh-HK": "洋車前子(Psyllium Husk)", "zh-CN": "洋车前子(Psyllium Husk)", "en": "Psyllium Husk" } },
      { name: { "zh-HK": "益生菌(Probiotics)", "zh-CN": "益生菌(Probiotics)", "en": "Probiotics" } },
      { name: { "zh-HK": "鎂(Magnesium)", "zh-CN": "镁(Magnesium)", "en": "Magnesium" } }
    ]
  },
  {
    id: "diarrhea",
    category_id: "digestive-support",
    names: {
      "zh-HK": "腹瀉/肚痾",
      "zh-CN": "腹泻/肚泻",
      "en": "Diarrhea / Upset Stomach"
    },
    iherb_category: {
      name: "Digestive Support",
      url: "https://www.iherb.com/c/digestive-support"
    },
    recommendations: [
      { name: { "zh-HK": "益生菌(Probiotics)", "zh-CN": "益生菌(Probiotics)", "en": "Probiotics" } },
      { name: { "zh-HK": "洋車前子(Psyllium Husk)", "zh-CN": "洋车前子(Psyllium Husk)", "en": "Psyllium Husk" } },
      { name: { "zh-HK": "鋅(Zinc)", "zh-CN": "锌(Zinc)", "en": "Zinc" } }
    ]
  },
  {
    id: "low-metabolism",
    category_id: "weight-management",
    names: {
      "zh-HK": "新陳代謝慢",
      "zh-CN": "新陈代谢慢",
      "en": "Slow Metabolism"
    },
    iherb_category: {
      name: "Weight Management",
      url: "https://www.iherb.com/c/weight-management"
    },
    recommendations: [
      { name: { "zh-HK": "碘(Iodine)", "zh-CN": "碘(Iodine)", "en": "Iodine" } },
      { name: { "zh-HK": "維他命B群", "zh-CN": "维生素B群", "en": "Vitamin B Complex" } },
      { name: { "zh-HK": "綠茶萃取(Green Tea)", "zh-CN": "绿茶萃取(Green Tea)", "en": "Green Tea Extract" } }
    ]
  },
  {
    id: "menopause",
    category_id: "womens-health",
    names: {
      "zh-HK": "更年期症狀",
      "zh-CN": "更年期症状",
      "en": "Menopause Symptoms"
    },
    iherb_category: {
      name: "Women's Health",
      url: "https://www.iherb.com/c/womens-health"
    },
    recommendations: [
      { name: { "zh-HK": "大豆異黃酮(Soy Isoflavones)", "zh-CN": "大豆异黄酮(Soy Isoflavones)", "en": "Soy Isoflavones" } },
      { name: { "zh-HK": "黑升麻(Black Cohosh)", "zh-CN": "黑升麻(Black Cohosh)", "en": "Black Cohosh" } },
      { name: { "zh-HK": "維他命E", "zh-CN": "维生素E", "en": "Vitamin E" } }
    ]
  },
  {
    id: "pms",
    category_id: "womens-health",
    names: {
      "zh-HK": "經前症候群(PMS)",
      "zh-CN": "经前症候群(PMS)",
      "en": "Premenstrual Syndrome (PMS)"
    },
    iherb_category: {
      name: "Women's Health",
      url: "https://www.iherb.com/c/womens-health"
    },
    recommendations: [
      { name: { "zh-HK": "月見草油(EPO)", "zh-CN": "月见草油(EPO)", "en": "Evening Primrose Oil" } },
      { name: { "zh-HK": "聖潔莓(Vitex)", "zh-CN": "圣洁莓(Vitex)", "en": "Vitex (Chasteberry)" } },
      { name: { "zh-HK": "維他命B6", "zh-CN": "维生素B6", "en": "Vitamin B6" } }
    ]
  },
  {
    id: "arthritis",
    category_id: "bone-joint",
    names: {
      "zh-HK": "關節炎",
      "zh-CN": "关节炎",
      "en": "Arthritis"
    },
    iherb_category: {
      name: "Bone, Joint & Cartilage",
      url: "https://www.iherb.com/c/bone-joint"
    },
    recommendations: [
      { name: { "zh-HK": "葡萄糖胺(Glucosamine)", "zh-CN": "葡萄糖胺(Glucosamine)", "en": "Glucosamine" } },
      { name: { "zh-HK": "軟骨素(Chondroitin)", "zh-CN": "软骨素(Chondroitin)", "en": "Chondroitin" } },
      { name: { "zh-HK": "薑黃素(Curcumin)", "zh-CN": "姜黄素(Curcumin)", "en": "Curcumin" } }
    ]
  },
  {
    id: "brain-fog",
    category_id: "brain-cognitive",
    names: {
      "zh-HK": "腦霧/專注力差",
      "zh-CN": "脑雾/专注力差",
      "en": "Brain Fog / Poor Focus"
    },
    iherb_category: {
      name: "Brain & Cognitive",
      url: "https://www.iherb.com/c/brain-cognitive"
    },
    recommendations: [
      { name: { "zh-HK": "Omega-3", "zh-CN": "Omega-3", "en": "Omega-3" } },
      { name: { "zh-HK": "磷脂酰絲氨酸(PS)", "zh-CN": "磷脂酰丝氨酸(PS)", "en": "Phosphatidylserine (PS)" } },
      { name: { "zh-HK": "銀杏(Ginkgo Biloba)", "zh-CN": "银杏(Ginkgo Biloba)", "en": "Ginkgo Biloba" } }
    ]
  },
  {
    id: "depression",
    category_id: "sleep-mood",
    names: {
      "zh-HK": "情緒低落/抑鬱",
      "zh-CN": "情绪低落/抑郁",
      "en": "Low Mood / Depression"
    },
    iherb_category: {
      name: "Sleep & Mood",
      url: "https://www.iherb.com/c/sleep-mood"
    },
    recommendations: [
      { name: { "zh-HK": "維他命D3", "zh-CN": "维生素D3", "en": "Vitamin D3" } },
      { name: { "zh-HK": "Omega-3", "zh-CN": "Omega-3", "en": "Omega-3" } },
      { name: { "zh-HK": "南非醉茄(Ashwagandha)", "zh-CN": "南非醉茄(Ashwagandha)", "en": "Ashwagandha" } }
    ]
  },
  {
    id: "eczema",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "濕疹/皮膚癢",
      "zh-CN": "湿疹/皮肤痒",
      "en": "Eczema / Itchy Skin"
    },
    iherb_category: {
      name: "Hair, Skin & Nails",
      url: "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations: [
      { name: { "zh-HK": "維他命D3", "zh-CN": "维生素D3", "en": "Vitamin D3" } },
      { name: { "zh-HK": "益生菌(Probiotics)", "zh-CN": "益生菌(Probiotics)", "en": "Probiotics" } },
      { name: { "zh-HK": "魚油(Omega-3)", "zh-CN": "鱼油(Omega-3)", "en": "Fish Oil (Omega-3)" } }
    ]
  },
  {
    id: "psoriasis",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "牛皮癬",
      "zh-CN": "牛皮癣",
      "en": "Psoriasis"
    },
    iherb_category: {
      name: "Hair, Skin & Nails",
      url: "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations: [
      { name: { "zh-HK": "魚油(Omega-3)", "zh-CN": "鱼油(Omega-3)", "en": "Fish Oil (Omega-3)" } },
      { name: { "zh-HK": "維他命D3", "zh-CN": "维生素D3", "en": "Vitamin D3" } },
      { name: { "zh-HK": "薑黃素(Curcumin)", "zh-CN": "姜黄素(Curcumin)", "en": "Curcumin" } }
    ]
  },
  {
    id: "premature-gray-hair",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "白頭髮/少年白",
      "zh-CN": "白头发/少年白",
      "en": "Premature Gray Hair"
    },
    iherb_category: {
      name: "Hair, Skin & Nails",
      url: "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations: [
      { name: { "zh-HK": "生物素(Biotin)", "zh-CN": "生物素(Biotin)", "en": "Biotin" } },
      { name: { "zh-HK": "銅(Copper)", "zh-CN": "铜(Copper)", "en": "Copper" } },
      { name: { "zh-HK": "維他命B12", "zh-CN": "维生素B12", "en": "Vitamin B12" } }
    ]
  },
  {
    id: "gum-bleeding",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "牙齦出血",
      "zh-CN": "牙龈出血",
      "en": "Bleeding Gums"
    },
    iherb_category: {
      name: "Hair, Skin & Nails",
      url: "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations: [
      { name: { "zh-HK": "維他命C", "zh-CN": "维生素C", "en": "Vitamin C" } },
      { name: { "zh-HK": "維他命K2", "zh-CN": "维生素K2", "en": "Vitamin K2" } },
      { name: { "zh-HK": "輔酶Q10(CoQ10)", "zh-CN": "辅酶Q10(CoQ10)", "en": "CoQ10" } }
    ]
  },
  {
    id: "bad-breath",
    category_id: "digestive-support",
    names: {
      "zh-HK": "口臭",
      "zh-CN": "口臭",
      "en": "Bad Breath"
    },
    iherb_category: {
      name: "Digestive Support",
      "url": "https://www.iherb.com/c/digestive-support"
    },
    recommendations: [
      { name: { "zh-HK": "益生菌", "zh-CN": "益生菌", "en": "Probiotics" } },
      { name: { "zh-HK": "綠茶萃取", "zh-CN": "绿茶萃取", "en": "Green Tea Extract" } },
      { name: { "zh-HK": "鋅", "zh-CN": "锌", "en": "Zinc" } }
    ]
  },
  {
    id: "sore-throat",
    category_id: "immune",
    names: {
      "zh-HK": "喉嚨痛",
      "zh-CN": "喉咙痛",
      "en": "Sore Throat"
    },
    iherb_category: {
      name: "Immune Support",
      "url": "https://www.iherb.com/c/immune-support"
    },
    recommendations: [
      { name: { "zh-HK": "維他命C", "zh-CN": "维生素C", "en": "Vitamin C" } },
      { name: { "zh-HK": "蜂蜜", "zh-CN": "蜂蜜", "en": "Honey" } },
      { name: { "zh-HK": "鋅", "zh-CN": "锌", "en": "Zinc" } }
    ]
  },
  {
    id: "frequent-colds",
    category_id: "immune",
    names: {
      "zh-HK": "成日感冒",
      "zh-CN": "成日感冒",
      "en": "Frequent Colds"
    },
    iherb_category: {
      name: "Immune Support",
      "url": "https://www.iherb.com/c/immune-support"
    },
    recommendations: [
      { name: { "zh-HK": "維他命C", "zh-CN": "维生素C", "en": "Vitamin C" } },
      { name: { "zh-HK": "維他命D3", "zh-CN": "维生素D3", "en": "Vitamin D3" } },
      { name: { "zh-HK": "紫錐花(Echinacea)", "zh-CN": "紫锥花(Echinacea)", "en": "Echinacea" } }
    ]
  },
  {
    id: "blurred-vision",
    category_id: "eye-vision",
    names: {
      "zh-HK": "視力模糊",
      "zh-CN": "视力模糊",
      "en": "Blurred Vision"
    },
    iherb_category: {
      name: "Eye Vision",
      "url": "https://www.iherb.com/c/eye-vision"
    },
    recommendations: [
      { name: { "zh-HK": "葉黃素", "zh-CN": "叶黄素", "en": "Lutein" } },
      { name: { "zh-HK": "山桑子", "zh-CN": "山桑子", "en": "Bilberry" } },
      { name: { "zh-HK": "魚油(Omega-3)", "zh-CN": "鱼油(Omega-3)", "en": "Fish Oil" } }
    ]
  },
  {
    id: "dry-eyes",
    category_id: "eye-vision",
    names: {
      "zh-HK": "眼睛乾澀",
      "zh-CN": "眼睛干涩",
      "en": "Dry Eyes"
    },
    iherb_category: {
      name: "Eye Vision",
      "url": "https://www.iherb.com/c/eye-vision"
    },
    recommendations: [
      { name: { "zh-HK": "魚油(Omega-3)", "zh-CN": "鱼油(Omega-3)", "en": "Fish Oil" } },
      { name: { "zh-HK": "維他命A", "zh-CN": "维生素A", "en": "Vitamin A" } },
      { name: { "zh-HK": "葉黃素", "zh-CN": "叶黄素", "en": "Lutein" } }
    ]
  },
  {
    id: "tinnitus",
    category_id: "brain-cognitive",
    names: {
      "zh-HK": "耳鳴",
      "zh-CN": "耳鸣",
      "en": "Tinnitus"
    },
    iherb_category: {
      name: "Brain & Cognitive",
      "url": "https://www.iherb.com/c/brain-cognitive"
    },
    recommendations: [
      { name: { "zh-HK": "銀杏", "zh-CN": "银杏", "en": "Ginkgo Biloba" } },
      { name: { "zh-HK": "鎂", "zh-CN": "镁", "en": "Magnesium" } },
      { name: { "zh-HK": "維他命B12", "zh-CN": "维生素B12", "en": "Vitamin B12" } }
    ]
  },
  {
    id: "dizziness",
    category_id: "brain-cognitive",
    names: {
      "zh-HK": "頭暈",
      "zh-CN": "头晕",
      "en": "Dizziness"
    },
    iherb_category: {
      name: "Brain & Cognitive",
      "url": "https://www.iherb.com/c/brain-cognitive"
    },
    recommendations: [
      { name: { "zh-HK": "維他命B12", "zh-CN": "维生素B12", "en": "Vitamin B12" } },
      { name: { "zh-HK": "鐵", "zh-CN": "铁", "en": "Iron" } },
      { name: { "zh-HK": "輔酶Q10", "zh-CN": "辅酶Q10", "en": "CoQ10" } }
    ]
  },
  {
    id: "anemia",
    category_id: "heart-health",
    names: {
      "zh-HK": "貧血",
      "zh-CN": "贫血",
      "en": "Anemia"
    },
    iherb_category: {
      name: "Heart Health",
      "url": "https://www.iherb.com/c/heart-health"
    },
    recommendations: [
      { name: { "zh-HK": "鐵", "zh-CN": "铁", "en": "Iron" } },
      { name: { "zh-HK": "維他命C", "zh-CN": "维生素C", "en": "Vitamin C" } },
      { name: { "zh-HK": "維他命B12", "zh-CN": "维生素B12", "en": "Vitamin B12" } }
    ]
  },
  {
    id: "cold-hands-feet",
    category_id: "heart-health",
    names: {
      "zh-HK": "手腳冰冷",
      "zh-CN": "手脚冰冷",
      "en": "Cold Hands & Feet"
    },
    iherb_category: {
      name: "Heart Health",
      "url": "https://www.iherb.com/c/heart-health"
    },
    recommendations: [
      { name: { "zh-HK": "鐵", "zh-CN": "铁", "en": "Iron" } },
      { name: { "zh-HK": "維他命B群", "zh-CN": "维生素B群", "en": "Vitamin B Complex" } },
      { name: { "zh-HK": "生薑萃取", "zh-CN": "生姜萃取", "en": "Ginger Extract" } }
    ]
  },
  {
    id: "frequent-urination",
    category_id: "digestive-support",
    names: {
      "zh-HK": "頻尿",
      "zh-CN": "频尿",
      "en": "Frequent Urination"
    },
    iherb_category: {
      name: "Digestive Support",
      "url": "https://www.iherb.com/c/digestive-support"
    },
    recommendations: [
      { name: { "zh-HK": "南瓜籽", "zh-CN": "南瓜籽", "en": "Pumpkin Seeds" } },
      { name: { "zh-HK": "鋸棕櫚", "zh-CN": "锯棕榈", "en": "Saw Palmetto" } },
      { name: { "zh-HK": "維他命D3", "zh-CN": "维生素D3", "en": "Vitamin D3" } }
    ]
  },
  {
    id: "hemorrhoids",
    category_id: "digestive-support",
    names: {
      "zh-HK": "痔瘡",
      "zh-CN": "痔疮",
      "en": "Hemorrhoids"
    },
    iherb_category: {
      name: "Digestive Support",
      "url": "https://www.iherb.com/c/digestive-support"
    },
    recommendations: [
      { name: { "zh-HK": "洋車前子", "zh-CN": "洋车前子", "en": "Psyllium Husk" } },
      { name: { "zh-HK": "生物類黃酮", "zh-CN": "生物类黄酮", "en": "Bioflavonoids" } },
      { name: { "zh-HK": "維他命C", "zh-CN": "维生素C", "en": "Vitamin C" } }
    ]
  },
  {
    id: "varicose-veins",
    category_id: "heart-health",
    names: {
      "zh-HK": "靜脈曲張",
      "zh-CN": "静脉曲张",
      "en": "Varicose Veins"
    },
    iherb_category: {
      name: "Heart Health",
      "url": "https://www.iherb.com/c/heart-health"
    },
    recommendations: [
      { name: { "zh-HK": "七葉樹萃取", "zh-CN": "七叶树萃取", "en": "Horse Chestnut Extract" } },
      { name: { "zh-HK": "維他命C", "zh-CN": "维生素C", "en": "Vitamin C" } },
      { name: { "zh-HK": "生物類黃酮", "zh-CN": "生物类黄酮", "en": "Bioflavonoids" } }
    ]
  },
  {
    id: "osteoporosis",
    category_id: "bone-joint",
    names: {
      "zh-HK": "骨質疏鬆",
      "zh-CN": "骨质疏松",
      "en": "Osteoporosis"
    },
    iherb_category: {
      name: "Bone, Joint & Cartilage",
      "url": "https://www.iherb.com/c/bone-joint"
    },
    recommendations: [
      { name: { "zh-HK": "維他命D3", "zh-CN": "维生素D3", "en": "Vitamin D3" } },
      { name: { "zh-HK": "鈣", "zh-CN": "钙", "en": "Calcium" } },
      { name: { "zh-HK": "維他命K2", "zh-CN": "维生素K2", "en": "Vitamin K2" } }
    ]
  },
  {
    id: "slow-wound-healing",
    category_id: "immune",
    names: {
      "zh-HK": "傷口癒合慢",
      "zh-CN": "伤口愈合慢",
      "en": "Slow Wound Healing"
    },
    iherb_category: {
      name: "Immune Support",
      "url": "https://www.iherb.com/c/immune-support"
    },
    recommendations: [
      { name: { "zh-HK": "維他命C", "zh-CN": "维生素C", "en": "Vitamin C" } },
      { name: { "zh-HK": "鋅", "zh-CN": "锌", "en": "Zinc" } },
      { name: { "zh-HK": "蛋白質", "zh-CN": "蛋白质", "en": "Protein" } }
    ]
  },
  {
    id: "cramps",
    category_id: "bone-joint",
    names: {
      "zh-HK": "抽筋",
      "zh-CN": "抽筋",
      "en": "Muscle Cramps"
    },
    iherb_category: {
      name: "Bone, Joint & Cartilage",
      "url": "https://www.iherb.com/c/bone-joint"
    },
    recommendations: [
      { name: { "zh-HK": "鎂", "zh-CN": "镁", "en": "Magnesium" } },
      { name: { "zh-HK": "鉀", "zh-CN": "钾", "en": "Potassium" } },
      { name: { "zh-HK": "鈣", "zh-CN": "钙", "en": "Calcium" } }
    ]
  },
  {
    id: "neck-pain",
    category_id: "bone-joint",
    names: {
      "zh-HK": "頸椎痛/頸痛",
      "zh-CN": "颈椎痛/颈痛",
      "en": "Neck Pain"
    },
    iherb_category: {
      name: "Bone, Joint & Cartilage",
      "url": "https://www.iherb.com/c/bone-joint"
    },
    recommendations: [
      { name: { "zh-HK": "薑黃素", "zh-CN": "姜黄素", "en": "Curcumin" } },
      { name: { "zh-HK": "鎂", "zh-CN": "镁", "en": "Magnesium" } },
      { name: { "zh-HK": "維他命D3", "zh-CN": "维生素D3", "en": "Vitamin D3" } }
    ]
  },
  {
    id: "lower-back-pain",
    category_id: "bone-joint",
    names: {
      "zh-HK": "腰椎痛/腰酸背痛",
      "zh-CN": "腰椎痛/腰酸背痛",
      "en": "Lower Back Pain"
    },
    iherb_category: {
      name: "Bone, Joint & Cartilage",
      "url": "https://www.iherb.com/c/bone-joint"
    },
    recommendations: [
      { name: { "zh-HK": "葡萄糖胺", "zh-CN": "葡萄糖胺", "en": "Glucosamine" } },
      { name: { "zh-HK": "維他命D3", "zh-CN": "维生素D3", "en": "Vitamin D3" } },
      { name: { "zh-HK": "薑黃素", "zh-CN": "姜黄素", "en": "Curcumin" } }
    ]
  },
  {
    id: "frozen-shoulder",
    category_id: "bone-joint",
    names: {
      "zh-HK": "肩周炎/五十肩",
      "zh-CN": "肩周炎/五十肩",
      "en": "Frozen Shoulder"
    },
    iherb_category: {
      name: "Bone, Joint & Cartilage",
      "url": "https://www.iherb.com/c/bone-joint"
    },
    recommendations: [
      { name: { "zh-HK": "葡萄糖胺", "zh-CN": "葡萄糖胺", "en": "Glucosamine" } },
      { name: { "zh-HK": "維他命D3", "zh-CN": "维生素D3", "en": "Vitamin D3" } },
      { name: { "zh-HK": "Omega-3", "zh-CN": "Omega-3", "en": "Omega-3" } }
    ]
  },
  {
    id: "carpal-tunnel",
    category_id: "bone-joint",
    names: {
      "zh-HK": "腕管綜合症",
      "zh-CN": "腕管综合症",
      "en": "Carpal Tunnel Syndrome"
    },
    iherb_category: {
      name: "Bone, Joint & Cartilage",
      "url": "https://www.iherb.com/c/bone-joint"
    },
    recommendations: [
      { name: { "zh-HK": "維他命B6", "zh-CN": "维生素B6", "en": "Vitamin B6" } },
      { name: { "zh-HK": "鎂", "zh-CN": "镁", "en": "Magnesium" } },
      { name: { "zh-HK": "薑黃素", "zh-CN": "姜黄素", "en": "Curcumin" } }
    ]
  },
  {
    id: "tennis-elbow",
    category_id: "bone-joint",
    names: {
      "zh-HK": "網球肘",
      "zh-CN": "网球肘",
      "en": "Tennis Elbow"
    },
    iherb_category: {
      name: "Bone, Joint & Cartilage",
      "url": "https://www.iherb.com/c/bone-joint"
    },
    recommendations: [
      { name: { "zh-HK": "薑黃素", "zh-CN": "姜黄素", "en": "Curcumin" } },
      { name: { "zh-HK": "鎂", "zh-CN": "镁", "en": "Magnesium" } },
      { name: { "zh-HK": "維他命C", "zh-CN": "维生素C", "en": "Vitamin C" } }
    ]
  },
  {
    id: "dry-skin",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "皮膚乾燥",
      "zh-CN": "皮肤干燥",
      "en": "Dry Skin"
    },
    iherb_category: {
      name: "Hair, Skin & Nails",
      "url": "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations: [
      { name: { "zh-HK": "魚油(Omega-3)", "zh-CN": "鱼油(Omega-3)", "en": "Fish Oil" } },
      { name: { "zh-HK": "維他命E", "zh-CN": "维生素E", "en": "Vitamin E" } },
      { name: { "zh-HK": "琉璃苣油", "zh-CN": "琉璃苣油", "en": "Borage Oil" } }
    ]
  },
  {
    id: "oily-skin",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "皮膚油膩",
      "zh-CN": "皮肤油腻",
      "en": "Oily Skin"
    },
    iherb_category: {
      name: "Hair, Skin & Nails",
      "url": "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations: [
      { name: { "zh-HK": "鋅", "zh-CN": "锌", "en": "Zinc" } },
      { name: { "zh-HK": "維他命B群", "zh-CN": "维生素B群", "en": "Vitamin B Complex" } },
      { name: { "zh-HK": "茶樹精油", "zh-CN": "茶树精油", "en": "Tea Tree Oil" } }
    ]
  },
  {
    id: "acne",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "暗瘡/青春痘",
      "zh-CN": "暗疮/青春痘",
      "en": "Acne"
    },
    iherb_category: {
      name: "Hair, Skin & Nails",
      "url": "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations: [
      { name: { "zh-HK": "鋅", "zh-CN": "锌", "en": "Zinc" } },
      { name: { "zh-HK": "維他命A", "zh-CN": "维生素A", "en": "Vitamin A" } },
      { name: { "zh-HK": "茶樹精油", "zh-CN": "茶树精油", "en": "Tea Tree Oil" } }
    ]
  },
  {
    id: "scars",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "疤痕/疤痕組織",
      "zh-CN": "疤痕/疤痕组织",
      "en": "Scars"
    },
    iherb_category: {
      name: "Hair, Skin & Nails",
      "url": "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations: [
      { name: { "zh-HK": "維他命C", "zh-CN": "维生素C", "en": "Vitamin C" } },
      { name: { "zh-HK": "矽", "zh-CN": "矽", "en": "Silica" } },
      { name: { "zh-HK": "積雪草", "zh-CN": "积雪草", "en": "Centella Asiatica" } }
    ]
  },
  {
    id: "stretch-marks",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "妊娠紋/肥胖紋",
      "zh-CN": "妊娠纹/肥胖纹",
      "en": "Stretch Marks"
    },
    iherb_category: {
      name: "Hair, Skin & Nails",
      "url": "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations: [
      { name: { "zh-HK": "維他命E", "zh-CN": "维生素E", "en": "Vitamin E" } },
      { name: { "zh-HK": "矽", "zh-CN": "矽", "en": "Silica" } },
      { name: { "zh-HK": "積雪草", "zh-CN": "积雪草", "en": "Centella Asiatica" } }
    ]
  },
  {
    id: "skin-aging",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "皮膚老化",
      "zh-CN": "皮肤老化",
      "en": "Skin Aging"
    },
    iherb_category: {
      name": "Hair, Skin & Nails",
      "url": "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations: [
      { name: { "zh-HK": "輔酶Q10", "zh-CN": "辅酶Q10", "en": "CoQ10" } },
      { name: { "zh-HK": "維他命C", "zh-CN": "维生素C", "en": "Vitamin C" } },
      { name: { "zh-HK": "蝦青素", "zh-CN": "虾青素", "en": "Astaxanthin" } }
    ]
  },
  {
    id: "wrinkles",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "皺紋/細紋",
      "zh-CN": "皱纹/细纹",
      "en": "Wrinkles"
    },
    iherb_category: {
      name": "Hair, Skin & Nails",
      "url": "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations: [
      { name: { "zh-HK": "輔酶Q10", "zh-CN": "辅酶Q10", "en": "CoQ10" } },
      { name: { "zh-HK": "維他命E", "zh-CN": "维生素E", "en": "Vitamin E" } },
      { name: { "zh-HK": "膠原蛋白", "zh-CN": "胶原蛋白", "en": "Collagen" } }
    ]
  },
  {
    id: "dark-circles",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "黑眼圈",
      "zh-CN": "黑眼圈",
      "en": "Dark Circles"
    },
    iherb_category: {
      name": "Hair, Skin & Nails",
      "url": "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations: [
      { name: { "zh-HK": "維他命K", "zh-CN": "维生素K", "en": "Vitamin K" } },
      { name: { "zh-HK": "維他命C", "zh-CN": "维生素C", "en": "Vitamin C" } },
      { name: { "zh-HK": "咖啡因", "zh-CN": "咖啡因", "en": "Caffeine" } }
    ]
  },
  {
    id: "eye-bags",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "眼袋",
      "zh-CN": "眼袋",
      "en": "Eye Bags"
    },
    iherb_category: {
      name": "Hair, Skin & Nails",
      "url": "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations: [
      { name: { "zh-HK": "咖啡因", "zh-CN": "咖啡因", "en": "Caffeine" } },
      { name: { "zh-HK": "維他命K", "zh-CN": "维生素K", "en": "Vitamin K" } },
      { name: { "zh-HK": "膠原蛋白", "zh-CN": "胶原蛋白", "en": "Collagen" } }
    ]
  },
  {
    id: "chapped-lips",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "嘴唇乾裂",
      "zh-CN": "嘴唇干裂",
      "en": "Chapped Lips"
    },
    iherb_category: {
      name": "Hair, Skin & Nails",
      "url": "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations: [
      { name: { "zh-HK": "維他命B2", "zh-CN": "维生素B2", "en": "Vitamin B2" } },
      { name: { "zh-HK": "維他命E", "zh-CN": "维生素E", "en": "Vitamin E" } },
      { name: { "zh-HK": "蜂蠟", "zh-CN": "蜂蜡", "en": "Beeswax" } }
    ]
  },
  {
    id: "mouth-ulcers",
    category_id: "digestive-support",
    names: {
      "zh-HK": "口腔潰痬/口瘡",
      "zh-CN": "口腔溃疡/口疮",
      "en": "Mouth Ulcers"
    },
    iherb_category: {
      name": "Digestive Support",
      "url": "https://www.iherb.com/c/digestive-support"
    },
    recommendations": [
      { name: { "zh-HK": "維他命B12", "zh-CN": "维生素B12", "en": "Vitamin B12" } },
      { name: { "zh-HK": "鐵", "zh-CN": "铁", "en": "Iron" } },
      { name: { "zh-HK": "益生菌", "zh-CN": "益生菌", "en": "Probiotics" } }
    ]
  },
  {
    id: "sensitive-teeth",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "牙齒敏感",
      "zh-CN": "牙齿敏感",
      "en": "Sensitive Teeth"
    },
    iherb_category: {
      name": "Hair, Skin & Nails",
      "url": "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations": [
      { name: { "zh-HK": "鈣", "zh-CN": "钙", "en": "Calcium" } },
      { name: { "zh-HK": "維他命D3", "zh-CN": "维生素D3", "en": "Vitamin D3" } },
      { name: { "zh-HK": "氟", "zh-CN": "氟", "en": "Fluoride" } }
    ]
  },
  {
    id: "hoarseness",
    category_id: "immune",
    names: {
      "zh-HK": "聲音嘶啞",
      "zh-CN": "声音嘶哑",
      "en": "Hoarseness"
    },
    iherb_category: {
      name": "Immune Support",
      "url": "https://www.iherb.com/c/immune-support"
    },
    recommendations": [
      { name: { "zh-HK": "蜂蜜", "zh-CN": "蜂蜜", "en": "Honey" } },
      { name: { "zh-HK": "生薑", "zh-CN": "生姜", "en": "Ginger" } },
      { name: { "zh-HK": "維他命C", "zh-CN": "维生素C", "en": "Vitamin C" } }
    ]
  },
  {
    id: "sinusitis",
    category_id: "immune",
    names: {
      "zh-HK": "鼻竇炎",
      "zh-CN": "鼻窦炎",
      "en": "Sinusitis"
    },
    iherb_category: {
      name": "Immune Support",
      "url": "https://www.iherb.com/c/immune-support"
    },
    recommendations": [
      { name: { "zh-HK": "維他命C", "zh-CN": "维生素C", "en": "Vitamin C" } },
      { name: { "zh-HK": "槲皮素", "zh-CN": "槲皮素", "en": "Quercetin" } },
      { name: { "zh-HK": "益生菌", "zh-CN": "益生菌", "en": "Probiotics" } }
    ]
  },
  {
    id: "allergic-rhinitis",
    category_id: "seasonal-allergies",
    names: {
      "zh-HK": "過敏性鼻炎",
      "zh-CN": "过敏性鼻炎",
      "en": "Allergic Rhinitis"
    },
    iherb_category: {
      name": "Seasonal Allergies",
      "url": "https://www.iherb.com/c/seasonal-allergies"
    },
    recommendations": [
      { name: { "zh-HK": "槲皮素", "zh-CN": "槲皮素", "en": "Quercetin" } },
      { name: { "zh-HK": "維他命C", "zh-CN": "维生素C", "en": "Vitamin C" } },
      { name: { "zh-HK": "益生菌", "zh-CN": "益生菌", "en": "Probiotics" } }
    ]
  },
  {
    id: "asthma",
    category_id: "immune",
    names: {
      "zh-HK": "哮喘",
      "zh-CN": "哮喘",
      "en": "Asthma"
    },
    iherb_category: {
      name": "Immune Support",
      "url": "https://www.iherb.com/c/immune-support"
    },
    recommendations": [
      { name: { "zh-HK": "魚油(Omega-3)", "zh-CN": "鱼油(Omega-3)", "en": "Fish Oil" } },
      { name: { "zh-HK": "維他命D3", "zh-CN": "维生素D3", "en": "Vitamin D3" } },
      { name: { "zh-HK": "鎂", "zh-CN": "镁", "en": "Magnesium" } }
    ]
  },
  {
    id: "bronchitis",
    category_id: "immune",
    names: {
      "zh-HK": "支氣管炎",
      "zh-CN": "支气管炎",
      "en": "Bronchitis"
    },
    iherb_category: {
      name": "Immune Support",
      "url": "https://www.iherb.com/c/immune-support"
    },
    recommendations": [
      { name: { "zh-HK": "維他命C", "zh-CN": "维生素C", "en": "Vitamin C" } },
      { name: { "zh-HK": "紫錐花", "zh-CN": "紫锥花", "en": "Echinacea" } },
      { name: { "zh-HK": "蜂膠", "zh-CN": "蜂胶", "en": "Propolis" } }
    ]
  },
  {
    id: "weak-lung",
    category_id: "immune",
    names: {
      "zh-HK": "肺功能弱",
      "zh-CN": "肺功能弱",
      "en": "Weak Lung Function"
    },
    iherb_category: {
      name": "Immune Support",
      "url": "https://www.iherb.com/c/immune-support"
    },
    recommendations": [
      { name: { "zh-HK": "魚油(Omega-3)", "zh-CN": "鱼油(Omega-3)", "en": "Fish Oil" } },
      { name: { "zh-HK": "維他命E", "zh-CN": "维生素E", "en": "Vitamin E" } },
      { name: { "zh-HK": "人參", "zh-CN": "人参", "en": "Ginseng" } }
    ]
  },
  {
    id: "shortness-breath",
    category_id": "heart-health",
    names: {
      "zh-HK": "氣短/呼吸急促",
      "zh-CN": "气短/呼吸急促",
      "en": "Shortness of Breath"
    },
    iherb_category: {
      name": "Heart Health",
      "url": "https://www.iherb.com/c/heart-health"
    },
    recommendations": [
      { name: { "zh-HK": "鐵", "zh-CN": "铁", "en": "Iron" } },
      { name: { "zh-HK": "CoQ10", "zh-CN": "CoQ10", "en": "CoQ10" } },
      { name: { "zh-HK": "維他命B12", "zh-CN": "维生素B12", "en": "Vitamin B12" } }
    ]
  },
  {
    id: "post-surgery-recovery",
    category_id": "immune",
    names: {
      "zh-HK": "手術後恢復",
      "zh-CN": "手术后恢复",
      "en": "Post-Surgery Recovery"
    },
    iherb_category: {
      name
  },
  {
    id: "hair-thinning",
    category_id: "hair-skin-nails",
    names: {
      "zh-HK": "頭髮稀疏",
      "zh-CN": "头发稀疏",
      "en": "Hair Thinning"
    },
    iherb_category: {
      name: "Hair, Skin and Nails",
      "url": "https://www.iherb.com/c/hair-skin-nails"
    },
    recommendations: [
      { name: { "zh-HK": "生物素(Biotin)", "zh-CN": "生物素(Biotin)", "en": "Biotin" } },
      { name: { "zh-HK": "角蛋白(Keratin)", "zh-CN": "角蛋白(Keratin)", "en": "Keratin" } },
      { name: { "zh-HK": "鋅(Zinc)", "zh-CN": "锌(Zinc)", "en": "Zinc" } }
    ]
  },
  {
    id: "hyperlipidemia",
    category_id: "heart-health",
    names: {
      "zh-HK": "高血脂/膽固醇高",
      "zh-CN": "高血脂/胆固醇高",
      "en": "High Cholesterol"
    },
    iherb_category: {
      name: "Heart Health",
      "url": "https://www.iherb.com/c/heart-health"
    },
    recommendations: [
      { name: { "zh-HK": "魚油(Omega-3)", "zh-CN": "鱼油(Omega-3)", "en": "Fish Oil" } },
      { name: { "zh-HK": "紅麴米", "zh-CN": "红曲米", "en": "Red Yeast Rice" } },
      { name: { "zh-HK": "植物固醇", "zh-CN": "植物固醇", "en": "Plant Sterols" } }
    ]
  },
  {
    id: "high-blood-pressure",
    category_id: "heart-health",
    names: {
      "zh-HK": "高血壓",
      "zh-CN": "高血压",
      "en": "High Blood Pressure"
    },
    iherb_category: {
      name: "Heart Health",
      "url": "https://www.iherb.com/c/heart-health"
    },
    recommendations: [
      { name: { "zh-HK": "魚油(Omega-3)", "zh-CN": "鱼油(Omega-3)", "en": "Fish Oil" } },
      { name: { "zh-HK": "輔酶Q10", "zh-CN": "辅酶Q10", "en": "CoQ10" } },
      { name: { "zh-HK": "大蒜精華", "zh-CN": "大蒜精华", "en": "Garlic Extract" } }
    ]
  },
  {
    id: "high-blood-sugar",
    category_id: "heart-health",
    names: {
      "zh-HK": "高血糖/糖尿病前期",
      "zh-CN": "高血糖/糖尿病前期",
      "en": "High Blood Sugar"
    },
    iherb_category: {
      name: "Heart Health",
      "url": "https://www.iherb.com/c/heart-health"
    },
    recommendations: [
      { name: { "zh-HK": "肉桂", "zh-CN": "肉桂", "en": "Cinnamon" } },
      { name: { "zh-HK": "鉻", "zh-CN": "铬", "en": "Chromium" } },
      { name: { "zh-HK": "苦瓜勝肽", "zh-CN": "苦瓜胜肽", "en": "Bitter Melon" } }
    ]
  },
  {
    id: "liver-detox",
    category_id: "digestive-support",
    names: {
      "zh-HK": "肝臟排毒/護肝",
      "zh-CN": "肝脏排毒/护肝",
      "en": "Liver Detox"
    },
    iherb_category: {
      name: "Digestive Support",
      "url": "https://www.iherb.com/c/digestive-support"
    },
    recommendations: [
      { name: { "zh-HK": "奶薊", "zh-CN": "奶蓟", "en": "Milk Thistle" } },
      { name: { "zh-HK": "薑黃", "zh-CN": "姜黄", "en": "Curcumin" } },
      { name: { "zh-HK": "NAC", "zh-CN": "NAC", "en": "NAC" } }
    ]
  },
  {
    id: "thyroid-support",
    category_id: "heart-health",
    names: {
      "zh-HK": "甲狀腺支持",
      "zh-CN": "甲状腺支持",
      "en": "Thyroid Support"
    },
    iherb_category: {
      name: "Heart Health",
      "url": "https://www.iherb.com/c/heart-health"
    },
    recommendations: [
      { name: { "zh-HK": "碘", "zh-CN": "碘", "en": "Iodine" } },
      { name: { "zh-HK": "硒", "zh-CN": "硒", "en": "Selenium" } },
      { name: { "zh-HK": "鋅", "zh-CN": "锌", "en": "Zinc" } }
    ]
  },
  {
    id: "prostate-health",
    category_id: "heart-health",
    names: {
      "zh-HK": "前列腺健康",
      "zh-CN": "前列腺健康",
      "en": "Prostate Health"
    },
    iherb_category: {
      name: "Heart Health",
      "url": "https://www.iherb.com/c/heart-health"
    },
    recommendations: [
      { name: { "zh-HK": "鋸棕櫚", "zh-CN": "锯棕榈", "en": "Saw Palmetto" } },
      { name: { "zh-HK": "南瓜籽", "zh-CN": "南瓜籽", "en": "Pumpkin Seed" } },
      { name: { "zh-HK": "番茄紅素", "zh-CN": "番茄红素", "en": "Lycopene" } }
    ]
  },
  {
    id: "athletic-performance",
    category_id: "bone-joint",
    names: {
      "zh-HK": "運動表現/體能提升",
      "zh-CN": "运动表现/体能提升",
      "en": "Athletic Performance"
    },
    iherb_category: {
      name: "Bone, Joint and Cartilage",
      "url": "https://www.iherb.com/c/bone-joint"
    },
    recommendations: [
      { name: { "zh-HK": "乳清蛋白", "zh-CN": "乳清蛋白", "en": "Whey Protein" } },
      { name: { "zh-HK": "BCAA", "zh-CN": "BCAA", "en": "BCAA" } },
      { name: { "zh-HK": "Beta-丙氨酸", "zh-CN": "Beta-丙氨酸", "en": "Beta-Alanine" } }
    ]
  },
  {
    id: "muscle-building",
    category_id: "bone-joint",
    names: {
      "zh-HK": "肌肉增長/增肌",
      "zh-CN": "肌肉增长/增肌",
      "en": "Muscle Building"
    },
    iherb_category: {
      name: "Bone, Joint and Cartilage",
      "url": "https://www.iherb.com/c/bone-joint"
    },
    recommendations: [
      { name: { "zh-HK": "乳清蛋白", "zh-CN": "乳清蛋白", "en": "Whey Protein" } },
      { name: { "zh-HK": "肌酸", "zh-CN": "肌酸", "en": "Creatine" } },
      { name: { "zh-HK": "HMB", "zh-CN": "HMB", "en": "HMB" } }
    ]
  },
  {
    id: "cognitive-decline",
    category_id: "brain-cognitive",
    names: {
      "zh-HK": "認知衰退/腦退化",
      "zh-CN": "认知衰退/脑退化",
      "en": "Cognitive Decline"
    },
    iherb_category: {
      name: "Brain and Cognitive",
      "url": "https://www.iherb.com/c/brain-cognitive"
    },
    recommendations: [
      { name: { "zh-HK": "磷脂酰絲氨酸(PS)", "zh-CN": "磷脂酰丝氨酸(PS)", "en": "Phosphatidylserine" } },
      { name: { "zh-HK": "銀杏", "zh-CN": "银杏", "en": "Ginkgo Biloba" } },
      { name: { "zh-HK": "Omega-3", "zh-CN": "Omega-3", "en": "Omega-3" } }
    ]
  },
  {
    id: "anxiety-relief",
    category_id: "sleep-mood",
    names: {
      "zh-HK": "焦慮緩解/舒壓",
      "zh-CN": "焦虑缓解/舒压",
      "en": "Anxiety Relief"
    },
    iherb_category: {
      name: "Sleep and Mood",
      "url": "https://www.iherb.com/c/sleep-mood"
    },
    recommendations: [
      { name: { "zh-HK": "南非醉茄", "zh-CN": "南非醉茄", "en": "Ashwagandha" } },
      { name: { "zh-HK": "L-茶氨酸", "zh-CN": "L-茶氨酸", "en": "L-Theanine" } },
      { name: { "zh-HK": "CBD油", "zh-CN": "CBD油", "en": "CBD Oil" } }
    ]
  },
  {
    id: "pregnancy-support",
    category_id: "womens-health",
    names: {
      "zh-HK": "懷孕營養支持",
      "zh-CN": "怀孕营养支持",
      "en": "Pregnancy Support"
    },
    iherb_category: {
      name: "Women Health",
      "url": "https://www.iherb.com/c/womens-health"
    },
    recommendations: [
      { name: { "zh-HK": "孕婦維他命", "zh-CN": "孕妇维生素", "en": "Prenatal Vitamin" } },
      { name: { "zh-HK": "DHA/Omega-3", "zh-CN": "DHA/Omega-3", "en": "DHA/Omega-3" } },
      { name: { "zh-HK": "鐵", "zh-CN": "铁", "en": "Iron" } }
    ]
  }
];
