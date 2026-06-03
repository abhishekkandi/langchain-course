from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel, Field

load_dotenv()

from langchain.agents import create_agent 
# bare minimum requirements to create agent - Tools & LLM
from langchain.tools import tool # tool is a function that an agent can execute
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """Schema for a source used by the agent"""

    url:str = Field(description="The URL of the source")

class AgentRespose(BaseModel):
    """Schema for agent response with answer and sources"""
    
    answer:str = Field(description="The agent's answer to the query")
    sources: List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")

llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm, 
                     tools=tools,
                     response_format=AgentRespose)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke(
        {"messages":HumanMessage(content="Search for 3 job posting for an ai engineer using langchain in bengaluru, india area on linkedin and list their details")},
        config={"recursion_limit": 5})
    print(result)

if __name__ == "__main__":
    main()
