import requests
import os
from dotenv import load_dotenv
load_dotenv()

def weather():
    print("\n Weather now")
    try:
        city = input("Please enter the city name: ")
        request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
        weather_data = requests.get(request_url).json()
        print(weather_data)
        print(f'\n Current weather for {weather_data["name"]}: ')
        print(f'The temperature is {weather_data ["main"]["temp"]} ,pressure is {weather_data ["main"]["pressure"]} and humidity is {weather_data ["main"]["temp"]}.')
    except KeyError:
        print("Please enter a valid name for city.")

if __name__ == "__main__":
    weather()