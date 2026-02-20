# Business Automation Local

Turn your AI agent into a business automation architect with full data privacy. Design, document, implement, and monitor automated workflows across sales, ops, finance, HR, and support — all running locally.

## Use When

- You need business automation without sending data to external services
- You want to automate sales, operations, finance, HR, or support workflows
- You need a private alternative to n8n, Zapier, or cloud-based automation
- You want full control over your data and AI models

## Features

- **Local-First Architecture**: All data stays on your machine
- **Multiple Business Domains**: Sales, Operations, Finance, HR, Support
- **Flexible LLM Options**: Use Ollama, LM Studio, or OpenAI API
- **Workflow Engine**: Design and execute automated workflows
- **API-First Design**: Easy integration with existing systems

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the CLI
python -m src.cli --help

# Start the API server
python -m src.api
```

## Architecture

```
Business Automation Local
├── src/
│   ├── cli.py          # Command-line interface
│   ├── api.py          # REST API server
│   ├── engine.py       # Workflow execution engine
│   ├── modules/        # Business domain modules
│   └── llm.py          # LLM adapter
├── config/             # Configuration files
└── data/               # Local data storage
```

## Configuration

Edit `config/settings.yaml` to configure:

- Database connection
- LLM provider and model
- API keys
- Workflow settings

## Modules

### Sales
- Lead management
- Quote generation
- Pipeline tracking

### Operations
- Task scheduling
- Inventory management
- Process automation

### Finance
- Invoice generation
- Expense tracking
- Financial reporting

### HR
- Employee records
- Leave management
- Performance tracking

### Support
- Ticket management
- FAQ automation
- Customer feedback

## Security

- All data stored locally (SQLite/PostgreSQL)
- Optional AES-256 encryption
- Role-based access control
- Audit logging

## Requirements

- Python 3.11+
- SQLite (default) or PostgreSQL
- Ollama (optional, for local LLM)

## License

MIT

---

* v0.1.0 - 2026-02-20 - Initial concept
