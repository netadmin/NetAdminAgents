# weather_agent/registration.py
import httpx
from agent_config import AGENT_METADATA

def register_with_directory(directory_url: str):
    try:
        response = httpx.post(f"{directory_url}/register", json=AGENT_METADATA)
        if response.status_code == 200:
            print("Successfully registered with MCP Directory.")
        else:
            print("Registration failed:", response.text)
    except Exception as e:
        print(f"Error during registration: {e}")
