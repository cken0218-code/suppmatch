#!/usr/bin/env python3
"""
Context Manager - Session-Aware Memory System

上下文管理器
跨對話的智能上下文共享與記憶系統
"""

import json
import time
import hashlib
from typing import Any, Dict, List, Optional
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from pathlib import Path
import threading


@dataclass
class ContextEntry:
    """上下文條目"""
    key: str
    value: Any
    created_at: float = field(default_factory=time.time)
    expires_at: Optional[float] = None
    access_count: int = 0
    metadata: Dict[str, Any] = field(default_factory=dict)


class ContextManager:
    """
    上下文管理器
    
    功能:
    - 跨對話的上下文共享
    - 智能 TTL 過期機制
    - 自動記憶整理
    - 線程安全
    """
    
    def __init__(
        self,
        session_id: str = "default",
        ttl_seconds: int = 3600,
        max_entries: int = 1000,
        storage_path: Optional[str] = None
    ):
        """
        初始化上下文管理器
        
        Args:
            session_id: 會話 ID
            ttl_seconds: 默認過期時間（秒）
            max_entries: 最大條目數
            storage_path: 持久化存儲路徑
        """
        self.session_id = session_id
        self.default_ttl = ttl_seconds
        self.max_entries = max_entries
        self.storage_path = storage_path
        
        # 內存存儲
        self._store: Dict[str, ContextEntry] = {}
        
        # 線程鎖
        self._lock = threading.RLock()
        
        # 統計
        self._hit_count = 0
        self._miss_count = 0
        
        # 嘗試加載持久化數據
        if storage_path:
            self._load_from_disk()
        
        print(f"[ContextManager] Initialized for session: {session_id}")
    
    def set(
        self,
        key: str,
        value: Any,
        ttl_seconds: Optional[int] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> bool:
        """
        設置上下文值
        
        Args:
            key: 鍵
            value: 值
            ttl_seconds: 過期時間（秒）
            metadata: 元數據
        
        Returns:
            bool: 是否成功
        """
        with self._lock:
            try:
                # 序列化複雜對象
                if not isinstance(value, (str, int, float, bool, list, dict)):
                    value = self._serialize(value)
                
                # 計算過期時間
                expires_at = None
                ttl = ttl_seconds or self.default_ttl
                if ttl > 0:
                    expires_at = time.time() + ttl
                
                # 創建條目
                entry = ContextEntry(
                    key=key,
                    value=value,
                    expires_at=expires_at,
                    metadata=metadata or {}
                )
                
                # 檢查是否需要清理
                if len(self._store) >= self.max_entries:
                    self._evict_lru()
                
                self._store[key] = entry
                
                # 持久化
                if self.storage_path:
                    self._save_to_disk(key, entry)
                
                return True
                
            except Exception as e:
                print(f"[ContextManager] Error setting key '{key}': {e}")
                return False
    
    def get(self, key: str) -> Any:
        """
        獲取上下文值
        
        Args:
            key: 鍵
        
        Returns:
            Any: 值，不存在返回 None
        """
        with self._lock:
            entry = self._store.get(key)
            
            if entry is None:
                self._miss_count += 1
                return None
            
            # 檢查過期
            if entry.expires_at and time.time() > entry.expires_at:
                del self._store[key]
                self._miss_count += 1
                return None
            
            # 更新訪問計數
            entry.access_count += 1
            self._hit_count += 1
            
            return entry.value
    
    def get_many(self, keys: List[str]) -> Dict[str, Any]:
        """
        批量獲取
        
        Args:
            keys: 鍵列表
        
        Returns:
            Dict of key -> value
        """
        return {key: self.get(key) for key in keys}
    
    def delete(self, key: str) -> bool:
        """刪除條目"""
        with self._lock:
            if key in self._store:
                del self._store[key]
                return True
            return False
    
    def clear(self) -> int:
        """
        清除所有條目
        
        Returns:
            int: 清除的條目數
        """
        with self._lock:
            count = len(self._store)
            self._store.clear()
            return count
    
    def exists(self, key: str) -> bool:
        """檢查鍵是否存在"""
        return self.get(key) is not None
    
    def keys(self) -> List[str]:
        """獲取所有鍵"""
        with self._lock:
            return list(self._store.keys())
    
    def values(self) -> List[Any]:
        """獲取所有值"""
        with self._lock:
            return [entry.value for entry in self._store.values()]
    
    def items(self) -> Dict[str, Any]:
        """獲取所有鍵值對"""
        with self._lock:
            return {entry.key: entry.value for entry in self._store.values()}
    
    def get_stats(self) -> Dict[str, Any]:
        """獲取統計信息"""
        with self._lock:
            total = self._hit_count + self._miss_count
            hit_rate = (self._hit_count / total * 100) if total > 0 else 0
            
            # 計算平均訪問次數
            access_counts = [e.access_count for e in self._store.values()]
            avg_access = sum(access_counts) / len(access_counts) if access_counts else 0
            
            # 過期條目數
            expired = sum(
                1 for e in self._store.values()
                if e.expires_at and time.time() > e.expires_at
            )
            
            return {
                "total_entries": len(self._store),
                "hit_count": self._hit_count,
                "miss_count": self._miss_count,
                "hit_rate": f"{hit_rate:.2f}%",
                "avg_access_count": f"{avg_access:.2f}",
                "expired_entries": expired,
                "session_id": self.session_id
            }
    
    def cleanup_expired(self) -> int:
        """清理過期條目"""
        with self._lock:
            expired_keys = [
                key for key, entry in self._store.items()
                if entry.expires_at and time.time() > entry.expires_at
            ]
            for key in expired_keys:
                del self._store[key]
            return len(expired_keys)
    
    def _evict_lru(self) -> int:
        """LRU 清理 - 移除最少訪問的條目"""
        if not self._store:
            return 0
        
        # 找到最少訪問的條目
        min_access = min(entry.access_count for entry in self._store.values())
        lru_keys = [
            key for key, entry in self._store.items()
            if entry.access_count == min_access
        ]
        
        # 移除最舊的
        for key in lru_keys[:1]:  # 只移除一個
            del self._store[key]
            return 1
        
        return 0
    
    def _serialize(self, obj: Any) -> str:
        """序列化複雜對象"""
        try:
            return json.dumps(obj, ensure_ascii=False, default=str)
        except (TypeError, ValueError):
            return str(obj)
    
    def _load_from_disk(self) -> None:
        """從磁盤加載"""
        if not self.storage_path:
            return
        
        path = Path(self.storage_path)
        if not path.exists():
            return
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for key, entry_data in data.items():
                    # 檢查過期
                    if entry_data.get('expires_at'):
                        if time.time() > entry_data['expires_at']:
                            continue
                    
                    entry = ContextEntry(
                        key=entry_data['key'],
                        value=entry_data['value'],
                        created_at=entry_data.get('created_at', time.time()),
                        expires_at=entry_data.get('expires_at'),
                        access_count=entry_data.get('access_count', 0),
                        metadata=entry_data.get('metadata', {})
                    )
                    self._store[key] = entry
                    
            print(f"[ContextManager] Loaded {len(self._store)} entries from disk")
            
        except Exception as e:
            print(f"[ContextManager] Error loading from disk: {e}")
    
    def _save_to_disk(self, key: str, entry: ContextEntry) -> None:
        """保存到磁盤"""
        if not self.storage_path:
            return
        
        path = Path(self.storage_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            # 加載現有數據
            data = {}
            if path.exists():
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            
            # 添加新條目
            data[key] = {
                'key': entry.key,
                'value': entry.value,
                'created_at': entry.created_at,
                'expires_at': entry.expires_at,
                'access_count': entry.access_count,
                'metadata': entry.metadata
            }
            
            # 保存
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                
        except Exception as e:
            print(f"[ContextManager] Error saving to disk: {e}")


# 全局默認實例
_default_context: ContextManager = None


def get_default_context() -> ContextManager:
    """獲取默認上下文管理器"""
    global _default_context
    if _default_context is None:
        _default_context = ContextManager(
            session_id="default",
            ttl_seconds=3600
        )
    return _default_context


if __name__ == "__main__":
    print("=== Context Manager Test ===\n")
    
    # 創建上下文管理器
    ctx = ContextManager(
        session_id="test-session",
        ttl_seconds=60  # 60秒過期
    )
    
    # 設置值
    print("1. Setting values...")
    ctx.set("username", "kai", ttl_seconds=120)
    ctx.set("preferences", {"theme": "dark", "language": "zh-TW"})
    ctx.set("last_analysis", {"videos_analyzed": 15, "avg_views": 5000})
    
    # 獲取值
    print("\n2. Getting values...")
    print(f"  username: {ctx.get('username')}")
    print(f"  preferences: {ctx.get('preferences')}")
    print(f"  last_analysis: {ctx.get('last_analysis')}")
    
    # 統計信息
    print(f"\n3. Stats: {ctx.get_stats()}")
    
    # 測試過期
    print("\n4. Testing expiration...")
    ctx.set("temp_data", "will_expire", ttl_seconds=1)
    print(f"  temp_data (before): {ctx.get('temp_data')}")
    time.sleep(1.1)
    print(f"  temp_data (after): {ctx.get('temp_data')}")
    
    # 批量操作
    print("\n5. Batch operations...")
    ctx.set("key1", "value1")
    ctx.set("key2", "value2")
    ctx.set("key3", "value3")
    print(f"  All keys: {ctx.keys()}")
    print(f"  All values: {ctx.values()}")
    
    print("\n=== Test Complete ===")
