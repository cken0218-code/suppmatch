#!/usr/bin/env python3
"""
YouTube Script Generator
基於 trending topic 生成完整腳本
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# 5 段式結構模板
STRUCTURE = {
    "hook": {
        "duration": "15s",
        "purpose": "抓住注意",
        "techniques": ["問問題", "數據震驚", "痛點共鳴", "承諾價值"]
    },
    "pain_point": {
        "duration": "30-60s",
        "purpose": "建立共鳴",
        "techniques": ["列舉症狀", "情景描述", "情感連結"]
    },
    "solution": {
        "duration": "60-90s",
        "purpose": "提供價值",
        "techniques": ["方法類", "知識類", "產品類", "工具類"]
    },
    "demo": {
        "duration": "30-60s",
        "purpose": "證明可行",
        "techniques": ["親身體驗", "用戶見證", "數據支持", "Before/After"]
    },
    "cta": {
        "duration": "15-30s",
        "purpose": "引導行動",
        "techniques": ["訂閱", "留言", "點擊連結", "分享"]
    }
}

def load_persona(persona_path):
    """載入 content persona"""
    try:
        with open(persona_path, 'r', encoding='utf-8') as f:
            # 簡單解析，實際應該用更完整的 parser
            content = f.read()
            return {
                "topics": ["健康資訊", "AI tools", "Productivity", "補充品"],
                "tone": "親切、溫暖、專業但不生硬",
                "target": "25-65歲，關注健康、睡眠、放鬆"
            }
    except FileNotFoundError:
        print(f"⚠️  Persona 文件不存在：{persona_path}")
        return None

def generate_titles(topic, count=3):
    """生成多個標題選項"""
    # 基於 topic 生成標題
    templates = [
        f"{topic} - 完整指南",
        f"點樣用{topic}改善生活？",
        f"2026年{topic}最新趨勢",
        f"{topic}：你需要知嘅所有嘢",
        f"為什麼{topic}咁重要？"
    ]
    
    return templates[:count]

def generate_hook(topic, style="question"):
    """生成開頭 Hook"""
    hooks = {
        "question": f"你有無諗過{topic}可以點樣幫到你？",
        "data": f"原來 70% 人都唔知{topic}嘅真正用處！",
        "pain": f"成日覺得好攰？可能同{topic}有關！",
        "promise": f"今日同你分享{topic}，包你學到嘢！"
    }
    
    return hooks.get(style, hooks["question"])

def generate_pain_points(topic):
    """生成痛點段落"""
    pain_points = [
        f"你有無呢啲情況？",
        f"成日覺得{topic}好難掌握？",
        f"試過好多次都唔成功？",
        f"其實你唔係一個人，好多人都有同樣問題..."
    ]
    
    return "\n".join(pain_points)

def generate_solution(topic, persona):
    """生成解決方案段落"""
    
    # 根據主題類型調整內容
    if "AI" in topic or "tools" in topic.lower():
        solution = f"""
要充分掌握{topic}，我會分三個層次同你講：

**1️⃣ 核心工具（必備）**
- ChatGPT / Claude - 文案、腳本、策略
- vidIQ - SEO 優化、關鍵字研究
- Canva AI - 設計、縮圖

**2️⃣ 進階工具（效率提升）**
- ElevenLabs - AI 配音
- Descript - 自動剪輯
- Midjourney - 圖片生成

**3️⃣ 自動化工具（規模化）**
- Shotstack - 批量視頻生成
- n8n - 工作流自動化
- OpenClaw - 多 Agent 協作

**💡 重點提示**：
唔使一次過學晒所有工具！揀 2-3 個最啱你嘅，熟練之後再加新工具。
"""
    elif "health" in topic.lower() or "sleep" in topic.lower() or "supplement" in topic.lower():
        solution = f"""
要改善{topic}相關問題，可以從三方面入手：

**1️⃣ 生活習慣調整**
- 固定作息時間
- 睡前 1 小時遠離電子產品
- 保持房間涼爽黑暗

**2️⃣ 營養補充（科學根據）**
- **鎂（Magnesium）** - 幫助放鬆肌肉、改善睡眠
- **褪黑激素（Melatonin）** - 調節生理時鐘
- **南非醉茄（Ashwagandha）** - 降低皮質醇

**3️⃣ 實用技巧**
- 4-7-8 呼吸法
- 睡前瑜伽
- 冥想練習

**⚠️ 重要提醒**：
補充劑效果因人而異，建議先諮詢醫生或營養師。
"""
    else:
        solution = f"""
要解決{topic}嘅問題，可以從三方面入手：

