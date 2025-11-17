from dotenv import load_dotenv
import os
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

tavily = TavilyClient()

@tool
def search(query:str) -> str:
    """
    Tool that searches the web for information
    Args:
        query: The query to search the web for

    Returns:
        The search results
    """
    print(f"Searching the web for {query}")
    return tavily.search(query=query)

@tool
def getTime(query:str) -> str:
    """
    Tool that returns the current time
    Args:
        query: The query to search the web for

    Returns:
        The search results
    """
    print(f"Searching the web for {query}")
    return tavily.search(query=query)

llm = ChatOpenAI() 

tools = [search, getTime]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchaintutorial!")
    #under the hood this is cast into a list with a single element; key is input and value is human message object
    result = agent.invoke({"messages": HumanMessage(content="What is the current time and current weather in Tokyo?")})
    print(result)
if __name__ == "__main__":
    main()
