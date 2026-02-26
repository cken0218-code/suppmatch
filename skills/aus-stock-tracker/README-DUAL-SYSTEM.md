# 双重股票监察系统 - 完整指南

> **创建时间**: 2026-02-27
> **版本**: 1.0

---

## 🎯 系统概述

### **双系统架构**

**系统一：固定监察** 🟢
- **对象**：已买入的股票
- **频率**：每日 09:15（周一至五）
- **目的**：监控持有股票，寻找加仓/止损机会

**系统二：市场扫描** 🟡
- **对象**：ASX 200 市场机会
- **频率**：每周二、四 09:30
- **目的**：发现新买入机会

---

## 📊 当前持仓

### **系统一：已持有股票**
- **AX1.AX** - 朋友买入 @ $1.5, 6000股

### **系统二：观察中**
1. CBA.AX
2. BHP.AX
3. CSL.AX
4. ANZ.AX
5. NAB.AX
6. WBC.AX
7. 4DX.AX
8. AD8.AX
9. ARU.AX
10. BGL.AX
11. ELD.AX
12. KMD.AX
13. VR1.AX
14. AVH.AX
15. BAP.AX
16. CTT.AX
17. FANG.AX

---

## 🛠️ 使用方法

### **查看持仓状态**
```bash
cd ~/.openclaw/workspace/skills/aus-stock-tracker
python3 stock-alert-manager.py status
```

### **添加已买入股票**
```bash
# 买入后，告诉系统
python3 stock-alert-manager.py buy CSL 买入@280

# 这会：
# 1. 从系统二移除 CSL
# 2. 添加到系统一（每日监察）
# 3. 保存备注
```

### **添加观察股票**
```bash
# 发现感兴趣但未买的股票
python3 stock-alert-manager.py watch XYZ

# 这会添加到系统二（每周扫描两次）
```

### **移除股票**
```bash
python3 stock-alert-manager.py remove AX1
```

---

## 📱 通知格式

### **系统一通知**（已持有）
```
🔔 **固定监察 - 买入信号** 🔔
📅 2026-02-28 09:15
───────────────────────────

📊 **AX1.AX**
💰 价格: $1.11
📉 RSI: 28.5 (超卖 ✅)
💪 ADX: 42.3 (强趋势 ✅)
💚 建议买入: $1.09

🎯 发现 1 只股票
⚠️ 注意：以上纯属技术分析，不构成投资建议
```

### **系统二通知**（市场扫描）
```
🆕 **市场扫描 - 新发现机会** 🆕
📅 2026-03-04 09:30
───────────────────────────

🔍 扫描: ASX 200
🎯 发现: 2 只股票

📊 **XYZ.AX**（新发现！）
💰 价格: $2.45
📉 RSI: 18.5 (超卖 ✅)
💪 ADX: 42.3 (强趋势 ✅)
💚 建议关注: $2.40

📊 **ABC.AX**
💰 价格: $5.60
📉 RSI: 22.1 (超卖 ✅)
💪 ADX: 35.8 (强趋势 ✅)

🎯 发现 2 只股票
💡 提示：这是市场扫描发现的新机会
📝 如果买入，告诉我股票代码，我会加入固定监察
⚠️ 注意：以上纯属技术分析，不构成投资建议
```

---

## ⚙️ 技术细节

### **买入信号条件**

**系统一**（较宽松）：
- RSI < 35（超卖）
- ADX > 20（有趋势）
- MACD golden cross

**系统二**（较严格）：
- RSI < 30（严重超卖）
- ADX > 25（强趋势）
- 排除已持有股票

### **扫描范围**

**系统一**：
- 只扫描 `portfolio.json` 中的 `system_1_owned`

**系统二**：
- 扫描 ASX 200（200 只股票）
- 排除 `system_1_owned` 中的股票

---

## 📂 文件结构

```
aus-stock-tracker/
├── portfolio.json              # 持仓配置 ⭐
├── stock-alert.py             # 系统一脚本
├── market-scanner.py          # 系统二脚本
├── stock-alert-manager.py     # 管理工具
├── stock-tracker.py           # 核心分析
├── auto-scan.sh              # 自动化脚本
├── history/                  # 历史数据
│   ├── 2026-02-26.json
│   └── 2026-02-27.json
└── README-DUAL-SYSTEM.md     # 本文档
```

---

## 🕐 Cron 时间表

| 名称 | 系统 | 时间 | 频率 |
|------|------|------|------|
| `stock-alert-morning` | 系统一 | 09:15 | 周一至五 |
| `stock-system2-scan-tue` | 系统二 | 09:30 | 每周二 |
| `stock-system2-scan-thu` | 系统二 | 09:30 | 每周四 |

---

## 🔄 工作流程

### **场景 1：发现新机会**

```
周二 09:30
    ↓
系统二扫描 ASX 200
    ↓
发现 XYZ.AX（RSI=18, ADX=45）
    ↓
Discord 通知你
    ↓
你研究后决定买入
    ↓
告诉我：买了 XYZ @ $2.5
    ↓
我运行：stock-alert-manager.py buy XYZ 买入@2.5
    ↓
XYZ 移到系统一（每日监察）
```

### **场景 2：持有股票出现信号**

```
周三 09:15
    ↓
系统一扫描 AX1
    ↓
发现 AX1 RSI=25（超卖）
    ↓
Discord 通知你
    ↓
你决定加仓或观望
```

---

## 🎨 自定义设置

### **调整买入阈值**

**系统一**（`stock-alert.py`）：
```python
# 第 105 行
buy_signals = check_buy_signals(
    stocks=owned,
    rsi_threshold=35,  # 调整这里
    adx_threshold=20   # 调整这里
)
```

**系统二**（`market-scanner.py`）：
```python
# 第 150 行
buy_signals = scan_market(
    ASX_200_TOP,
    rsi_threshold=30,  # 调整这里
    adx_threshold=25   # 调整这里
)
```

### **添加/修改 ASX 200 列表**

编辑 `market-scanner.py` 第 25-65 行的 `ASX_200_TOP` 列表

---

## ⚠️ 重要提醒

1. **纯属技术分析**，不构成投资建议
2. **建议结合**：基本面 + 技术面 + 个人风险承受能力
3. **止损位**：买入后记得设置止损
4. **仓位管理**：唔好 All in
5. **定期检查**：每周回顾持仓状态

---

## 📞 常见问题

### **Q: 如何查看当前持仓？**
```bash
python3 stock-alert-manager.py status
```

### **Q: 买了一只股票，怎么添加？**
```bash
python3 stock-alert-manager.py buy <股票代码> <备注>
# 例如：python3 stock-alert-manager.py buy CSL 买入@280
```

### **Q: 想观察一只股票，但未买？**
```bash
python3 stock-alert-manager.py watch <股票代码>
```

### **Q: 如何手动触发扫描？**
```bash
# 系统一
python3 stock-alert.py

# 系统二
python3 market-scanner.py
```

### **Q: 通知太多/太少怎么办？**
调整 `rsi_threshold` 和 `adx_threshold` 参数

---

## 🚀 下一步

1. ✅ **系统已启动**
2. ⏳ **等待通知**：明早 09:15 系统一，周二/四 09:30 系统二
3. 📝 **买入后告诉我**：我会自动移到系统一
4. 🎯 **定期回顾**：每周检查持仓状态

---

**双重系统已就绪！开始帮你搵钱 🚀**

---

*Last updated: 2026-02-27*
