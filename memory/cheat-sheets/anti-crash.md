# 🛡️ 防死機 Cheat Sheet

> **Last Updated**: 2026-03-04 01:30
> **用途**: 防止 OpenClaw config 更新導致死機

---

## ⚠️ 高危操作

以下操作**必須**先驗證 config：

1. **更新 OpenClaw 版本**
2. **修改 ~/.openclaw/openclaw.json**
3. **新增 Telegram bot account**
4. **修改 channels 配置**

---

## ✅ 安全操作流程

### 更新 OpenClaw

```bash
# 1. 備份 config
cp ~/.openclaw/openclaw.json ~/.openclaw/backups/openclaw_$(date +%Y%m%d_%H%M%S).json

# 2. 更新 OpenClaw
npm install -g openclaw@latest

# 3. 驗證 config
openclaw config validate

# 4. 如果有錯誤，修復
openclaw doctor --fix

# 5. 重啟 gateway
openclaw gateway restart

# 6. 檢查狀態
openclaw status
```

---

### 新增 Telegram Bot

```bash
# 1. 備份 config
cp ~/.openclaw/openclaw.json ~/.openclaw/backups/openclaw_$(date +%Y%m%d_%H%M%S).json

# 2. 編輯 config（使用 template）
code ~/.openclaw/openclaw.json

# 3. 驗證
openclaw config validate

# 4. 重啟
openclaw gateway restart

# 5. 檢查
openclaw status | grep Telegram
```

---

## 🚨 緊急恢復

### 如果死機咗...

```bash
# 1. 搵最新備份
ls -lt ~/.openclaw/backups/ | head -5

# 2. 回滾
cp ~/.openclaw/backups/openclaw_XXXXXX.json ~/.openclaw/openclaw.json

# 3. 驗證
openclaw config validate

# 4. 重啟
openclaw gateway restart

# 5. 檢查
openclaw status
```

---

## 📝 Config 修改規則

### ✅ 可以加嘅 keys

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "dmPolicy": "pairing",
      "groupPolicy": "allowlist",
      "accounts": {
        "account-name": {
          "botToken": "...",
          "dmPolicy": "pairing"
        }
      }
    }
  }
}
```

### ❌ 唔好加嘅 keys

```json
{
  "channels": {
    "telegram": {
      "streaming": "partial"  // ❌ 唔支援
    }
  }
}
```

---

## 🔍 常見錯誤

### 錯誤 1：Unrecognized key

```
Invalid config: Unrecognized key: "streaming"
```

**解決**：移除不支援的 key

---

### 錯誤 2：Missing required field

```
Invalid config: channels.telegram.accounts requires "botToken"
```

**解決**：加返 botToken

---

### 錯誤 3：Gateway 啟動失敗

```
Gateway: unreachable
```

**解決**：
1. 檢查 config
2. 回滾到上一個版本
3. 重啟

---

## 💡 最佳實踐

1. **每次改 config 前備份**
2. **用 version control（git）**
3. **改完即驗證**
4. **測試 gateway 啟動**
5. **保留最近 5 個備份**

---

## 📞 求助

如果搞唔掂：
1. DM 我（Telegram / Discord）
2. 貼錯誤 message
3. 我會幫你 fix

---

*記住：驗證先行，備份為王！*
