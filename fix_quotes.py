#!/usr/bin/env python3
"""Fix quotes in symptoms.ts"""

with open('src/data/symptoms.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix all wrong quotes patterns (curly quotes to straight quotes)
content = content.replace('name":', 'name:')
content = content.replace('"url":', 'url:')
content = content.replace('recommendations":', 'recommendations:')
content = content.replace('category_id":', 'category_id:')
content = content.replace('"zh-HK":', '"zh-HK":')
content = content.replace('"zh-CN":', '"zh-CN":')
content = content.replace('"en":', '"en":')

with open('src/data/symptoms.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed!")
