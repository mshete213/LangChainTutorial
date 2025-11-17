from typing import List
#BaseModel is a class that defines the structure of the data that will be returned by the tool, define schema for the data
#Field allows us to specify a description for the field, and other metadata
from pydantic import BaseModel, Field


from dotenv import load_dotenv
import os
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

tavily = TavilyClient()
class Source(BaseModel):
    """ Schema for a source of the agent """
    url: str = Field(description="The url of the source")


class AgentResponse(BaseModel):
    """ Schemafor the response of the agent """

    answer: str = Field(description="The agent's answer to the question")
    #default_factory is a function that will be called to create a default value for the field, in this case an empty list
    sources: List[Source]= Field(default_factory=list, description="The list ofsources used to answer the question")
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
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main():
    print("Hello from langchaintutorial!")
    #under the hood this is cast into a list with a single element; key is input and value is human message object
    #invoke is a method that takes a dictionary of messages and returns a response: FILL IN MESSAGES vs INPUT 
    # result is of type AgentResponse
    result = agent.invoke({"messages": HumanMessage(content="What is the current time and current weather in Tokyo?")})
    print(result)
if __name__ == "__main__":
    main()
