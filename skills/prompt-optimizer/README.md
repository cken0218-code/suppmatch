# Prompt Optimizer Skill

Use Grok to optimize user prompts before executing with other models.

## Quick Start

```bash
# Install dependencies
pip install openai

# Set API key
export XAI_API_KEY="your_grok_api_key"

# Run
python3 prompt_optimizer.py "帮我睇下 CBA 股票"
```

## Usage

### As CLI

```bash
# Basic usage
python3 prompt_optimizer.py "你的指令"

# Specify target model
python3 prompt_optimizer.py "你的指令" --target MiniMax

# Raw output (only optimized prompt)
python3 prompt_optimizer.py "你的指令" --raw
```

### As Python Module

```python
from prompt_optimizer import PromptOptimizer

optimizer = PromptOptimizer()
result = optimizer.optimize("帮我睇下 CBA 股票")

if result["success"]:
    print(result["optimized_prompt"])
```

## Configuration

Add to `~/.openclaw/openclaw.json`:

```json
{
  "providers": {
    "xai": {
      "apiKey": "your_grok_api_key",
      "baseUrl": "https://api.x.ai/v1"
    }
  }
}
```

## Cost

Using Grok 4.1 Fast:
- Input: $0.20 / 1M tokens
- Output: $0.50 / 1M tokens
- Estimated cost per optimization: ~$0.001

## Examples

See SKILL.md for detailed examples.
