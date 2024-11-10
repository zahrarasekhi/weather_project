import requests
from dotenv import load_dotenv
import os

load_dotenv()
def get_city_temperature(city_name):
    api_key = os.getenv('API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    
    try:
        response = requests.get(url)  
        response.raise_for_status()  
        
        data = response.json()  
        temperature = data['main']['temp']  
        return temperature  
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}") 
    except Exception as err:
        print(f"An error occurred: {err}")  


city = input("please enter a city name: ")
temperature = get_city_temperature(city)

if temperature is not None:
    print(f"Temprature of city{city} is {temperature} degree celsios.")
