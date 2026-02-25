# OpenClaw Pixel Office

> **Version**: 1.0
> **Created**: 2026-02-25
> **Purpose**: Visualize OpenClaw agents as animated pixel art characters

---

## 概述

將 OpenClaw agents 變成像素小人，喺虛擬辦公室入面活動！

## 功能

- ✅ 像素小人代表每個 agent
- ✅ 虛擬辦公室環境
- ✅ 實時動畫（根據 agent 活動）
- ✅ 多個 agents 同時顯示
- ✅ 活動狀態視覺化

## 使用方法

```bash
# 打開 Pixel Office
open ~/.openclaw/workspace/skills/pixel-office/webview/index.html
```

或者：
```bash
python3 -m http.server 8080 -d ~/.openclaw/workspace/skills/pixel-office/webview
```

然後打開：http://localhost:8080

## 動畫說明

| 活動 | 動畫 |
|------|------|
| **Thinking** | 🤔 思考動畫 |
| **Reading** | 📖 閱讀動畫 |
| **Writing** | ✍️ 打字動畫 |
| **Waiting** | ✋ 舉手動畫 |
| **Idle** | 😴 站立/發呆 |

---

*Created by OpenClaw*
