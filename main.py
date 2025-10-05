
from typing import List
from dotenv import load_dotenv
load_dotenv()
import os
from langchain_openai import ChatOpenAI, OpenAI
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.tools import Tool, tool



@tool
def get_text_length(text: str) -> int:
    """Returns the length of a text by characters"""
    print(f"get_text_length enter with {text=}\n")
    text = text.strip("'\n").strip(
        '"'
    )  # stripping away non alphabetic characters just in case
    return len(text)

def find_tool_by_name(tools: List[Tool], tool_name: str) -> Tool:
    for tool in tools:
        if tool.name == tool_name:
            return tool
    raise ValueError(f"Tool wtih name {tool_name} not found")



def main():
    
    print(f"Hello function-calling-case1 from langchain!\n")
    
    tools = [get_text_length]
    llm  = ChatOpenAI(temperature=0)
    llm_with_tools = llm.bind_tools(tools)

    messages = [HumanMessage(content="What is the length of word: Chirag")]

    while True:
        ai_message = llm_with_tools.invoke(messages)
        tool_calls = getattr(ai_message, "tool_calls", None) or []
        if len(tool_calls)>0:
            messages.append(ai_message)
            for tool_call in tool_calls:
                tool_name = tool_call.get("name")
                tool_args = tool_call.get("args", {})
                tool_call_id = tool_call.get("id")
                tool_to_use = find_tool_by_name(tools, tool_name)
                observation = tool_to_use.invoke(tool_args)
                print(f"Observation: {observation}\n")
                messages.append(
                    ToolMessage(content=str(observation), tool_call_id=tool_call_id)
                )
            continue
        print(f"LLM-Response: {ai_message.content}\n")
        break



if __name__ == "__main__":
    main()
