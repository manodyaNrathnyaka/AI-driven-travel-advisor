from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool
from langchain.agents import AgentExecutor
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from langchain.agents.openai_tools import create_openai_tools_agent
from prompt import prompt  # Import the prompt from prompt.py
import os
from dotenv import load_dotenv 
print(load_dotenv())


# Use environment variables for API keys, never hardcode them
# Example of how you would get it from environment: os.environ["OPENAI_API_KEY"]

# load_dotenv() already loaded your API keys from .env file above

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# The prompt is now imported from prompt.py



weather_tool=OpenWeatherMapAPIWrapper()
weather_tool.name="weather"

search_tool=DuckDuckGoSearchRun()
search_tool.name="search"

tools=[search_tool,weather_tool]

agent=create_openai_tools_agent(llm,tools,prompt)

agentExecutor=AgentExecutor(agent=agent,tools=tools,verbose=True, handle_parsing_errors=True)
response=agentExecutor.invoke({"input":"What's the weather like in New York City and any recent news about it?"})
print(response["output"])



