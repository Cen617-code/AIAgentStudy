import asyncio
import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool as langchain_tool
from langchain_openai import ChatOpenAI

try:
    import nest_asyncio
except ImportError:
    nest_asyncio = None

load_dotenv()

def format_message_content(content) -> str:
    if isinstance(content, str):
        return content

    if isinstance(content, list):
        text_parts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                text_parts.append(item.get("text", ""))
            else:
                text_parts.append(str(item))
        return "\n".join(part for part in text_parts if part)

    return str(content)

try:
    # 使用 ChatOpenAI 并将 base_url 指向 OpenRouter
    llm = ChatOpenAI(
        base_url="https://openrouter.ai/api/v1", 
        model="openrouter/free", 
        temperature=0,
        default_headers={
            "HTTP-Referer": "https://github.com/Cen617-code/AIAgentStudy", 
            "X-Title": "AIAgentStudy",
        }
    )
    print(f"Language model initialized via OpenRouter: {llm.model_name}")
except Exception as e:
    print(f"Error initializing language model: {e}")
    llm = None

@langchain_tool
def search_information(query: str) -> str:
    """Search a small built-in knowledge base for simple factual questions."""
    print(f"\n--- Tool Called: search_information with query: '{query}' ---")
    simulated_results = {
        "weather in london": "The weather in London is currently cloudy with a temperature of 15°C.",
        "capital of france": "The capital of France is Paris.",
        "population of earth": "The estimated population of Earth is around 8 billion people.",
        "tallest mountain": "Mount Everest is the tallest mountain above sea level.",
        "default": f"Simulated search result for '{query}': No specific information found, but the topic seems interesting.",
    }
    result = simulated_results.get(query.strip().lower(), simulated_results["default"])
    print(f"--- TOOL RESULT: {result} ---")
    return result


tools = [search_information]
agent = None

if llm:
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt="You are a helpful assistant.",
    )


async def run_agent_with_tool(query: str):
    print(f"\n--- Running Agent with Query: '{query}' ---")

    if agent is None:
        print("Agent is unavailable because the language model was not initialized.")
        return

    try:
        response = await agent.ainvoke(
            {"messages": [{"role": "user", "content": query}]}
        )
        print("\n--- Final Agent Response ---")
        print(format_message_content(response["messages"][-1].content))
    except Exception as e:
        print(f"\nAn error occurred during agent execution: {e}")


async def main():
    tasks = [
        run_agent_with_tool("What is the capital of France?"),
        run_agent_with_tool("What's the weather like in London?"),
        run_agent_with_tool("Tell me something about dogs."),
    ]
    await asyncio.gather(*tasks)


if nest_asyncio is not None:
    nest_asyncio.apply()

asyncio.run(main())
