#!/usr/bin/env python3
"""
Task Router - Intelligent Task Classification

智能任務路由器
基於自然語言處理的任務分類與路由
"""

import re
from typing import Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass


class AgentType(Enum):
    """目標代理類型"""
    YOUTUBE_PRO = "youtube_pro"
    DATA_PRO = "data_pro"
    PREDICTIVE = "predictive_engine"
    SECURITY = "security_agent"
    GENERAL = "general"


@dataclass
class RoutingRule:
    """路由規則"""
    patterns: List[str]
    agent_type: AgentType
    priority: int
    action: str


class TaskRouter:
    """
    智能任務路由器
    
    根據任務描述自動分類並路由到適當的代理
    """
    
    def __init__(self):
        # 定義路由規則
        self.rules: List[RoutingRule] = [
            # YouTube 相關規則 (最高優先級)
            RoutingRule(
                patterns=[
                    r"youtube.*",
                    r"影片.*",
                    r"觀看.*",
                    r"訂閱.*",
                    r"頻道.*",
                    r"觀眾.*",
                    r"收入.*",
                    r"點擊率.*",
                    r"縮圖.*",
                    r"標題.*"
                ],
                agent_type=AgentType.YOUTUBE_PRO,
                priority=10,
                action="analyze"
            ),
            
            # 數據分析規則
            RoutingRule(
                patterns=[
                    r"數據.*",
                    r"分析.*",
                    r"統計.*",
                    r"csv.*",
                    r"excel.*",
                    r"趨勢.*",
                    r"異常.*",
                    r"報告.*"
                ],
                agent_type=AgentType.DATA_PRO,
                priority=9,
                action="analyze"
            ),
            
            # 預測分析規則
            RoutingRule(
                patterns=[
                    r"預測.*",
                    r"未來.*",
                    r"增長.*",
                    r"預估.*",
                    r"預期.*",
                    r"趨勢.*",
                    r"forecast.*"
                ],
                agent_type=AgentType.PREDICTIVE,
                priority=8,
                action="predict"
            ),
            
            # 安全審計規則
            RoutingRule(
                patterns=[
                    r"安全.*",
                    r"審計.*",
                    r"風險.*",
                    r"漏洞.*",
                    r"威脅.*",
                    r"audit.*",
                    r"security.*"
                ],
                agent_type=AgentType.SECURITY,
                priority=7,
                action="audit"
            ),
            
            # 通用規則
            RoutingRule(
                patterns=[
                    r".*",  # 預設
                ],
                agent_type=AgentType.GENERAL,
                priority=0,
                action="execute"
            )
        ]
        
        # 動作映射
        self.action_keywords: Dict[AgentType, Dict[str, str]] = {
            AgentType.YOUTUBE_PRO: {
                "performance": "analyze_performance",
                "預測": "predict_performance",
                "趨勢": "analyze_trends",
                "最佳": "find_optimal",
                "推薦": "generate_recommendations",
                "報告": "generate_report"
            },
            AgentType.DATA_PRO: {
                "分析": "analyze",
                "查詢": "query",
                "統計": "statistics",
                "異常": "detect_anomalies",
                "清洗": "clean_data",
                "趨勢": "analyze_trends"
            },
            AgentType.PREDICTIVE: {
                "預測": "predict",
                "增長": "predict_growth",
                "收入": "predict_revenue",
                "ROI": "predict_roi"
            },
            AgentType.SECURITY: {
                "審計": "audit",
                "掃描": "scan",
                "檢測": "detect"
            }
        }
        
        logger.info("Task Router initialized with {} rules".format(len(self.rules)))
    
    def route(self, description: str) -> AgentType:
        """
        路由任務到適當的代理
        
        Args:
            description: 任務描述
        
        Returns:
            AgentType: 目標代理類型
        """
        description_lower = description.lower()
        
        # 按優先級排序規則
        sorted_rules = sorted(self.rules, key=lambda r: r.priority, reverse=True)
        
        for rule in sorted_rules:
            for pattern in rule.patterns:
                if re.search(pattern, description_lower, re.IGNORECASE):
                    logger.debug(f"Matched pattern '{pattern}' -> {rule.agent_type}")
                    return rule.agent_type
        
        return AgentType.GENERAL
    
    def suggest_action(self, description: str) -> str:
        """
        建議動作
        
        Args:
            description: 任務描述
        
        Returns:
            str: 建議的動作名稱
        """
        description_lower = description.lower()
        
        # 嘗試匹配動作關鍵詞
        for agent_type, keywords in self.action_keywords.items():
            for keyword, action in keywords.items():
                if keyword in description_lower:
                    logger.debug(f"Matched action '{keyword}' -> {action}")
                    return action
        
        # 返回默認動作
        agent_type = self.route(description)
        default_actions = {
            AgentType.YOUTUBE_PRO: "analyze",
            AgentType.DATA_PRO: "analyze",
            AgentType.PREDICTIVE: "predict",
            AgentType.SECURITY: "audit",
            AgentType.GENERAL: "execute"
        }
        
        return default_actions.get(agent_type, "execute")
    
    def batch_route(
        self,
        descriptions: List[str]
    ) -> List[Tuple[str, AgentType]]:
        """
        批量路由
        
        Args:
            descriptions: 任務描述列表
        
        Returns:
            List of (description, agent_type) tuples
        """
        return [(desc, self.route(desc)) for desc in descriptions]
    
    def get_routing_info(self, description: str) -> Dict[str, any]:
        """
        獲取完整路由信息
        
        Args:
            description: 任務描述
        
        Returns:
            Dict containing routing details
        """
        agent_type = self.route(description)
        action = self.suggest_action(description)
        
        return {
            "description": description,
            "agent_type": agent_type.value,
            "action": action,
            "confidence": self._calculate_confidence(description, agent_type)
        }
    
    def _calculate_confidence(
        self,
        description: str,
        agent_type: AgentType
    ) -> float:
        """計算路由置信度"""
        description_lower = description.lower()
        matched_keywords = 0
        total_keywords = 0
        
        for keyword in self.action_keywords.get(agent_type, {}).keys():
            total_keywords += 1
            if keyword in description_lower:
                matched_keywords += 1
        
        if total_keywords == 0:
            return 0.5
        
        return matched_keywords / total_keywords


# 便捷函數
def quick_route(description: str) -> str:
    """快速路由"""
    router = TaskRouter()
    return router.route(description).value


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    
    router = TaskRouter()
    
    test_cases = [
        "分析我的 YouTube 影片表現",
        "找出 CSV 數據中的異常",
        "預測下個月的收入增長",
        "執行安全審計",
        "幫我寫一個腳本"
    ]
    
    print("=== Task Router Test ===\n")
    
    for desc in test_cases:
        info = router.get_routing_info(desc)
        print(f"Input: {desc}")
        print(f"  → Agent: {info['agent_type']}")
        print(f"  → Action: {info['action']}")
        print(f"  → Confidence: {info['confidence']:.2f}")
        print()
