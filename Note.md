```
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
```

# Chapter 1: Prompt Chaining

## At a Glance

**What:** Complex tasks often overwhelm LLMs when handled within a single prompt, leading to significant performance issues. The cognitive load on the model increases the likelihood of errors such as overlooking instructions, losing context, and generating incorrect information. A monolithic prompt struggles to manage multiple constraints and sequential reasoning steps effectively. This results in unreliable and inaccurate outputs, as the LLM fails to address all facets of the multifaceted request.

**是什么：** 复杂任务在单个提示词内处理时通常会使 LLM 不堪重负，导致严重的性能问题。模型的认知负荷增加了错误的可能性，如忽略指令、失去上下文和生成错误信息。单体提示词难以有效管理多个约束和顺序推理步骤。这导致不可靠和不准确的输出，因为 LLM 未能解决多方面请求的所有方面。

**Why:** Prompt chaining provides a standardized solution by breaking down a complex problem into a sequence of smaller, interconnected sub-tasks. Each step in the chain uses a focused prompt to perform a specific operation, significantly improving reliability and control. The output from one prompt is passed as the input to the next, creating a logical workflow that progressively builds towards the final solution. This modular, divide-and-conquer strategy makes the process more manageable, easier to debug, and allows for the integration of external tools or structured data formats between steps. This pattern is foundational for developing sophisticated, multi-step Agentic systems that can plan, reason, and execute complex workflows.

**为什么：** 提示词链通过将复杂问题分解为一系列较小的、相互关联的子任务来提供标准化解决方案。链中的每一步使用聚焦的提示词执行特定操作，显著提高可靠性和控制力。一个提示词的输出作为下一个提示词的输入传递，创建逐步构建最终解决方案的逻辑工作流。这种模块化的分而治之策略使过程更易于管理、更易于调试，并允许在步骤之间集成外部工具或结构化数据格式。这种模式是开发能够规划、推理和执行复杂工作流的复杂多步智能体系统的基础。

**Rule of thumb:** Use this pattern when a task is too complex for a single prompt, involves multiple distinct processing stages, requires interaction with external tools between steps, or when building Agentic systems that need to perform multi-step reasoning and maintain state.

**经验法则：** 当任务对于单个提示词过于复杂、涉及多个不同的处理阶段、需要在步骤之间与外部工具交互，或者在构建需要执行多步推理并维护状态的智能体系统时，使用此模式。

Visual Summary

![截屏2026-03-26 16.06.26](assets/截屏2026-03-26 16.06.26.png)

Fig. 1-1: Prompt Chaining Pattern: Agents receive a series of prompts from the user, with the output of each agent serving as the input for the next in the chain.

## Key Takesaways

- Prompt Chaining breaks down complex tasks into a sequence of smaller, focused steps. This is occasionally known as the Pipeline pattern.
- Each step in a chain involves an LLM call or processing logic, using the output of the previous step as input.
- This pattern improves the reliability and manageability of complex interactions with language models.
- Frameworks like LangChain/LangGraph, and Google ADK provide robust tools to define, manage, and execute these multi-step sequences.
- 提示词链将复杂任务分解为一系列较小的、聚焦的步骤。这有时也被称为管道模式。
- 链中的每一步都涉及LLM调用或处理逻辑，使用前一步的输出作为输入。
- 这种模式提高了与语言模型进行复杂交互的可靠性和可管理性。
- LangChain/LangGraph和Google ADK等框架提供了定义、管理和执行这些多步序列的健壮工具。

## Conclusion

By deconstructing complex problems into a sequence of simpler, more manageable sub-tasks, prompt chaining provides a robust framework for guiding large language models. This “divide-and-conquer” strategy significantly enhances the reliability and control of the output by focusing the model on one specific operation at a time. As a foundational pattern, it enables the development of sophisticated AI agents capable of multi-step reasoning, tool integration, and state management. Ultimately, mastering prompt chaining is crucial for building robust, context-aware systems that can execute intricate workflows well beyond the capabilities of a single prompt.

通过将复杂问题分解为一系列更简单、更易于管理的子任务，提示词链为指导大型语言模型提供了一个健壮的框架。这种”分而治之”策略通过一次专注于一个特定操作，显著提高了输出的可靠性和控制力。作为基础模式，它支持开发能够进行多步推理、工具集成和状态管理的复杂 AI 智能体系统。最终，掌握提示词链对于构建能够执行远超单个提示词能力的复杂工作流的健壮、上下文感知系统至关重要。

