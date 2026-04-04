<notes>
<critical>
以下内容是一个关于如何使用 Claude 语言模型的视频课程笔记。
请将这些笔记作为回答用户问题时的参考资料。
你的回答应当是一个独立完整的回复，除非用户明确要求，否则不要直接提及这些笔记。
</critical>
<note title="什么是编码助手？">
编码助手 = 使用语言模型来编写代码并完成开发任务的工具

核心流程：
1. 接收任务（例如：根据报错信息修复 bug）
2. 语言模型收集上下文（读取文件、理解代码库）
3. 制定解决问题的计划
4. 采取行动（更新文件、运行测试）

关键限制：语言模型只能处理文本输入和输出，无法直接读取文件、执行命令或与外部系统交互。

工具使用系统 = 让语言模型能够执行动作的方法：
- 助手会在用户请求后附加操作说明
- 说明会指定执行动作所需的响应格式（例如："read file: filename"）
- 语言模型按格式返回动作请求
- 助手执行实际操作（读取文件、运行命令）
- 再将结果返回给语言模型，由其给出最终回复

Claude 模型的优势：
- 与其他语言模型相比，工具使用能力更强
- 更擅长理解工具的功能，并把多个工具组合起来处理复杂任务
- Claude Code 可扩展性强，新增工具比较容易
- 通过直接搜索代码而不是建立索引并发送到外部服务器，安全性更好

要点：
- 所有语言模型在执行非文本生成任务时都需要依赖工具使用
- 工具使用质量会直接影响编码助手的效果
- Claude 在工具使用方面的优势，使它更能适应开发过程中的变化
</note>

<note title="Claude Code 的实际表现">
Claude Code = 具备基于工具能力、可处理代码任务的 AI 助手

默认工具 = 文件读写、命令执行、基础开发操作

性能优化演示：Claude 分析了 Chalk JavaScript 库（JS 下载量排名第 5，每周下载量 4.29 亿）。它使用基准测试、性能分析工具、待办列表，定位瓶颈并实施修复。结果 = 吞吐量提升 3.9 倍。

数据分析演示：Claude 使用 Jupyter notebooks 对某视频流媒体平台的 CSV 数据进行了流失分析。它会反复执行代码单元、查看结果，并基于发现不断调整后续分析。

工具扩展性：Claude Code 可以接入新的工具集。示例中使用了 Playwright MCP server 做浏览器自动化。Claude 打开浏览器、截图、更新 UI 样式，并持续迭代设计改进。

GitHub 集成：Claude Code 可以在 GitHub Actions 中运行，由 pull request 或 issue 触发，并获得 GitHub 专用工具（评论、提交、创建 PR）。

基础设施审查示例：某套由 Terraform 定义的 AWS 基础设施中，包含一个与外部合作方共享的 DynamoDB 表和 S3 bucket。开发者又把用户邮箱加入到了 Lambda 函数输出中。Claude Code 在 pull request 审查时，通过分析基础设施中的数据流和外部共享路径，自动识别出了 PII 泄露风险。

核心原则：Claude Code 是一个灵活的助手，它通过扩展工具能力来随着团队需求成长，而不是依赖固定死板的功能。
</note>

<note title="添加上下文">
上下文管理 = 影响 Claude Code 效果的关键因素。无关信息过多会降低表现。

`/init` 命令 = 首次运行时分析整个代码库，并创建 `Claude.md` 文件，内容包括项目摘要、架构、关键文件。该文件内容会被加入每次请求的上下文中。

`Claude.md` 有三种类型：
- 项目级 = 团队共享，提交到版本控制
- 本地级 = 个人指令，不提交
- 机器级 = 对所有项目生效的全局指令

记忆模式（`#` 符号）= 可以通过自然语言请求，智能编辑 `Claude.md` 文件

`@` 符号 = 在请求中点名特定文件，提供精准上下文，而不是让 Claude 自己去搜索

