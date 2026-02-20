---
name: data-analyzer-local
description: 数据分析 skill - 分析 CSV/Excel 数据并生成报告
version: 1.0.0
author: local
license: MIT
---

# Data Analyzer Skill

## 功能
- 分析 CSV/Excel 文件
- 统计数据摘要
- 生成可视化报告
- 导出分析结果

## 使用方式

### 读取 CSV
```bash
# 查看文件结构
head -n 20 file.csv

# 统计行数
wc -l file.csv

# 查看列名
head -n 1 file.csv | tr ',' '\n'
```

### 基础统计
使用 Python（如果已安装）：
```python
import pandas as pd
df = pd.read_csv('file.csv')
print(df.describe())
print(df.info())
```

### 数据可视化
```python
import matplotlib.pyplot as plt
df.plot()
plt.savefig('chart.png')
```

## 分析报告格式

```markdown
# 数据分析报告

## 数据概览
- 文件: filename.csv
- 行数: X
- 列数: Y
- 文件大小: Z KB

## 统计摘要
[生成的统计表格]

## 数据质量
- 缺失值: X%
- 重复行: Y
- 异常值: Z

## 关键发现
- 发现1
- 发现2
- 发现3

## 建议
- 建议1
- 建议2
```

## 支持格式

✅ CSV
✅ Excel (.xlsx)
✅ JSON
✅ TSV
