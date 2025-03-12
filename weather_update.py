import requests


def get_weather(city):
    api_key = "256211d07f150589cc9f1d0ea9c0239b"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    print(f"Sending request to: {url}")  # Debug: Print the API URL

    response = requests.get(url).json()

    if response.get("cod") != 200:
        print(f"Error: {response.get('message', 'Unknown error')}")
        return

    weather = response["weather"][0]["description"]
    temperature = response["main"]["temp"]
    print(f"The weather in {city} is {weather} with a temperature of {temperature}°C.")