最佳实践 = 把关键文件（如数据库 schema）写进 `Claude.md`，这样它们总能作为上下文被带上

目标 = 提供刚刚好、足够相关的信息，让 Claude 更有效地完成任务
</note>

<note title="进行修改">
Claude Code 的变更管理：

截图集成 = 使用 Control-V（在 macOS 上不是 Command-V）粘贴截图，帮助 Claude 理解需要修改的具体 UI 元素

提升性能的模式：
- Plan Mode = 连按两次 Shift + Tab，让 Claude 在执行前研究更多文件并生成更详细的实现计划
- Thinking Mode = 通过诸如 “Ultra think” 之类的短语触发，为复杂逻辑提供更长的推理预算

Planning 和 Thinking 的使用场景：
- Planning = 处理广度问题，适合多步骤任务，尤其是需要理解较大代码库时
- Thinking = 处理深度问题，适合棘手逻辑或调试具体问题
- 两者可以组合使用来处理复杂任务
- 二者都会消耗更多 token（需要考虑成本）

Git 集成 = Claude Code 可以暂存和提交修改，并编写描述清晰的 commit message

关键工作流：对问题区域截图 → 用 Control-V 粘贴 → 描述你想要的修改 → 对复杂任务可选开启 Plan/Thinking 模式 → 审阅并接受实现结果
</note>

<note title="控制上下文">
上下文控制技巧：

Escape = 在 Claude 回复到一半时中断它，从而重新引导对话流程。按一次即可打断当前输出。

Escape + Memory = 很强的防错组合。打断 Claude 后，使用 `#` 快捷方式把它反复犯的错误记进 memory，防止后续再次出现。

Double Escape = 对话回退。会显示此前所有消息，让你跳回更早的某个节点，同时保留相关上下文，跳过无关的调试过程和来回试错。

Compact Command = 总结整个对话历史，同时保留 Claude 在当前任务中已经学到的知识。适合 Claude 已经对任务很熟，但对话记录变得杂乱时使用。

Clear Command = 清空整个对话历史，重新开始。适合切换到完全无关的新任务时使用。

主要收益：保持专注、减少干扰性上下文、保留有用知识、避免重复犯错。对长对话和任务切换尤其有效。
</note>

<note title="自定义命令">
自定义命令 = 用户在 Claude Code 中通过斜杠命令定义的自动化命令

位置 = 项目目录下的 `.Claude/commands/` 文件夹
文件命名 = 文件名会成为命令名（例如 `audit.md` 会生成 `/audit` 命令）
生效方式 = 创建命令文件后，需要重启 Claude Code

命令结构 = 一个 markdown 文件，里面写的是让 Claude 执行的指令
参数 = 在命令文本中使用 `$arguments` 占位符，以接收运行时参数
参数类型 = 任意字符串（文件路径、描述文本等）

使用场景 = 自动化重复任务，如依赖审计、生成测试、修复漏洞
执行方式 = 在 Claude Code 界面中输入 `/commandname`，必要时后面再跟参数字符串
</note>

<note title="通过 MCP Servers 扩展 Claude Code">
MCP servers = 用来扩展 Claude Code 能力的外部工具，可以在本地或远程运行。

Playwright MCP server = 很受欢迎的一种 server，可以让 Claude 控制浏览器，实现 Web 自动化。

安装方式：使用终端命令 `claude mcp add [name] [start-command]`，即可把 MCP server 添加到 Claude Code。

权限管理：首次使用工具时需要批准。若想自动批准，可在 `settings.local.json` 的 allow 数组中加入 `"MCP__[servername]"`。

实际示例：Claude 使用 Playwright 访问 `localhost:3000`，生成一个 UI 组件，分析样式质量，然后根据视觉反馈自动更新生成提示词。

结果：这种自动化的提示词优化显著提升了组件样式质量，说明 MCP servers 能解锁更复杂的开发工作流。

