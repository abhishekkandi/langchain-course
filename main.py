from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent 
# bare minimum requirements to create agent - Tools & LLM
from langchain.tools import tool # tool is a function that an agent can execute
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="Search for 3 job posting for an ai engineer using langchain in bengaluru, india area on linkedin and list their details")})
    print(result)

if __name__ == "__main__":
    main()
