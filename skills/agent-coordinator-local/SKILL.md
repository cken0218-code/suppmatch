---
name: agent-coordinator-local
description: 多代理协调系统 - 任务分配、负载均衡、故障恢复
version: 1.0.0
author: local
license: MIT
---

# Agent Coordinator - 多代理协调系统

## 功能概述

实现完整的多代理协调系统，包括：
- 智能任务分配
- 负载均衡
- 故障检测与恢复
- 实时监控
- 代理间通信

## 核心组件

### 1. Agent Registry（代理注册表）

管理所有代理的注册、发现和健康检查。

```python
# scripts/agent_registry.py

import asyncio
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
import sqlite3
import threading

@dataclass
class AgentInfo:
    id: str
    name: str
    capabilities: List[str]
    tier: str  # low, medium, high
    specialty: str
    max_concurrent_tasks: int
    current_load: float = 0.0
    status: str = 'active'  # active, idle, overloaded, offline
    last_heartbeat: Optional[str] = None
    success_rate: float = 0.9
    metadata: Dict = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}
        if self.last_heartbeat is None:
            self.last_heartbeat = datetime.now().isoformat()

class AgentRegistry:
    """
    代理注册表 - 管理代理的生命周期
    使用 SQLite + WAL 模式实现持久化
    """
    
    def __init__(self, db_path: str = 'data/agent_registry.db'):
        self.db_path = db_path
        self._local = threading.local()
        self._init_db()
        
    def _get_conn(self):
        """获取线程本地的数据库连接"""
        if not hasattr(self._local, 'conn'):
            self._local.conn = sqlite3.connect(
                self.db_path,
                check_same_thread=False
            )
            self._local.conn.execute('PRAGMA journal_mode=WAL')
            self._local.conn.row_factory = sqlite3.Row
        return self._local.conn
    
    def _init_db(self):
        """初始化数据库"""
        conn = self._get_conn()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS agents (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                capabilities TEXT NOT NULL,
                tier TEXT NOT NULL,
                specialty TEXT,
                max_concurrent_tasks INTEGER DEFAULT 1,
                current_load REAL DEFAULT 0.0,
                status TEXT DEFAULT 'active',
                last_heartbeat TEXT,
                success_rate REAL DEFAULT 0.9,
                metadata TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.execute('''
            CREATE INDEX IF NOT EXISTS idx_status ON agents(status)
        ''')
        
        conn.execute('''
            CREATE INDEX IF NOT EXISTS idx_capabilities ON agents(capabilities)
        ''')
        
        conn.commit()
    
    def register(self, agent: AgentInfo) -> bool:
        """注册新代理"""
        conn = self._get_conn()
        
        try:
            conn.execute('''
                INSERT OR REPLACE INTO agents 
                (id, name, capabilities, tier, specialty, max_concurrent_tasks,
                 current_load, status, last_heartbeat, success_rate, metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                agent.id,
                agent.name,
                json.dumps(agent.capabilities),
                agent.tier,
                agent.specialty,
                agent.max_concurrent_tasks,
                agent.current_load,
                agent.status,
                agent.last_heartbeat,
                agent.success_rate,
                json.dumps(agent.metadata)
            ))
            
            conn.commit()
            return True
            
        except Exception as e:
            print(f"注册失败: {e}")
            return False
    
    def unregister(self, agent_id: str) -> bool:
        """注销代理"""
        conn = self._get_conn()
        
        try:
            conn.execute('DELETE FROM agents WHERE id = ?', (agent_id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"注销失败: {e}")
            return False
    
    def get_agent(self, agent_id: str) -> Optional[AgentInfo]:
        """获取代理信息"""
        conn = self._get_conn()
        
        row = conn.execute(
            'SELECT * FROM agents WHERE id = ?', 
            (agent_id,)
        ).fetchone()
        
        if row:
            return self._row_to_agent(row)
        return None
    
    def discover(self, required_capabilities: List[str]) -> List[AgentInfo]:
        """发现具有所需能力的代理"""
        conn = self._get_conn()
        
        # 获取所有活跃代理
        rows = conn.execute(
            'SELECT * FROM agents WHERE status != "offline"'
        ).fetchall()
        
        # 过滤具有所有所需能力的代理
        matching = []
        for row in rows:
            agent = self._row_to_agent(row)
            agent_caps = set(agent.capabilities)
            required_caps = set(required_capabilities)
            
            if required_caps.issubset(agent_caps):
                matching.append(agent)
        
        return matching
    
    def update_heartbeat(self, agent_id: str, load: float = None):
        """更新代理心跳"""
        conn = self._get_conn()
        
        update_fields = ['last_heartbeat = ?', 'updated_at = CURRENT_TIMESTAMP']
        params = [datetime.now().isoformat()]
        
        if load is not None:
            update_fields.append('current_load = ?')
            params.append(load)
        
        params.append(agent_id)
        
        conn.execute(
            f'UPDATE agents SET {", ".join(update_fields)} WHERE id = ?',
            params
        )
        conn.commit()
    
    def update_status(self, agent_id: str, status: str):
        """更新代理状态"""
        conn = self._get_conn()
        
        conn.execute('''
            UPDATE agents 
            SET status = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (status, agent_id))
        conn.commit()
    
    def update_load(self, agent_id: str, delta: float):
        """更新代理负载"""
        conn = self._get_conn()
        
        conn.execute('''
            UPDATE agents 
            SET current_load = MAX(0, current_load + ?),
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (delta, agent_id))
        conn.commit()
    
    def get_all_active(self) -> List[AgentInfo]:
        """获取所有活跃代理"""
        conn = self._get_conn()
        
        rows = conn.execute(
            'SELECT * FROM agents WHERE status != "offline"'
        ).fetchall()
        
        return [self._row_to_agent(row) for row in rows]
    
    def _row_to_agent(self, row) -> AgentInfo:
        """将数据库行转换为 AgentInfo"""
        return AgentInfo(
            id=row['id'],
            name=row['name'],
            capabilities=json.loads(row['capabilities']),
            tier=row['tier'],
            specialty=row['specialty'],
            max_concurrent_tasks=row['max_concurrent_tasks'],
            current_load=row['current_load'],
            status=row['status'],
            last_heartbeat=row['last_heartbeat'],
            success_rate=row['success_rate'],
            metadata=json.loads(row['metadata']) if row['metadata'] else {}
        )
    
    def health_check(self, timeout_minutes: int = 5) -> Dict:
        """健康检查 - 标记超时的代理为离线"""
        conn = self._get_conn()
        
        threshold = datetime.now() - timedelta(minutes=timeout_minutes)
        
        # 查找超时代理
        rows = conn.execute('''
            SELECT id FROM agents 
            WHERE status != 'offline' 
            AND datetime(last_heartbeat) < datetime(?)
        ''', (threshold.isoformat(),)).fetchall()
        
        offline_ids = [row['id'] for row in rows]
        
        # 标记为离线
        if offline_ids:
            placeholders = ','.join('?' * len(offline_ids))
            conn.execute(
                f'UPDATE agents SET status = "offline" WHERE id IN ({placeholders})',
                offline_ids
            )
            conn.commit()
        
        return {
            'checked': len(rows),
            'marked_offline': len(offline_ids),
            'offline_ids': offline_ids
        }

# 使用示例
if __name__ == '__main__':
    # 创建注册表
    registry = AgentRegistry()
    
    # 注册代理
    agent = AgentInfo(
        id='research-001',
        name='Research Agent',
        capabilities=['web_search', 'data_analysis', 'summarization'],
        tier='high',
        specialty='market_research',
        max_concurrent_tasks=3,
        metadata={'version': '1.0', 'language': 'zh-TW'}
    )
    
    registry.register(agent)
    print(f"✅ 注册代理: {agent.name}")
    
    # 发现代理
    matching = registry.discover(['web_search', 'data_analysis'])
    print(f"🔍 发现 {len(matching)} 个匹配代理")
    
    # 更新心跳
    registry.update_heartbeat('research-001', load=0.5)
    print("💓 更新心跳")
    
    # 健康检查
    result = registry.health_check()
    print(f"🏥 健康检查: {result}")
```

