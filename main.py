import requests

def get_weather(city):
    # Replace with your actual API key from WeatherAPI
    api_key = 'acc443b018804acca11170126240109'
    url = f"http://api.weatherapi.com/v1/current.json?key=acc443b018804acca11170126240109&q={city}&aqi=no"


    try:
        # Send a request to the WeatherAPI
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            location = data['location']
            current = data['current']

            # Extract relevant weather details
            city_name = location['name']
            region = location['region']
            country = location['country']
            temp_c = current['temp_c']
            condition = current['condition']['text']
            wind_kph = current['wind_kph']
            humidity = current['humidity']
            feels_like_c = current['feelslike_c']

            # Print weather details
            print(f"Weather in {city_name}, {region}, {country}:")
            print(f"Temperature: {temp_c}°C")
            print(f"Condition: {condition}")
            print(f"Wind: {wind_kph} kph")
            print(f"Humidity: {humidity}%")
            print(f"Feels Like: {feels_like_c}°C")
        else:
            print("Failed to retrieve weather data. Please check the city name or try again later.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the Weather App!")
    city = input("Enter the city name: ")
    get_weather(city)
