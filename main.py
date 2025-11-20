from dotenv import load_dotenv
import os

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch

from schemas import AgentResponse

tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4", temperature=0)

agent = create_agent(
    model=llm,
    tools=tools,
    response_format=AgentResponse,
)


def main():
    print("Hello from langchaintutorial!")

    #in this case, the result is a dictionary with keys "structured_response" and "intermediate_steps"
    #however, .invoke() on a runnablewill not always return a dictionary, be sure to check the specific doccumentation
    result = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content=(
                        "search for 3 job openings for an ai engineer using langchain "
                        "in the bay area on linkedin and list their details."
                    )
                )
            ]
        }
    )

    #print(result)
    structured = result.get("structured_response",None)
    print(structured)


if __name__ == "__main__":
    main()