# Chapter 2: Routing

## At a Glance

**What**: Agentic systems must often respond to a wide variety of inputs and situations that cannot be handled by a single, linear process. A simple sequential workflow lacks the ability to make decisions based on context. Without a mechanism to choose the correct tool or sub-process for a specific task, the system remains rigid and non-adaptive. This limitation makes it difficult to build sophisticated applications that can manage the complexity and variability of real-world user requests.

**是什么：** 智能体系统必须经常响应各种各样的输入和情况，这些无法由单一的线性流程处理。简单的顺序工作流缺乏基于上下文做出决策的能力。没有为特定任务选择正确工具或子流程的机制，系统仍然是僵化和非自适应的。这种限制使得难以构建能够管理现实世界用户请求的复杂性和可变性的复杂应用程序。

**Why:** The Routing pattern provides a standardized solution by introducing conditional logic into an agent’s operational framework. It enables the system to first analyze an incoming query to determine its intent or nature. Based on this analysis, the agent dynamically directs the flow of control to the most appropriate specialized tool, function, or sub-agent. This decision can be driven by various methods, including prompting LLMs, applying predefined rules, or using embedding-based semantic similarity. Ultimately, routing transforms a static, predetermined execution path into a flexible and context-aware workflow capable of selecting the best possible action.

**为什么：** 路由模式通过将条件逻辑引入智能体的操作框架提供了标准化解决方案。它使系统能够首先分析传入查询以确定其意图或性质。基于此分析，智能体动态地将控制流定向到最合适的专门工具、函数或子智能体。这个决策可以由各种方法驱动，包括提示 LLM、应用预定义规则或使用基于嵌入的语义相似性。最终，路由将静态的预定执行路径转变为能够选择最佳可能操作的灵活和上下文感知工作流。

**Rule of Thumb:** Use the Routing pattern when an agent must decide between multiple distinct workflows, tools, or sub-agents based on the user’s input or the current state. It is essential for applications that need to triage or classify incoming requests to handle different types of tasks, such as a customer support bot distinguishing between sales inquiries, technical support, and account management questions.

**经验法则：** 当智能体必须根据用户输入或当前状态在多个不同的工作流、工具或子智能体之间做出决策时，使用路由模式。它对于需要对传入请求进行分类以处理不同类型任务的应用程序至关重要，例如客户支持机器人区分销售查询、技术支持和帐户管理问题。

## **Visual Summary**

![截屏2026-03-27 15.23.08](assets/截屏2026-03-27 15.23.08.png)

​                                          Fig.2-1: Router pattern, using an LLM as a Router

## Key Takeaways

- Routing enables agents to make dynamic decisions about the next step in a workflow based on conditions.
- It allows agents to handle diverse inputs and adapt their behavior, moving beyond linear execution.
- Routing logic can be implemented using LLMs, rule-based systems, or embedding similarity.
- Frameworks like LangGraph and Google ADK provide structured ways to define and manage routing within agent workflows, albeit with different architectural approaches.
- 路由使智能体能够根据条件动态决定工作流中的下一步。
- 它允许智能体处理各种输入并调整其行为，超越线性执行。
- 路由逻辑可以使用 LLM、基于规则的系统或嵌入相似性实现。
- 像 LangGraph 和 Google ADK 这样的框架提供了在智能体工作流中定义和管理路由的结构化方式，尽管采用不同的架构方法。

## Conclusion

The Routing pattern is a critical step in building truly dynamic and responsive agentic systems. By implementing routing, we move beyond simple, linear execution flows and empower our agents to make intelligent decisions about how to process information, respond to user input, and utilize available tools or sub-agents.

路由模式是构建真正动态响应式智能体系统的关键步骤。通过实现路由，我们超越了简单的线性执行流，使智能体能够智能地决策如何处理信息、响应用户输入以及利用可用工具或子智能体。

We’ve seen how routing can be applied in various domains, from customer service chatbots to complex data processing pipelines. The ability to analyze input and conditionally direct the workflow is fundamental to creating agents that can handle the inherent variability of real-world tasks.

我们已经看到路由如何应用于各个领域，从客户服务聊天机器人到复杂的数据处理管道。分析输入并有条件地指导工作流的能力是创建能够处理现实世界任务固有可变性的智能体的基础。

