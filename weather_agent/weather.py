# weather_agent/weather.py
import os
import httpx

ACCU_API_KEY = os.getenv("ACCUWEATHER_API_KEY")  # Set this in Docker/env

def get_weather(location: str):
    # Placeholder locationKey lookup (normally you'd call AccuWeather Locations API)
    dummy_location_key = "349727"  # Example: Denver, CO

    url = f"http://dataservice.accuweather.com/currentconditions/v1/{dummy_location_key}"
    params = {"apikey": ACCU_API_KEY}

    try:
        response = httpx.get(url, params=params)
        data = response.json()
        if data:
            return {
                "temperature": data[0]["Temperature"]["Imperial"]["Value"],
                "conditions": data[0]["WeatherText"],
                "humidity": data[0].get("RelativeHumidity", None)
            }
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return None
