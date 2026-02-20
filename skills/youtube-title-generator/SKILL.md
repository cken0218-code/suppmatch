# YouTube Title Generator

為 YouTube 影片生成吸引人的標題，提升點擊率和觀眾參與度。

## 功能

- 🎯 根據主題生成多種風格的標題
- 📊 5種標題風格：教學、吸引點擊、問答、趨勢、挑戰
- 🔍 標題分析功能（長度、數字、情緒詞）
- 💾 自動保存生成歷史
- 🎨 互動模式和命令列模式

## 安裝

```bash
cd /Users/cken0218/.openclaw/workspace/skills/youtube-title-generator
```

無需額外安裝，使用 Python 3 即可運行。

## 使用方法

### 互動模式

```bash
python3 youtube_title_generator.py
```

### 命令列模式

```bash
# 基本用法
python3 youtube_title_generator.py --topic "Python程式設計"

# 指定風格
python3 youtube_title_generator.py --topic "健身" --style "挑戰"

# 指定關鍵詞
python3 youtube_title_generator.py --topic "投資理財" --keywords "股票,基金,理財"

# 生成多個標題
python3 youtube_title_generator.py --topic "烹飪教學" --count 10

# 分析現有標題
python3 youtube_title_generator.py --analyze "你的標題文字"
```

### 參數說明

| 參數 | 簡寫 | 說明 | 預設 |
|------|------|------|------|
| `--topic` | `-t` | 影片主題 | 互動輸入 |
| `--style` | `-s` | 標題風格 | 吸引點擊 |
| `--keywords` | `-k` | 關鍵詞 (逗號分隔) | 使用主題 |
| `--count` | `-c` | 生成數量 | 5 |
| `--analyze` | `-a` | 分析現有標題 | - |
| `--output` | `-o` | 保存歷史檔案 | title_history.json |

### 標題風格

1. **教學** - 適合教學影片，突出學習價值
2. **吸引點擊** - 使用情緒化鉤子，提高點擊率
3. **問答** - 解答觀眾疑問，增加互動
4. **趨勢** - 跟隨時事熱潮，蹭熱度
5. **挑戰** - 製造懸念，吸引好奇心

## 輸出範例

```
🎬 主題: Python程式設計
🎨 風格: 吸引點擊
🏷️  關鍵詞: Python,程式設計
==================================================
✨ 生成的標題:
--------------------------------------------------
  1. 你絕對想不到的Python方法！
  2. Python背後的秘密 | 看完才懂
  3. Python讓我成功了！| 經驗分享
  4. Python注意事項 | 90%人都做錯
  5. 為什麼Python這麼有效？
--------------------------------------------------
💡 小提示:
   • 前30個字符最重要，確保包含核心關鍵詞
   • 使用數字和問句增加點擊率
   • 避免過度點擊誘餌 (clickbait)
```

## 標題分析

分析現有標題的各項指標：

- **長度** - YouTube 標題最佳長度 30-60 字元
- **數字** - 包含數字的標題點擊率更高
- **情緒詞** - 情緒化詞彙增加吸引力
- **建議** - 針對性的優化建議

```bash
python3 youtube_title_generator.py --analyze "震驚！Python十分鐘學會"
```

## 集成到工作流

```python
from youtube_title_generator import YouTubeTitleGenerator

generator = YouTubeTitleGenerator()

# 生成標題
titles = generator.generate(
    topic="產品評測",
    style="吸引點擊",
    keywords=["iPhone,手機,評測"],
    count=10
)

for title in titles:
    print(f"- {title}")
```

## 最佳實踐

1. **A/B 測試** - 生成多個標題進行測試
2. **關鍵詞優先** - 核心關鍵詞放在前 30 字元
3. **避免 clickbait** - 標題要與內容相符
4. **數字效應** - 使用具體數字增加可信度
5. **情緒連結** - 使用情緒詞引發觀眾共鳴

## 文件結構

```
youtube-title-generator/
├── youtube_title_generator.py  # 主程式
├── SKILL.md                   # 本文件
└── title_history.json          # 生成歷史 (運行後產生)
```

## 依賴

- Python 3.7+
- 無需第三方套件 (標準函式庫即可)

## 更新日誌

### v1.0.0
- 初始版本
- 5種標題風格
- 標題分析功能
- 歷史記錄保存