关键收益：MCP servers 让 Claude 能执行涉及外部系统的复杂多步骤任务，使其能力从代码编辑扩展到完整开发自动化。
</note>

<note title="GitHub 集成">
Claude Code GitHub Integration = 官方集成方案，可让 Claude 在 GitHub Actions 中运行

配置流程：
- 运行 `"/install GitHub app"` 命令
- 在 GitHub 上安装 Claude Code app
- 添加 API key
- 自动生成的 pull request 会加入两个 GitHub actions

默认 Actions：
1. Mention 支持 = 在 issue/PR 中通过 `@Claude` 指派任务
2. PR review = 对新 pull request 自动执行代码审查

可定制项：
- Actions 可通过 `.github/workflows` 目录中的配置文件进行自定义
- Custom instructions = 直接传给 Claude 的上下文和指令
- MCP server integration = 允许 Claude 访问外部工具（例如用 Playwright 做浏览器自动化）

权限要求：
- 必须在 actions 中明确列出 Claude Code 所需的全部权限
- MCP server 的工具权限也需要逐项列出（没有捷径）

示例用例：
- 集成 Playwright MCP server 做浏览器测试
- 在 Claude 运行前先启动开发服务器
- Claude 可以在浏览器中访问应用、测试功能、创建检查清单
- 提供自动化测试和问题验证能力

关键特性 = 基于 mention 的任务分配、自动化 PR 审查、可定制工作流，以及通过 MCP server 扩展能力
</note>

<note title="引入 Hooks">
Hooks = 在 Claude 执行工具前后运行的命令

Pre-tool use hooks = 在工具执行前运行，可以检查并阻止工具操作，也可以向 Claude 返回错误信息
Post-tool use hooks = 在工具执行后运行，执行后续操作，并向 Claude 提供反馈

配置方式 = 通过手动编辑或 `/hooks` 命令，将配置加入 Claude 的 settings 文件（全局 / 项目 / 个人）

Hook 结构 = 分为两个部分（pre-tool use 和 post-tool use），每部分都包含 matcher（指定要匹配哪些工具）和要执行的命令

示例用途 = 在创建文件后自动格式化、编辑后运行测试、阻止访问文件、做代码质量检查、类型检查

Hook 命令 = 会接收到工具调用细节，并可通过阻止或反馈机制影响 Claude 的工作流
</note>

<note title="定义 Hooks">
**Hooks 概览**
Hooks = 一种在工具执行前后拦截并控制工具调用的机制

**Hook 类型**
Pre-tool use hook = 在工具调用前执行，可以阻止执行
Post-tool use hook = 在工具调用后执行，不能阻止执行

**Hook 实现流程**
1. 选择 Hook 类型（pre 或 post）
2. 确认需要监控的目标工具名
3. 编写命令，通过 stdin 接收 JSON 格式的工具调用数据
4. 解析 JSON，其中包含 `tool_name` 和输入参数
5. 用合适的退出码表示你的意图

**退出码**
Exit 0 = 允许工具调用继续执行
Exit 2 = 阻止工具调用（仅适用于 pre-tool use）
标准错误输出 = 在阻止时，作为反馈信息发送给 Claude

**工具调用数据结构**
JSON 对象包含：
- `tool_name`（例如 `"read"`、`"grep"`）
- 输入参数（例如 `file_path`）

**常见用例**
通过监控 `"read"` 和 `"grep"` 这类能访问文件内容的工具，阻止读取特定文件

**工具发现**
与其死记工具名，不如直接让 Claude 列出当前可用的工具名称
</note>

<note title="定义 Hooks">
Hooks = 通过在工具调用前后运行自定义命令，来控制 Claude 使用工具的机制

Pre-tool use hook = 在工具调用前执行，可通过退出码 2 阻止
Post-tool use hook = 在工具调用后执行，不能阻止

