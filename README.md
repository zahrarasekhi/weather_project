
#WEATHER IN YOUR CITY

The weather project is designed to provide real-time weather information for a specific location using Python. It leverages a weather API (such as OpenWeatherMap) to retrieve current weather data, including temperature, humidity, wind speed, and weather conditions. The project can be run in a console or as a simple web application.



## API-KEY

1. Sign up on [OpenWeatherMap](https://openweathermap.org/)

2. Fill Out the Registration Form: Provide the required information, which typically includes:

   • Your email address

   • A password

   • Any other required details

3. Accept Terms and Conditions: Make sure to read and accept the terms of service and privacy policy.

4. Verify Your Email: After submitting the registration form, check your email for a verification link. Click on that link to verify your account.

5. Log In: Once your email is verified, return to the OpenWeatherMap website and log in using your credentials.

6. Get Your API Key: After logging in, navigate to the API section of your account dashboard to find your API key, which you will use to access weather data.


## Installation

1. Install Required Libraries:

   You need the requests library to make HTTP requests and python-dotenv to read the .env file. Install them using pip:

```bash
  pip install requests python-dotenv
```
2. 2. Create a .env File:
   In your project directory, create a file named .env and add your OpenWeatherMap API key:
   
   
```bash
     OPENWEATHER_API_KEY=your_api_key_here

```



    
## Running Tests

Run the script, and it will prompt you to enter a city name. After entering the name, it will display the current temperature in that city. Make sure to replace your_api_key_here in the .env file with your actual OpenWeatherMap API key.
