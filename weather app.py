import requests

def get_weather(city):
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = "f0a16c42aa0f48974a4b16115524a3ae"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if data["cod"] == 200:
            main = data["main"]
            weather = data["weather"][0]
            print(f"Weather in {city}:")
            print(f"Temperature: {main['temp']}°C")
            print(f"Humidity: {main['humidity']}%")
            print(f"Condition: {weather['description']}")
        else:
            print("City not found or invalid API key.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)