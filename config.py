"""Configuration settings for the AI-driven travel advisor."""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
AMADEUS_API_KEY = os.getenv('AMADEUS_API_KEY')
AMADEUS_API_SECRET = os.getenv('AMADEUS_API_SECRET')
OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')

# Amadeus API Configuration
AMADEUS_HOST = 'test.api.amadeus.com'  # Change to 'api.amadeus.com' for production
AMADEUS_BASE_URL = f'https://{AMADEUS_HOST}'

# OpenAI Configuration
OPENAI_MODEL = "gpt-3.5-turbo"  # or "gpt-4" if you're using it
MAX_TOKENS = 150

# Application Settings
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'