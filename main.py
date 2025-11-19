from dotenv import load_dotenv
import os
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_tavily import TavilySearch

tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4", temperature=0)

#this is the special react prompt, more on this later
react_prompt = hub.pull("hwchase17/react")

#This creates the agent, which is a react agent that uses the tools to search the web and return the results
#This is the actual runtime object, which is like the "body" to the agents "brain"
#I need to pass tools to both
agent = create_react_agent(llm = llm, tools = tools, prompt = react_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)




def main():
    print("Hello from langchaintutorial!")

    result =agent_executor.invoke({"input": "search for 3 job openings for an ai engineer using langchain in the bay area on linkedin and list their details."})
    print(result)

if __name__ == "__main__":
    main()
