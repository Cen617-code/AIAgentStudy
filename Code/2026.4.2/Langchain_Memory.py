from langchain_classic.memory import ConversationBufferMemory

memory = ConversationBufferMemory()

memory.save_context({"input": "What's the weather like?"}, {"output": "It's sunny today."})

print(memory.load_memory_variables({}))