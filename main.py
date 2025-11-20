from dotenv import load_dotenv
import os

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_tavily import TavilySearch
from prompt import rawReactFormatInstructions
from schemas import AgentResponse
from langchain_core.prompts import PromptTemplate

# from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_core.runnables import RunnableLambda

# turns any python function -> usually a lambda function -> into a Runnable
# Runnable is a class that is used to run the agent (invokable)


tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4", temperature=0)
structuredLLM = llm.with_structured_output(AgentResponse)
# use with_structured_output to create a structured output LLM, accepts pydantic object as input


# outputParser = PydanticOutputParser (pydantic_object=AgentResponse)
# reactPromptWithFormat = PromptTemplate(template=rawReactFormatInstructions, 
    # input_variables=["input", "agent_scratchpad", "tool_names"], 
    # output_parser=outputParser).partial(format_instructions=
    # outputParser.get_format_instructions())
reactPromptWithFormat = PromptTemplate(
    template=rawReactFormatInstructions,
    input_variables=["input", "agent_scratchpad", "tool_names"],
).partial(format_instructions="")


# this is the special react prompt, more on this later
react_prompt = hub.pull("hwchase17/react")

# This creates the agent, which is a react agent that uses the tools to search the web and return the results
# This is the actual runtime object, which is like the "body" to the agents "brain"
# I need to pass tools to both
agent = create_react_agent(llm=llm, tools=tools, prompt=reactPromptWithFormat)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
# outputs dictionary with keys "output" and "intermediate steps"
extractOutput = RunnableLambda(lambda x: x["output"])
# extracts the output from the dictionary into a JSON string ("{:}")
# parseOutput = RunnableLambda(lambda x: outputParser.parse(x))
# converts the JSON string into a pydantic object, will have structure set in schemas.py along with other metadata
# that class inherits BaseModel

chain = agent_executor | extractOutput | structuredLLM


def main():
    print("Hello from langchaintutorial!")

    result = chain.invoke(
        {
            "input": "search for 3 job openings for an ai engineer using langchain in the bay area on linkedin and list their details."
        }
    )
    print(result)


if __name__ == "__main__":
    main()
