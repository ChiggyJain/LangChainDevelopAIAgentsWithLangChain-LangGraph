
from dotenv import load_dotenv
load_dotenv()
import os

from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch


tools = [TavilySearch()]
llm = ChatOpenAI(model="gpt-4")
react_prompt = hub.pull("hwchase17/react")
agent = create_react_agent(
    llm = llm,
    tools = tools,
    prompt=react_prompt
)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
chain = agent_executor


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

