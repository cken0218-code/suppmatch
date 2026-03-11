#!/usr/bin/env python3
"""
每小时赚钱 Idea 自动发送系统
每小时发送 1 个适合用户的赚钱 idea
"""

import json
from datetime import datetime
from pathlib import Path

# 用户画像
USER_PROFILE = {
    "location": "香港",
    "preference": "唔想沟通（内容创作）",
    "skill": "新手",
    "budget": "0-300 HKD",
    "channels": ["telegram"]
}

# Idea 库（按难度分类）
IDEAS = {
    "easy": [
        {
            "id": 1,
            "name": "AI 热点废片（YouTube）",
            "type": "废片",
            "cost": "0 HKD",
            "income": {
                "month1": "0-100 HKD",
                "month3": "300-900 HKD",
                "month6": "600-1500 HKD"
            },
            "steps": [
                "每日扫 trending（AI 自动）",
                "生成 1-2 分钟废片",
                "Upload YouTube",
                "等待流量变现"
            ],
            "ai_help": "全自动化：扫 trending、写脚本、配音、剪片",
            "user_work": "Upload 视频（2 分钟）",
            "risk": "低"
        },
        {
            "id": 2,
            "name": "小红书 AI 工具分享",
            "type": "小红书",
            "cost": "0 HKD",
            "income": {
                "month1": "0-500 HKD",
                "month3": "1500-3000 HKD",
                "month6": "3000-6000 HKD"
            },
            "steps": [
                "整小红书账号",
                "每日分享 1 个 AI 工具",
                "建立 audience",
                "接品牌合作（1k 粉丝开始）"
            ],
            "ai_help": "生成内容 + 封面设计",
            "user_work": "发布 + 回复评论（5 分钟）",
            "risk": "低"
        },
        {
            "id": 3,
            "name": "香港餐厅废片",
            "type": "废片",
            "cost": "0 HKD",
            "income": {
                "month1": "0-200 HKD",
                "month3": "500-1000 HKD",
                "month6": "1000-2000 HKD"
            },
            "steps": [
                "收集香港餐厅信息",
                "生成餐厅介绍废片",
                "Upload YouTube/TikTok",
                "等待流量 + 本地广告"
            ],
            "ai_help": "写脚本 + 配音",
            "user_work": "收集餐厅名单（一次性）",
            "risk": "低"
        },
        {
            "id": 4,
            "name": "AI 股市分析废片",
            "type": "废片",
            "cost": "0 HKD",
            "income": {
                "month1": "0-300 HKD",
                "month3": "600-1500 HKD",
                "month6": "1200-3000 HKD"
            },
            "steps": [
                "每日扫股市数据",
                "生成分析废片",
                "Upload YouTube",
                "建立财经 audience"
            ],
            "ai_help": "数据分析 + 脚本 + 配音",
            "user_work": "Review 内容（1 分钟）",
            "risk": "低"
        },
        {
            "id": 5,
            "name": "AI 小说生成（网文）",
            "type": "小说",
            "cost": "0 HKD",
            "income": {
                "month1": "0-100 HKD",
                "month3": "200-800 HKD",
                "month6": "500-2000 HKD"
            },
            "steps": [
                "选择平台（起点/番茄）",
                "每日生成 2000-5000 字",
                "发布连载",
                "等待订阅收入"
            ],
            "ai_help": "全自动化写作",
            "user_work": "发布（1 分钟）",
            "risk": "低-中"
        }
    ],
    "medium": [
        {
            "id": 6,
            "name": "Seedance 2.0 AI 剧",
            "type": "AI 剧",
            "cost": "100-450 HKD（首月）",
            "income": {
                "month1": "0-200 HKD",
                "month3": "500-2000 HKD",
                "month6": "2000-10000 HKD"
            },
            "steps": [
                "学习 Seedance 2.0（1-2 周）",
                "写剧本",
                "生成视频",
                "发布抖音/YouTube"
            ],
            "ai_help": "写剧本 + 设计 prompt",
            "user_work": "学习工具 + 制作（每日 2-4 小时）",
            "risk": "中"
        },
        {
            "id": 7,
            "name": "香港本地 WhatsApp Bot",
            "type": "本地服务",
            "cost": "0-200 HKD",
            "income": {
                "month1": "0-1000 HKD",
                "month3": "2000-5000 HKD",
                "month6": "5000-10000 HKD"
            },
            "steps": [
                "整 WhatsApp Business API",
                "连接 AI 自动回复",
                "揾本地商家（餐厅/诊所）",
                "收费 $500-1500/月"
            ],
            "ai_help": "写 code + 设置 API",
            "user_work": "揾客户（但可以 WhatsApp 沟通）",
            "risk": "中"
        },
        {
            "id": 8,
            "name": "小红书香港生活",
            "type": "小红书",
            "cost": "0 HKD",
            "income": {
                "month1": "0-500 HKD",
                "month3": "1000-3000 HKD",
                "month6": "3000-8000 HKD"
            },
            "steps": [
                "分享香港本地内容",
                "餐厅 review、好去处",
                "建立本地 audience",
                "接本地品牌合作"
            ],
            "ai_help": "生成内容 + 封面",
            "user_work": "拍照 + 发布（10 分钟）",
            "risk": "低-中"
        }
    ],
    "advanced": [
        {
            "id": 9,
            "name": "YouTube Automation 系统",
            "type": "综合",
            "cost": "200-500 HKD",
            "income": {
                "month1": "0-500 HKD",
                "month3": "2000-5000 HKD",
                "month6": "5000-15000 HKD"
            },
            "steps": [
                "建立 3-5 个 YouTube channel",
                "自动化内容生成",
                "交叉推广",
                "多元化收入（广告 + 联盟）"
            ],
            "ai_help": "全自动化",
            "user_work": "策略调整（每周 30 分钟）",
            "risk": "中-高"
        },
        {
            "id": 10,
            "name": "Multi-Agent 赚钱系统",
            "type": "综合",
            "cost": "300-800 HKD",
            "income": {
                "month1": "0-1000 HKD",
                "month3": "3000-8000 HKD",
                "month6": "8000-20000 HKD"
            },
            "steps": [
                "设置 6-Agent 系统",
                "每个 agent 负责唔同任务",
                "自动化赚钱",
                "优化策略"
            ],
            "ai_help": "设置 + 维护",
            "user_work": "监督 + 决策（每日 10 分钟）",
            "risk": "中-高"
        }
    ]
}

