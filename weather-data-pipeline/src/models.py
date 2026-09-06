import dataclasses

@dataclasses.dataclass
class WeatherData:
    temperature: float
    humidity: float
    wind_speed: float
    

if __name__ == "__main__":
    
    sample = WeatherData(
        temperature=30.5,
        humidity=65.0,
        wind_speed=12.0
    )
    print("Model Verified:", sample)    
    time="2026-09-05T10:00"
  