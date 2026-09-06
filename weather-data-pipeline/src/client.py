from requests import get
from dotenv import load_dotenv  
from src.config import WEATHER_API_URL
from src.models import WeatherData
def fetch_weather() -> WeatherData:
    """
    Fetches weather data from the API and returns it as a WeatherData instance.
    
    Returns:
        WeatherData: An instance containing temperature, humidity, and wind speed.
    """
    response = get(WEATHER_API_URL)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    
    # Extract relevant weather data
    temperature = data.get("current_weather", {}).get("temperature")
    humidity = data.get("current_weather", {}).get("humidity")
    wind_speed = data.get("current_weather", {}).get("windspeed")
    
    return WeatherData(
        temperature=temperature,
        humidity=humidity,
        wind_speed=wind_speed
    )
    

if __name__ == "__main__":
    weather = fetch_weather()
    print("Live Weather Data Fetched:", weather)    
      