1. **基礎認知** - 先了解{topic}嘅基本概念
2. **實際操作** - 點樣喺日常生活中應用
3. **工具輔助** - 用咩工具可以幫到你

今日重點講第三樣...
"""
    
    return solution

def generate_demo(topic):
    """生成示範段落"""
    demo = f"""
我自己試咗一段時間，發現{topic}真係有用：

✅ 效果 1：效率提升咗
✅ 效果 2：慳咗好多時間
✅ 效果 3：質素好咗

當然，每個人情況唔同，建議你自己試下...
"""
    return demo

def generate_cta(topic):
    """生成 CTA 段落"""
    cta = f"""
如果你想知更多關於{topic}嘅資訊，可以睇下簡介欄嘅資源。

記住訂閱，下集會同你講更多實用技巧！

有咩問題？留言話我知，我會盡量答！
"""
    return cta

def generate_script(topic, persona, output_dir="youtube-scripts"):
    """生成完整腳本"""
    print(f"📝 生成腳本：{topic}")
    print("=" * 50)
    
    # 生成各部分
    titles = generate_titles(topic)
    hook = generate_hook(topic)
    pain_points = generate_pain_points(topic)
    solution = generate_solution(topic, persona)
    demo = generate_demo(topic)
    cta = generate_cta(topic)
    
    # 組合完整腳本
    script = f"""
# {titles[0]}

## 📌 基本信息
- **主題**: {topic}
- **目標受眾**: {persona['target'] if persona else '一般觀眾'}
- **預計時長**: 8-12 分鐘
- **風格**: {persona['tone'] if persona else '親切、專業'}

---

## 🎬 完整腳本

### 1️⃣ Hook（15 秒）
{hook}

---

### 2️⃣ 痛點（30-60 秒）
{pain_points}

---

### 3️⃣ 解決方案（60-90 秒）
{solution}

---

### 4️⃣ 示範（30-60 秒）
{demo}

---

### 5️⃣ CTA（15-30 秒）
{cta}

---

## 📊 標題選項

"""
    for i, title in enumerate(titles, 1):
        script += f"{i}. {title}\n"
    
    script += f"""

## 💰 變現建議

### Affiliate 整合
- **主要**: CustomGPT (20% recurring)
- **次要**: Amazon Associates（相關產品）

### 簡介欄連結
- 🔗 詳細資源：[連結]
- 🔗 推薦工具：[連結]
- 🔗 訂閱：[連結]

---

## ⚠️ 免責聲明

本內容僅供參考，不構成專業建議。
如有疑問，請諮詢專業人士。

---

**生成時間**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**腳本版本**: v1.0
"""
    
    # 保存腳本
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    filename = f"script-{datetime.now().strftime('%Y-%m-%d-%H%M')}.md"
    filepath = output_path / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(script)
    
    print(f"\n✅ 腳本已保存：{filepath}")
    print(f"\n📄 標題選項：")
    for i, title in enumerate(titles, 1):
        print(f"   {i}. {title}")
    
    return {
        "filepath": str(filepath),
        "titles": titles,
        "topic": topic,
        "generated_at": datetime.now().isoformat()
    }

def main():
    """主流程"""
    # 從 trending 結果讀取最佳題目
    # 嘗試多個可能的路徑
    possible_paths = [
        f"youtube-scripts/trending-{datetime.now().strftime('%Y-%m-%d')}.json",
        f"skills/youtube-workflow-local/youtube-scripts/trending-{datetime.now().strftime('%Y-%m-%d')}.json"
    ]
    
    trending_data = None
    for trending_file in possible_paths:
        try:
            with open(trending_file, 'r', encoding='utf-8') as f:
                trending_data = json.load(f)
                topic = trending_data['selected']['topic']
                print(f"✅ 讀取 trending 文件：{trending_file}")
                break
        except FileNotFoundError:
            continue
    
    if not trending_data:
        print(f"⚠️  找唔到 trending 文件，使用預設題目...")
        topic = "AI Tools Productivity 2026"
    
    # 載入 persona
    persona_path = "memory/projects/content-persona.md"
    persona = load_persona(persona_path)
    
    # 生成腳本
    result = generate_script(topic, persona)
    
    print("\n" + "=" * 50)
    print("🎉 腳本生成完成！")
    print(f"📄 文件：{result['filepath']}")
    print(f"🎯 題目：{result['topic']}")
    
    return result

if __name__ == "__main__":
    try:
        result = main()
        sys.exit(0)
    except Exception as e:
        print(f"❌ 錯誤：{e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