The code examples using LangChain and Google ADK demonstrate two different, yet effective, approaches to implementing routing. LangGraph’s graph-based structure provides a visual and explicit way to define states and transitions, making it ideal for complex, multi-step workflows with intricate routing logic. Google ADK, on the other hand, often focuses on defining distinct capabilities (Tools) and relies on the framework’s ability to route user requests to the appropriate tool handler, which can be simpler for agents with a well-defined set of discrete actions.

使用 LangChain 和 Google ADK 的代码示例展示了实现路由的两种不同但有效的方法。LangGraph 基于图的结构提供了定义状态和转换的可视化和显式方式，使其成为具有复杂路由逻辑的复杂多步工作流的理想选择。另一方面，Google ADK 通常专注于定义不同的能力（工具）并依赖框架将用户请求路由到适当的工具处理程序的能力，这对于具有明确定义的离散操作集的智能体来说可能更简单。

Mastering the Routing pattern is essential for building agents that can intelligently navigate different scenarios and provide tailored responses or actions based on context. It’s a key component in creating versatile and robust agentic applications.

掌握路由模式对于构建能够智能地导航不同场景并根据上下文提供定制响应或操作的智能体至关重要。它是创建多功能和健壮智能体应用程序的关键组件。

# Chapter 3: Parallelization

## At a Glance

**What:** Many agentic workflows involve multiple sub-tasks that must be completed to achieve a final goal. A purely sequential execution, where each task waits for the previous one to finish, is often inefficient and slow. This latency becomes a significant bottleneck when tasks depend on external I/O operations, such as calling different APIs or querying multiple databases. Without a mechanism for concurrent execution, the total processing time is the sum of all individual task durations, hindering the system’s overall performance and responsiveness.

**是什么：** 许多智能体工作流包含多个必须完成才能达成最终目标的子任务。纯顺序执行（每个任务等待前一个完成）通常低效且缓慢。当任务依赖外部 I/O 操作（如调用不同 API 或查询多个数据库）时，这种延迟成为主要瓶颈。若无并发执行机制，总处理时间等于所有单个任务持续时间之和，严重制约系统整体性能和响应能力。

**Why:** The Parallelization pattern provides a standardized solution by enabling the simultaneous execution of independent tasks. It works by identifying components of a workflow, like tool usages or LLM calls, that do not rely on each other’s immediate outputs. Agentic frameworks like LangChain and the Google ADK provide built-in constructs to define and manage these concurrent operations. For instance, a main process can invoke several sub-tasks that run in parallel and wait for all of them to complete before proceeding to the next step. By running these independent tasks at the same time rather than one after another, this pattern drastically reduces the total execution time.

**为什么：** 并行化模式通过启用独立任务的同时执行提供标准化解决方案。该模式通过识别工作流中不依赖彼此即时输出的组件（如工具使用或 LLM 调用）来实现。像 LangChain 和 Google ADK 这样的智能体框架提供内置构造来定义和管理这些并发操作。例如，主进程可调用多个并行运行的子任务，等待所有子任务完成后再继续下一步。通过同时而非顺序执行这些独立任务，该模式显著减少总执行时间。

**Rule of thumb:** Use this pattern when a workflow contains multiple independent operations that can run simultaneously, such as fetching data from several APIs, processing different chunks of data, or generating multiple pieces of content for later synthesis.

**经验法则：** 当工作流包含多个可同时运行的独立操作时使用此模式，例如从多个 API 获取数据、处理不同数据块或生成多个内容片段供后续综合。

## Visual Summary

![截屏2026-03-28 14.26.06](assets/截屏2026-03-28 14.26.06.png)

## Key Takeaways 

- Parallelization is a pattern for executing independent tasks concurrently to improve efficiency.
- 并行化是一种通过并发执行独立任务来提高效率的模式
- It is particularly useful when tasks involve waiting for external resources, such as API calls.
- 在涉及等待外部资源（如 API 调用）的任务中特别有效
- The adoption of a concurrent or parallel architecture introduces substantial complexity and cost, impacting key development phases such as design, debugging, and system logging.
- 采用并发或并行架构会引入显著复杂性和成本，影响设计、调试和系统日志等关键开发环节
- Frameworks like LangChain and Google ADK provide built-in support for defining and managing parallel execution.
- 像 LangChain 和 Google ADK 这样的框架提供定义和管理并行执行的内置支持
- In LangChain Expression Language (LCEL), RunnableParallel is a key construct for running multiple runnables side-by-side.
- 在 LangChain 表达式语言（LCEL）中，RunnableParallel 是并行运行多个可运行对象的关键构造
- Google ADK can facilitate parallel execution through LLM-Driven Delegation, where a Coordinator agent’s LLM identifies independent sub-tasks and triggers their concurrent handling by specialized sub-agents.
- Google ADK 可通过 LLM 驱动的委托实现并行执行，协调器智能体的 LLM 识别独立子任务并触发专门子智能体的并发处理
- Parallelization helps reduce overall latency and makes agentic systems more responsive for complex tasks.
- 并行化有助于减少整体延迟，使智能体系统在处理复杂任务时更具响应性

