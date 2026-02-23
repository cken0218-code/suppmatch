# 澳洲股票分析工具

> **Created**: 2026-02-20
> **Location**: `~/.openclaw/workspace/skills/aus-stock-tracker/`

---

## 追踪股票（13 隻）

CBA, BHP, CSL, ANZ, NAB, WBC, 4DX, AD8, ARU, BGL, ELD, KMD, VR1

---

## 技术指标（5 个）

| 指标 | 用途 |
|------|------|
| RSI | 相对强弱指标 |
| MACD | 动量 + 趋势 |
| EMA (12/26) | 敏感移动平均 |
| ADX | 趋势强度，过滤假突破 |
| ATR | 波幅，set stop loss |

---

## Signal 逻辑

**BUY**: ADX > 25 + RSI < 30 + MACD golden cross

---

## 每日自动化

- **时间**: 09:00 (礼拜一至五)
- **Cron**: 每日自动 save history
- **通知**: Discord DM 通知完成

---

## 历史记录功能

- `history/YYYY-MM-DD.json` - 每日数据
- `--history N` - 睇最近 N 日
- `--verify N` - 验证信号准确度

---

## Signal 验证结果 (2026-02-20)

- 100% accuracy (4/4 signals correct)
- Avg price change: +1.30%

---

## 2026-02-20 新增功能

- 新增 7 隻 ASX 股票: 4DX, AD8, ARU, BGL, ELD, KMD, VR1
- 新增 ADX + ATR 指标
- 新增 history save 功能
- 新增 verify signals 功能

---
*Last updated: 2026-02-20*
