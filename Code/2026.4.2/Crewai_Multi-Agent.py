import os
from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def main():
    try:
        model_name = "openrouter/openrouter/free"
        api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "Set OPENROUTER_API_KEY or OPENAI_API_KEY before running this script."
            )

        # CrewAI Agent expects a CrewAI LLM (or model string), not a LangChain ChatOpenAI instance.
        llm = LLM(
            base_url="https://openrouter.ai/api/v1", 
            model=model_name,
            api_key=api_key,
            temperature=0,
            default_headers={
                "HTTP-Referer": "https://github.com/Cen617-code/AIAgentStudy", 
                "X-Title": "AIAgentStudy",
            }
        )
        print(f"Language model initialized via OpenRouter: {model_name}")
    except Exception as e:
        raise SystemExit(f"Error initializing CrewAI language model: {e}")

    researcher = Agent(
        role='Senior Research Analyst',
        goal='Find and summarize the latest trends in AI.',
        backstory="You are an experienced research analyst with a knack for identifying key trend and synthesizing information.",
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    writer = Agent(
        role='Technical Content Writer',
        goal='Write a clear and engaging blog post based on research findings.',
        backstory="You are a skilled writer who can translate complex technical topics into accessible content.",
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )

    research_task = Task(
        description="Research the top 3 emerging trends in Artificial Intelligence in 2024-2025. Focus on practical applications and potential impact.",
        expected_output="A detailed summary of the top 3 AI trends, including key points and sources.",
        agent=researcher,
    )

    writing_task = Task(
       description="Write a 500-word blog post based on the research findings. The post should be engaging and easy for a general audience to understand.",
       expected_output="A complete 500-word blog post about the latest AI trends.",
       agent=writer,
       context=[research_task],
    )
    
    blog_creation_crew = Crew(
       agents=[researcher, writer],
       tasks=[research_task, writing_task],
       process=Process.sequential,
       verbose=True
   )

    print("## Running the bolg creation crew with OpenRouter/free... ##")
    try:
        result = blog_creation_crew.kickoff()
        print("\n------------------\n")
        print("## Crew Final Output ##")
        print(result)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()