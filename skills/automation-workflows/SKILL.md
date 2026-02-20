# automation-workflows

本地工作流自動化工具 - File operations、Git 整合、系統命令

## 功能

### 📁 File Operations
- 批量文件移動/複製/重命名
- 資料夾結構創建
- 文件內容批量處理
- 備份與同步

### 🔧 Git Workflows
- 自動 commit 與 push
- Branch 管理
- Pull request 創建
- Git status 監控

### ⚙️ System Automation
- 排程任務執行
- 系統監控自動化
- 定期清理任務
- 自動化腳本執行

## 使用方式

```bash
# 文件操作
claw workflow move --pattern "*.tmp" --destination /tmp

# Git 自動化
claw workflow git commit --message "auto: backup" --push

# 系統任務
claw workflow cron --daily "cleanup-logs"
```

## 依賴
- 無外部 API
- 100% 本地操作
