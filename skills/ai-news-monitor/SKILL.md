# AI News Monitor Skill

自動生成 AI 每日簡報，整合多個數據源。

## 功能

- 📰 AI 趨勢摘要
- 🎬 YouTube Automation 機會
- 💰 網賺方向
- 🔧 OpenClaw 開發進度

## 使用方法

```bash
cd /Users/cken0218/.openclaw/workspace/skills/ai-news-monitor
python3 monitor.py
```

## 輸出

會生成 `daily_report.md` 文件，包含：
- 每日 AI 趨勢
- 商機分析
- 開發進度

## Cron 整合

建議每日早上運行：

```bash
# 每日 08:00 生成報告
0 8 * * * cd /Users/cken0218/.openclaw/workspace/skills/ai-news-monitor && python3 monitor.py
```

---
*Created: 2026-02-21*
