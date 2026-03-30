import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

google_api_key = os.getenv("GOOGLE_API_KEY")
model_name = os.getenv("GOOGLE_MODEL", "gemini-2.5-flash")

if not google_api_key:
    raise ValueError("Missing GOOGLE_API_KEY in system environment")

## Initialize the Language Model
llm = ChatGoogleGenerativeAI(
    model=model_name,
    temperature=0,
    google_api_key=google_api_key,
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
try:
    final_result = full_chain.invoke({"text_input": input_text})
except Exception as exc:
    raise RuntimeError(
        f"Gemini request failed. Check GOOGLE_API_KEY and GOOGLE_MODEL. "
        f"Current model={model_name!r}. Original error: {exc}"
    ) from exc

print("\n--- Final JSON Output ---")
print(final_result)
