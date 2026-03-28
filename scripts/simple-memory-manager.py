#!/usr/bin/env python3
"""
Simple Memory Manager - 简化版记忆管理工具

基于 Memory-Manager 和 MemoClaw 概念的轻量级实现
支持三层记忆架构：Episodic、Semantic、Procedural

Author: Ken (AI Assistant)
Date: 2026-03-28
Version: 1.0.0
"""

import os
import json
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# 配置
MEMORY_ROOT = Path.home() / ".openclaw" / "workspace" / "memory"
EPISODIC_DIR = MEMORY_ROOT / "episodic"
SEMANTIC_DIR = MEMORY_ROOT / "semantic"
PROCEDURAL_DIR = MEMORY_ROOT / "procedural"
SNAPSHOT_DIR = MEMORY_ROOT / "snapshots"

# 记忆类型半衰期（天）
HALF_LIVES = {
    "correction": 180,
    "preference": 180,
    "decision": 90,
    "episodic": 30,
    "semantic": 60,
    "procedural": 90,
    "general": 60,
}

# 重要性默认值
DEFAULT_IMPORTANCE = {
    "correction": 0.95,
    "preference": 0.8,
    "decision": 0.85,
    "episodic": 0.5,
    "semantic": 0.6,
    "procedural": 0.7,
    "general": 0.5,
}


