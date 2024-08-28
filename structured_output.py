from config import llm
from Joke import Joke

#structured output not supported by llama3
structured_llm = llm.with_structured_output(Joke)

print(structured_llm.invoke("Tell me a joke about cats"))





