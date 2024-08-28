from config import llm
#structured output not supported by llama3
# structured_llm = llm.with_structured_output(Joke)

# print(structured_llm.invoke("Tell me a joke about cats"))

#Streaming
messages = [
    ("system", "You are a helpful translator. Translate the user sentence to French."),
    ("human", "I love programming."),
]

stream = llm.stream(messages)
full = next(stream)

for chunk in stream:
    full += chunk
print(full)



