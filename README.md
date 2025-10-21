# AI-Driven Travel Advisor

I'm developing the backend for An intelligent travel advisory system that helps users find and book hotels,and get real time weather updates using AI-powered conversations. The system leverages the Amadeus API for hotel searches and LangChain for natural language processing.

## Project Structure

- `agent.py`: Main agent implementation using LangChain
- `hotel_tool.py`: Hotel search functionality using Amadeus API
- `tool.py`: Tool definitions and setup for the agent
- `prompt.py`: Conversation prompts and templates
- `test_amadeus.py`: Test suite for Amadeus API integration

  ## Technologies Used

- Python
- LangChain
- Amadeus API
- OpenAI GPT
- OpenWeatherMap API
- Agentic AI


## Setup

1. Clone the repository
```bash
git clone https://github.com/manodyaNrathnyaka/AI-driven-travel-advisor.git
```

2. Create a virtual environment
```bash
python -m venv agent_venv
source agent_venv/bin/activate  # On Windows: agent_venv\Scripts\activate
```


3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
Create a `.env` file with the following:
```
OPENAI_API_KEY=your_openai_key
AMADEUS_API_KEY=your_amadeus_key
AMADEUS_API_SECRET=your_amadeus_secret
OPENWEATHERMAP_API_KEY=your_weather_key
```

## Usage

Run the main agent:
```bash
python agent.py
```

