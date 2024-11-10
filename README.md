# weather_project
To create a function in Python that takes a city name as input and returns the temperature of that city, you can use the OpenWeatherMap API. You'll also need to use a .env file to store your API key securely. Below are the steps to achieve this:

▎Step 1: Set Up Your Environment

1. Install Required Libraries:
   You'll need the requests library to make HTTP requests and python-dotenv to read the .env file. You can install them using pip:

   
   pip install requests python-dotenv
   

2. Create a .env File:
   Create a file named .env in your project directory and add your OpenWeatherMap API key:

   
   OPENWEATHER_API_KEY=your_api_key_here
   
Step 2: Run The Program

Run the weather.py file



▎Explanation:

• Environment Variables: The load_dotenv() function loads environment variables from the .env file, allowing you to access your API key securely.

• Function Definition: The get_city_temperature function takes a city name as an argument and constructs a request to the OpenWeatherMap API.

• API Request: It sends a GET request with parameters including the city name, API key, and units (metric for Celsius).

• Response Handling: If the request is successful (HTTP status code 200), it extracts and returns the temperature. If there's an error, it prints an error message.

▎Usage:

Run the script, and it will prompt you to enter a city name. After entering the name, it will display the current temperature in that city. Make sure to replace your_api_key_here in the .env file with your actual OpenWeatherMap API key.
