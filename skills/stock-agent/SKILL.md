---
name: stock-agent
description: Stock Agent - 澳洲股票分析、Signal监控、每日报告
version: 1.0.0
author: local
license: MIT
---

# Stock Agent 💰

> 专门负责股票分析相关

## 职责

1. **每日报告** - 澳洲股票每日分析
2. **Signal 监控** - 技术指标信号
3. **历史追踪** - 历史数据分析
4. **趋势分析** - 市场趋势判断

---

## 追踪股票

### ASX 主要股票
| 代码 | 名称 | 类型 |
|------|------|------|
| CBA | Commonwealth Bank | 银行 |
| BHP | BHP Group | 矿业 |
| CSL | CSL Limited | 生物医药 |
| ANZ | ANZ Bank | 银行 |
| NAB | NAB | 银行 |
| WBC | Westpac | 银行 |

### ASX 中小盘
| 代码 | 名称 | 类型 |
|------|------|------|
| 4DX | 4DMedical | 医疗 |
| AD8 | Adairs | 零售 |
| ARU | Arafura Rare | 矿业 |
| BGL | Bellevue Gold | 矿业 |
| ELD | Elders | 农业 |
| KMD | Kathmandu | 零售 |
| VR1 | Vection | 科技 |

---

## 技术指标

### Signal 逻辑
```
BUY Signal:
- ADX > 25 (趋势强度)
- RSI < 30 (超卖)
- MACD Golden Cross

SELL Signal:
- ADX < 20 (趋势减弱)
- RSI > 70 (超买)
- MACD Death Cross
```

### 指标说明
- **RSI**: 相对强弱指标 (14日)
- **MACD**: 12日EMA - 26日EMA
- **ADX**: 趋向指标
- **ATR**: 平均真实波幅

---

## 使用方式

### 每日报告
```
"run daily stock report"
```

### Signal 检查
```
"check stock signals for CBA, BHP"
```

### 历史分析
```
"show 4DX history last 30 days"
```

### Signal 验证
```
"verify signals accuracy last 10 days"
```

---

## Cron Jobs

- **Daily Report**: 每日 09:00 (平日)
- **History Save**: 每日 09:00
- **Weekly Analysis**: 每週五 18:00

---

## 输出格式

### Daily Report
```
📈 ASX Daily Report
Date: 2026-02-22

🔔 Signals:
- CBA: BUY (ADX: 28, RSI: 25, MACD: ▲)
- BHP: HOLD (ADX: 22, RSI: 45, MACD: -)

📊 Market Summary:
- Index: 7,850.3 (+0.5%)
- Volume: 850M

📈 Top Movers:
- 4DX: +3.2%
- VR1: -2.1%
```

---

## 数据来源

- Yahoo Finance (yfinance)
- 免费 API，无需额外配置

---

## 注意事项

- 仅限 ASX 股票
- 信号仅供参考，不构成投资建议
- 建议配合其他分析工具使用

---

**目标**: 自动化股票分析！
