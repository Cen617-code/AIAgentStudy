import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

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

planner_writer_agent = Agent(
   role='Article Planner and Writer',
   goal='Plan and then write a concise, engaging summary on a specified topic.',
   backstory=(
       'You are an expert technical writer and content strategist. '
       'Your strength lies in creating a clear, actionable plan before writing, '
       'ensuring the final summary is both informative and easy to digest.'
   ),
   verbose=True,
   allow_delegation=False,
   llm=llm
)

topic = "The importance of Reinforcement Learning in AI"

high_level_task = Task(
   description=(
       f"1. Create a bullet-point plan for a summary on the topic: '{topic}'.\n"
       f"2. Write the summary based on your plan, keeping it around 200 words."
   ),
   expected_output=(
       "A final report containing two distinct sections:\n\n"
       "### Plan\n"
       "- A bulleted list outlining the main points of the summary.\n\n"
       "### Summary\n"
       "- A concise and well-structured summary of the topic."
   ),
   agent=planner_writer_agent,
)

crew = Crew(
   agents=[planner_writer_agent],
   tasks=[high_level_task],
   process=Process.sequential,
)

print("## Running the planning and writing task ##")
result = crew.kickoff()
print("\n\n---\n## Task Result ##\n---")
print(result)
