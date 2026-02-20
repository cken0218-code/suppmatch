#!/bin/bash
# 研究流程示例 - 演示如何執行完整的研究工作流

source "$(dirname "$0")/orchestrator.sh"

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║           🔬 MULTI-AGENT RESEARCH FLOW                   ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

if [ -z "$1" ]; then
    echo -e "${RED}❌ 請指定研究主題${NC}"
    echo ""
    echo "用法:"
    echo "  $0 \"AI trends 2026\""
    echo "  $0 \"YouTube automation\""
    echo "  $0 \"web development tools\""
    echo ""
    exit 1
fi

TOPIC="$1"
echo -e "${CYAN}研究主題: $TOPIC${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 流程配置
STEPS=3
CURRENT_STEP=1

# 階段 1: 搜尋
echo ""
echo -e "${YELLOW}[$CURRENT_STEP/$STEPS] 階段 1: 搜尋資訊${NC}"
echo "─────────────────────────────────────────────────────────"
run_agent "ddg-web-search" "--query=$TOPIC --limit=10"
((CURRENT_STEP++))

# 階段 2: 掃描
echo ""
echo -e "${YELLOW}[$CURRENT_STEP/$STEPS] 階段 2: 掃描工具${NC}"
echo "─────────────────────────────────────────────────────────"
run_agent "skill-scanner" "--query=$TOPIC --limit=5"
((CURRENT_STEP++))

# 階段 3: 分析
echo ""
echo -e "${YELLOW}[$CURRENT_STEP/$STEPS] 階段 3: 分析數據${NC}"
echo "─────────────────────────────────────────────────────────"
run_agent "data-analyzer-local" "--topic=$TOPIC"
((CURRENT_STEP++))

# 完成
echo ""
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║              🎉 研究流程完成                              ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""
echo -e "${GREEN}✅ 研究完成: $TOPIC${NC}"
echo ""
echo "💡 後續建議:"
echo "  • 使用 content-creator 生成內容計劃"
echo "  • 使用 workflow-trigger 設定定期監控"
echo "  • 使用 income-tracker 追蹤相關收益"
