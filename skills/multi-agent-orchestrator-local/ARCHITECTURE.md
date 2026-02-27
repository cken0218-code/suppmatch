# 詳細架構設計

## 系統層級圖

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              用戶輸入層                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│  渠道: Discord, Slack, Terminal, API                                        │
│  格式: 自然語言、命令格式、API 調用                                          │
└──────────────────────────────────┬────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           意圖識別層 (Intent Layer)                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Intent Classifier                                                    │   │
│  │                                                                     │   │
│  │   ┌─────────┐     ┌─────────┐     ┌─────────┐     ┌─────────┐      │   │
│  │   │ Keyword │     │  Pattern│     │ Context │     │ History │      │   │
│  │   │ Matcher │     │ Matcher │     │ Analyzer│     │  Lookup │      │   │
│  │   └────┬────┘     └────┬────┘     └────┬────┘     └────┬────┘      │   │
│  │        │               │               │               │            │   │
│  │        └───────────────┴───────────────┴───────────────┘            │   │
│  │                               │                                      │   │
│  │                               ▼                                      │   │
│  │                    ┌────────────────────┐                            │   │
│  │                    │  Intent Decision   │                            │   │
│  │                    │  (Planner/Artificer│                           │   │
│  │                    │   Scout/Inquisitor │                            │   │
│  │                    │   /Logistics)     │                            │   │
│  │                    └────────────────────┘                            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└──────────────────────────────────┬────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          複雜度評估層 (Complexity Layer)                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Complexity Analyzer                                                 │   │
│  │                                                                     │   │
│  │   Factors:                                                         │   │
│  │   • Input length (tokens)                                           │   │
│  │   • Task type (research/code/writing/etc)                           │   │
│  │   • Expected output length                                          │   │
│  │   • Historical complexity                                           │   │
│  │                                                                     │   │
│  │   Output:                                                           │   │
│  │   • Simple → MiniMax (90%)                                         │   │
│  │   • Complex → GLM-5 (10%)                                          │   │
│  │                                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└──────────────────────────────────┬────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           技能路由層 (Skill Routing Layer)                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Skill Registry                                                      │   │
│  │                                                                     │   │
│  │   PLANNER SKILLS:                                                   │   │
│  │   ├── youtube-analytics-local    [READY]                            │   │
│  │   ├── content-creator-local     [READY]                            │   │
│  │   ├── video-script-writer-local  [READY]                            │   │
│  │   └── income-tracker-local       [READY]                            │   │
│  │                                                                     │   │
│  │   ARTIFICER SKILLS:                                                 │   │
│  │   ├── app-scaffold-local        [READY]                            │   │
│  │   ├── github                    [READY]                            │   │
│  │   ├── git-automation            [READY]                            │   │
│  │   ├── auto-publisher-local      [READY]                            │   │
│  │   └── automation-workflows      [READY]                            │   │
│  │                                                                     │   │
│  │   SCOUT SKILLS:                                                     │   │
│  │   ├── ddg-web-search            [READY]                            │   │
│  │   ├── data-analyzer-local       [READY]                            │   │
│  │   └── skill-scanner             [READY]                            │   │
│  │                                                                     │   │
│  │   INQUISITOR SKILLS:                                                │   │
│  │   ├── security-audit            [READY]                            │   │
│  │   ├── api-security-check        [READY]                            │   │
│  │   ├── system-monitor            [READY]                            │   │
│  │   ├── cron-manager              [READY]                            │   │
│  │   └── agent-audit               [READY]                            │   │
│  │                                                                     │   │
│  │   LOGISTICS SKILLS:                                                 │   │
│  │   ├── backup-manager            [READY]                            │   │
│  │   ├── workflow-trigger-local    [READY]                            │   │
│  │   ├── openclaw-token-save       [READY]                            │   │
│  │   └── token-maximizer           [READY]                            │   │
│  │                                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└──────────────────────────────────┬────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    🦞 Superpowers Task Dispatch Layer                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Superpowers Workflow (For Complex Tasks)                            │   │
│  │                                                                     │   │
│  │   ┌─────────────────┐     ┌─────────────────┐                     │   │
│  │   │  Brainstorming  │────▶│   Spec Writer   │                     │   │
│  │   │  (Clarify Goal) │     │  (Plan Draft)  │                     │   │
│  │   └─────────────────┘     └────────┬────────┘                     │   │
│  │                                     │                                │   │
│  │                                     ▼                                │   │
│  │   ┌─────────────────┐     ┌─────────────────┐                     │   │
│  │   │ Human Approval  │◀────│ Task Breakdown │                     │   │
│  │   │   (Checkpoint)  │     │ (2-5min tasks) │                     │   │
│────────  │   └┬────────┘     └────────┬────────┘                     │   │
│  │            │                       │                                │   │
│  │            │                       ▼                                │   │
│  │            │            ┌─────────────────┐                       │   │
│  │            │            │ Subagent Dispatch│                       │   │
│  │            │            │ (per task)      │                       │   │
│  │            │            └────────┬────────┘                       │   │
│  │            │                       │                                │   │
│  │            │                       ▼                                │   │
│  │            │            ┌─────────────────┐                       │   │
│  │            │            │ Two-Stage Review│                       │   │
│  │            │            │ 1. Spec Check   │                       │   │
│  │            │            │ 2. Quality Check│                       │   │
│  │            │            └────────┬────────┘                       │   │
│  │            │                       │                                │   │
│  │            └──────────────────────┘                                │   │
│  │                              │                                       │   │
│  │                              ▼                                      │   │
│  │                    ┌─────────────────┐                             │   │
│  │                    │  Finish Branch   │                             │   │
│  │                    │ PR/Merge/Discard│                             │   │
│  │                    └─────────────────┘                             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└──────────────────────────────────┬────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          執行引擎層 (Execution Engine Layer)                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────────────┐  ┌──────────────────────┐                      │
│  │  Pipeline Executor   │  │  Parallel Executor    │                      │
│  │  (Sequential)        │  │  (Concurrent)         │                      │
│  └──────────┬───────────┘  └──────────┬───────────┘                      │
│             │                        │                                   │
│             ▼                        ▼                                   │
│  ┌──────────────────────┐  ┌──────────────────────┐                      │
│  │ Task 1 → Task 2 → ...│  │ Task 1, Task 2, ...  │                      │
│  └──────────┬───────────┘  └──────────┬───────────┘                      │
│             │                        │                                   │
│             └───────────┬───────────┘                                   │
│                         ▼                                               │
│              ┌──────────────────────┐                                    │
│              │   Result Aggregator │                                    │
│              └──────────────────────┘                                    │
│                                                                             │
└──────────────────────────────────┬────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           輸出層 (Output Layer)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Output Formatter                                                     │   │
│  │                                                                     │   │
│  │   Channel适配:                                                       │   │
│  │   • Discord → Markdown                                              │   │
│  │   • Slack → Block Kit                                              │   │
│  │   • Terminal → Plain Text                                          │   │
│  │   • API → JSON                                                     │   │
│  │                                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 數據流程圖