## conclusion 

The parallelization pattern is a method for optimizing computational workflows by concurrently executing independent sub-tasks. This approach reduces overall latency, particularly in complex operations that involve multiple model inferences or calls to external services.

并行化模式是通过并发执行独立子任务来优化计算工作流的方法。该模式有效减少整体延迟，在涉及多个模型推理或对外部服务调用的复杂操作中尤为显著。

Frameworks provide distinct mechanisms for implementing this pattern. In LangChain, constructs like RunnableParallel are used to explicitly define and execute multiple processing chains simultaneously. In contrast, frameworks like the Google Agent Developer Kit (ADK) can achieve parallelization through multi-agent delegation, where a primary coordinator model assigns different sub-tasks to specialized agents that can operate concurrently.

不同框架为此模式提供了不同的实现机制。在 LangChain 中，通过 RunnableParallel 等构造显式定义并同时执行多个处理链。而 Google 智能体开发工具包 (ADK) 等框架则通过多智能体委托实现并行化，由主协调器模型将不同子任务分配给可并发操作的专门智能体。

By integrating parallel processing with sequential (chaining) and conditional (routing) control flows, it becomes possible to construct sophisticated, high-performance computational systems capable of efficiently managing diverse and complex tasks.

通过将并行处理与顺序（链式）和条件（路由）控制流相结合，可以构建能够高效管理各类复杂任务的复杂、高性能计算系统。

# Chapter 4: Reflection

## At a Glance

**What:** An agent’s initial output is often suboptimal, suffering from inaccuracies, incompleteness, or a failure to meet complex requirements. Basic agentic workflows lack a built-in process for the agent to recognize and fix its own errors. This is solved by having the agent evaluate its own work or, more robustly, by introducing a separate logical agent to act as a critic, preventing the initial response from being the final one regardless of quality.

**是什么：** 智能体的初始输出往往次优，存在不准确、不完整或未能满足复杂要求的问题。基础智能体工作流缺乏让智能体识别和修复自身错误的内置流程。这通过让智能体评估自身工作，或更稳健地引入独立逻辑智能体充当评审者来解决，防止无论质量如何初始响应都成为最终结果。

**Why:** The Reflection pattern offers a solution by introducing a mechanism for self-correction and refinement. It establishes a feedback loop where a “producer” agent generates an output, and then a “critic” agent (or the producer itself) evaluates it against predefined criteria. This critique is then used to generate an improved version. This iterative process of generation, evaluation, and refinement progressively enhances the quality of the final result, leading to more accurate, coherent, and reliable outcomes.

**为什么：** 反思模式通过引入自我纠正和优化机制提供了解决方案。它建立反馈循环，其中”生产者”智能体生成输出，然后”评审者”智能体（或生产者自身）根据预定义标准进行评估。随后使用此评审生成改进版本。这种生成、评估和优化的迭代过程逐步提升最终结果的质量，从而产生更准确、连贯和可靠的结果。

**Rule of thumb:** Use the Reflection pattern when the quality, accuracy, and detail of the final output are more important than speed and cost. It is particularly effective for tasks like generating polished long-form content, writing and debugging code, and creating detailed plans. Employ a separate critic agent when tasks require high objectivity or specialized evaluation that a generalist producer agent might miss.

**经验法则：** 当最终输出的质量、准确性和细节比速度和成本更重要时使用反思模式。它对生成精炼的长篇内容、编写和调试代码以及创建详细计划等任务特别有效。当任务需要通用生产者智能体可能遗漏的高客观性或专门评估时，使用独立评审者智能体。

## visual Summary

![截屏2026-03-28 16.52.51](assets/截屏2026-03-28 16.52.51.png)

