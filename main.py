
from dotenv import load_dotenv
load_dotenv()
import os

from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain.output_parsers import OutputFixingParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
from schemas import AgentResponse

tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4")
react_prompt = hub.pull("hwchase17/react")
output_parser = PydanticOutputParser(pydantic_object=AgentResponse)

"""
output_parser = OutputFixingParser.from_llm(
    parser=PydanticOutputParser(pydantic_object=AgentResponse),
    llm=ChatOpenAI(model="gpt-4")
)
"""

react_prompt_with_format_instructions = PromptTemplate(
    template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
    input_variables=[
        "input", "agent_scratchpad", "tool_names"
    ]
).partial(format_instructions=output_parser.get_format_instructions())


agent = create_react_agent(
    llm = llm,
    tools = tools,
    prompt=react_prompt_with_format_instructions
)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
extract_output = RunnableLambda(lambda x: x["output"])
parse_output = RunnableLambda(lambda x: output_parser.parse(x))
chain = agent_executor | extract_output | parse_output


def main():
    print("Hello from langchain-course!")
    result = chain.invoke(
        input={
            "input" : "Search for 3 job postings for an AI Engineer using LangChain in the bay area on LinkedIn and list their details"
        }
    )
    print(f"LLM-Response: {result}")


if __name__ == "__main__":
    main()

