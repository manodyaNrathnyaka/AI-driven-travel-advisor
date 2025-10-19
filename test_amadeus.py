from amadeus import Client
from dotenv import load_dotenv
import os

def test_amadeus_connection():
    # Load environment variables
    load_dotenv()
    
    # Get credentials
    api_key = os.getenv('AMADEUS_API_KEY')
    api_secret = os.getenv('AMADEUS_API_SECRET')
    
    if not api_key or not api_secret:
        print("Error: Amadeus credentials not found in .env file")
        return
    
    try:
        # Initialize Amadeus client
        amadeus = Client(
            client_id=api_key,
            client_secret=api_secret
        )
        
        # Test API connection with a simple hotel search
        response = amadeus.reference_data.locations.hotels.by_city.get(
            cityCode='PAR',  # Paris
        )
        
        print("Connection successful!")
        print(f"Found {len(response.data)} hotels in Paris")
        if response.data:
            print("\nSample hotel:")
            print(f"Hotel ID: {response.data[0]['hotelId']}")
            print(f"Name: {response.data[0]['name']}")
            print(f"Location: {response.data[0]['address']['cityName']}")
        
    except Exception as e:
        print("Connection failed!")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_amadeus_connection()