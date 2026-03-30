import os
import asyncio
from typing import Optional
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable, RunnableParallel, RunnablePassthrough

try:
    llm: Optional[ChatGoogleGenerativeAI] = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
except Exception as e:
    print(f"Error initializing language model: {e}")
    llm = None

summarize_chain: Runnable = (
    ChatPromptTemplate.from_messages([
        ("system", "Summarize the following topic concesely:"),
        ("user", "{topic}")
    ])
    | llm
    | StrOutputParser()
)

questions_chain: Runnable = (
    ChatPromptTemplate.from_messages([
        ("system", "Generate three interesting questions about the following topic:"),
        ("user", "{topic}")
    ])
    | llm
    | StrOutputParser()
)

terms_chain: Runnable = (
    ChatPromptTemplate.from_messages([
        ("system", "Identify 5-10 key terms from the following topic, separated by commas:"),
        ("user", "{topic}")
    ])
    | llm
    | StrOutputParser()
)

map_chain = RunnableParallel(
    {
        "summary": summarize_chain,
        "questions": questions_chain,
        "key_terms": terms_chain,
        "topic": RunnablePassthrough(),
    }
)

synthesis_prompt = ChatPromptTemplate.from_messages([
    ("system", """Based on the following information:
    Summary: {summary}
    Related Questions: {questions}
    Key Terms: {key_terms}
    Synthesize a comprehensive answer."""),
    ("user", "Original topic: {topic}")
])

async def run_paraller_example(topic: str) -> None:
    if not llm:
        print("LLM not initialized. Cannot run example.")
        return
    
    print(f"\n--- Running Parallel LangChain Example for Topic: '{topic}' ---")
    try:
        response = await map_chain.ainvoke(topic)
        print("\n--- Final Response ---")
        print(response)
    except Exception as e:
        print(f"\nAn error occurred during chain execution: {e}")

if __name__ == "__main__":
    test_topic = "The hisory of space exploration"
    asyncio.run(run_paraller_example(test_topic))