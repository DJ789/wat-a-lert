import requests

# Enter your OpenWeatherMap API key and location information
api_key = "YOUR_API_KEY_HERE"
city_name = "CITY_NAME_HERE"
country_code = "COUNTRY_CODE_HERE"

# Construct the API URL using the API key and location information
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={api_key}"

# Send a GET request to the API URL and get the JSON response
response = requests.get(url)
weather_data = response.json()

# Extract the temperature and weather description from the JSON response
temperature = weather_data["main"]["temp"]
description = weather_data["weather"][0]["description"]

# Send the temperature and weather description to the viewer app
send_data_to_viewer_app(temperature, description)
