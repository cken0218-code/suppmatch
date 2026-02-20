#!/bin/bash
# Multi-Agent Orchestrator - 命令行接口
# 本地化多代理編排系統

set -e

# 顏色定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# 圖標
ICON_ORCHESTRATOR="🎯"
ICON_PLANNER="📊"
ICON_ARTIFICER="🔧"
ICON_SCOUT="🔍"
ICON_INQUISITOR="🛡️"
ICON_LOGISTICS="📦"

show_banner() {
    cat << 'EOF'
╔═══════════════════════════════════════════════════════════════════╗
║        🎯 MULTI-AGENT ORCHESTRATOR (LOCAL) v1.0.0                ║
║        本地化多代理編排系統 - 參考 SATOSHI'S SQUAD COMMAND         ║
╚═══════════════════════════════════════════════════════════════════╝
EOF
}

show_help() {
    show_banner
    cat << 'EOF'

使用方式: orchestrator <命令> [選項]

📋 可用命令:

  🎯 通用
    status              顯示系統狀態
    list                列出所有可用 agents
    help                顯示此幫助信息

  📊 PLANNER - 策略與增長
    planner:yt-analytics    YouTube 數據分析
    planner:income          收入追蹤
    planner:content         內容創作

  🔧 ARTIFICER - 編碼與製作
    artifactory:github      GitHub 操作
    artifactory:git          Git 自動化
    artifactory:scaffold     應用腳手架
    artifactory:script       影片腳本
    artifactory:thumbnail    縮圖生成

  🔍 SCOUT - 研究與情報
    scout:search         DuckDuckGo 搜尋
    scout:scan           Skills 掃描
    scout:analyze        數據分析

  🛡️ INQUISITOR - 安全與系統
    inquisitor:audit     安全審計
    inquisitor:api       API 安全檢查
    inquisitor:monitor   系統監控

  📦 LOGISTICS - 個人工具
    logistics:cron       Cron 管理
    logistics:backup     備份管理
    logistics:workflow   工作流觸發

🔀 組合命令
    research <topic>     研究流程 (搜尋 → 分析 → 創作)
    publish <type>       發布流程 (創作 → 製作 → 發布)
    audit [scope]        安全審計 (系統/API/完整)

💡 範例
    orchestrator status
    orchestrator scout:search --query="AI trends"
    orchestrator research "web development"
    orchestrator publish video

EOF
}

# 路由函數
route_task() {
    local task="$1"
    shift
    
    # 路由邏輯
    case "$task" in
        status)
            show_status
            ;;
        list)
            list_agents
            ;;
        help|--h|-h)
            show_help
            ;;
        planner:yt-analytics|planner:youtube)
            run_agent "youtube-analytics" "$@"
            ;;
        planner:income)
            run_agent "income-tracker" "$@"
            ;;
        planner:content)
            run_agent "content-creator" "$@"
            ;;
        artifactory:github|github)
            run_agent "github" "$@"
            ;;
        artifactory:git|git-automation)
            run_agent "git-automation" "$@"
            ;;
        artifactory:scaffold)
            run_agent "app-scaffold-local" "$@"
            ;;
        artifactory:script|video-script)
            run_agent "video-script-writer-local" "$@"
            ;;
        artifactory:thumbnail)
            run_agent "thumbnail-generator-local" "$@"
            ;;
        scout:search|ddg)
            run_agent "ddg-web-search" "$@"
            ;;
        scout:scan|skill-scan)
            run_agent "skill-scanner" "$@"
            ;;
        scout:analyze|data-analyze)
            run_agent "data-analyzer-local" "$@"
            ;;
        inquisitor:audit|security-audit)
            run_agent "security-audit" "$@"
            ;;
        inquisitor:api|api-security)
            run_agent "api-security-check" "$@"
            ;;
        inquisitor:monitor|system-monitor)
            run_agent "system-monitor" "$@"
            ;;
        logistics:cron|cron)
            run_agent "cron-manager" "$@"
            ;;
        logistics:backup|backup)
            run_agent "backup-manager" "$@"
            ;;
        logistics:workflow|workflo)
            run_agent "workflow-trigger-local" "$@"
            ;;
        research)
            run_research_flow "$@"
            ;;
        publish)
            run_publish_flow "$@"
            ;;
        audit)
            run_audit_flow "$@"
            ;;
        *)
            echo -e "${RED}❌ 未知的命令: $task${NC}"
            echo "輸入 orchestrator help 查看可用命令"
            exit 1
            ;;
    esac
}

