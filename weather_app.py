# weather_app.py

import requests
import json

# Constants
API_KEY = 'your_openweathermap_api_key'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'

def fetch_weather(city_name: str) -> dict:
    """Fetch weather data from OpenWeatherMap API for the specified city."""
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}

def process_weather_data(data: dict) -> str:
    """Process and format weather data."""
    if not data:
        return "No data available."

    try:
        city = data['name']
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        formatted_data = (
            f"Weather in {city}:\n"
            f"Description: {weather.capitalize()}\n"
            f"Temperature: {temp}°C\n"
            f"Feels like: {feels_like}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind speed: {wind_speed} m/s"
        )
        return formatted_data
    except (KeyError, TypeError) as e:
        print(f"Error processing data: {e}")
        return "Error processing data."

def display_weather(formatted_data: str):
    """Display the formatted weather data."""
    print(formatted_data)

def main():
    city_name = input("Enter city name: ")
    weather_data = fetch_weather(city_name)
    formatted_data = process_weather_data(weather_data)
    display_weather(formatted_data)

if __name__ == "__main__":
    main()