### 2. Task Queue（任务队列）

管理任务的生命周期、依赖关系和优先级。

```python
# scripts/task_queue.py

import sqlite3
import json
import threading
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum
import uuid

class TaskStatus(Enum):
    CREATED = 'created'
    ASSIGNED = 'assigned'
    IN_PROGRESS = 'in_progress'
    PAUSED = 'paused'
    REVIEW = 'review'
    COMPLETED = 'completed'
    FAILED = 'failed'
    CANCELLED = 'cancelled'
    REJECTED = 'rejected'
    ARCHIVED = 'archived'

class TaskPriority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4

@dataclass
class Task:
    id: str
    type: str
    payload: Dict[str, Any]
    priority: TaskPriority = TaskPriority.MEDIUM
    status: TaskStatus = TaskStatus.CREATED
    assigned_agent: Optional[str] = None
    depends_on: List[str] = None
    result: Optional[Dict] = None
    error: Optional[str] = None
    created_at: Optional[str] = None
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
    deadline: Optional[str] = None
    estimated_duration: Optional[int] = None  # minutes
    metadata: Dict = None
    
    def __post_init__(self):
        if self.depends_on is None:
            self.depends_on = []
        if self.metadata is None:
            self.metadata = {}
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()
        if isinstance(self.priority, TaskPriority):
            self.priority = self.priority
        if isinstance(self.status, TaskStatus):
            self.status = self.status

class TaskQueue:
    """
    任务队列 - 管理任务生命周期
    支持：
    - 优先级队列
    - 依赖管理
    - 原子性任务声明
    - 状态转换验证
    """
    
    # 合法的状态转换
    VALID_TRANSITIONS = {
        TaskStatus.CREATED: [TaskStatus.ASSIGNED, TaskStatus.CANCELLED],
        TaskStatus.ASSIGNED: [TaskStatus.IN_PROGRESS, TaskStatus.FAILED, TaskStatus.CANCELLED],
        TaskStatus.IN_PROGRESS: [TaskStatus.REVIEW, TaskStatus.PAUSED, TaskStatus.FAILED],
        TaskStatus.PAUSED: [TaskStatus.IN_PROGRESS, TaskStatus.CANCELLED],
        TaskStatus.REVIEW: [TaskStatus.COMPLETED, TaskStatus.REJECTED, TaskStatus.IN_PROGRESS],
        TaskStatus.REJECTED: [TaskStatus.IN_PROGRESS, TaskStatus.FAILED],
        TaskStatus.COMPLETED: [TaskStatus.ARCHIVED],
        TaskStatus.FAILED: [TaskStatus.ASSIGNED],
        TaskStatus.CANCELLED: [],
        TaskStatus.ARCHIVED: []
    }
    
    def __init__(self, db_path: str = 'data/task_queue.db'):
        self.db_path = db_path
        self._local = threading.local()
        self._init_db()
    
    def _get_conn(self):
        if not hasattr(self._local, 'conn'):
            self._local.conn = sqlite3.connect(
                self.db_path,
                check_same_thread=False
            )
            self._local.conn.execute('PRAGMA journal_mode=WAL')
            self._local.conn.row_factory = sqlite3.Row
        return self._local.conn
    
    def _init_db(self):
        conn = self._get_conn()
        
        conn.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                type TEXT NOT NULL,
                payload TEXT NOT NULL,
                priority INTEGER DEFAULT 2,
                status TEXT DEFAULT 'created',
                assigned_agent TEXT,
                depends_on TEXT DEFAULT '[]',
                result TEXT,
                error TEXT,
                created_at TEXT,
                started_at TEXT,
                completed_at TEXT,
                deadline TEXT,
                estimated_duration INTEGER,
                metadata TEXT,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # 索引
        conn.execute('CREATE INDEX IF NOT EXISTS idx_status ON tasks(status)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_priority ON tasks(priority DESC)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_assigned ON tasks(assigned_agent)')
        conn.execute('CREATE INDEX IF NOT EXISTS idx_created ON tasks(created_at)')
        
        # 状态转换历史表
        conn.execute('''
            CREATE TABLE IF NOT EXISTS task_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id TEXT NOT NULL,
                from_status TEXT,
                to_status TEXT NOT NULL,
                timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
                metadata TEXT,
                FOREIGN KEY (task_id) REFERENCES tasks(id)
            )
        ''')
        
        conn.commit()
    
    def create(self, task: Task) -> bool:
        """创建新任务"""
        conn = self._get_conn()
        
        try:
            conn.execute('''
                INSERT INTO tasks
                (id, type, payload, priority, status, depends_on, deadline,
                 estimated_duration, metadata, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                task.id,
                task.type,
                json.dumps(task.payload),
                task.priority.value,
                task.status.value,
                json.dumps(task.depends_on),
                task.deadline,
                task.estimated_duration,
                json.dumps(task.metadata),
                task.created_at
            ))
            
            # 记录历史
            self._record_history(conn, task.id, None, task.status.value)
            
            conn.commit()
            return True
            
        except Exception as e:
            print(f"创建任务失败: {e}")
            return False
    
    def claim(self, agent_id: str, capabilities: List[str]) -> Optional[Task]:
        """
        原子性任务声明
        返回该代理可以执行的优先级最高的任务
        """
        conn = self._get_conn()
        
        # 查找符合条件的任务
        rows = conn.execute('''
            SELECT * FROM tasks
            WHERE status = 'created' OR status = 'assigned'
            ORDER BY priority DESC, created_at ASC
            LIMIT 10
        ''').fetchall()
        
        for row in rows:
            task = self._row_to_task(row)
            
            # 检查依赖是否完成
            if not self._check_dependencies(task.depends_on):
                continue
            
            # 检查能力匹配（这里简化处理）
            # 实际应该根据任务类型和能力匹配
            
            # 原子性更新
            try:
                conn.execute('''
                    UPDATE tasks
                    SET status = 'assigned',
                        assigned_agent = ?,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE id = ? AND (status = 'created' OR assigned_agent IS NULL)
                ''', (agent_id, task.id))
                
                if conn.total_changes > 0:
                    # 记录历史
                    self._record_history(
                        conn, task.id, 
                        task.status.value, 
                        TaskStatus.ASSIGNED.value,
                        {'agent_id': agent_id}
                    )
                    
                    conn.commit()
                    
                    # 更新任务对象
                    task.status = TaskStatus.ASSIGNED
                    task.assigned_agent = agent_id
                    
                    return task
                    
            except Exception as e:
                print(f"声明任务失败: {e}")
                continue
        
        return None
    
    def update_status(self, task_id: str, new_status: TaskStatus, 
                     metadata: Dict = None) -> bool:
        """更新任务状态（带转换验证）"""
        conn = self._get_conn()
        
        # 获取当前任务
        row = conn.execute(
            'SELECT * FROM tasks WHERE id = ?', (task_id,)
        ).fetchone()
        
        if not row:
            return False
        
        current_status = TaskStatus(row['status'])
        
        # 验证转换合法性
        if new_status not in self.VALID_TRANSITIONS.get(current_status, []):
            print(f"非法状态转换: {current_status.value} → {new_status.value}")
            return False
        
        # 更新状态
        update_fields = ['status = ?', 'updated_at = CURRENT_TIMESTAMP']
        params = [new_status.value]
        
        if new_status == TaskStatus.IN_PROGRESS:
            update_fields.append('started_at = ?')
            params.append(datetime.now().isoformat())
        
        elif new_status == TaskStatus.COMPLETED:
            update_fields.append('completed_at = ?')
            params.append(datetime.now().isoformat())
        
        params.append(task_id)
        
        conn.execute(
            f'UPDATE tasks SET {", ".join(update_fields)} WHERE id = ?',
            params
        )
        
        # 记录历史
        self._record_history(
            conn, task_id, current_status.value, 
            new_status.value, metadata
        )
        
        conn.commit()
        return True
    
    def set_result(self, task_id: str, result: Dict) -> bool:
        """设置任务结果"""
        conn = self._get_conn()
        
        conn.execute('''
            UPDATE tasks
            SET result = ?, status = 'completed',
                completed_at = CURRENT_TIMESTAMP,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (json.dumps(result), task_id))
        
        conn.commit()
        return True
    
    def set_error(self, task_id: str, error: str) -> bool:
        """设置任务错误"""
        conn = self._get_conn()
        
        conn.execute('''
            UPDATE tasks
            SET error = ?, status = 'failed',
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (error, task_id))
        
        conn.commit()
        return True
    
    def get_task(self, task_id: str) -> Optional[Task]:
        """获取任务"""
        conn = self._get_conn()
        
        row = conn.execute(
            'SELECT * FROM tasks WHERE id = ?', (task_id,)
        ).fetchone()
        
        if row:
            return self._row_to_task(row)
        return None
    
    def get_pending_tasks(self, limit: int = 10) -> List[Task]:
        """获取待处理任务（按优先级排序）"""
        conn = self._get_conn()
        
        rows = conn.execute('''
            SELECT * FROM tasks
            WHERE status = 'created' OR status = 'assigned'
            ORDER BY priority DESC, created_at ASC
            LIMIT ?
        ''', (limit,)).fetchall()
        
        return [self._row_to_task(row) for row in rows]
    
    def get_agent_tasks(self, agent_id: str) -> List[Task]:
        """获取代理的任务"""
        conn = self._get_conn()
        
        rows = conn.execute('''
            SELECT * FROM tasks
            WHERE assigned_agent = ?
            ORDER BY priority DESC, created_at ASC
        ''', (agent_id,)).fetchall()
        
        return [self._row_to_task(row) for row in rows]
    
    def _check_dependencies(self, depends_on: List[str]) -> bool:
        """检查依赖是否完成"""
        if not depends_on:
            return True
        
        conn = self._get_conn()
        
        for dep_id in depends_on:
            row = conn.execute(
                'SELECT status FROM tasks WHERE id = ?', (dep_id,)
            ).fetchone()
            
            if not row or row['status'] != 'completed':
                return False
        
        return True
    
    def _record_history(self, conn, task_id: str, from_status: str, 
                       to_status: str, metadata: Dict = None):
        """记录状态转换历史"""
        conn.execute('''
            INSERT INTO task_history (task_id, from_status, to_status, metadata)
            VALUES (?, ?, ?, ?)
        ''', (task_id, from_status, to_status, json.dumps(metadata or {})))
    
    def _row_to_task(self, row) -> Task:
        """将数据库行转换为 Task"""
        return Task(
            id=row['id'],
            type=row['type'],
            payload=json.loads(row['payload']),
            priority=TaskPriority(row['priority']),
            status=TaskStatus(row['status']),
            assigned_agent=row['assigned_agent'],
            depends_on=json.loads(row['depends_on']),
            result=json.loads(row['result']) if row['result'] else None,
            error=row['error'],
            created_at=row['created_at'],
            started_at=row['started_at'],
            completed_at=row['completed_at'],
            deadline=row['deadline'],
            estimated_duration=row['estimated_duration'],
            metadata=json.loads(row['metadata']) if row['metadata'] else {}
        )

# 使用示例
if __name__ == '__main__':
    queue = TaskQueue()
    
    # 创建任务
    task = Task(
        id=str(uuid.uuid4()),
        type='content_creation',
        payload={'topic': 'AI Trends 2026', 'length': 1500},
        priority=TaskPriority.HIGH,
        estimated_duration=60
    )
    
    queue.create(task)
    print(f"✅ 创建任务: {task.id}")
    
    # 声明任务
    claimed = queue.claim('research-001', ['content_generation'])
    if claimed:
        print(f"🎯 声明任务: {claimed.id}")
        
        # 更新状态
        queue.update_status(claimed.id, TaskStatus.IN_PROGRESS)
        print("▶️ 任务进行中")
        
        # 完成任务
        queue.set_result(claimed.id, {'content': 'Generated content...'})
        print("✅ 任务完成")
```

