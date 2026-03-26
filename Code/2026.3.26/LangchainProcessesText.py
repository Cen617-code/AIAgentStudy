import os 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

## For better security, load enviromment variables from a .env file
## from dotenv import load_dotenv
## load_dotenv()
## Make sure your OPENAI_API_KEY is set in the .env file

load_dotenv()

## Initialize the Language Model 
llm = ChatOpenAI(
    model="gpt-5.4",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
    )

## --- Prompt 1: Extract Information ---
prompt_extract = ChatPromptTemplate.from_template(
    "Extract the technical specifications from the follow text:\n\n{text_input}"
)

## --- Prompt 2: Transform to JSON ---
prompt_transform = ChatPromptTemplate.from_template(
    "Transform the following specifications into a JSON object with 'cpu', 'memory', and 'storage' as keys:\n\n{specifications}"
)

## --- Build the Chain using LCEL ---
## The StrOutputParser() converts the LLM's message output to asimple string.
extraction_chain = prompt_extract | llm | StrOutputParser()

## The full chain passes the output of the extraction chain into the 'specifications'
## variable for the transformation prompt.
full_chain = (
    {"specifications": extraction_chain}
    | prompt_transform
    | llm
    | StrOutputParser()
)

## --- Run the Chain ---
input_text = "The new laptop model fertures a 3.5 Ghz octa-core processor, 16GB of RAM, and a 1TB NVMe SSD."

## Execute the chain with the input text dictionary.
final_result = full_chain.invoke({"text_input": input_text})

print("\n--- Final JSON Output ---")
print(final_result)