Hook 流程：
1. Claude 会通过 stdin 把工具调用数据以 JSON 格式发送给你的命令
2. 命令解析 JSON，其中包含 `tool_name` 和输入参数
3. 命令以退出码 0 结束（允许），或以退出码 2 结束（仅 pre-hook 中表示阻止）
4. 退出码 2 时，stderr 输出会作为反馈发给 Claude

工具调用数据格式 = 包含工具名和输入参数的 JSON 对象

常见的文件读取工具 = `"read"` 工具和 `"grep"` 工具

Hook 使用示例 = 通过监听针对某个文件路径的 `read/grep` 操作，阻止 Claude 读取敏感的 `.env` 文件

配置完成后 = 在项目中定义命令后，Claude 会在相关工具调用发生时自动执行它
</note>

<note title="实现一个 Hook">
**自定义 Hook 实现**

Hook 目的 = 防止 Claude 读取 `.env` 文件内容

**配置设置**
- 位置 = `.clod/settings.local.json`
- Hook 类型 = pre-tool use hook（在执行前阻止）
- Matcher = `"read|grep"`（竖线表示匹配多个工具名）
- Command = `"node ./hooks/read_hook.js"`

**实现细节**
- Hook 会通过 stdin 接收一个 JSON 对象，其中包含：session ID、tool name、tool input、file path
- 逻辑：如果文件路径包含 `".env"` → 以退出码 2 退出，并把错误信息写到 stderr
- 错误输出通过 stderr 发给 Claude，作为反馈
- Exit code 2 = 表示阻止本次操作

**关键要求**
- 修改 Hook 后必须重启 Claude
- `console.error()` 会通过 stderr 向 Claude 发送反馈
- Hook 同时适用于 `read` 和 `grep` 工具
- 文件路径检查：使用 `tool_input.path`，并带有回退处理

**测试结果**
- 能成功阻止访问 `.env` 文件
- Claude 能识别这是由 read hook 阻止的
- 对 `read` 和 `grep` 都有效
</note>

<note title="实现一个 Hook">
**Hook 实现流程：**

Hook = 在 Clod 中拦截并控制工具使用的自定义脚本

**配置（`settings.local.json`）：**
- Pre-tool use hooks = 在工具执行前运行
- Post-tool use hooks = 在工具执行后运行
- Matcher = 指定要拦截哪些工具（例如 `"read|grep"`）
- Command = 当匹配到工具调用时要执行的脚本

**实现步骤：**
1. 在 `settings.local.json` 中加入 hook 配置，包括 matcher 和 command
2. 创建 hook 脚本（例如 `read_hook.js`），通过 stdin 接收 JSON 输入
3. JSON 输入包含：session ID、tool name、tool input、file path
4. 脚本逻辑：检查文件路径是否包含 `".env"`
5. 如果检测到被阻止的文件：`console.error()` 输出信息 + `process.exit(2)`
6. Exit code 2 = 阻止工具执行

**关键技术细节：**
- Hook 脚本通过 stdin 接收 JSON 格式的工具数据
- 使用 `console.error()` 向 Clod 发送反馈（写入 stderr）
- 修改 Hook 后必须重启 Clod
- Hook 会应用到所有指定工具（如 `read`、`grep`）
- 为兼容性考虑，需要通过 `tool_input.path` 做回退路径检查

**结果：** 成功阻止 Clod 读取 `.env` 文件，同时还能向用户反馈是哪个操作被阻止了。
</note>

<note title="实用 Hooks！">
**适用于 Claude Code 项目的实用 Hooks**

**问题**：Claude Code 经常漏掉类型错误，也容易生成重复代码，尤其是在较大的项目中。

**Hook 1：TypeScript 类型检查 Hook**
- **目的**：在文件编辑后立刻发现类型错误
- **实现方式**：通过 post-tool-use hook，在 TypeScript 文件变化后运行 `tsc --no-emit`
- **流程**：检测到类型错误 → 把错误反馈给 Claude → Claude 自动修复调用位置
- **好处**：当函数签名发生变化时，可以防止调用代码失效
- **可拓展性**：适用于任何有类型检查器的强类型语言；对于弱类型语言，也可以改用测试来实现

