from amadeus import Client, ResponseError
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# from langchain.agents import initialize_agent,AgentExecutor,Tool
# from langchain_community.chat_models import ChatOpenAI

class HotelSearchTool:
    def __init__(self):
        load_dotenv()
        self.amadeus = Client(
            client_id=os.getenv('AMADEUS_API_KEY'),
            client_secret=os.getenv('AMADEUS_API_SECRET')
        )

    def run(self, query):
        try:
            # Parse the input query (expected format: "CITY_CODE, CHECK_IN_DATE, CHECK_OUT_DATE")
            parts = [part.strip() for part in query.split(',')]
            
            # Convert city name to airport code if needed
            city = parts[0].upper()
            if city == "NEW YORK" or city == "NEWYORK":
                city = "NYC"
            
            # If dates aren't provided, use tomorrow and day after tomorrow
            today = datetime.now()
            if len(parts) > 1 and parts[1]:
                check_in_date = parts[1]
            else:
                check_in_date = (today + timedelta(days=1)).strftime('%Y-%m-%d')
                
            if len(parts) > 2 and parts[2]:
                check_out_date = parts[2]
            else:
                check_out_date = (today + timedelta(days=2)).strftime('%Y-%m-%d')
            
            print(f"Searching for hotels in {city} for dates: {check_in_date} to {check_out_date}")
            return self.search_hotels(city, check_in_date, check_out_date)
        except Exception as e:
            return {
                'error': f"Error processing request: {str(e)}",
                'available': False
            }

    def search_hotels(self, city, check_in_date=None, check_out_date=None):
        try:
            # Just get hotels in the city without checking availability
            print(f"Debug: Fetching hotels for city {city}")
            hotels_response = self.amadeus.reference_data.locations.hotels.by_city.get(
                cityCode=city
            )
            hotels_count = len(hotels_response.data)
            print(f"Debug: Found {hotels_count} hotels in city")
            
            # Return basic hotel information without availability check
            hotels = []
            for hotel in hotels_response.data[:5]:  # Show first 5 hotels as examples
                hotels.append({
                    'name': hotel.get('name', 'N/A'),
                    'hotelId': hotel.get('hotelId', 'N/A'),
                    'address': hotel.get('address', {}).get('lines', ['N/A'])[0],
                    'distance': f"{hotel.get('distance', {}).get('value', 'N/A')} {hotel.get('distance', {}).get('unit', '')}",
                })
            return {
                'city': city,
                'total_hotels': hotels_count,
                'sample_hotels': hotels,
                'message': f"Found {hotels_count} hotels in {city}. Showing first 5 as examples."
            }

        except ResponseError as error:
            return {
                'error': str(error),
                'available': False
            }
