#!/usr/bin/env python3
"""
史萊姆技能演化引擎
Slime Skill Evolution Engine

功能：
- 檢測技能演化需求
- 自動升級技能版本
- 管理技能融合
- 記錄演化歷史
- RPG 系統整合
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# 路徑配置
SKILL_GENOME_PATH = Path(__file__).parent / "skill-genome.json"
OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


class SlimeEvolutionEngine:
    """史萊姆演化引擎"""

    def __init__(self):
        self.genome = self.load_genome()

    def load_genome(self) -> Dict:
        """載入技能基因庫"""
        if SKILL_GENOME_PATH.exists():
            with open(SKILL_GENOME_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            print(f"❌ 技能基因庫不存在: {SKILL_GENOME_PATH}")
            sys.exit(1)

    def save_genome(self):
        """保存技能基因庫"""
        self.genome["last_updated"] = datetime.now().isoformat()
        with open(SKILL_GENOME_PATH, 'w', encoding='utf-8') as f:
            json.dump(self.genome, f, indent=2, ensure_ascii=False)
        print(f"✅ 技能基因庫已更新: {SKILL_GENOME_PATH}")

    def detect_evolution_needs(self, skill_name: str) -> List[str]:
        """檢測技能演化需求"""
        if skill_name not in self.genome["skills"]:
            print(f"❌ 技能不存在: {skill_name}")
            return []

        skill = self.genome["skills"][skill_name]
        needs = []

        # 檢查健康度
        if skill["health_score"] < 70:
            needs.append(f"健康度過低 ({skill['health_score']})，需要優化")

        # 檢查使用頻率
        if skill["last_used"]:
            last_used = datetime.fromisoformat(skill["last_used"])
            days_unused = (datetime.now() - last_used).days
            if days_unused > 7:
                needs.append(f"已 {days_unused} 日未使用，可能需要激活")

        # 檢查融合候選
        for candidate in skill.get("next_evolution_candidates", []):
            needs.append(f"可融合技能: {candidate}")

        return needs

    def evolve_skill(
        self,
        skill_name: str,
        changes: str,
        trigger: str,
        evolution_type: str = "feature_addition",
        consumed_skills: List[str] = None
    ) -> bool:
        """演化技能"""
        if skill_name not in self.genome["skills"]:
            print(f"❌ 技能不存在: {skill_name}")
            return False

        skill = self.genome["skills"][skill_name]

        # 版本升級邏輯
        current_version = skill["version"]
        major, minor, patch = map(int, current_version.split('.'))

        if evolution_type == "major_evolution":
            major += 1
            minor = 0
            patch = 0
        elif evolution_type == "feature_addition":
            minor += 1
        else:
            patch += 1

        new_version = f"{major}.{minor}.{patch}"

        # 添加演化記錄
        evolution_record = {
            "version": new_version,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "changes": changes,
            "trigger": trigger,
            "type": evolution_type
        }

        if consumed_skills:
            evolution_record["consumed"] = consumed_skills
            skill["consumed_skills"].extend(consumed_skills)

        skill["evolution_history"].append(evolution_record)
        skill["version"] = new_version
        skill["last_used"] = datetime.now().strftime("%Y-%m-%d")

        # 增加 RPG 經驗值
        self.genome["rpg_stats"]["total_xp"] += self.calculate_xp(evolution_type)

        print(f"🎉 技能演化成功！")
        print(f"   {skill_name}: {current_version} → {new_version}")
        print(f"   變化: {changes}")
        print(f"   獲得 XP: {self.calculate_xp(evolution_type)}")

        return True

    def check_fusion_opportunities(self) -> List[Dict]:
        """檢查技能融合機會"""
        fusions = self.genome.get("fusion_candidates", [])
        valid_fusions = []

        for fusion in fusions:
            skill_a = fusion["skill_a"]
            skill_b = fusion["skill_b"]

            if skill_a in self.genome["skills"] and skill_b in self.genome["skills"]:
                valid_fusions.append(fusion)

        return valid_fusions

    def merge_skills(self, skill_a: str, skill_b: str, new_name: str) -> bool:
        """融合兩個技能"""
        if skill_a not in self.genome["skills"] or skill_b not in self.genome["skills"]:
            print(f"❌ 技能不存在")
            return False

        skill_a_data = self.genome["skills"][skill_a]
        skill_b_data = self.genome["skills"][skill_b]

        # 創建新技能
        new_skill = {
            "name": new_name,
            "version": "1.0.0",
            "created": datetime.now().strftime("%Y-%m-%d"),
            "category": skill_a_data.get("category", "merged"),
            "status": "active",
            "evolution_history": [
                {
                    "version": "1.0.0",
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "changes": f"融合 {skill_a} + {skill_b}",
                    "trigger": "技能融合",
                    "type": "fusion",
                    "parents": [skill_a, skill_b]
                }
            ],
            "consumed_skills": [skill_a, skill_b],
            "can_merge_with": [],
            "next_evolution_candidates": [],
            "health_score": max(skill_a_data["health_score"], skill_b_data["health_score"]),
            "last_used": datetime.now().strftime("%Y-%m-%d")
        }

        self.genome["skills"][new_name] = new_skill
        self.genome["total_skills"] += 1

        # 增加 RPG 經驗值（融合獎勵高）
        self.genome["rpg_stats"]["total_xp"] += 100
        self.check_achievements("skill_fusion")

        print(f"🎉 技能融合成功！")
        print(f"   {skill_a} + {skill_b} → {new_name}")
        print(f"   獲得 XP: 100")

        return True

    def calculate_xp(self, evolution_type: str) -> int:
        """計算經驗值"""
        xp_table = {
            "creation": 50,
            "feature_addition": 20,
            "major_evolution": 100,
            "fusion": 150,
            "optimization": 15
        }
        return xp_table.get(evolution_type, 10)

    def check_achievements(self, trigger: str):
        """檢查成就"""
        achievements = []

        # 技能融合成就
        if trigger == "skill_fusion":
            achievements.append("🥈 首次技能融合")

        # XP 里程碑
        total_xp = self.genome["rpg_stats"]["total_xp"]
        if total_xp >= 100:
            achievements.append("🌟 達到 100 XP")
        if total_xp >= 500:
            achievements.append("⭐ 達到 500 XP")

        # 技能數量里程碑
        total_skills = self.genome["total_skills"]
        if total_skills >= 5:
            achievements.append("📦 擁有 5 個技能")
        if total_skills >= 10:
            achievements.append("🏆 擁有 10 個技能")

        for achievement in achievements:
            if achievement not in self.genome["rpg_stats"]["achievements"]:
                self.genome["rpg_stats"]["achievements"].append(achievement)
                print(f"🏆 解鎖成就: {achievement}")

    def generate_report(self) -> str:
        """生成演化報告"""
        report_lines = [
            "📊 史萊姆技能演化報告",
            "=" * 60,
            f"📅 日期: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            f"🔢 總技能數: {self.genome['total_skills']}",
            f"📈 總演化次數: {self.genome['total_evolutions']}",
            "",
            "🎮 RPG 狀態:",
            f"   等級: {self.genome['rpg_stats']['level']}",
            f"   經驗值: {self.genome['rpg_stats']['total_xp']} XP",
            f"   連續天數: {self.genome['rpg_stats']['streak_days']} 天",
            f"   成就: {len(self.genome['rpg_stats']['achievements'])} 個",
            "",
            "🔧 技能列表:"
        ]

        for skill_name, skill_data in self.genome["skills"].items():
            report_lines.append(
                f"   • {skill_data['name']} v{skill_data['version']} "
                f"(健康度: {skill_data['health_score']})"
            )
            if skill_data["evolution_history"]:
                last_evolution = skill_data["evolution_history"][-1]
                report_lines.append(
                    f"     └─ 最近演化: {last_evolution['changes']}"
                )

        # 融合機會
        fusions = self.check_fusion_opportunities()
        if fusions:
            report_lines.extend([
                "",
                "🔮 融合機會:"
            ])
            for fusion in fusions[:3]:  # 最多顯示 3 個
                report_lines.append(
                    f"   • {fusion['skill_a']} + {fusion['skill_b']} "
                    f"(協同度: {fusion['synergy_score']}%)"
                )

        return "\n".join(report_lines)


def main():
    """主程序"""
    print("🐱 史萊姆技能演化引擎")
    print("=" * 60)

    engine = SlimeEvolutionEngine()

    # 生成報告
    report = engine.generate_report()
    print(report)

    # 檢查融合機會
    print("\n" + "=" * 60)
    print("🔍 檢查融合機會...")
    fusions = engine.check_fusion_opportunities()
    if fusions:
        print(f"發現 {len(fusions)} 個融合機會")
    else:
        print("暫無融合機會")

    # 保存基因庫
    engine.save_genome()

    print("\n✅ 演化引擎執行完成")


if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except Exception as e:
        print(f"❌ 錯誤: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
