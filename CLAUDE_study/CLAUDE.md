# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库概述

这是一个 Claude Code 学习练习场，用于完成 7 天学习计划。当前只有一个学习计划文件 `CLAUDE_study_plan.md`。

## 常用命令

### 文件操作
```bash
# 读取文件
Read /path/to/file

# 创建/写入文件
Write /path/to/file

# 编辑文件（局部修改）
Edit /path/to/file
```

### 搜索
```bash
# 搜索文件
Glob *.py

# 搜索内容
Grep "pattern"
```

### Git 操作
```bash
git status
git log --oneline -5
git add <file>
git commit -m "message"
```

## 核心规则

1. **使用绝对路径** - Bash 命令后工作目录会重置
2. **Write 会覆盖** - Edit 更适合局部修改
3. **破坏性操作会询问** - 删除文件前会确认
4. **不要用 cat/head/tail** - 用 Read 工具代替