const fs = require('fs');
const p = 'src/contexts/LocaleContext.tsx';
let c = fs.readFileSync(p, 'utf8');

// Normalize smart quotes
c = c
  .replace(/\u2018|\u2019/g, "'")
  .replace(/\u201C|\u201D/g, '"');

// Chinese quotation that was wrongly turned into ASCII quotes
const pairs = [
  ["点'关注价格'。", '点「关注价格」。'],
  ["撳'關注價格'。", '撳「關注價格」。'],
  ["例如'我最近很累又失眠'", '例如「我最近很累又失眠」'],
  ["例如'我近排好攰又失眠'", '例如「我近排好攰又失眠」'],
  ["点“关注价格”。", '点「关注价格」。'],
];
for (const [a, b] of pairs) c = c.split(a).join(b);

// Rewrite fragile blocks cleanly
c = c.replace(
  /'content\.title':\s*\{[\s\S]*?\},\s*\n\s*'content\.subtitle'/,
  [
    "'content.title': {",
    "    'zh-HK': '內容矩陣',",
    "    'zh-CN': '内容矩阵',",
    "    en: 'Content matrix',",
    '  },',
    "  'content.subtitle'",
  ].join('\n'),
);

c = c.replace(
  /'price\.empty':\s*\{[\s\S]*?\},\s*\n\s*'price\.back'/,
  [
    "'price.empty': {",
    "    'zh-HK': '未有關注產品。喺推薦結果撳「關注價格」。',",
    "    'zh-CN': '暂无关注产品。在推荐结果点「关注价格」。',",
    "    en: 'Nothing watched yet. Tap Watch price on a product card.',",
    '  },',
    "  'price.back'",
  ].join('\n'),
);

// mode.chat.desc force rewrite
c = c.replace(
  /'mode\.chat\.desc':\s*\{[\s\S]*?\},\s*\n\s*'mode\.chat\.cta'/,
  [
    "'mode.chat.desc': {",
    "    'zh-HK': '用日常說話描述，例如「我近排好攰又失眠」——離線關鍵詞理解，唔使 API。',",
    "    'zh-CN': '用日常说话描述，例如「我最近很累又失眠」——离线关键词理解，不用 API。',",
    "    en: 'Describe in plain language, e.g. tired and cannot sleep — offline keyword matching, no API.',",
    '  },',
    "  'mode.chat.cta'",
  ].join('\n'),
);

c = c.replace(
  /'feedback\.desc':\s*\{[\s\S]*?\},\s*\n\s*'feedback\.helpful'/,
  [
    "'feedback.desc': {",
    "    'zh-HK': '只收集「體驗／是否有用」，唔係療效聲稱。資料只存在本機。',",
    "    'zh-CN': '只收集「体验／是否有用」，不是疗效声称。数据只存在本机。',",
    "    en: 'Rates usefulness only — not medical efficacy. Stored on this device.',",
    '  },',
    "  'feedback.helpful'",
  ].join('\n'),
);

fs.writeFileSync(p, c, 'utf8');

// Report suspicious single-quoted values containing internal '
const lines = c.split(/\n/);
let bad = 0;
for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  const m = line.match(/^\s+'(zh-HK|zh-CN|en)':\s*'(.*)',?\s*$/);
  if (!m) continue;
  if (m[2].includes("'")) {
    console.log('SUSPECT', i + 1, line.slice(0, 120));
    bad++;
  }
}
console.log(bad ? `found ${bad} suspects` : 'clean');
