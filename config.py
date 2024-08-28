from langchain_ollama import ChatOllama

llm = ChatOllama(
    model = "llama3",
    temperature= 0.8,
    num_predict=256
)
