import requests

# Function to get weather data from OpenWeatherMap API
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Create the full API URL with the city and API key
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    
    # Send a request to the API
    response = requests.get(complete_url)
    
    # Check if the response status is OK (200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()
        
        # Extract necessary weather details
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        humidity = main['humidity']
        description = weather['description']
        
        # Display weather information
        print(f"Weather in {city.capitalize()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
    else:
        print(f"City {city} not found. Please try again.")

# Main program
def main():
    api_key = "YOUR_API_KEY_HERE"  # Replace this with your OpenWeatherMap API key
    city = input("Enter the city name: ")
    
    # Call the weather function
    get_weather(city, api_key)

# Entry point
if __name__ == "__main__":
    main()
