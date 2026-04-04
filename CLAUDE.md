# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库概述

AI Agent 学习仓库，包含两个主要部分：

- **`CLAUDE_study/`** — Claude Code 工具学习练习（7 天计划，已完成），包含 Flask 应用、排序工具、日志解析、批量重命名等 Python 练习
- **`Code/`** — AI Agent 设计模式的代码实现，按日期组织，每个目录对应 `Note.md` 中的一个章节
- **`Note.md`** — 中英双语学习笔记，涵盖 Prompt Chaining、Routing、Parallelization、Reflection、Tool Use、Multi-Agent 等模式

## 技术栈

- Python 3.13
- 框架：LangChain (LCEL)、Google ADK、CrewAI、Flask
- LLM 后端：Google Gemini（`gemini-2.0-flash`、`gemini-2.5-flash`）、OpenRouter
- API Key 环境变量：`GOOGLE_API_KEY`、`OPENROUTER_API_KEY`、`OPENAI_API_KEY`

## 常用命令

```bash
# 激活 Code/ 目录的虚拟环境
source /Users/ceno_0/study/AI_Agent/Code/.venv/bin/activate

# 运行 Code/ 下的 Agent 示例
python /Users/ceno_0/study/AI_Agent/Code/2026.3.26/LangchainProcessesText.py

# 运行 CLAUDE_study/ 的测试
python -m pytest /Users/ceno_0/study/AI_Agent/CLAUDE_study/test_sort.py
python -m pytest /Users/ceno_0/study/AI_Agent/CLAUDE_study/test_log_utils.py

# 运行 Flask 笔记应用
python /Users/ceno_0/study/AI_Agent/CLAUDE_study/app.py

# 批量重命名工具
python /Users/ceno_0/study/AI_Agent/CLAUDE_study/batch_rename.py --help
```

## 项目结构要点

### Code/ — Agent 模式示例（按日期）

| 日期目录 | 模式 | 关键框架 |
|---|---|---|
| `2026.3.26/` | Prompt Chaining | LangChain LCEL |
| `2026.3.27/` | Routing | LangChain RunnableBranch、Google ADK |
| `2026.3.28/` | Parallelization、Reflection | LangChain RunnableParallel、ADK ParallelAgent |
| `2026.3.31/` | Tool Use | LangChain create_agent + 自定义工具 |
| `2026.4.1/` | Tool Use | CrewAI |
| `2026.4.2/` | Multi-Agent、Memory | CrewAI Crew、LangChain ConversationMemory |

### CLAUDE_study/ — 练习文件

测试文件以 `test_` 前缀命名，使用 pytest 运行。`CLAUDE_study/` 有独立的 `CLAUDE.md` 提供子目录级别的指导。

## 注意事项

- 没有 `requirements.txt` 或 `pyproject.toml`，依赖通过 `Code/.venv` 管理但未声明
- `Code/` 下的示例需要对应的 API Key 环境变量才能运行
- `.env` 文件已在 `.gitignore` 中排除
