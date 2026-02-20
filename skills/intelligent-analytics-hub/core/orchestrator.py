#!/usr/bin/env python3
"""
Intelligent Analytics Hub - Main Orchestrator

智能分析樞紐 - 主協調器
整合多代理分析與 AI 預測功能
"""

import json
import logging
import time
from datetime import datetime
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

from .core.task_router import TaskRouter
from .core.context_manager import ContextManager
from .core.metrics_collector import MetricsCollector

# 配置日誌
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class AgentType(Enum):
    """代理類型"""
    YOUTUBE_PRO = "youtube_pro"
    DATA_PRO = "data_pro"
    PREDICTIVE = "predictive_engine"
    SECURITY = "security_agent"
    GENERAL = "general"


@dataclass
class Task:
    """任務結構"""
    id: str
    description: str
    agent_type: AgentType
    priority: int = 0
    payload: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TaskResult:
    """任務結果"""
    task_id: str
    success: bool
    data: Any = None
    error: Optional[str] = None
    metrics: Dict[str, Any] = field(default_factory=dict)
    execution_time_ms: float = 0.0


class IntelligentOrchestrator:
    """
    智能分析樞紐主協調器
    
    負責:
    - 任務路由與調度
    - 多代理協調
    - 上下文管理
    - 性能監控
    """
    
    def __init__(
        self,
        config_path: Optional[str] = None,
        enable_metrics: bool = True
    ):
        self.config_path = config_path
        self.task_router = TaskRouter()
        self.context_manager = ContextManager()
        self.metrics_collector = MetricsCollector() if enable_metrics else None
        
        # 代理實例緩存
        self._agent_instances: Dict[AgentType, Any] = {}
        
        # 任務隊列
        self._task_queue: List[Task] = []
        
        # 性能指標
        self._total_tasks = 0
        self._successful_tasks = 0
        self._failed_tasks = 0
        
        logger.info("Intelligent Orchestrator initialized")
    
    def _get_agent(self, agent_type: AgentType) -> Any:
        """獲取或創建代理實例"""
        if agent_type not in self._agent_instances:
            self._agent_instances[agent_type] = self._load_agent(agent_type)
        return self._agent_instances[agent_type]
    
    def _load_agent(self, agent_type: AgentType) -> Any:
        """加載代理模組"""
        agent_map = {
            AgentType.YOUTUBE_PRO: ("agents.youtube_pro", "YouTubeAnalyticsPro"),
            AgentType.DATA_PRO: ("agents.data_pro", "DataAnalyzerPro"),
            AgentType.PREDICTIVE: ("agents.predictive_engine", "PredictiveEngine"),
            AgentType.SECURITY: ("agents.security_agent", "SecurityAgent"),
            AgentType.GENERAL: ("agents.general_agent", "GeneralAgent"),
        }
        
        if agent_type not in agent_map:
            raise ValueError(f"Unknown agent type: {agent_type}")
        
        module_name, class_name = agent_map[agent_type]
        try:
            from importlib import import_module
            module = import_module(module_name)
            agent_class = getattr(module, class_name)
            return agent_class()
        except ImportError as e:
            logger.warning(f"Agent {agent_type} not available: {e}")
            return None
    
    def execute_task(
        self,
        description: str,
        payload: Optional[Dict[str, Any]] = None,
        priority: int = 0
    ) -> TaskResult:
        """
        執行單一任務
        
        Args:
            description: 任務描述
            payload: 任務數據
            priority: 優先級 (0-10)
        
        Returns:
            TaskResult: 執行結果
        """
        task_id = f"task_{int(time.time() * 1000)}"
        start_time = time.time()
        
        logger.info(f"Executing task: {description[:100]}...")
        
        try:
            # 1. 路由任務
            agent_type = self.task_router.route(description)
            task = Task(
                id=task_id,
                description=description,
                agent_type=agent_type,
                priority=priority,
                payload=payload or {}
            )
            
            # 2. 獲取代理
            agent = self._get_agent(agent_type)
            if agent is None:
                raise ValueError(f"Agent {agent_type} not available")
            
            # 3. 執行任務
            action = self.task_router.suggest_action(description)
            result_data = self._execute_agent_action(
                agent, action, task.payload
            )
            
            execution_time = (time.time() - start_time) * 1000
            
            # 4. 更新上下文
            self.context_manager.set(f"last_result_{task_id}", result_data)
            
            # 5. 記錄指標
            if self.metrics_collector:
                self.metrics_collector.record_task(
                    task_id=task_id,
                    agent_type=agent_type.value,
                    execution_time_ms=execution_time,
                    success=True
                )
            
            self._total_tasks += 1
            self._successful_tasks += 1
            
            logger.info(f"Task completed in {execution_time:.2f}ms")
            
            return TaskResult(
                task_id=task_id,
                success=True,
                data=result_data,
                execution_time_ms=execution_time
            )
            
        except Exception as e:
            execution_time = (time.time() - start_time) * 1000
            error_msg = str(e)
            
            logger.error(f"Task failed: {error_msg}")
            
            if self.metrics_collector:
                self.metrics_collector.record_task(
                    task_id=task_id,
                    agent_type=agent_type.value if 'agent_type' in dir() else "unknown",
                    execution_time_ms=execution_time,
                    success=False,
                    error=error_msg
                )
            
            self._total_tasks += 1
            self._failed_tasks += 1
            
            return TaskResult(
                task_id=task_id,
                success=False,
                error=error_msg,
                execution_time_ms=execution_time
            )
    
    def _execute_agent_action(
        self,
        agent: Any,
        action: str,
        payload: Dict[str, Any]
    ) -> Any:
        """執行代理動作"""
        if hasattr(agent, action):
            method = getattr(agent, action)
            return method(**payload)
        elif hasattr(agent, 'execute'):
            return agent.execute(action, **payload)
        else:
            return agent.process(payload)
    
    def execute_workflow(
        self,
        workflow: Dict[str, Any]
    ) -> Dict[str, TaskResult]:
        """
        執行工作流
        
        Args:
            workflow: 工作流定義
        
        Returns:
            Dict of task_id -> TaskResult
        """
        results = {}
        
        for step in workflow.get("steps", []):
            agent_type_str = step.get("agent")
            action = step.get("action")
            payload = step.get("payload", {})
            
            # 轉換代理類型
            try:
                agent_type = AgentType(agent_type_str)
            except ValueError:
                # 嘗試從描述推斷
                description = f"{action} {agent_type_str}"
                agent_type = self.task_router.route(description)
            
            # 創建任務
            task_id = f"step_{len(results)}_{int(time.time() * 1000)}"
            task = Task(
                id=task_id,
                description=f"{agent_type}: {action}",
                agent_type=agent_type,
                payload=payload
            )
            
            # 執行
            result = self.execute_task(
                description=task.description,
                payload=payload
            )
            results[task_id] = result
            
            # 如果失敗且是必需步�則停止
            if not result.success and step.get("required", False):
                logger.error(f"Required step failed: {step}")
                break
            
            # 將結果傳遞到下一步
            if result.success and result.data:
                payload["previous_result"] = result.data
        
        return results
    
    def get_status(self) -> Dict[str, Any]:
        """獲取協調器狀態"""
        return {
            "total_tasks": self._total_tasks,
            "successful_tasks": self._successful_tasks,
            "failed_tasks": self._failed_tasks,
            "success_rate": (
                self._successful_tasks / self._total_tasks * 100
                if self._total_tasks > 0 else 0
            ),
            "agent_count": len(self._agent_instances),
            "queue_size": len(self._task_queue)
        }
    
    def get_metrics(self) -> Dict[str, Any]:
        """獲取性能指標"""
        if self.metrics_collector:
            return self.metrics_collector.get_summary()
        return {}


# 便捷函數
def analyze_youtube(
    channel_id: str,
    period_days: int = 30
) -> Dict[str, Any]:
    """快速 YouTube 分析"""
    orchestrator = IntelligentOrchestrator()
    return orchestrator.execute_task(
        description=f"分析 YouTube 頻道 {channel_id} 過去 {period_days} 天的數據",
        payload={
            "channel_id": channel_id,
            "period_days": period_days
        }
    )


def analyze_data(
    data_source: str,
    query: str
) -> Dict[str, Any]:
    """快速數據分析"""
    orchestrator = IntelligentOrchestrator()
    return orchestrator.execute_task(
        description=f"分析 {data_source} 中的數據: {query}",
        payload={
            "data_source": data_source,
            "query": query
        }
    )


if __name__ == "__main__":
    # 測試
    orchestrator = IntelligentOrchestrator()
    
    print("=== Intelligent Analytics Hub ===")
    print(f"Status: {orchestrator.get_status()}")
