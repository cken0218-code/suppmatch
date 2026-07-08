'use client';

import { useState, createContext, useContext, ReactNode, useEffect } from 'react';
import { STORAGE_KEYS } from '@/lib/storage';

export type Locale = 'zh-HK' | 'zh-CN' | 'en';

interface LocaleContextType {
  locale: Locale;
  setLocale: (locale: Locale) => void;
  t: (key: string, vars?: Record<string, string>) => string;
}

const translations: Record<string, Record<Locale, string>> = {
  'app.title': {
    'zh-HK': 'SuppMatch',
    'zh-CN': 'SuppMatch',
    en: 'SuppMatch',
  },
  'app.subtitle': {
    'zh-HK': '症狀揀選 → 營養補充品推薦',
    'zh-CN': '症状选取 → 营养补充品推荐',
    en: 'Select Symptoms → Get Supplement Recommendations',
  },
  'app.tagline': {
    'zh-HK': 'AI 營養補充品推薦',
    'zh-CN': 'AI 营养补充品推荐',
    en: 'AI Supplement Recommendations',
  },
  'app.hero': {
    'zh-HK': '營養補充品推薦',
    'zh-CN': '营养补充品推荐',
    en: 'Supplement Recommendations',
  },
  'app.description': {
    'zh-HK': '揀選你嘅症狀，獲取個性化 supplement 建議',
    'zh-CN': '选择你的症状，获取个性化 supplement 建议',
    en: 'Select your symptoms for personalized supplement suggestions',
  },
  'search.placeholder': {
    'zh-HK': '邊度唔舒服？',
    'zh-CN': '哪里不舒服？',
    en: "What's bothering you?",
  },
  'search.clear': {
    'zh-HK': '清除搜尋',
    'zh-CN': '清除搜索',
    en: 'Clear search',
  },
  'search.recent': {
    'zh-HK': '最近搜尋：',
    'zh-CN': '最近搜索：',
    en: 'Recent searches:',
  },
  'search.clearHistory': {
    'zh-HK': '清除',
    'zh-CN': '清除',
    en: 'Clear',
  },
  'search.results': {
    'zh-HK': '搵到 {count} 個症狀',
    'zh-CN': '找到 {count} 个症状',
    en: 'Found {count} symptoms',
  },
  'search.noResults': {
    'zh-HK': '搵唔到相關症狀',
    'zh-CN': '找不到相关症状',
    en: 'No matching symptoms found',
  },
  'search.type.symptom': {
    'zh-HK': '症狀',
    'zh-CN': '症状',
    en: 'Symptom',
  },
  'search.type.supplement': {
    'zh-HK': '補充品',
    'zh-CN': '补充品',
    en: 'Supplement',
  },
  'search.type.category': {
    'zh-HK': '分類',
    'zh-CN': '分类',
    en: 'Category',
  },
  'category.label': {
    'zh-HK': '症狀分類',
    'zh-CN': '症状分类',
    en: 'Symptom categories',
  },
  'category.all': {
    'zh-HK': '全部',
    'zh-CN': '全部',
    en: 'All',
  },
  'popular.title': {
    'zh-HK': '熱門症狀',
    'zh-CN': '热门症状',
    en: 'Popular Symptoms',
  },
  'recommendation.personalized': {
    'zh-HK': '已按你嘅設定排序（年齡 {age} · {gender}）',
    'zh-CN': '已按你的设置排序（年龄 {age} · {gender}）',
    en: 'Sorted for your profile (age {age} · {gender})',
  },
  'recommendation.multiMatch': {
    'zh-HK': '{count} 個症狀都建議',
    'zh-CN': '{count} 个症状都建议',
    en: 'Suggested by {count} symptoms',
  },
  'personalize.female': {
    'zh-HK': '女性較常關注',
    'zh-CN': '女性较常关注',
    en: 'Often relevant for women',
  },
  'personalize.male': {
    'zh-HK': '男性較常關注',
    'zh-CN': '男性较常关注',
    en: 'Often relevant for men',
  },
  'personalize.senior': {
    'zh-HK': '55+ 較常補充',
    'zh-CN': '55+ 较常补充',
    en: 'Often relevant for 55+',
  },
  'personalize.young': {
    'zh-HK': '年輕族群常見',
    'zh-CN': '年轻族群常见',
    en: 'Common for younger adults',
  },
  'profile.edit': {
    'zh-HK': '✏️ 編輯個人化設定',
    'zh-CN': '✏️ 编辑个性化设置',
    en: '✏️ Edit personalization',
  },
  'button.recommend': {
    'zh-HK': '獲取推薦 ({count} 個症狀)',
    'zh-CN': '获取推荐 ({count} 个症状)',
    en: 'Get Recommendations ({count} symptoms)',
  },
  'button.back': {
    'zh-HK': '返回揀症狀',
    'zh-CN': '返回选症状',
    en: 'Back to symptoms',
  },
  'recommendation.selected': {
    'zh-HK': '你揀咗 {count} 個症狀',
    'zh-CN': '你选了 {count} 个症状',
    en: 'You selected {count} symptoms',
  },
  'recommendation.noProducts': {
    'zh-HK': '暫時未有產品資料',
    'zh-CN': '暂时没有产品资料',
    en: 'No product data available yet',
  },
  'iherb.more': {
    'zh-HK': '去 iHerb 睇更多產品',
    'zh-CN': '去 iHerb 看更多产品',
    en: 'View more products on iHerb',
  },
  'disclaimer': {
    'zh-HK': '⚠️ 本網站提供嘅資訊僅供參考，不構成醫療建議。使用前請諮詢醫生。',
    'zh-CN': '⚠️ 本网站提供的信息仅供参考，不构成医疗建议。使用前请咨询医生。',
    en: '⚠️ This website provides information for reference only and does not constitute medical advice. Please consult a doctor before use.',
  },
  'disclaimer.full': {
    'zh-HK': '⚠️ 聲明：本網站提供資訊僅供參考，不構成醫療建議。使用任何補充品前請諮詢醫生。本網站包含附屬連結，透過購買我們可能獲得佣金。',
    'zh-CN': '⚠️ 声明：本网站提供信息仅供参考，不构成医疗建议。使用任何补充品前请咨询医生。本网站包含附属链接，通过购买我们可能获得佣金。',
    en: '⚠️ Disclaimer: Information on this site is for reference only and is not medical advice. Consult a doctor before using any supplements. This site contains affiliate links and we may earn commission from purchases.',
  },
  'profile.title': {
    'zh-HK': '個人化設定',
    'zh-CN': '个性化设置',
    en: 'Personalization',
  },
  'profile.close': {
    'zh-HK': '關閉',
    'zh-CN': '关闭',
    en: 'Close',
  },
  'profile.age': {
    'zh-HK': '年齡',
    'zh-CN': '年龄',
    en: 'Age',
  },
  'profile.gender': {
    'zh-HK': '性別',
    'zh-CN': '性别',
    en: 'Gender',
  },
  'profile.selectAge': {
    'zh-HK': '選擇年齡',
    'zh-CN': '选择年龄',
    en: 'Select age',
  },
  'profile.selectGender': {
    'zh-HK': '選擇性別',
    'zh-CN': '选择性别',
    en: 'Select gender',
  },
  'profile.male': {
    'zh-HK': '男性',
    'zh-CN': '男性',
    en: 'Male',
  },
  'profile.female': {
    'zh-HK': '女性',
    'zh-CN': '女性',
    en: 'Female',
  },
  'profile.other': {
    'zh-HK': '其他',
    'zh-CN': '其他',
    en: 'Other',
  },
  'profile.saved': {
    'zh-HK': '✅ 已保存！我哋會根據你嘅設定推薦最適合嘅補充品',
    'zh-CN': '✅ 已保存！我们会根据你的设置推荐最适合的补充品',
    en: '✅ Saved! We will tailor recommendations to your profile',
  },
  'footer.shortcuts': {
    'zh-HK': '⌨️ 快速模式按 / 搜尋 | 按 ESC 返回主頁',
    'zh-CN': '⌨️ 快速模式按 / 搜索 | 按 ESC 返回主页',
    en: '⌨️ In quick mode press / to search | ESC home',
  },
  'mode.intro': {
    'zh-HK': '揀一種方式開始',
    'zh-CN': '选一种方式开始',
    en: 'Choose how to start',
  },
  'mode.quick.title': {
    'zh-HK': '快速模式',
    'zh-CN': '快速模式',
    en: 'Quick mode',
  },
  'mode.quick.desc': {
    'zh-HK': '搜尋、分類篩選、一次揀多個症狀，適合已經知自己想搵咩。',
    'zh-CN': '搜索、分类筛选、一次选多个症状，适合已经知道自己想找什么。',
    en: 'Search, filter by category, multi-select symptoms. Best if you know what you need.',
  },
  'mode.quick.cta': {
    'zh-HK': '即刻開始',
    'zh-CN': '马上开始',
    en: 'Start now',
  },
  'mode.guided.title': {
    'zh-HK': '問卷模式',
    'zh-CN': '问卷模式',
    en: 'Guided questionnaire',
  },
  'mode.guided.desc': {
    'zh-HK': '三步引導：關注領域 → 具體症狀 → 年齡/性別/服藥提示。',
    'zh-CN': '三步引导：关注领域 → 具体症状 → 年龄/性别/服药提示。',
    en: '3 steps: focus areas → symptoms → age/gender/meds note.',
  },
  'mode.guided.cta': {
    'zh-HK': '逐步完成',
    'zh-CN': '逐步完成',
    en: 'Start guided flow',
  },
  'mode.backHome': {
    'zh-HK': '返回主頁',
    'zh-CN': '返回主页',
    en: 'Back to home',
  },
  'wizard.cancel': {
    'zh-HK': '取消',
    'zh-CN': '取消',
    en: 'Cancel',
  },
  'wizard.back': {
    'zh-HK': '上一步',
    'zh-CN': '上一步',
    en: 'Back',
  },
  'wizard.next': {
    'zh-HK': '下一步',
    'zh-CN': '下一步',
    en: 'Next',
  },
  'wizard.step': {
    'zh-HK': '第 {current} / {total} 步',
    'zh-CN': '第 {current} / {total} 步',
    en: 'Step {current} / {total}',
  },
  'wizard.step1.title': {
    'zh-HK': '你最關心邊方面？',
    'zh-CN': '你最关心哪方面？',
    en: 'What do you care about most?',
  },
  'wizard.step1.desc': {
    'zh-HK': '可以多選。我哋會只顯示相關症狀。',
    'zh-CN': '可以多选。我们会只显示相关症状。',
    en: "Pick one or more. We'll only show related symptoms.",
  },
  'wizard.step2.title': {
    'zh-HK': '有邊啲症狀？',
    'zh-CN': '有哪些症状？',
    en: 'Which symptoms apply?',
  },
  'wizard.step2.desc': {
    'zh-HK': '喺 {count} 個相關症狀入面揀選（可多選）',
    'zh-CN': '在 {count} 个相关症状里选择（可多选）',
    en: 'Select from {count} related symptoms (multi-select)',
  },
  'wizard.step2.selected': {
    'zh-HK': '已揀 {count} 個',
    'zh-CN': '已选 {count} 个',
    en: '{count} selected',
  },
  'wizard.step3.title': {
    'zh-HK': '個人資料（可選）',
    'zh-CN': '个人资料（可选）',
    en: 'Your profile (optional)',
  },
  'wizard.step3.desc': {
    'zh-HK': '用嚟微調推薦排序，唔會上傳到伺服器。',
    'zh-CN': '用于微调推荐排序，不会上传到服务器。',
    en: 'Used only to tweak ranking. Stored locally, not uploaded.',
  },
  'wizard.finish': {
    'zh-HK': '睇推薦（{count} 個症狀）',
    'zh-CN': '看推荐（{count} 个症状）',
    en: 'See recommendations ({count} symptoms)',
  },
  'wizard.meds.label': {
    'zh-HK': '我而家有服用藥物 / 慢性病跟進',
    'zh-CN': '我现在有服用药物 / 慢性病跟进',
    en: 'I currently take medication / have ongoing conditions',
  },
  'wizard.meds.hint': {
    'zh-HK': '只會顯示注意提示，唔會改推薦清單本身',
    'zh-CN': '只会显示注意提示，不会改推荐清单本身',
    en: 'Only shows a caution note; does not change the list itself',
  },
  'wizard.meds.warning': {
    'zh-HK': '⚠️ 你有標示正在服藥。補充品可能同藥物有相互作用，開始任何補充前請先咨詢醫生或藥劑師。',
    'zh-CN': '⚠️ 你已标示正在服药。补充品可能与药物有相互作用，开始任何补充前请先咨询医生或药师。',
    en: '⚠️ You indicated you take medication. Supplements may interact with drugs — consult a doctor or pharmacist before starting anything new.',
  },
  'favorites.open': {
    'zh-HK': '我嘅收藏',
    'zh-CN': '我的收藏',
    en: 'My favorites',
  },
  'favorites.count': {
    'zh-HK': '{count} 項',
    'zh-CN': '{count} 项',
    en: '{count} items',
  },
  'favorites.emptyShort': {
    'zh-HK': '未有收藏',
    'zh-CN': '暂无收藏',
    en: 'None yet',
  },
  'favorites.title': {
    'zh-HK': '收藏嘅補充品',
    'zh-CN': '收藏的补充品',
    en: 'Saved supplements',
  },
  'favorites.subtitle': {
    'zh-HK': '資料只存在呢部裝置',
    'zh-CN': '数据只保存在这台设备',
    en: 'Saved only on this device',
  },
  'favorites.empty': {
    'zh-HK': '未有收藏。喺推薦頁撳 ⭐ 就可以儲起。',
    'zh-CN': '暂无收藏。在推荐页点 ⭐ 即可保存。',
    en: 'No favorites yet. Tap ⭐ on a recommendation to save it.',
  },
  'favorites.back': {
    'zh-HK': '返回',
    'zh-CN': '返回',
    en: 'Back',
  },
  'favorites.clear': {
    'zh-HK': '清空全部',
    'zh-CN': '清空全部',
    en: 'Clear all',
  },
  'favorites.add': {
    'zh-HK': '加入收藏',
    'zh-CN': '加入收藏',
    en: 'Add to favorites',
  },
  'favorites.remove': {
    'zh-HK': '取消收藏',
    'zh-CN': '取消收藏',
    en: 'Remove favorite',
  },
  'share.button': {
    'zh-HK': '分享',
    'zh-CN': '分享',
    en: 'Share',
  },
  'share.copyLink': {
    'zh-HK': '複製連結',
    'zh-CN': '复制链接',
    en: 'Copy link',
  },
  'share.done': {
    'zh-HK': '已分享',
    'zh-CN': '已分享',
    en: 'Shared',
  },
  'share.copied': {
    'zh-HK': '已複製分享內容到剪貼簿',
    'zh-CN': '已复制分享内容到剪贴板',
    en: 'Share text copied to clipboard',
  },
  'share.linkCopied': {
    'zh-HK': '連結已複製',
    'zh-CN': '链接已复制',
    en: 'Link copied',
  },
  'share.failed': {
    'zh-HK': '分享失敗，請再試',
    'zh-CN': '分享失败，请重试',
    en: 'Share failed, please try again',
  },
  'recommendation.priorityTitle': {
    'zh-HK': '優先考慮',
    'zh-CN': '优先考虑',
    en: 'Prioritize first',
  },
  'recommendation.priorityDesc': {
    'zh-HK': '以下補充品同時對應多個你揀嘅症狀，建議優先了解。',
    'zh-CN': '以下补充品同时对应多个你选的症状，建议优先了解。',
    en: 'These supplements cover multiple selected symptoms — consider them first.',
  },
  'recommendation.priorityItem': {
    'zh-HK': '{count} 個症狀：{symptoms}',
    'zh-CN': '{count} 个症状：{symptoms}',
    en: '{count} symptoms: {symptoms}',
  },
  'recommendation.covers': {
    'zh-HK': '覆蓋：{symptoms}',
    'zh-CN': '覆盖：{symptoms}',
    en: 'Covers: {symptoms}',
  },
  'symptom.guide': {
    'zh-HK': '症狀指南（SEO）',
    'zh-CN': '症状指南（SEO）',
    en: 'Symptom guide',
  },
  'guides.open': {
    'zh-HK': '症狀指南列表',
    'zh-CN': '症状指南列表',
    en: 'Symptom guide library',
  },
  'guides.hint': {
    'zh-HK': '可分享 · 適合搜尋',
    'zh-CN': '可分享 · 适合搜索',
    en: 'Shareable · SEO pages',
  },
  'mode.chat.title': {
    'zh-HK': '對話式推薦',
    'zh-CN': '对话式推荐',
    en: 'Chat-style recommend',
  },
  'mode.chat.desc': {
    'zh-HK': '用日常說話描述，例如「我近排好攰又失眠」——離線關鍵詞理解，唔使 API。',
    'zh-CN': '用日常说话描述，例如「我最近很累又失眠」——离线关键词理解，不用 API。',
    en: 'Describe in plain language, e.g. tired and cannot sleep — offline keyword matching, no API.',
  },
  'mode.chat.cta': {
    'zh-HK': '打字開始',
    'zh-CN': '打字开始',
    en: 'Start typing',
  },
  'chat.title': {
    'zh-HK': '用說話搵症狀',
    'zh-CN': '用说话找症状',
    en: 'Describe how you feel',
  },
  'chat.desc': {
    'zh-HK': '本地規則匹配（非 ChatGPT）。結果只供參考。',
    'zh-CN': '本地规则匹配（非 ChatGPT）。结果仅供参考。',
    en: 'Local rule matching (not ChatGPT). For reference only.',
  },
  'chat.placeholder': {
    'zh-HK': '例如：近排好攰，又成日瞓唔着，壓力好大…',
    'zh-CN': '例如：最近很累，又经常睡不着，压力很大…',
    en: "e.g. I have been exhausted, cannot sleep, and stressed...",
  },
  'chat.analyze': {
    'zh-HK': '分析並配對症狀',
    'zh-CN': '分析并配对症状',
    en: 'Analyze & match symptoms',
  },
  'chat.noMatch': {
    'zh-HK': '未配對到症狀。試下更具體：失眠、頭痛、脫髮、消化…',
    'zh-CN': '未配对到症状。试着更具体：失眠、头痛、脱发、消化…',
    en: 'No match yet. Try clearer words: insomnia, headache, hair loss, digestion…',
  },
  'chat.matched': {
    'zh-HK': '配對到 {count} 個可能相關症狀',
    'zh-CN': '配对到 {count} 个可能相关症状',
    en: 'Matched {count} possible symptoms',
  },
  'chat.disclaimer': {
    'zh-HK': '自動配對可能唔準，你可以之後喺快速模式再改。',
    'zh-CN': '自动配对可能不准，你可以之后在快速模式再改。',
    en: 'Auto-match can be imperfect — refine later in quick mode.',
  },
  'chat.toRecs': {
    'zh-HK': '用呢 {count} 個症狀睇推薦',
    'zh-CN': '用这 {count} 个症状看推荐',
    en: 'See recommendations for {count} symptoms',
  },
  'interactions.title': {
    'zh-HK': '補充品疊加提示',
    'zh-CN': '补充品叠加提示',
    en: 'Stacking / interaction notes',
  },
  'interactions.desc': {
    'zh-HK': '當清單同時出現某啲組合時顯示（教育資訊，非處方）。',
    'zh-CN': '当清单同时出现某些组合时显示（教育信息，非处方）。',
    en: 'Shown when certain pairs appear together (educational, not prescribing).',
  },
  'interactions.footer': {
    'zh-HK': '服藥中或有慢性病，請咨詢醫生／藥劑師。',
    'zh-CN': '服药中或有慢性病，请咨询医生／药师。',
    en: 'If you take meds or have conditions, ask a doctor/pharmacist.',
  },
  'price.open': {
    'zh-HK': '價格關注',
    'zh-CN': '价格关注',
    en: 'Price watch',
  },
  'price.hint': {
    'zh-HK': '本機清單',
    'zh-CN': '本机清单',
    en: 'Local list',
  },
  'price.title': {
    'zh-HK': '價格關注清單',
    'zh-CN': '价格关注清单',
    en: 'Price watchlist',
  },
  'price.subtitle': {
    'zh-HK': '靜態站無法自動抓即時價。你可記錄目標價，用 Email／Telegram 提醒自己去 iHerb 核對。',
    'zh-CN': '静态站无法自动抓即时价。你可记录目标价，用 Email／Telegram 提醒自己去 iHerb 核对。',
    en: "Static site cannot live-scrape prices. Save targets and email/Telegram yourself to recheck iHerb.",
  },
  'price.empty': {
    'zh-HK': '未有關注產品。喺推薦結果撳「關注價格」。',
    'zh-CN': '暂无关注产品。在推荐结果点「关注价格」。',
    en: 'Nothing watched yet. Tap Watch price on a product card.',
  },
  'price.back': {
    'zh-HK': '返回',
    'zh-CN': '返回',
    en: 'Back',
  },
  'price.email': {
    'zh-HK': 'Email 提醒自己',
    'zh-CN': 'Email 提醒自己',
    en: 'Email myself',
  },
  'price.telegram': {
    'zh-HK': 'Telegram 分享',
    'zh-CN': 'Telegram 分享',
    en: 'Share on Telegram',
  },
  'price.remove': {
    'zh-HK': '移除',
    'zh-CN': '移除',
    en: 'Remove',
  },
  'price.targetPlaceholder': {
    'zh-HK': '目標價備註（例如 <$15）',
    'zh-CN': '目标价备注（例如 <$15）',
    en: 'Target note (e.g. under $15)',
  },
  'price.watch': {
    'zh-HK': '關注價格',
    'zh-CN': '关注价格',
    en: 'Watch price',
  },
  'price.watching': {
    'zh-HK': '已關注',
    'zh-CN': '已关注',
    en: 'Watching',
  },
  'feedback.title': {
    'zh-HK': '呢份清單對你有冇幫助？',
    'zh-CN': '这份清单对你有没有帮助？',
    en: 'Was this list useful to you?',
  },
  'feedback.desc': {
    'zh-HK': '只收集「體驗／是否有用」，唔係療效聲稱。資料只存在本機。',
    'zh-CN': '只收集「体验／是否有用」，不是疗效声称。数据只存在本机。',
    en: 'Rates usefulness only — not medical efficacy. Stored on this device.',
  },
  'feedback.helpful': {
    'zh-HK': '有幫助',
    'zh-CN': '有帮助',
    en: 'Helpful',
  },
  'feedback.ok': {
    'zh-HK': '一般',
    'zh-CN': '一般',
    en: 'OK',
  },
  'feedback.not': {
    'zh-HK': '唔係好有用',
    'zh-CN': '不太有用',
    en: 'Not useful',
  },
  'feedback.commentPlaceholder': {
    'zh-HK': '可選留言（唔好寫病歷）',
    'zh-CN': '可选留言（不要写病历）',
    en: 'Optional note (no medical history)',
  },
  'feedback.thanks': {
    'zh-HK': '多謝你嘅反饋 🙏',
    'zh-CN': '谢谢你的反馈 🙏',
    en: 'Thanks for the feedback 🙏',
  },
  'content.open': {
    'zh-HK': '內容矩陣',
    'zh-CN': '内容矩阵',
    en: 'Content matrix',
  },
  'content.hint': {
    'zh-HK': '小紅書／YT 文案',
    'zh-CN': '小红书／YT 文案',
    en: 'Social captions',
  },
  'content.title': {
    'zh-HK': '內容矩陣',
    'zh-CN': '内容矩阵',
    en: 'Content matrix',
  },
  'content.subtitle': {
    'zh-HK': '預設文案 + SEO 症狀頁連結，方便發小紅書／YouTube／Threads。記得加免責。',
    'zh-CN': '预设文案 + SEO 症状页链接，方便发小红书／YouTube／Threads。记得加免责。',
    en: 'Ready captions + SEO symptom links for social. Keep the disclaimer.',
  },
  'content.back': {
    'zh-HK': '返回',
    'zh-CN': '返回',
    en: 'Back',
  },
  'content.copy': {
    'zh-HK': '複製完整文案',
    'zh-CN': '复制完整文案',
    en: 'Copy full caption',
  },
  'content.copied': {
    'zh-HK': '已複製到剪貼簿',
    'zh-CN': '已复制到剪贴板',
    en: 'Copied to clipboard',
  },
};

