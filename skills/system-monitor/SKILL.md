---
name: system-monitor
description: 系统监控 skill - 监控 CPU、内存、磁盘、网络
version: 1.0.0
author: local
license: MIT
---

# System Monitor Skill

## 功能
- 监控系统资源使用情况
- 检查进程状态
- 监控磁盘空间
- 网络连接状态

## 使用方式

当用户要求检查系统状态时，执行以下命令：

### CPU & 内存
```bash
top -l 1 | head -n 10
```

### 磁盘使用
```bash
df -h
```

### 内存详情
```bash
vm_stat
```

### 网络连接
```bash
netstat -an | grep LISTEN
```

### 进程列表
```bash
ps aux | head -n 20
```

## 输出格式

提供简洁的系统状态摘要：
- CPU 使用率
- 内存使用情况
- 磁盘剩余空间
- 活跃网络连接数
- 关键进程状态

## 警报阈值

- CPU > 80%: 警告
- 内存 > 90%: 警告
- 磁盘 < 10%: 严重警告
