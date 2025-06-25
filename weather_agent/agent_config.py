# weather_agent/agent_config.py
AGENT_METADATA = {
    "id": "weather-agent",
    "name": "Weather Agent",
    "version": "1.0.0",
    "description": "Provides current weather data using AccuWeather API",
    "endpoint": "http://weather-agent.local:8000",  # Replace with actual hostname/IP
    "capabilities": ["get_weather"],
    "tags": ["utility", "weather", "environment"],
    "context": {
        "inputs": ["location"],
        "outputs": ["temperature", "conditions", "humidity"]
    }
}