```
User Input: "分析我的 YouTube 數據"

    │
    ▼

┌────────────────────────┐
│  Intent Recognition   │
│  ──────────────────── │
│  Keywords:            │
│  • "YouTube"          │
│  • "分析"             │
│  → Intent: PLANNER    │
└───────────┬────────────┘
            │
            ▼

┌────────────────────────┐
│ Complexity Assessment │
│  ────────────────────  │
│  • Input: 12 tokens    │
│  • Type: Analysis     │
│  → Complexity: HIGH   │
│  → Model: GLM-5       │
└───────────┬────────────┘
            │
            ▼

┌────────────────────────┐
│   Skill Selection     │
│  ────────────────────  │
│  Match:               │
│  "youtube-analysis"   │
│  → Skill:             │
│  youtube-analytics-   │
│  local                │
└───────────┬────────────┘
            │
            ▼

┌────────────────────────┐
│   Execution           │
│  ────────────────────  │
│  Mode: SINGLE         │
│  Agent: THE PLANNER    │
│  Skill: youtube-       │
│  analytics-local      │
│  Model: GLM-5         │
└───────────┬────────────┘
            │
            ▼

┌────────────────────────┐
│   Result Processing   │
│  ────────────────────  │
│  • Format output       │
│  • Add metadata        │
│  • Log execution       │
└───────────┬────────────┘
            │
            ▼

Output: 📊 YouTube 頻道月度報告...
```

---

## 狀態管理

```typescript
interface OrchestratorState {
  sessionId: string;
  userId: string;
  channel: string;
  
  intent: 'planner' | 'artificer' | 'scout' | 'inquisitor' | 'logistics';
  complexity: 'simple' | 'complex';
  model: 'minimax' | 'glm-5';
  
  selectedSkill: string;
  executionMode: 'single' | 'pipeline' | 'parallel' | 'debate';
  
  taskQueue?: Task[];
  results?: Result[];
  
  startedAt: Date;
  completedAt?: Date;
  tokenUsed: number;
}
```

---

## 錯誤處理

```typescript
class OrchestratorError extends Error {
  type: 'ROUTING_ERROR' | 'SKILL_NOT_FOUND' | 'EXECUTION_ERROR' | 'TIMEOUT';
  recoverable: boolean;
  fallback?: string;
}

// 錯誤處理策略
const ERROR_STRATEGIES = {
  SKILL_NOT_FOUND: {
    action: 'try_parent_agent',
    fallback: 'use_general_model'
  },
  EXECUTION_ERROR: {
    action: 'retry_with_downgrade',
    fallback: 'return_partial_result'
  },
  TIMEOUT: {
    action: 'return_progress',
    fallback: 'schedule_retry'
  }
};
```

---

## 監控指標

```typescript
const METRICS = {
  // 性能指標
  avgResponseTime: number,      // 平均響應時間
  p95ResponseTime: number,      // 95% 分位響應時間
  throughput: number,            // 每分鐘任務數
  
  // 成本指標
  totalTokens: number,
  minimaxTokens: number,
  glm5Tokens: number,
  costEstimate: number,
  
  // 質量指標  
  routingAccuracy: number,       // 路由準確率
  taskCompletionRate: number,   // 任務完成率
  userSatisfaction: number,     // 用戶滿意度
  
  // 系統指標
  activeSessions: number,
  errorRate: number,
  skillAvailability: Record<string, boolean>
};
```
