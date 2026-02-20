---
name: app-scaffold-local
description: 本地应用脚手架工具（安全替代 app-builder）
version: 1.0.0
author: local
license: MIT
---

# App Scaffold Local - 应用脚手架工具

## 安全说明
- ✅ 完全本地运行，不依赖外部服务
- ✅ 使用标准工具（Node.js, Python, Git）
- ✅ 代码清晰可读
- ✅ 用户完全控制

## 功能
- 快速创建应用脚手架
- 支持多种应用模板
- 自动配置开发环境
- 集成常用工具和库

## 支持的应用类型

### 1. Node.js 应用
- Express API
- Next.js Web App
- React SPA
- Vue.js App
- CLI Tool

### 2. Python 应用
- Flask API
- FastAPI
- Django Web App
- CLI Tool
- Data Science Project

### 3. 静态网站
- HTML/CSS/JS
- Bootstrap Template
- Tailwind CSS

## 使用方式

### 创建新应用

#### Node.js Express API
```bash
# 创建项目目录
mkdir my-api && cd my-api

# 初始化
npm init -y

# 安装依赖
npm install express cors dotenv

# 创建基础结构
mkdir -p src/routes src/controllers src/models

# 创建入口文件
cat > src/index.js << 'EOF'
const express = require('express');
const cors = require('cors');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

app.get('/health', (req, res) => {
  res.json({ status: 'ok' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
EOF

# 创建 .env 文件
cat > .env << 'EOF'
PORT=3000
NODE_ENV=development
EOF

# 启动
node src/index.js
```

#### Python FastAPI
```bash
# 创建项目目录
mkdir my-api && cd my-api

# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install fastapi uvicorn python-dotenv

# 创建基础结构
mkdir -p app/routers app/models

# 创建入口文件
cat > app/main.py << 'EOF'
from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
EOF

# 创建 .env 文件
cat > .env << 'EOF'
PORT=8000
ENV=development
EOF

# 启动
python app/main.py
```

#### Next.js Web App
```bash
# 使用 create-next-app
npx create-next-app@latest my-app --typescript --tailwind --app

# 进入项目
cd my-app

# 启动开发服务器
npm run dev
```

### 2. 使用模板（推荐）

#### 创建通用模板目录
```bash
# 在 workspace 创建模板
mkdir -p ~/.openclaw/workspace/templates

# Express API 模板
mkdir -p ~/.openclaw/workspace/templates/express-api
# ... 复制上面的 Express 代码

# FastAPI 模板
mkdir -p ~/.openclaw/workspace/templates/fastapi-api
# ... 复制上面的 FastAPI 代码
```

#### 从模板创建
```bash
# 复制模板
cp -r ~/.openclaw/workspace/templates/express-api my-new-api
cd my-new-api

# 初始化 Git
git init
git add .
git commit -m "Initial commit"

# 安装依赖
npm install

# 启动
npm start
```

## 常用配置

### 1. package.json 脚本
```json
{
  "scripts": {
    "start": "node src/index.js",
    "dev": "nodemon src/index.js",
    "test": "jest",
    "lint": "eslint src/"
  }
}
```

### 2. Git 初始化
```bash
# 初始化 Git
git init

# 创建 .gitignore
cat > .gitignore << 'EOF'
node_modules/
.env
.DS_Store
*.log
venv/
__pycache__/
EOF

# 首次提交
git add .
git commit -m "Initial commit"
```

### 3. README 模板
```markdown
# Project Name

## 安装
\`\`\`bash
npm install
\`\`\`

## 配置
复制 `.env.example` 到 `.env` 并填写配置

## 运行
\`\`\`bash
npm start
\`\`\`

## 测试
\`\`\`bash
npm test
\`\`\`
```

## 针对用户需求的模板

### YouTube Automation 工具
```bash
# 创建项目
mkdir youtube-automation && cd youtube-automation

# Python 环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install google-api-python-client pandas python-dotenv

# 创建结构
mkdir -p src/analytics src/upload src/utils

# 创建主文件
cat > src/main.py << 'EOF'
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    print("YouTube Automation Tool")
    # TODO: 实现功能

if __name__ == "__main__":
    main()
EOF
```

### 网赚工具
```bash
# 创建项目
mkdir income-tracker && cd income-tracker

# Node.js 环境
npm init -y

# 安装依赖
npm install express sqlite3 dotenv

# 创建结构
mkdir -p src/routes src/db src/utils

# 创建数据库
cat > src/db/init.js << 'EOF'
const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('./income.db');

db.serialize(() => {
  db.run(`
    CREATE TABLE IF NOT EXISTS income (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      source TEXT,
      amount REAL,
      date TEXT,
      notes TEXT
    )
  `);
});

module.exports = db;
EOF
```

## 项目结构最佳实践

### Node.js API
```
my-api/
├── src/
│   ├── index.js          # 入口
│   ├── routes/           # 路由
│   ├── controllers/      # 控制器
│   ├── models/           # 数据模型
│   └── utils/            # 工具函数
├── tests/                # 测试
├── .env                  # 环境变量
├── .gitignore
├── package.json
└── README.md
```

### Python API
```
my-api/
├── app/
│   ├── main.py           # 入口
│   ├── routers/          # 路由
│   ├── models/           # 数据模型
│   └── utils/            # 工具函数
├── tests/                # 测试
├── .env                  # 环境变量
├── requirements.txt
├── .gitignore
└── README.md
```

## 开发工具集成

### 1. ESLint (Node.js)
```bash
npm install --save-dev eslint
npx eslint --init
```

### 2. Prettier
```bash
npm install --save-dev prettier
```

### 3. Nodemon (自动重启)
```bash
npm install --save-dev nodemon
# 在 package.json 中添加: "dev": "nodemon src/index.js"
```

### 4. Jest (测试)
```bash
npm install --save-dev jest
# 在 package.json 中添加: "test": "jest"
```

## 与 app-builder 的区别

### app-builder（不安全）
- ❌ 依赖外部服务
- ❌ 不透明的构建过程
- ❌ 可能包含恶意代码

### app-scaffold-local（安全）
- ✅ 完全本地运行
- ✅ 使用标准工具（npm, pip, git）
- ✅ 代码清晰可审查
- ✅ 用户完全控制

## 快速启动清单

创建新项目时：
- [ ] 创建项目目录
- [ ] 初始化 Git
- [ ] 创建 .gitignore
- [ ] 设置环境变量（.env）
- [ ] 安装依赖
- [ ] 创建基础结构
- [ ] 编写 README
- [ ] 首次提交

## 示例：完整的 Express API

```bash
# 一键创建 Express API
mkdir my-api && cd my-api
npm init -y
npm install express cors dotenv
npm install --save-dev nodemon

mkdir -p src/routes src/controllers

# 创建文件（参考上面的代码）
# ...

# 配置 package.json
npm pkg set scripts.start="node src/index.js"
npm pkg set scripts.dev="nodemon src/index.js"

# 启动
npm run dev
```

---

**安全承诺**:
- ✅ 不依赖外部服务
- ✅ 使用标准开发工具
- ✅ 完全透明的构建过程
- ✅ 用户完全控制所有步骤

**适用场景**: 快速原型、API 开发、Web 应用、CLI 工具、数据分析项目
