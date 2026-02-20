# MiniMax 模型 ID 修复 - 2026-02-18

**问题**: HTTP 400: invalid params, unknown model 'm2.5' (2013)
**修复时间**: 2026-02-18 14:35
**状态**: ✅ 已修复

---

## 🔍 问题分析

### 错误信息
```
HTTP 400: invalid params, unknown model 'm2.5' (2013)
```

### 根本原因
**模型 ID 错误**
- ❌ 错误配置: `m2.5`
- ✅ 正确配置: `MiniMax-M2.5`

### MiniMax 官方模型列表

**Text 模型**:
1. **MiniMax-M2.5** - 代码生成和重构（推荐）
2. **MiniMax-M2.5-highspeed** - 快速版本
3. **MiniMax-M2.1** - 230B 参数，优化代码
4. **MiniMax-M2.1-highspeed** - 快速版本
5. **MiniMax-M2** - 200k context, 128k output
6. **M2-her** - 角色扮演和多轮对话

**Audio 模型**:
- speech-2.8-hd
- speech-2.8-turbo
- speech-2.6-hd
- speech-2.6-turbo

**Video 模型**:
- MiniMax Hailuo 2.3
- MiniMax Hailuo 2.3Fast
- MiniMax Hailuo 02

**Music 模型**:
- Music-2.5
- Music-2.0

---

## 🔧 修复内容

### 1. Provider 配置
```json
{
  "minimax": {
    "models": [
      {
        "id": "MiniMax-M2.5",  // ✅ 修复
        "name": "MiniMax M2.5"
      }
    ]
  }
}
```

### 2. Fallback 策略
```json
{
  "model": {
    "fallbacks": [
      "minimax/MiniMax-M2.5"  // ✅ 修复
    ]
  }
}
```

### 3. Alias 配置
```json
{
  "models": {
    "minimax/MiniMax-M2.5": {  // ✅ 修复
      "alias": "MiniMax"
    }
  }
}
```

---

## 📊 修复验证

### Gateway 状态
- ✅ 已重启
- ✅ 配置已生效

### 预期效果
- ✅ GLM-5 失败时能正确切换到 MiniMax
- ✅ 不再出现 "unknown model" 错误
- ✅ 容灾机制正常工作

---

## 💡 经验教训

### 1. API 文档重要性
- ✅ 使用官方文档确认模型 ID
- ✅ 不要猜测模型名称

### 2. 错误排查流程
1. 查看错误信息
2. 检查官方文档
3. 修正配置
4. 重启服务
5. 验证修复

### 3. 配置验证
- ✅ 使用正确的模型 ID
- ✅ 保持 provider/model 格式一致
- ✅ 测试 fallback 功能

---

## 📝 相关文件

- **配置**: `~/.openclaw/openclaw.json`
- **官方文档**: https://platform.minimax.io/docs/guides/models-intro
- **修复记录**: `memory/minimax-model-fix-2026-02-18.md`

---

## 🎯 未来预防

### 自动检测（可以开发）
```bash
# 检测模型 ID 是否有效
openclaw model validate --provider minimax --model MiniMax-M2.5
```

### 配置模板
使用官方验证过的配置模板，避免手动输入错误。

---

**结论**: 问题已修复，模型容灾机制现在应该能正常工作。下次遇到类似错误，首先检查官方文档确认正确的模型 ID。
