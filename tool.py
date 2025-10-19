from langchain_community.chat_models import ChatOpenAI
from langchain.agents import AgentExecutor, Tool, AgentType
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from langchain.agents import initialize_agent
from datetime import datetime, timedelta
from prompt import prompt
from dotenv import load_dotenv
from hotel_tool import HotelSearchTool
import os

# Load environment variables
if not load_dotenv():
    raise EnvironmentError("Failed to load .env file")

# Debug: Print to verify API key is loaded (will show first few characters only)
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    print(f"API key loaded and starts with: {api_key[:7]}...")
else:
    raise EnvironmentError("OPENAI_API_KEY not found in environment variables")
def setup_tools():
    # Initialize search tool
    search = DuckDuckGoSearchRun()
    search_tool = Tool(
        name="search",
        func=search.run,
        description="Search the internet for information about recent events or general queries."
    )
    
    # Initialize weather tool
    weather = OpenWeatherMapAPIWrapper()
    weather_tool = Tool(
        name="weather",
        func=weather.run,
        description="Get the current weather for a specific location. Input should be a city name."
    )
    
    # Initialize hotel search tool
    hotel_search = HotelSearchTool()
    hotel_tool = Tool(
        name="hotel_search",
        func=hotel_search.run,
        description="Search for hotels in a city. Just provide the city code (e.g., 'NYC' for New York, 'PAR' for Paris) to see if hotels exist in that area."
    )
    
    return [search_tool, weather_tool, hotel_tool]

def create_agent_executor():
    # Initialize the language model
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",  # Using the standard GPT-3.5 model
        temperature=0
    )
    
    # Setup tools
    tools = setup_tools()
    
    # Initialize the agent with OpenAI Functions
    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True,
        handle_parsing_errors=True
    )

# Only run if this file is run directly (not imported)
if __name__ == "__main__":
    # Create agent executor
    agent_executor = create_agent_executor()
    
    # Test the agent with a sample query
    # Use current year (2025) in the query
    response = agent_executor.invoke({
        "input": "Are there any hotels in NYC?"
    })
    print(response["output"])