### 3. Load Balancer（负载均衡器）

实现智能负载均衡算法。

```python
# scripts/load_balancer.py

from typing import List, Dict, Optional
import random
from datetime import datetime
from .agent_registry import AgentRegistry, AgentInfo

class LoadBalancer:
    """
    智能负载均衡器
    
    支持：
    - 加权轮询
    - 最少连接
    - 能力匹配
    - 健康检查
    """
    
    def __init__(self, registry: AgentRegistry):
        self.registry = registry
        self.current_index = 0
    
    def assign_task(self, task_type: str, 
                   required_capabilities: List[str],
                   task_complexity: str = 'medium') -> Optional[AgentInfo]:
        """
        为任务分配最佳代理
        
        Args:
            task_type: 任务类型
            required_capabilities: 所需能力列表
            task_complexity: 任务复杂度 (low/medium/high)
        
        Returns:
            最佳代理，如果没有可用代理则返回 None
        """
        # 1. 发现候选代理
        candidates = self.registry.discover(required_capabilities)
        
        if not candidates:
            return None
        
        # 2. 过滤可用代理
        available = [
            agent for agent in candidates
            if agent.status in ['active', 'idle']
            and agent.current_load < agent.max_concurrent_tasks
        ]
        
        if not available:
            # 所有代理都忙，选择负载最低的
            available = sorted(candidates, key=lambda a: a.current_load)
            if available:
                return available[0]
            return None
        
        # 3. 计算有效权重
        weighted = []
        for agent in available:
            weight = self._calculate_weight(agent, task_complexity)
            weighted.append((agent, weight))
        
        # 4. 加权随机选择
        return self._weighted_random_select(weighted)
    
    def _calculate_weight(self, agent: AgentInfo, task_complexity: str) -> float:
        """
        计算代理的权重
        
        考虑因素：
        - 代理等级（tier）
        - 当前负载
        - 历史成功率
        - 任务复杂度匹配
        """
        # 1. 基础权重（tier）
        tier_weights = {'high': 1.0, 'medium': 0.7, 'low': 0.5}
        base_weight = tier_weights.get(agent.tier, 0.5)
        
        # 2. 负载因子
        load_factor = 1.0 - (agent.current_load / max(agent.max_concurrent_tasks, 1))
        
        # 3. 成功率因子
        success_factor = agent.success_rate
        
        # 4. 复杂度匹配
        complexity_match = self._match_complexity(agent.tier, task_complexity)
        
        # 综合权重
        total_weight = (
            base_weight * 0.3 +
            load_factor * 0.3 +
            success_factor * 0.2 +
            complexity_match * 0.2
        )
        
        return total_weight
    
    def _match_complexity(self, agent_tier: str, task_complexity: str) -> float:
        """匹配代理能力和任务复杂度"""
        complexity_map = {
            'high': {'low': 0.8, 'medium': 0.9, 'high': 1.0},
            'medium': {'low': 0.9, 'medium': 1.0, 'high': 0.6},
            'low': {'low': 1.0, 'medium': 0.5, 'high': 0.2}
        }
        
        return complexity_map.get(agent_tier, {}).get(task_complexity, 0.5)
    
    def _weighted_random_select(self, weighted: List[tuple]) -> AgentInfo:
        """加权随机选择"""
        if not weighted:
            return None
        
        # 提取权重
        agents, weights = zip(*weighted)
        total_weight = sum(weights)
        
        if total_weight == 0:
            return random.choice(agents)
        
        # 归一化
        normalized = [w / total_weight for w in weights]
        
        # 随机选择
        r = random.random()
        cumulative = 0.0
        
        for agent, norm_weight in zip(agents, normalized):
            cumulative += norm_weight
            if r <= cumulative:
                return agent
        
        # 兜底返回最后一个
        return agents[-1]
    
    def get_load_stats(self) -> Dict:
        """获取负载统计"""
        agents = self.registry.get_all_active()
        
        if not agents:
            return {
                'total': 0,
                'active': 0,
                'idle': 0,
                'overloaded': 0,
                'avg_load': 0.0
            }
        
        active = [a for a in agents if a.status == 'active']
        idle = [a for a in agents if a.status == 'idle']
        overloaded = [a for a in agents if a.current_load >= a.max_concurrent_tasks]
        
        avg_load = sum(a.current_load for a in agents) / len(agents)
        
        return {
            'total': len(agents),
            'active': len(active),
            'idle': len(idle),
            'overloaded': len(overloaded),
            'avg_load': round(avg_load, 2)
        }

# 使用示例
if __name__ == '__main__':
    registry = AgentRegistry()
    balancer = LoadBalancer(registry)
    
    # 分配任务
    agent = balancer.assign_task(
        task_type='content_creation',
        required_capabilities=['content_generation', 'seo_optimization'],
        task_complexity='high'
    )
    
    if agent:
        print(f"✅ 分配给代理: {agent.name} (负载: {agent.current_load})")
    else:
        print("❌ 无可用代理")
    
    # 查看负载统计
    stats = balancer.get_load_stats()
    print(f"📊 负载统计: {stats}")
```

