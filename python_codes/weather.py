import requests

def get_weather(city_name, api_key):
    # Base URL for Current Weather Data API
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    # Define query parameters (using metric units for Celsius)
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # Use 'imperial' for Fahrenheit
    }

    try:
        # Make the GET request to the API
        response = requests.get(base_url, params=params)

        # Check if the request was successful (Status Code 200)
        if response.status_code == 200:
            data = response.json()

            # Parsing specific data from the JSON response
            weather_desc = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]

            print(f"--- Weather in {city_name.title()} ---")
            print(f"Condition:   {weather_desc.capitalize()}")
            print(f"Temperature: {temp}°C")
            print(f"Feels Like:  {feels_like}°C")
            print(f"Humidity:    {humidity}%")

        elif response.status_code == 404:
            print(f"Error: The city '{city_name}' was not found. Please check your spelling.")
        elif response.status_code == 401:
            print("Error: Invalid API Key. Please check your OpenWeatherMap credentials.")
        else:
            print(f"Error: Failed to fetch data. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred connecting to the network: {e}")

if __name__ == "__main__":
    # Replace with your actual OpenWeatherMap API key
    API_KEY = "44f67f27f1a041af39965c3cb8e04c21"

    city = input("Enter city name: ")
    get_weather(city, API_KEY)

