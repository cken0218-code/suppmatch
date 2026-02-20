#!/bin/bash
# 發布流程示例 - 演示如何執行完整的影片發布工作流

source "$(dirname "$0")/orchestrator.sh"

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║           📤 MULTI-AGENT PUBLISH FLOW                   ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

if [ -z "$1" ]; then
    echo -e "${RED}❌ 請指定發布類型${NC}"
    echo ""
    echo "用法:"
    echo "  $0 video \"AI Tutorial\""
    echo "  $0 article \"技術文章標題\""
    echo "  $0 social \"社交媒體內容\""
    echo ""
    exit 1
fi

TYPE="$1"
TITLE="${2:-Untitled}"

echo -e "${CYAN}發布類型: $TYPE${NC}"
echo -e "${CYAN}標題: $TITLE${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 流程配置
STEPS=4
CURRENT_STEP=1

case "$TYPE" in
    video)
        echo "🎬 影片發布流程"
        echo ""
        
        # 階段 1: 創作腳本
        echo ""
        echo -e "${YELLOW}[$CURRENT_STEP/$STEPS] 階段 1: 創作腳本${NC}"
        echo "─────────────────────────────────────────────────────────"
        run_agent "video-script-writer-local" "--title=\"$TITLE\""
        ((CURRENT_STEP++))
        
        # 階段 2: 生成縮圖
        echo ""
        echo -e "${YELLOW}[$CURRENT_STEP/$STEPS] 階段 2: 生成縮圖${NC}"
        echo "─────────────────────────────────────────────────────────"
        run_agent "thumbnail-generator-local" "--title=\"$TITLE\""
        ((CURRENT_STEP++))
        
        # 階段 3: Git commit
        echo ""
        echo -e "${YELLOW}[$CURRENT_STEP/$STEPS] 階段 3: Git Commit${NC}"
        echo "─────────────────────────────────────────────────────────"
        run_agent "git-automation" "--message=\"Add video: $TITLE\" --files=\"script.md thumbnail.png\""
        ((CURRENT_STEP++))
        
        # 階段 4: 觸發發布
        echo ""
        echo -e "${YELLOW}[$CURRENT_STEP/$STEPS] 階段 4: 觸發發布${NC}"
        echo "─────────────────────────────────────────────────────────"
        run_agent "workflow-trigger-local" "--workflow=publish-video --title=\"$TITLE\""
        ((CURRENT_STEP++))
        ;;
        
    article)
        echo "📝 文章發布流程"
        echo ""
        
        # 階段 1: 創作內容
        echo ""
        echo -e "${YELLOW}[$CURRENT_STEP/$STEPS] 階段 1: 創作內容${NC}"
        echo "─────────────────────────────────────────────────────────"
        run_agent "content-creator" "--title=\"$TITLE\" --type=article"
        ((CURRENT_STEP++))
        
        # 階段 2: Git commit
        echo ""
        echo -e "${YELLOW}[$CURRENT_STEP/$STEPS] 階段 2: Git Commit${NC}"
        echo "─────────────────────────────────────────────────────────"
        run_agent "git-automation" "--message=\"Publish article: $TITLE\" --files=\"article.md\""
        ;;
        
    social)
        echo "📱 社交媒體發布流程"
        echo ""
        
        # 階段 1: 生成內容
        echo ""
        echo -e "${YELLOW}[$CURRENT_STEP/$STEPS] 階段 1: 生成社交內容${NC}"
        echo "─────────────────────────────────────────────────────────"
        run_agent "content-creator" "--title=\"$TITLE\" --type=social"
        ;;
        
    *)
        echo -e "${RED}❌ 未知的發布類型: $TYPE${NC}"
        echo "可用類型: video, article, social"
        exit 1
        ;;
esac

# 完成
echo ""
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║              🎉 發布流程完成                              ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""
echo -e "${GREEN}✅ 發布完成: $TYPE - $TITLE${NC}"
echo ""
echo "💡 後續建議:"
echo "  • 使用 youtube-analytics 追蹤觀看"
echo "  • 使用 income-tracker 追蹤收益"
echo "  • 使用 planner:content 規劃下一個內容"
