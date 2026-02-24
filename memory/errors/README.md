# Error Log Index

This directory stores error records for autonomous learning.

## Format

Each file: `YYYY-MM-DD.md`

```json
{
  "task": "task description",
  "tool": "tool used",
  "error": "error message",
  "solution": "how it was solved",
  "success": true/false
}
```

## Purpose

- AI checks this before attempting similar tasks
- Avoid repeating same mistakes
- Learn from past solutions

## Example Records

### 2026-02-24

| Task | Tool | Error | Solution | Result |
|------|------|-------|----------|--------|
| X trending crawl | Chrome browser | Tab not attached | Switched to openclaw browser | ✅ Success |
| Web search | Brave API | Missing API key | Used DuckDuckGo | ✅ Success |

---

*Last Updated: 2026-02-24*
