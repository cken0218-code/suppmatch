#!/bin/bash
# 安全審計流程示例 - 演示如何執行完整的安全審計工作流

source "$(dirname "$0")/orchestrator.sh"

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║           🛡️ MULTI-AGENT SECURITY AUDIT                  ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

SCOPE="${1:-full}"

echo -e "${CYAN}審計範圍: $SCOPE${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 流程配置
STEPS=3
CURRENT_STEP=1

case "$SCOPE" in
    full|all)
        echo "🔒 完整安全審計"
        echo ""
        
        # 階段 1: API 安全檢查
        echo ""
        echo -e "${YELLOW}[$CURRENT_STEP/$STEPS] 階段 1: API 安全檢查${NC}"
        echo "─────────────────────────────────────────────────────────"
        echo "檢查敏感信息洩露..."
        run_agent "api-security-check" "--scan=all"
        ((CURRENT_STEP++))
        
        # 階段 2: 系統安全審計
        echo ""
        echo -e "${YELLOW}[$CURRENT_STEP/$STEPS] 階段 2: 系統安全審計${NC}"
        echo "─────────────────────────────────────────────────────────"
        echo "評估系統風險..."
        run_agent "security-audit" "--full=true"
        ((CURRENT_STEP++))
        
        # 階段 3: 系統監控
        echo ""
        echo -e "${YELLOW}[$CURRENT_STEP/$STEPS] 階段 3: 系統監控${NC}"
        echo "─────────────────────────────────────────────────────────"
        echo "監控 CPU/記憶體/磁碟..."
        run_agent "system-monitor" "--check=all"
        ;;
        
    api)
        echo "🔐 API 安全檢查"
        echo ""
        run_agent "api-security-check" "--scan=all"
        ;;
        
    system)
        echo "💻 系統監控與審計"
        echo ""
        run_agent "system-monitor" "--check=all"
        echo ""
        run_agent "security-audit" "--full=false"
        ;;
        
    security)
        echo "🛡️ 安全審計"
        echo ""
        run_agent "security-audit" "--full=true"
        ;;
        
    *)
        echo -e "${RED}❌ 未知的審計範圍: $SCOPE${NC}"
        echo ""
        echo "可用範圍:"
        echo "  full   - 完整審計 (API + 安全 + 監控)"
        echo "  api    - 僅 API 安全檢查"
        echo "  system - 系統監控與安全"
        echo "  security - 安全審計"
        echo ""
        echo "用法:"
        echo "  $0 full"
        echo "  $0 api"
        echo "  $0 system"
        echo ""
        exit 1
        ;;
esac

# 完成
echo ""
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║              🎉 審計流程完成                              ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""
echo -e "${GREEN}✅ 安全審計完成: $SCOPE${NC}"
echo ""
echo "💡 後續建議:"
echo "  • 使用 backup-manager 備份配置"
echo "  • 使用 cron-manager 設定定期審計"
echo "  • 發現問題立即修復"