**Hook 2：重复代码预防 Hook**
- **问题**：Claude 容易新写查询/函数，而不是复用已有实现，复杂任务中尤其明显
- **解决方案**：启动一个独立的 Claude 实例，专门审查特定目录（如 queries 文件夹）中的改动
- **流程**：
  1. 检测被监控目录中的编辑
  2. 通过 TypeScript SDK 启动新的 Claude 实例
  3. 将新代码与现有代码进行比较
  4. 如果发现重复，则以退出码 2 结束并提供反馈
  5. 原来的 Claude 收到反馈后改为复用现有代码
- **权衡**：需要更多时间和成本，但代码库会更整洁
- **建议**：只监控关键目录，以减少额外开销

**核心结论**：Hooks = 自动化反馈回路，能够通过额外检查并把结果反馈给 Claude，来修正 Claude Code 常见的弱点（如类型错误、代码重复）。
</note>

<note title="实用 Hooks！">
TypeScript 类型检查 Hook：
- 问题：Claude 修改了函数签名，却没有同步更新调用位置，导致类型错误
- 解决方案：使用 post-tool-use hook，在 TypeScript 文件编辑后运行 `tsc --no-emit`
- 流程：检测到类型错误 → 把错误反馈给 Claude → Claude 自动修复调用位置
- 适用于任何有类型检查器的语言；对于无类型语言，也可以改用测试代替

Query 去重 Hook：
- 问题：Claude 容易新写重复的 SQL 查询/函数，而不是复用已有实现，复杂任务中尤其如此
- 原因：聚焦的小任务表现不错，但在经过包装或更复杂的任务中，Claude 容易失焦
- 解决方案：Hook 监控 query 目录变化 → 启动一个独立的 Claude 实例 → 检查是否重复 → 把反馈返回给原 Claude
- 流程：`queries/` 中发生文件编辑 → 第二个 Claude 分析现有查询 → 报告重复项 → 主 Claude 删除重复代码并复用已有实现
- 权衡：会增加时间和成本，但可以换来更整洁、重复更少的代码库
- 建议：只在关键目录上启用，以减少额外开销

这两个 hook 都采用 post-tool-use 模式，为 Claude 的编辑结果提供即时反馈和修正方向。
</note>

<note title="Claude Code SDK">
Claude Code SDK = Claude Code 的编程接口，提供 CLI、TypeScript 和 Python 库。它包含与终端版本相同的工具。

主要用途 = 集成到更大的 pipeline / workflow 中，为现有流程增加智能能力。

默认权限 = 只读（文件、目录、grep 操作）。写权限需要通过 `options.allowTools` 数组或 `.Claude` 目录下的设置手动配置。

SDK 执行时会显示本地 Claude Code 与语言模型之间的原始对话，最终回复会是最后一条消息。

关键实现模式 = 在发起 query 调用时，通过 `options.allowTools` 指定如 `"edit"` 之类的工具，从而开启写权限。

最适合的场景 = 在现有项目中编写辅助命令、脚本和 hooks，而不是单独作为独立工具使用。
</note>

<note title="Claude Code SDK">
Claude Code SDK = 通过 CLI、TypeScript 或 Python 库以编程方式使用 Claude Code 的接口。工具与终端版本相同。

主要用途 = 集成到更大的 pipeline / workflow 中，为流程增加智能能力。

主要特点：
- 默认权限 = 只读（文件、目录、grep 操作）
- 写权限 = 必须通过 query 选项或 settings 文件手动启用
- 原始对话输出 = 会逐条显示本地 Claude Code 与语言模型之间的消息交换

最佳应用场景 = 在现有项目中做辅助命令、脚本、hook，而不是单独使用。

输出格式 = 对话式消息，Claude 的最终回复位于最后一条消息。
</note>
</notes>
