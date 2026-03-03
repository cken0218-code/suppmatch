#!/usr/bin/env python3
"""
第一個 Multi-Agent Demo
兩個 AI 一齊工作：Researcher + Writer
"""

from crewai import Agent, Task, Crew

# Agent 1: 研究員（搵料）
researcher = Agent(
    role="研究員",
    goal="搵最新 AI trending topics",
    backstory="你係一個專門搵科技趨勢嘅研究員",
    verbose=True
)

# Agent 2: 寫手（寫文）
writer = Agent(
    role="內容寫手",
    goal="將研究結果寫成廣東話貼文",
    backstory="你係一個擅長用廣東話寫科技內容嘅寫手",
    verbose=True
)

# Task 1: 研究
research_task = Task(
    description="搵 3 個 2026 年最 hot 嘅 AI agent 趨勢",
    agent=researcher,
    expected_output="3 個 AI agent 趨勢，每個一行"
)

# Task 2: 寫文
write_task = Task(
    description="用廣東話寫一個 IG 貼文，介紹剛才搵到嘅 AI 趨勢",
    agent=writer,
    expected_output="一個完整嘅 IG 貼文（廣東話）"
)

# 組隊
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    verbose=True
)

# 開工！
print("🐱 Multi-Agent 開始運作...\n")
result = crew.run()
print("\n" + "="*50)
print("🎯 最終輸出：")
print("="*50)
print(result)
