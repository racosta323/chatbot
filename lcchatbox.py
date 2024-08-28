import getpass
import os


os.environ["OPENAI_API_KEY"] = getpass.getpass()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model = "llama3")

from langchain_core.messages import HumanMessage

print(model.invoke(HumanMessage(content="Hi, I'm Rene")))