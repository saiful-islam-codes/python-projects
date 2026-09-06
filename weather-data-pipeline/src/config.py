import os 
from dotenv import load_dotenv

load_dotenv()

# Load environment variables from .env file
WEATHER_API_URL = os.getenv("WEATHER_API_URL")
if WEATHER_API_URL is None:
    raise ValueError("WEATHER_API_URL is not set in the environment variables.")    

