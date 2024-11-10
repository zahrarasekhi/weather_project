import os
import requests
from dotenv import load_dotenv


load_dotenv()

def get_city_temperature(city_name):
    
    api_key = os.getenv('OPENWEATHER_API_KEY')
    
    
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  
    }
    
    
    response = requests.get(url, params=params)
    
    
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        return temperature
    else:
        print(f"Error: {response.status_code} - {response.json().get('message')}")
        return None


if __name__ == "__main__":
    city = input("Enter the city name: ")
    temperature = get_city_temperature(city)
    if temperature is not None:
        print(f"The temperature in {city} is {temperature}°C.")