def get_next_idea():
    """获取下一个 idea（按顺序）"""
    state_file = Path.home() / ".openclaw" / "workspace" / "memory" / "money-ideas-state.json"

    if state_file.exists():
        with open(state_file) as f:
            state = json.load(f)
        current_id = state.get("current_idea_id", 0)
    else:
        current_id = 0

    # 获取所有 ideas
    all_ideas = IDEAS["easy"] + IDEAS["medium"] + IDEAS["advanced"]

    # 找下一个
    next_id = current_id + 1
    if next_id > len(all_ideas):
        next_id = 1  # 循环

    # 找到对应 idea
    for idea in all_ideas:
        if idea["id"] == next_id:
            # 更新状态
            state = {"current_idea_id": next_id, "last_sent": datetime.now().isoformat()}
            state_file.parent.mkdir(parents=True, exist_ok=True)
            with open(state_file, "w") as f:
                json.dump(state, f, indent=2)
            return idea

    return None

def format_idea_message(idea):
    """格式化 idea 为消息"""
    msg = f"""
💰 **赚钱 Idea #{idea['id']}**: {idea['name']}

───

📊 **基本信息**
• **类型**: {idea['type']}
• **启动成本**: {idea['cost']}
• **风险**: {idea['risk']}

───

💵 **预期收入**
• **首月**: {idea['income']['month1']}
• **3 个月**: {idea['income']['month3']}
• **6 个月**: {idea['income']['month6']}

───

🎯 **执行步骤**
"""
    for i, step in enumerate(idea['steps'], 1):
        msg += f"{i}. {step}\n"

    msg += f"""
───

🤖 **我帮你做**
{idea['ai_help']}

👤 **你要做**
{idea['user_work']}

───

⏰ **下一个 idea**: 1 小时后

想立即开始？讲声「开始」！🐱
"""
    return msg

def send_to_telegram(message):
    """发送到 Telegram（通过 OpenClaw message tool）"""
    # 这里需要调用 OpenClaw 的 message tool
    # 但 Python 脚本不能直接调用，需要通过其他方式
    print(f"[TELEGRAM] {message}")
    return True

def main():
    """主函数"""
    idea = get_next_idea()
    if idea:
        message = format_idea_message(idea)
        send_to_telegram(message)
        print(f"✅ Sent idea #{idea['id']}: {idea['name']}")
    else:
        print("❌ No idea found")

if __name__ == "__main__":
    main()
