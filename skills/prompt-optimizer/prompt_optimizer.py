#!/usr/bin/env python3
"""
Prompt Optimizer - Use Grok to optimize user prompts before execution
"""

import os
import sys
import json
from typing import Optional, Dict, Any

# Try to import OpenAI-compatible client
try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False
    print("Warning: openai package not installed. Run: pip install openai")


class PromptOptimizer:
    """Optimize user prompts using Grok API"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("XAI_API_KEY")
        self.base_url = "https://api.x.ai/v1"
        self.model = "grok-4-1-fast"  # Best value for money
        
        if HAS_OPENAI and self.api_key:
            self.client = OpenAI(
                api_key=self.api_key,
                base_url=self.base_url
            )
        else:
            self.client = None
    
    def optimize(
        self, 
        user_prompt: str, 
        target_model: str = "GLM-5",
        task_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Optimize a user prompt for better execution.
        
        Args:
            user_prompt: The original user prompt
            target_model: The model that will execute the prompt
            task_type: Optional task type hint (research, content, code, etc.)
        
        Returns:
            Dict with optimized prompt and metadata
        """
        
        if not self.client:
            return {
                "success": False,
                "error": "Grok API not configured. Set XAI_API_KEY environment variable.",
                "original_prompt": user_prompt,
                "optimized_prompt": None
            }
        
        optimization_prompt = f"""你是一個 Prompt 優化專家。請分析並優化以下用戶指令。

## 用戶原始指令
{user_prompt}

## 目標執行模型
{target_model}

## 優化要求

1. **識別任務類型**
   - Research（研究/分析）
   - Content（內容創作）
   - Organization（整理/歸檔）
   - Monitoring（監控/檢查）
   - Development（開發/編程）

2. **補充缺少的參數**
   - 時間範圍
   - 數據源
   - 輸出格式
   - 數量限制

3. **明確執行步驟**
   - 第一步做什麼
   - 需要什麼工具
   - 輸出到哪裡

4. **輸出格式**
   - 表格 > 列表 > 純文本
   - 繁體中文 + 廣東話口語（如適用）

## 輸出格式

請以以下格式輸出優化後的指令：

```
任務：[任務名稱]

參數：
- [參數1]: [值1]
- [參數2]: [值2]

執行步驟：
1. [步驟1]
2. [步驟2]

輸出格式：
[具體的輸出格式要求]

工具：
- 使用 [skill名稱]
- 輸出到 [文件路徑]
```

只輸出優化後的指令，不要有其他解釋。"""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "你是一個專業的 Prompt 優化專家，擅長將簡單的用戶指令轉換為結構化、可執行的詳細指令。"},
                    {"role": "user", "content": optimization_prompt}
                ],
                temperature=0.3,  # Lower temperature for more consistent output
                max_tokens=2000
            )
            
            optimized = response.choices[0].message.content
            
            return {
                "success": True,
                "original_prompt": user_prompt,
                "optimized_prompt": optimized,
                "target_model": target_model,
                "optimizer_model": self.model,
                "usage": {
                    "input_tokens": response.usage.prompt_tokens,
                    "output_tokens": response.usage.completion_tokens
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "original_prompt": user_prompt,
                "optimized_prompt": None
            }
    
    def optimize_and_format(self, user_prompt: str, target_model: str = "GLM-5") -> str:
        """Optimize and return formatted string for display"""
        result = self.optimize(user_prompt, target_model)
        
        if not result["success"]:
            return f"❌ 優化失敗: {result['error']}"
        
        output = f"""
📝 **指令優化結果**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**原始指令：**
{result['original_prompt']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**優化後指令：**
{result['optimized_prompt']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**優化器：** {result['optimizer_model']}
**目標模型：** {result['target_model']}
**Token 用量：** {result.get('usage', {}).get('input_tokens', '?')} in / {result.get('usage', {}).get('output_tokens', '?')} out
"""
        return output


def main():
    """CLI interface"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Optimize prompts using Grok API"
    )
    parser.add_argument(
        "prompt",
        help="The user prompt to optimize"
    )
    parser.add_argument(
        "--target", "-t",
        default="GLM-5",
        help="Target model for execution (default: GLM-5)"
    )
    parser.add_argument(
        "--raw", "-r",
        action="store_true",
        help="Output only the optimized prompt (no formatting)"
    )
    parser.add_argument(
        "--api-key",
        help="Grok API key (or set XAI_API_KEY env var)"
    )
    
    args = parser.parse_args()
    
    optimizer = PromptOptimizer(api_key=args.api_key)
    result = optimizer.optimize(args.prompt, args.target)
    
    if args.raw:
        if result["success"]:
            print(result["optimized_prompt"])
        else:
            print(f"Error: {result['error']}", file=sys.stderr)
            sys.exit(1)
    else:
        print(optimizer.optimize_and_format(args.prompt, args.target))


if __name__ == "__main__":
    main()
