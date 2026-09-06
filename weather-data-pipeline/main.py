import sys
from src.client import fetch_weather


def run_pipeline():
    print("Starting Weather Data Pipeline...\n")

    try:
        print("Fetching current weather data...")
        weather = fetch_weather()

        print("\n--- Live Weather Update ---")
        print(f"Temperature : {weather.temperature}°C")
        print(f"Wind Speed  : {weather.wind_speed} km/h")
        print(f"Humidity    : {weather.humidity}")
        print("---------------------------")
        print("\nPipeline executed successfully!")

    except Exception as e:
        print(f"Pipeline execution failed: {e}", file=sys.stderr)


if __name__ == "__main__":
    run_pipeline()