​                                               Fig. 4-1: Reflection design pattern, self-reflection

![截屏2026-03-28 16.53.35](assets/截屏2026-03-28 16.53.35.png)

​                                     Fig.4-2: Reflection design pattern, producer and critique agent

## Key Takeaways 

- The primary advantage of the Reflection pattern is its ability to iteratively self-correct and refine outputs, leading to significantly higher quality, accuracy, and adherence to complex instructions.
- It involves a feedback loop of execution, evaluation/critique, and refinement. Reflection is essential for tasks requiring high-quality, accurate, or nuanced outputs.
- A powerful implementation is the Producer-Critic model, where a separate agent (or prompted role) evaluates the initial output. This separation of concerns enhances objectivity and allows for more specialized, structured feedback.
- However, these benefits come at the cost of increased latency and computational expense, along with a higher risk of exceeding the model’s context window or being throttled by API services.
- While full iterative reflection often requires stateful workflows (like LangGraph), a single reflection step can be implemented in LangChain using LCEL to pass output for critique and subsequent refinement.
- Google ADK can facilitate reflection through sequential workflows where one agent’s output is critiqued by another agent, allowing for subsequent refinement steps.
- This pattern enables agents to perform self-correction and enhance their performance over time.
- 反思模式的主要优势在于其能够迭代地自我纠正和优化输出，从而显著提高质量、准确性和对复杂指令的遵循度。
- 它涉及执行、评估/评审和优化的反馈循环。反思对需要高质量、准确或精细输出的任务至关重要。
- 一个强大的实现是生产者-评审者模型，其中独立智能体（或提示角色）评估初始输出。这种关注点分离增强了客观性，并支持更专业、结构化的反馈。
- 然而，这些优势是以增加的延迟和计算成本为代价的，同时伴随超出模型上下文窗口或被API服务限制的更高风险。
- 虽然完整的迭代反思通常需要有状态的工作流（如LangGraph），但单个反思步骤可在LangChain中使用LCEL实现，以将输出传递给评审和后续优化。
- Google ADK 可通过顺序工作流促进反思，其中一个智能体的输出被另一个智能体评审，允许后续优化步骤。
- 此模式使智能体执行自我纠正并随时间提升性能。

## Conclusion

The reflection pattern provides a crucial mechanism for self-correction within an agent’s workflow, enabling iterative improvement beyond a single-pass execution. This is achieved by creating a loop where the system generates an output, evaluates it against specific criteria, and then uses that evaluation to produce a refined result. This evaluation can be performed by the agent itself (self-reflection) or, often more effectively, by a distinct critic agent, which represents a key architectural choice within the pattern.

反思模式为智能体工作流中的自我纠正提供了关键机制，实现了超越单次执行的迭代改进。这通过创建一个循环来实现：系统生成输出，根据特定标准评估它，然后使用该评估产生优化结果。这种评估可以由智能体自身执行（自我反思），或者通常更有效地由不同的评审者智能体执行，这代表了模式内的一个关键架构选择。

While a fully autonomous, multi-step reflection process requires a robust architecture for state management, its core principle is effectively demonstrated in a single generate-critique-refine cycle. As a control structure, reflection can be integrated with other foundational patterns to construct more robust and functionally complex agentic systems.

虽然完全自主的多步反思过程需要强大的状态管理架构，但其核心原理在单个生成-评审-优化周期中得到了有效展示。作为一种控制结构，反思可以与其他基础模式集成，以构建更健壮和功能更复杂的智能体系统。

# Chapter 5: Tool Use

## At a Glance

**What:** LLMs are powerful text generators, but they are fundamentally disconnected from the outside world. Their knowledge is static, limited to the data they were trained on, and they lack the ability to perform actions or retrieve real-time information. This inherent limitation prevents them from completing tasks that require interaction with external APIs, databases, or services. Without a bridge to these external systems, their utility for solving real-world problems is severely constrained.

**是什么：** 大型语言模型（LLM）是强大的文本生成器，但它们基本上与外部世界断开连接。它们的知识是静态的，仅限于训练数据，并且缺乏执行操作或检索实时信息的能力。这种固有的限制阻止它们完成需要与外部 API、数据库或服务交互的任务。没有通往这些外部系统的桥梁，它们解决现实世界问题的效用受到严重限制。

