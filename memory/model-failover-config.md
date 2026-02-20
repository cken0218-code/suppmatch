# 模型容灾机制配置 - 2026-02-18

**目标**: 确保 Agent 永不停机，多级自动切换

---

## 📊 当前配置

### 主模型
- **Primary**: zai/glm-5 (GLM-5)
- **Fallback**: minimax/m2.5 (MiniMax) - 已定义但需要完善

### 需要的 Provider
根据小红书笔记建议：
1. **Anthropic** (Claude-3.5-Sonnet) - 高质量推理
2. **OpenAI** (GPT-4/GPT-4-turbo) - 稳定可靠
3. **Google** (Gemini Pro) - 备用选择

---

## 🎯 三级容灾策略

### Level 1: GLM-5 (主模型)
- **Provider**: zai
- **Model**: glm-5
- **Context**: 204800 tokens
- **Reasoning**: ✅
- **Cost**: 免费

### Level 2: MiniMax M2.5 (第一备用)
- **Provider**: minimax
- **Model**: m2.5
- **Context**: 大窗口
- **Reasoning**: ✅
- **Cost**: 便宜

### Level 3: OpenAI GPT-4 (第二备用)
- **Provider**: openai
- **Model**: gpt-4-turbo
- **Context**: 128000 tokens
- **Reasoning**: ✅
- **Cost**: 付费

### Level 4: Anthropic Claude (第三备用)
- **Provider**: anthropic
- **Model**: claude-3-5-sonnet-20241022
- **Context**: 200000 tokens
- **Reasoning**: ✅
- **Cost**: 付费

---

## 🔑 需要的 API Keys

### 必需（已有）
- ✅ **zai**: GLM-5 API key (已配置)

### 必需（需要添加）
- ⚠️ **minimax**: MiniMax API key (需要配置)

### 可选（推荐）
- ⚠️ **openai**: OpenAI API key
- ⚠️ **anthropic**: Anthropic API key

---

## 📝 配置步骤

### 步骤 1: 完善 MiniMax 配置

如果你有 MiniMax API key，我可以添加：

```json
{
  "providers": {
    "minimax": {
      "baseUrl": "https://api.minimax.chat/v1",
      "api": "openai-completions",
      "apiKey": "YOUR_MINIMAX_API_KEY",
      "models": [
        {
          "id": "m2.5",
          "name": "MiniMax M2.5",
          "reasoning": true,
          "contextWindow": 245000,
          "maxTokens": 16384
        }
      ]
    }
  }
}
```

### 步骤 2: 添加 OpenAI (可选)

```json
{
  "providers": {
    "openai": {
      "baseUrl": "https://api.openai.com/v1",
      "api": "openai-completions",
      "apiKey": "YOUR_OPENAI_API_KEY",
      "models": [
        {
          "id": "gpt-4-turbo",
          "name": "GPT-4 Turbo",
          "reasoning": true,
          "contextWindow": 128000,
          "maxTokens": 4096
        }
      ]
    }
  }
}
```

### 步骤 3: 添加 Anthropic (可选)

```json
{
  "providers": {
    "anthropic": {
      "baseUrl": "https://api.anthropic.com",
      "api": "anthropic",
      "apiKey": "YOUR_ANTHROPIC_API_KEY",
      "models": [
        {
          "id": "claude-3-5-sonnet-20241022",
          "name": "Claude 3.5 Sonnet",
          "reasoning": true,
          "contextWindow": 200000,
          "maxTokens": 8192
        }
      ]
    }
  }
}
```

### 步骤 4: 配置 Fallback 策略

```json
{
  "agents": {
    "defaults": {
      "model": {
        "primary": "zai/glm-5",
        "fallbacks": [
          "minimax/m2.5",
          "openai/gpt-4-turbo",
          "anthropic/claude-3-5-sonnet-20241022"
        ]
      }
    }
  }
}
```

---

## 🚨 容灾触发条件

自动切换会在以下情况触发：
1. **API 超时** - 请求超过 30 秒无响应
2. **Rate Limit** - 达到 API 限制
3. **服务不可用** - API 返回 5xx 错误
4. **认证失败** - API key 失效

---

## 💡 推荐配置（基于你的情况）

### 方案 A: 最小容灾（免费）
**只需完善 MiniMax**
- 主: GLM-5 (免费)
- 备: MiniMax M2.5 (便宜)

**优势**:
- ✅ 低成本
- ✅ 基本容灾
- ✅ 适合测试

### 方案 B: 标准容灾（推荐）
**添加 OpenAI**
- 主: GLM-5
- 备1: MiniMax M2.5
- 备2: OpenAI GPT-4-turbo

**优势**:
- ✅ 更可靠
- ✅ 高质量备用
- ✅ 适合生产

### 方案 C: 完整容灾（最强）
**添加所有 Provider**
- 主: GLM-5
- 备1: MiniMax M2.5
- 备2: OpenAI GPT-4-turbo
- 备3: Anthropic Claude-3.5-Sonnet

**优势**:
- ✅ 最高可靠性
- ✅ 多重保障
- ✅ 永不停机

---

## 📋 下一步

请告诉我：
1. **你有 MiniMax API key 吗？** (必需)
2. **你有 OpenAI API key 吗？** (推荐)
3. **你有 Anthropic API key 吗？** (可选)

或者，你可以直接提供 API keys，我会帮你配置：

```
格式：
- MiniMax API Key: xxxx
- OpenAI API Key: xxxx (可选)
- Anthropic API Key: xxxx (可选)
```

---

## ⚠️ 安全提醒

- ✅ API keys 会保存在本地配置文件
- ✅ 不会上传到云端
- ✅ 你可以随时修改或删除
- ✅ 建议使用环境变量（更安全）

---

**等待你的 API keys 信息，我会即刻帮你配置！** 🚀