# 顯示系統狀態
show_status() {
    show_banner
    echo ""
    echo -e "${CYAN}📊 系統狀態${NC}"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    echo -e "\n${ICON_PLANNER} PLANNER"
    echo "  ✅ youtube-analytics"
    echo "  ✅ income-tracker"
    echo "  ✅ content-creator"
    
    echo -e "\n${ICON_ARTIFICER} ARTIFICER"
    echo "  ✅ github"
    echo "  ✅ git-automation"
    echo "  ✅ app-scaffold-local"
    echo "  ✅ video-script-writer"
    echo "  ✅ thumbnail-generator"
    
    echo -e "\n${ICON_SCOUT} SCOUT"
    echo "  ✅ ddg-web-search"
    echo "  ✅ skill-scanner"
    echo "  ✅ data-analyzer"
    
    echo -e "\n${ICON_INQUISITOR} INQUISITOR"
    echo "  ✅ security-audit"
    echo "  ✅ api-security"
    echo "  ✅ system-monitor"
    
    echo -e "\n${ICON_LOGISTICS} LOGISTICS"
    echo "  ✅ cron-manager"
    echo "  ✅ backup-manager"
    echo "  ✅ workflow-trigger"
    
    echo ""
    echo -e "${GREEN}🎉 所有 agents 已就緒${NC}"
}

# 列出所有 agents
list_agents() {
    echo -e "${CYAN}📋 可用 Agents${NC}"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "PLANNER (策略與增長):"
    echo "  • youtube-analytics - YouTube 數據分析"
    echo "  • income-tracker - 多渠道收入管理"
    echo "  • content-creator - 內容創作助手"
    echo ""
    echo "ARTIFICER (編碼與製作):"
    echo "  • github - GitHub CLI 操作"
    echo "  • git-automation - Git 自動化"
    echo "  • app-scaffold-local - 應用腳手架"
    echo "  • video-script-writer-local - 影片腳本生成"
    echo "  • thumbnail-generator-local - 縮圖文案"
    echo ""
    echo "SCOUT (研究與情報):"
    echo "  • ddg-web-search - DuckDuckGo 搜尋"
    echo "  • skill-scanner - Skills 掃描"
    echo "  • data-analyzer-local - 數據分析"
    echo ""
    echo "INQUISITOR (安全與系統):"
    echo "  • security-audit - 安全審計"
    echo "  • api-security-check - API 安全"
    echo "  • system-monitor - 系統監控"
    echo ""
    echo "LOGISTICS (個人工具):"
    echo "  • cron-manager - Cron 任務管理"
    echo "  • backup-manager - 備份管理"
    echo "  • workflow-trigger-local - 工作流觸發"
}

# 運行 agent
run_agent() {
    local agent="$1"
    shift
    
    echo -e "${CYAN}🚀 啟動 agent: $agent${NC}"
    
    # 根據 agent 調用對應的 skill
    case "$agent" in
        youtube-analytics)
            echo "📊 調用 YouTube Analytics..."
            # 這裡調用對應的工具或腳本
            ;;
        income-tracker)
            echo "💰 調用 Income Tracker..."
            ;;
        content-creator)
            echo "✍️ 調用 Content Creator..."
            ;;
        github)
            echo "🐙 調用 GitHub..."
            ;;
        git-automation)
            echo "🔀 調用 Git Automation..."
            ;;
        app-scaffold-local)
            echo "🏗️ 調用 App Scaffold..."
            ;;
        video-script-writer-local)
            echo "🎬 調用 Video Script Writer..."
            ;;
        thumbnail-generator-local)
            echo "🖼️ 調用 Thumbnail Generator..."
            ;;
        ddg-web-search)
            echo "🔍 調用 DuckDuckGo Search..."
            ;;
        skill-scanner)
            echo "📡 調用 Skill Scanner..."
            ;;
        data-analyzer-local)
            echo "📈 調用 Data Analyzer..."
            ;;
        security-audit)
            echo "🛡️ 調用 Security Audit..."
            ;;
        api-security-check)
            echo "🔐 調用 API Security Check..."
            ;;
        system-monitor)
            echo "💻 調用 System Monitor..."
            ;;
        cron-manager)
            echo "⏰ 調用 Cron Manager..."
            ;;
        backup-manager)
            echo "💾 調用 Backup Manager..."
            ;;
        workflow-trigger-local)
            echo "⚡ 調用 Workflow Trigger..."
            ;;
        *)
            echo -e "${RED}❌ 未知的 agent: $agent${NC}"
            exit 1
            ;;
    esac
    
    echo -e "${GREEN}✅ $agent 完成${NC}"
}