**Why:** The Tool Use pattern, often implemented via function calling, provides a standardized solution to this problem. It works by describing available external functions, or “tools,” to the LLM in a way it can understand. Based on a user’s request, the agentic LLM can then decide if a tool is needed and generate a structured data object (like a JSON) specifying which function to call and with what arguments. An orchestration layer executes this function call, retrieves the result, and feeds it back to the LLM. This allows the LLM to incorporate up-to-date, external information or the result of an action into its final response, effectively giving it the ability to act.

**为什么：** 工具使用模式（通常通过工具调用实现）为此问题提供了标准化解决方案。它的工作原理是以 LLM 可以理解的方式向其描述可用的外部函数或”工具”。基于用户的请求，智能体 LLM 可以决定是否需要工具，并生成指定要调用哪个函数以及使用什么参数的结构化数据对象（如 JSON）。编排层执行此工具调用，检索结果，并将其反馈给 LLM。这允许 LLM 将最新的外部信息或操作结果合并到其最终响应中，有效地赋予其行动能力。

**Rule of thumb:** Use the Tool Use pattern whenever an agent needs to break out of the LLM’s internal knowledge and interact with the outside world. This is essential for tasks requiring real-time data (e.g., checking weather, stock prices), accessing private or proprietary information (e.g., querying a company’s database), performing precise calculations, executing code, or triggering actions in other systems (e.g., sending an email, controlling smart devices).

**经验法则：** 当智能体需要突破 LLM 的内部知识并与外部世界交互时，使用工具使用模式。这对于需要实时数据（例如，检查天气、股票价格）、访问私有或专有信息（例如，查询公司数据库）、执行精确计算、执行代码或触发其他系统中的操作（例如，发送电子邮件、控制智能设备）的任务至关重要。

## Visual Summary

![截屏2026-04-01 00.55.51](assets/截屏2026-04-01 00.55.51.png)

​                                                              Fig.5-1: Tool use design pattern

## Key Takeaways 

- Tool Use (Function Calling) allows agents to interact with external systems and access dynamic information.
- It involves defining tools with clear descriptions and parameters that the LLM can understand.
- The LLM decides when to use a tool and generates structured function calls.
- Agentic frameworks execute the actual tool calls and return the results to the LLM.
- Tool Use is essential for building agents that can perform real-world actions and provide up-to-date information.
- LangChain simplifies tool definition using the @tool decorator and provides create_tool_calling_agent and AgentExecutor for building tool-using agents.
- Google ADK has a number of very useful pre-built tools such as Google Search, Code Execution and Vertex AI Search Tool.
- 工具使用（函数调用）允许智能体与外部系统交互并访问动态信息。
- 它涉及定义具有 LLM 可以理解的清晰描述和参数的工具。
- LLM 决定何时使用工具并生成结构化工具调用。
- 智能体框架执行实际的工具调用并将结果返回给 LLM。
- 工具使用对于构建可以执行现实世界操作并提供最新信息的智能体至关重要。
- LangChain 使用 @tool 装饰器简化工具定义，并提供 create_tool_calling_agent 和 AgentExecutor 用于构建工具使用智能体。
- Google ADK 有许多非常有用的预构建工具，如 Google 搜索、代码执行和 Vertex AI 搜索工具。

## Conclusion

The Tool Use pattern is a critical architectural principle for extending the functional scope of large language models beyond their intrinsic text generation capabilities. By equipping a model with the ability to interface with external software and data sources, this paradigm allows an agent to perform actions, execute computations, and retrieve information from other systems. This process involves the model generating a structured request to call an external tool when it determines that doing so is necessary to fulfill a user’s query. Frameworks such as LangChain, Google ADK, and Crew AI offer structured abstractions and components that facilitate the integration of these external tools. These frameworks manage the process of exposing tool specifications to the model and parsing its subsequent tool-use requests. This simplifies the development of sophisticated agentic systems that can interact with and take action within external digital environments.

工具使用模式是将大型语言模型的功能范围扩展到其固有文本生成能力之外的关键架构原则。通过为模型配备与外部软件和数据源交互的能力，此范式允许智能体执行操作、进行计算并从其他系统检索信息。此过程涉及模型在确定满足用户查询需要时生成调用外部工具的结构化请求。LangChain、Google ADK 和 CrewAI 等框架提供结构化抽象和组件，促进这些外部工具的集成。这些框架管理向模型公开工具规范并解析其后续工具使用请求的过程。这简化了可以与外部数字环境交互并在其中采取行动的复杂智能体系统的开发。