const LocaleContext = createContext<LocaleContextType | null>(null);

const VALID_LOCALES: Locale[] = ['zh-HK', 'zh-CN', 'en'];

export function LocaleProvider({ children, locale: initialLocale }: { children: ReactNode; locale: Locale }) {
  const [locale, setLocaleState] = useState<Locale>(initialLocale);

  // Restore saved locale after hydration to avoid server/client mismatch
  useEffect(() => {
    const saved = localStorage.getItem(STORAGE_KEYS.LOCALE) as Locale;
    if (saved && VALID_LOCALES.includes(saved)) {
      setLocaleState(saved);
    }
  }, []);

  useEffect(() => {
    localStorage.setItem(STORAGE_KEYS.LOCALE, locale);
    document.documentElement.lang = locale;
  }, [locale]);

  const setLocale = (newLocale: Locale) => {
    setLocaleState(newLocale);
  };

  const t = (key: string, vars?: Record<string, string>): string => {
    let text = translations[key]?.[locale] || key;
    if (vars) {
      for (const [name, value] of Object.entries(vars)) {
        text = text.replace(`{${name}}`, value);
      }
    }
    return text;
  };

  return (
    <LocaleContext.Provider value={{ locale, setLocale, t }}>
      {children}
    </LocaleContext.Provider>
  );
}

export function useLocale() {
  const context = useContext(LocaleContext);
  if (!context) {
    throw new Error('useLocale must be used within LocaleProvider');
  }
  return context;
}