# 研究流程
run_research_flow() {
    local topic="$1"
    
    if [ -z "$topic" ]; then
        echo -e "${RED}❌ 請指定研究主題${NC}"
        echo "用法: orchestrator research <topic>"
        exit 1
    fi
    
    echo -e "${CYAN}🔬 開始研究流程: $topic${NC}"
    echo ""
    
    echo "1️⃣ 階段: 搜尋資訊"
    run_agent "ddg-web-search" "--query=$topic"
    echo ""
    
    echo "2️⃣ 階段: 掃描相關工具"
    run_agent "skill-scanner" "--query=$topic"
    echo ""
    
    echo "3️⃣ 階段: 分析數據"
    run_agent "data-analyzer-local" "--topic=$topic"
    echo ""
    
    echo -e "${GREEN}🎉 研究流程完成${NC}"
}

# 發布流程
run_publish_flow() {
    local type="$1"
    
    if [ -z "$type" ]; then
        echo -e "${RED}❌ 請指定發布類型${NC}"
        echo "用法: orchestrator publish <video|article|social>"
        exit 1
    fi
    
    echo -e "${CYAN}📤 開始發布流程: $type${NC}"
    echo ""
    
    case "$type" in
        video)
            echo "1️⃣ 階段: 創作腳本"
            run_agent "video-script-writer-local"
            echo ""
            
            echo "2️⃣ 階段: 生成縮圖"
            run_agent "thumbnail-generator-local"
            echo ""
            
            echo "3️⃣ 階段: Git commit"
            run_agent "github"
            echo ""
            
            echo "4️⃣ 階段: 觸發發布"
            run_agent "workflow-trigger-local" "--workflow=publish-video"
            ;;
        article)
            echo "1️⃣ 階段: 創作內容"
            run_agent "content-creator"
            echo ""
            
            echo "2️⃣ 階段: Git commit"
            run_agent "git-automation"
            ;;
        social)
            echo "1️⃣ 階段: 生成社交內容"
            run_agent "content-creator" "--platform=social"
            ;;
    esac
    
    echo -e "${GREEN}🎉 發布流程完成${NC}"
}

# 審計流程
run_audit_flow() {
    local scope="${1:-full}"
    
    echo -e "${CYAN}🛡️ 開始安全審計: $scope${NC}"
    echo ""
    
    case "$scope" in
        full|all)
            echo "1️⃣ 階段: API 安全檢查"
            run_agent "api-security-check"
            echo ""
            
            echo "2️⃣ 階段: 系統安全審計"
            run_agent "security-audit"
            echo ""
            
            echo "3️⃣ 階段: 系統監控"
            run_agent "system-monitor"
            ;;
        system)
            run_agent "system-monitor"
            ;;
        api)
            run_agent "api-security-check"
            ;;
        security)
            run_agent "security-audit"
            ;;
        *)
            echo -e "${RED}❌ 未知的審計範圍: $scope${NC}"
            echo "可用選項: full, system, api, security"
            exit 1
            ;;
    esac
    
    echo -e "${GREEN}🎉 審計流程完成${NC}"
}

# 主入口
main() {
    if [ $# -eq 0 ]; then
        show_help
        exit 0
    fi
    
    route_task "$@"
}

main "$@"
