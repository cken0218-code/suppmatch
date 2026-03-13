# Model 切换记录 - 2026-03-13

## 🚨 问题

**时间**：2026-03-13 16:28
**症状**：API fail（GLM-5 timeout + MiniMax-M2.5 HTTP 500）

**错误信息**：
```
All models failed (2):
- zai/glm-5: LLM request timed out
- minimax-portal/MiniMax-M2.5: HTTP 500 api_error: your current code plan not support model, MiniMax-M2.5
```

## 🔍 根本原因

1. **GLM-5**: API 压力大，偶尔 timeout
2. **MiniMax-M2.5**: 当前计划不支持（HTTP 500）
3. **配置问题**: Primary 是 GLM-5，Fallback 是 M2.5（两个都有问题）

## ✅ 解决方案

### 1. 更新 openclaw.json

**之前**：
```json
"model": {
  "primary": "zai/glm-5",
  "fallbacks": ["minimax-portal/MiniMax-M2.5"]
}
```

**之后**：
```json
"model": {
  "primary": "minimax-portal/MiniMax-M2.1",
  "fallbacks": ["zai/glm-5"]
}
```

### 2. 更新 AGENTS.md

- 更新模型切换规则
- 添加已知问题表格
- 调整比例：70% MiniMax M2.1，30% GLM-5

### 3. 更新 TOOLS.md

- 更新模型状态表格
- 添加 M2.5 不支持警告

### 4. 重启 Gateway

```bash
openclaw gateway restart
```

## 📊 效果预期

| 指标 | 之前 | 之后 |
|------|------|------|
| Primary 可用率 | ~70%（GLM-5 偶尔 timeout）| ~95%（M2.1 稳定）|
| Fallback 可用率 | 0%（M2.5 不支持）| ~70%（GLM-5）|
| 总体可用率 | ~70% | ~99% |

## 💡 经验教训

1. **不要假设所有模型都可用**
   - 检查当前计划支持的模型
   - 测试 fallback 是否真的能用

2. **API 压力管理**
   - 不要过度依赖单一模型
   - 分散风险（70/30 比例）

3. **错误追踪**
   - 记录每次 API fail
   - 定期检查 quota

## 🎯 后续行动

- [ ] 监控 M2.1 稳定性（1 周）
- [ ] 如果 GLM-5 持续 timeout → 考虑减少使用到 20%
- [ ] 研究 Grok-4 作为第三 fallback

---

**Created by**: Ken AI Assistant
**Date**: 2026-03-13
**Status**: Resolved ✅