class MemoryEntry:
    """记忆条目"""
    
    def __init__(
        self,
        content: str,
        memory_type: str = "general",
        importance: Optional[float] = None,
        tags: Optional[List[str]] = None,
        namespace: str = "default",
        pinned: bool = False,
    ):
        self.id = self._generate_id(content)
        self.content = content
        self.memory_type = memory_type
        self.importance = importance or DEFAULT_IMPORTANCE.get(memory_type, 0.5)
        self.tags = tags or []
        self.namespace = namespace
        self.pinned = pinned
        self.created_at = datetime.now().isoformat()
        self.access_count = 0
        self.half_life = HALF_LIVES.get(memory_type, 60)
    
    @staticmethod
    def _generate_id(content: str) -> str:
        """基于内容生成唯一 ID"""
        return hashlib.md5(content.encode()).hexdigest()[:12]
    
    def to_dict(self) -> Dict:
        """转换为字典"""
        return {
            "id": self.id,
            "content": self.content,
            "memory_type": self.memory_type,
            "importance": self.importance,
            "tags": self.tags,
            "namespace": self.namespace,
            "pinned": self.pinned,
            "created_at": self.created_at,
            "access_count": self.access_count,
            "half_life": self.half_life,
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> "MemoryEntry":
        """从字典创建"""
        entry = cls(
            content=data["content"],
            memory_type=data.get("memory_type", "general"),
            importance=data.get("importance"),
            tags=data.get("tags"),
            namespace=data.get("namespace", "default"),
            pinned=data.get("pinned", False),
        )
        entry.id = data.get("id", entry.id)
        entry.created_at = data.get("created_at", entry.created_at)
        entry.access_count = data.get("access_count", 0)
        return entry


class SimpleMemoryManager:
    """简化版记忆管理器"""
    
    def __init__(self):
        self._ensure_dirs()
    
    def _ensure_dirs(self):
        """确保目录存在"""
        for dir_path in [EPISODIC_DIR, SEMANTIC_DIR, PROCEDURAL_DIR, SNAPSHOT_DIR]:
            dir_path.mkdir(parents=True, exist_ok=True)
    
    def store(
        self,
        content: str,
        memory_type: str = "general",
        importance: Optional[float] = None,
        tags: Optional[List[str]] = None,
        namespace: str = "default",
        auto_categorize: bool = True,
    ) -> Tuple[str, str]:
        """
        存储记忆
        
        Args:
            content: 记忆内容
            memory_type: 记忆类型
            importance: 重要性（0-1）
            tags: 标签列表
            namespace: 命名空间
            auto_categorize: 自动分类到三层架构
        
        Returns:
            (memory_id, file_path)
        """
        entry = MemoryEntry(
            content=content,
            memory_type=memory_type,
            importance=importance,
            tags=tags,
            namespace=namespace,
        )
        
        # 自动分类
        if auto_categorize:
            category = self._auto_categorize(content, memory_type)
            file_path = self._get_category_file(category)
        else:
            file_path = self._get_type_file(memory_type)
        
        # 读取现有记忆
        memories = self._load_memories(file_path)
        
        # 检查重复
        if entry.id in memories:
            print(f"⚠️ 记忆已存在: {entry.id}")
            return entry.id, str(file_path)
        
        # 添加新记忆
        memories[entry.id] = entry.to_dict()
        
        # 保存
        self._save_memories(file_path, memories)
        
        return entry.id, str(file_path)
    
    def recall(
        self,
        query: str,
        memory_type: Optional[str] = None,
        namespace: Optional[str] = None,
        limit: int = 10,
        min_importance: float = 0.0,
    ) -> List[Dict]:
        """
        回忆记忆（关键词搜索）
        
        Args:
            query: 搜索查询
            memory_type: 过滤类型
            namespace: 过滤命名空间
            limit: 最大结果数
            min_importance: 最小重要性
        
        Returns:
            记忆列表
        """
        results = []
        query_lower = query.lower()
        
        # 搜索所有类别
        for category in ["episodic", "semantic", "procedural"]:
            file_path = self._get_category_file(category)
            if not file_path.exists():
                continue
            
            memories = self._load_memories(file_path)
            
            for mem_id, mem_data in memories.items():
                # 过滤条件
                if memory_type and mem_data.get("memory_type") != memory_type:
                    continue
                if namespace and mem_data.get("namespace") != namespace:
                    continue
                if mem_data.get("importance", 0) < min_importance:
                    continue
                
                # 关键词匹配
                content = mem_data.get("content", "").lower()
                if query_lower in content:
                    mem_data["_category"] = category
                    mem_data["_relevance"] = content.count(query_lower)
                    results.append(mem_data)
        
        # 按相关性和重要性排序
        results.sort(
            key=lambda x: (x.get("_relevance", 0), x.get("importance", 0)),
            reverse=True
        )
        
        return results[:limit]
    
    def get_core_memories(self, limit: int = 10) -> List[Dict]:
        """
        获取核心记忆（高重要性 + 高访问 + 已固定）
        
        Args:
            limit: 最大结果数
        
        Returns:
            核心记忆列表
        """
        all_memories = []
        
        # 收集所有记忆
        for category in ["episodic", "semantic", "procedural"]:
            file_path = self._get_category_file(category)
            if not file_path.exists():
                continue
            
            memories = self._load_memories(file_path)
            for mem_data in memories.values():
                mem_data["_category"] = category
                all_memories.append(mem_data)
        
        # 排序：固定 > 重要性 > 访问次数
        all_memories.sort(
            key=lambda x: (
                x.get("pinned", False),
                x.get("importance", 0),
                x.get("access_count", 0),
            ),
            reverse=True
        )
        
        return all_memories[:limit]
    
    def consolidate(self, namespace: str = "default", dry_run: bool = True) -> Dict:
        """
        合并相似记忆
        
        Args:
            namespace: 命名空间
            dry_run: 仅预览不执行
        
        Returns:
            合并统计
        """
        stats = {
            "clusters_found": 0,
            "memories_merged": 0,
            "clusters": [],
        }
        
        # 收集所有记忆
        all_memories = []
        for category in ["episodic", "semantic", "procedural"]:
            file_path = self._get_category_file(category)
            if file_path.exists():
                memories = self._load_memories(file_path)
                for mem_id, mem_data in memories.items():
                    if mem_data.get("namespace") == namespace:
                        all_memories.append((mem_id, mem_data, category))
        
        # 简单的相似度检测（基于内容哈希前缀）
        hash_groups = {}
        for mem_id, mem_data, category in all_memories:
            content_prefix = mem_data.get("content", "")[:50]
            prefix_hash = hashlib.md5(content_prefix.encode()).hexdigest()[:8]
            
            if prefix_hash not in hash_groups:
                hash_groups[prefix_hash] = []
            hash_groups[prefix_hash].append((mem_id, mem_data, category))
        
        # 找出重复组
        for prefix_hash, group in hash_groups.items():
            if len(group) > 1:
                stats["clusters_found"] += 1
                stats["memories_merged"] += len(group) - 1
                stats["clusters"].append({
                    "ids": [g[0] for g in group],
                    "category": group[0][2],
                    "preview": group[0][1].get("content", "")[:100],
                })
        
        if not dry_run and stats["clusters_found"] > 0:
            # TODO: 实际合并逻辑
            print("⚠️ 实际合并功能待实现")
        
        return stats
    
    def detect_compression_risk(self) -> Dict:
        """
        检测压缩风险
        
        Returns:
            风险评估
        """
        total_size = 0
        file_count = 0
        largest_file = ("", 0)
        
        for category in ["episodic", "semantic", "procedural"]:
            file_path = self._get_category_file(category)
            if file_path.exists():
                size = file_path.stat().st_size
                total_size += size
                file_count += 1
                
                if size > largest_file[1]:
                    largest_file = (str(file_path), size)
        
        # 估算 token 使用（假设 1 token ≈ 4 bytes）
        estimated_tokens = total_size / 4
        
        # 风险评估
        if estimated_tokens > 80000:
            risk_level = "🚨 CRITICAL"
            risk_percent = 90
        elif estimated_tokens > 60000:
            risk_level = "⚠️ WARNING"
            risk_percent = 70
        else:
            risk_level = "✅ SAFE"
            risk_percent = int((estimated_tokens / 100000) * 100)
        
        return {
            "total_size_bytes": total_size,
            "total_size_kb": round(total_size / 1024, 2),
            "estimated_tokens": int(estimated_tokens),
            "file_count": file_count,
            "largest_file": largest_file[0],
            "risk_level": risk_level,
            "risk_percent": risk_percent,
        }
    
    def create_snapshot(self, label: str = "") -> str:
        """
        创建快照
        
        Args:
            label: 快照标签
        
        Returns:
            快照文件路径
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        snapshot_name = f"snapshot_{timestamp}"
        if label:
            snapshot_name += f"_{label}"
        
        snapshot_file = SNAPSHOT_DIR / f"{snapshot_name}.json"
        
        # 收集所有记忆
        snapshot_data = {
            "timestamp": timestamp,
            "label": label,
            "categories": {},
        }
        
        for category in ["episodic", "semantic", "procedural"]:
            file_path = self._get_category_file(category)
            if file_path.exists():
                snapshot_data["categories"][category] = self._load_memories(file_path)
        
        # 保存
        with open(snapshot_file, "w", encoding="utf-8") as f:
            json.dump(snapshot_data, f, ensure_ascii=False, indent=2)
        
        return str(snapshot_file)
    
    def stats(self) -> Dict:
        """
        获取统计信息
        
        Returns:
            统计数据
        """
        stats = {
            "categories": {},
            "total_memories": 0,
            "total_size_kb": 0,
        }
        
        for category in ["episodic", "semantic", "procedural"]:
            file_path = self._get_category_file(category)
            if file_path.exists():
                memories = self._load_memories(file_path)
                count = len(memories)
                size = file_path.stat().st_size / 1024
                
                stats["categories"][category] = {
                    "count": count,
                    "size_kb": round(size, 2),
                }
                stats["total_memories"] += count
                stats["total_size_kb"] += size
        
        stats["total_size_kb"] = round(stats["total_size_kb"], 2)
        return stats
    
    # === 私有方法 ===
    
    def _auto_categorize(self, content: str, memory_type: str) -> str:
        """自动分类到三层架构"""
        # 基于记忆类型
        type_mapping = {
            "episodic": "episodic",
            "semantic": "semantic",
            "procedural": "procedural",
            "correction": "semantic",
            "preference": "semantic",
            "decision": "procedural",
            "general": "semantic",
        }
        
        return type_mapping.get(memory_type, "semantic")
    
    def _get_category_file(self, category: str) -> Path:
        """获取类别文件路径"""
        category_dirs = {
            "episodic": EPISODIC_DIR,
            "semantic": SEMANTIC_DIR,
            "procedural": PROCEDURAL_DIR,
        }
        
        dir_path = category_dirs.get(category, SEMANTIC_DIR)
        return dir_path / f"{category}.json"
    
    def _get_type_file(self, memory_type: str) -> Path:
        """根据记忆类型获取文件路径"""
        category = self._auto_categorize("", memory_type)
        return self._get_category_file(category)
    
    def _load_memories(self, file_path: Path) -> Dict:
        """加载记忆文件"""
        if not file_path.exists():
            return {}
        
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    
    def _save_memories(self, file_path: Path, memories: Dict):
        """保存记忆文件"""
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(memories, f, ensure_ascii=False, indent=2)


# === CLI 接口 ===

def main():
    """命令行接口"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Simple Memory Manager")
    parser.add_argument("command", choices=["store", "recall", "core", "stats", "risk", "snapshot", "consolidate"])
    parser.add_argument("--content", "-c", help="Memory content")
    parser.add_argument("--query", "-q", help="Search query")
    parser.add_argument("--type", "-t", default="general", help="Memory type")
    parser.add_argument("--importance", "-i", type=float, help="Importance (0-1)")
    parser.add_argument("--tags", help="Comma-separated tags")
    parser.add_argument("--namespace", "-n", default="default", help="Namespace")
    parser.add_argument("--limit", "-l", type=int, default=10, help="Result limit")
    parser.add_argument("--dry-run", action="store_true", help="Dry run mode")
    
    args = parser.parse_args()
    
    manager = SimpleMemoryManager()
    
    if args.command == "store":
        if not args.content:
            print("❌ --content required for store")
            return
        
        tags = args.tags.split(",") if args.tags else []
        mem_id, file_path = manager.store(
            content=args.content,
            memory_type=args.type,
            importance=args.importance,
            tags=tags,
            namespace=args.namespace,
        )
        print(f"✅ Stored: {mem_id}")
        print(f"📄 File: {file_path}")
    
    elif args.command == "recall":
        if not args.query:
            print("❌ --query required for recall")
            return
        
        results = manager.recall(
            query=args.query,
            memory_type=args.type if args.type != "general" else None,
            namespace=args.namespace if args.namespace != "default" else None,
            limit=args.limit,
        )
        
        print(f"\n🎯 Found {len(results)} memories:\n")
        for i, mem in enumerate(results, 1):
            print(f"{i}. [{mem.get('_category')}] {mem.get('content', '')[:80]}...")
            print(f"   Importance: {mem.get('importance', 0):.2f} | Type: {mem.get('memory_type')}")
            print()
    
    elif args.command == "core":
        results = manager.get_core_memories(limit=args.limit)
        
        print(f"\n💎 Core memories ({len(results)}):\n")
        for i, mem in enumerate(results, 1):
            print(f"{i}. [{mem.get('_category')}] {mem.get('content', '')[:80]}...")
            print(f"   Importance: {mem.get('importance', 0):.2f} | Pinned: {mem.get('pinned', False)}")
            print()
    
    elif args.command == "stats":
        stats = manager.stats()
        
        print("\n📊 Memory Statistics:\n")
        print(f"Total memories: {stats['total_memories']}")
        print(f"Total size: {stats['total_size_kb']} KB\n")
        
        for category, data in stats["categories"].items():
            print(f"  {category}: {data['count']} memories, {data['size_kb']} KB")
    
    elif args.command == "risk":
        risk = manager.detect_compression_risk()
        
        print("\n⚠️ Compression Risk Assessment:\n")
        print(f"Risk Level: {risk['risk_level']}")
        print(f"Risk Percent: {risk['risk_percent']}%")
        print(f"Estimated Tokens: {risk['estimated_tokens']:,}")
        print(f"Total Size: {risk['total_size_kb']} KB")
        print(f"Largest File: {risk['largest_file']}")
    
    elif args.command == "snapshot":
        snapshot_path = manager.create_snapshot(label=args.content or "")
        print(f"✅ Snapshot created: {snapshot_path}")
    
    elif args.command == "consolidate":
        stats = manager.consolidate(namespace=args.namespace, dry_run=args.dry_run)
        
        print(f"\n🔄 Consolidation {'(Dry Run)' if args.dry_run else ''}:\n")
        print(f"Clusters found: {stats['clusters_found']}")
        print(f"Memories to merge: {stats['memories_merged']}")
        
        if stats['clusters']:
            print("\nClusters:")
            for i, cluster in enumerate(stats['clusters'], 1):
                print(f"\n  Cluster {i}:")
                print(f"    IDs: {', '.join(cluster['ids'])}")
                print(f"    Preview: {cluster['preview']}")


if __name__ == "__main__":
    main()