## 使用方式

### 1. 基础设置

```python
from agent_registry import AgentRegistry, AgentInfo
from task_queue import TaskQueue, Task, TaskPriority
from load_balancer import LoadBalancer

# 初始化
registry = AgentRegistry()
queue = TaskQueue()
balancer = LoadBalancer(registry)
```

### 2. 注册代理

```python
# 注册研究代理
research_agent = AgentInfo(
    id='research-001',
    name='Research Agent',
    capabilities=['web_search', 'data_analysis'],
    tier='high',
    specialty='market_research',
    max_concurrent_tasks=3
)

registry.register(research_agent)
```

### 3. 创建任务

```python
# 创建内容创作任务
task = Task(
    id='task-001',
    type='content_creation',
    payload={
        'topic': 'AI Trends 2026',
        'length': 1500,
        'language': 'zh-TW'
    },
    priority=TaskPriority.HIGH,
    estimated_duration=60
)

queue.create(task)
```

### 4. 分配和执行

```python
# 分配任务
agent = balancer.assign_task(
    task_type='content_creation',
    required_capabilities=['content_generation'],
    task_complexity='medium'
)

if agent:
    # 代理声明任务
    claimed = queue.claim(agent.id, agent.capabilities)
    
    if claimed:
        # 更新状态
        queue.update_status(claimed.id, TaskStatus.IN_PROGRESS)
        
        # 执行任务...
        result = execute_task(claimed)
        
        # 完成任务
        queue.set_result(claimed.id, result)
```

