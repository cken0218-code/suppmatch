# Crypto Agent - 加密货币分析

## 用途
追踪 BTC/ETH/SOL 价格，分析 Fear & Greed Index，发送突破/跌破警报。

## 触发条件
- 每日 08:30（早市扫描）
- 单日波动 > 8%
- 用户要求「睇下 [币]」

## 使用方式

### 1. 获取价格数据
```bash
# 获取实时价格
python3 scripts/fetch-prices.py --coins BTC,ETH,SOL

# 使用 coingecko skill
# coingecko price BTC ETH SOL
```

### 2. 技术分析
```bash
# 计算技术指标
python3 scripts/crypto-analysis.py --coin BTC

# 输出位置
# memory/reports/crypto-YYYY-MM-DD.md
```

### 3. 发送警报
```bash
# 检查突破/跌破
python3 scripts/check-alerts.py

# 如果波动 > 8% → Telegram DM 通知
```

## 范例

**用户**：「睇下 BTC 而家点」

**Crypto Agent**：
1. 获取 BTC 实时价格
2. 检查 24h 变化
3. 计算 RSI / MACD
4. 输出分析报告

## 报告格式

```markdown
# Crypto Report - YYYY-MM-DD 08:30

## 💰 价格概览
| 币种 | 价格 | 24h 变化 | RSI | 趋势 |
|------|------|----------|-----|------|
| BTC | $XX,XXX | +X.X% | XX | 📈 |
| ETH | $X,XXX | -X.X% | XX | 📉 |
| SOL | $XXX | +X.X% | XX | ➡️ |

## 📊 市场情绪
- Fear & Greed Index: XX
- 状态: [Extreme Fear / Fear / Neutral / Greed / Extreme Greed]

## 🚨 警报
- [如果有波动 > 8%]

## 💡 操作建议
- BTC: [建议]
- ETH: [建议]
- SOL: [建议]

⚠️ 免责声明：此分析仅供参考，不构成投资建议。
```

## 监控清单
- **BTC**: $80,000-85,000 range
- **ETH**: $1,900-2,100 range（预测：$2,560 by end of March）
- **SOL**: 监控突破

## 相关文件
- 报告：`memory/reports/crypto-*.md`
- 历史数据：`data/crypto-prices.csv`

## 模型
- **数据分析**：MiniMax

## 依赖
- CoinGecko API（通过 coingecko skill）
- Fear & Greed Index API

## 状态
- ✅ 基本框架完成
- ⏳ 技术分析指标开发中
