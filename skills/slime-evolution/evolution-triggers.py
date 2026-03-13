#!/usr/bin/env python3
"""
史萊姆演化觸發器
Slime Evolution Triggers

整合到 Heartbeat，自動檢測演化機會
"""

import json
from datetime import datetime, timedelta
from pathlib import Path

SKILL_GENOME_PATH = Path(__file__).parent / "skill-genome.json"

class EvolutionTriggers:
    """演化觸發器"""

    def __init__(self):
        with open(SKILL_GENOME_PATH, 'r', encoding='utf-8') as f:
            self.genome = json.load(f)

    def check_time_trigger(self) -> list:
        """時間觸發器 - 每週檢查技能健康度"""
        actions = []

        for skill_name, skill in self.genome["skills"].items():
            # 檢查健康度
            if skill["health_score"] < 70:
                actions.append({
                    "type": "health_warning",
                    "skill": skill_name,
                    "message": f"{skill['name']} 健康度過低 ({skill['health_score']})，需要優化"
                })

            # 檢查使用頻率
            if skill.get("last_used"):
                last_used = datetime.fromisoformat(skill["last_used"])
                days_unused = (datetime.now() - last_used).days

                if days_unused > 7:
                    actions.append({
                        "type": "unused_skill",
                        "skill": skill_name,
                        "message": f"{skill['name']} 已 {days_unused} 日未使用"
                    })

        return actions

    def check_fusion_trigger(self) -> list:
        """融合觸發器 - 檢測技能協同效應"""
        actions = []

        fusions = self.genome.get("fusion_candidates", [])

        for fusion in fusions:
            if fusion["synergy_score"] >= 90:
                actions.append({
                    "type": "fusion_opportunity",
                    "skills": [fusion["skill_a"], fusion["skill_b"]],
                    "message": f"發現高協同度融合機會：{fusion['skill_a']} + {fusion['skill_b']} ({fusion['synergy_score']}%)"
                })

        return actions

    def check_evolution_candidates(self) -> list:
        """演化候選觸發器 - 檢測可進化技能"""
        actions = []

        for skill_name, skill in self.genome["skills"].items():
            candidates = skill.get("next_evolution_candidates", [])

            for candidate in candidates:
                actions.append({
                    "type": "evolution_candidate",
                    "skill": skill_name,
                    "candidate": candidate,
                    "message": f"{skill['name']} 可以融合 {candidate}"
                })

        return actions

    def run_all_triggers(self) -> dict:
        """運行所有觸發器"""
        results = {
            "timestamp": datetime.now().isoformat(),
            "time_triggers": self.check_time_trigger(),
            "fusion_triggers": self.check_fusion_trigger(),
            "evolution_triggers": self.check_evolution_candidates()
        }

        return results

    def generate_report(self, results: dict) -> str:
        """生成觸發器報告"""
        lines = [
            "🔮 史萊姆演化觸發器報告",
            "=" * 60,
            f"📅 時間：{results['timestamp']}",
            ""
        ]

        # 時間觸發器
        if results["time_triggers"]:
            lines.append("⏰ 時間觸發器：")
            for action in results["time_triggers"]:
                emoji = "⚠️" if action["type"] == "health_warning" else "💤"
                lines.append(f"  {emoji} {action['message']}")
            lines.append("")

        # 融合觸發器
        if results["fusion_triggers"]:
            lines.append("🔮 融合觸發器：")
            for action in results["fusion_triggers"]:
                lines.append(f"  ⭐ {action['message']}")
            lines.append("")

        # 演化觸發器
        if results["evolution_triggers"]:
            lines.append("🧬 演化候選：")
            for action in results["evolution_triggers"][:5]:  # 最多顯示 5 個
                lines.append(f"  💡 {action['message']}")
            lines.append("")

        if not any([results["time_triggers"], results["fusion_triggers"], results["evolution_triggers"]]):
            lines.append("✅ 無演化需求")

        return "\n".join(lines)


def main():
    """主程序"""
    print("🔮 史萊姆演化觸發器")
    print("=" * 60)

    triggers = EvolutionTriggers()
    results = triggers.run_all_triggers()

    report = triggers.generate_report(results)
    print(report)

    # 保存結果
    output_file = Path(__file__).parent / "output" / f"trigger-{datetime.now().strftime('%Y-%m-%d-%H%M%S')}.json"
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n✅ 結果已保存：{output_file}")

    return results


if __name__ == "__main__":
    main()
