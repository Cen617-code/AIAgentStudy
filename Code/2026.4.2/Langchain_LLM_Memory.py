import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model_name = "openrouter/free"
api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Set OPENROUTER_API_KEY or OPENAI_API_KEY before running this script.")

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    model=model_name,
    api_key=api_key,
    temperature=0,
    default_headers={
        "HTTP-Referer": "https://github.com/Cen617-code/AIAgentStudy",
        "X-Title": "AIAgentStudy",
    },
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}"),
])

chain = prompt | llm | StrOutputParser()

store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

conversation = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="chat_history",
)

response = conversation.invoke(
    {"question": "Hi, I'm Jane."},
    config={"configurable": {"session_id": "demo-user"}},
)
print(response)

response = conversation.invoke(
    {"question": "Do you remember my name?"},
    config={"configurable": {"session_id": "demo-user"}},
)
print(response)