## 配置

在 `~/.openclaw/openclaw.json` 中添加：

```json
{
  "agentCoordinator": {
    "registryDb": "data/agent_registry.db",
    "taskQueueDb": "data/task_queue.db",
    "healthCheckInterval": 300,
    "maxRetries": 3,
    "taskTimeout": 3600
  }
}
```

## 监控

### 查看代理状态
```python
agents = registry.get_all_active()
for agent in agents:
    print(f"{agent.name}: {agent.status} (负载: {agent.current_load})")
```

### 查看任务队列
```python
pending = queue.get_pending_tasks(limit=10)
for task in pending:
    print(f"{task.id}: {task.type} (优先级: {task.priority.name})")
```

### 负载统计
```python
stats = balancer.get_load_stats()
print(f"总代理: {stats['total']}, 平均负载: {stats['avg_load']}")
```

## 注意事项

1. **数据库持久化**: 所有数据存储在 SQLite，确保 `data/` 目录可写
2. **线程安全**: 使用线程本地连接，支持多线程访问
3. **健康检查**: 定期调用 `registry.health_check()` 标记离线代理
4. **任务超时**: 实现任务超时检测和自动重新分配
5. **故障恢复**: 记录任务历史，支持失败任务重试

## 扩展方向

- [ ] 添加 Prometheus 指标导出
- [ ] 实现 WebSocket 实时监控
- [ ] 添加任务依赖图可视化
- [ ] 支持代理分组和标签
- [ ] 实现动态能力发现

---

**版本**: 1.0.0
**作者**: local
**更新日期**: 2026-03-28
