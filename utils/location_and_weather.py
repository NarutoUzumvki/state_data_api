import requests

from params import GOOGLEMAPS_API_KEY, OPENWEATHERMAP_API_KEY


# Function to get the latitude and longitude of a place using Google Maps API
def get_location_coordinates(place):
    if not place or place=="":
        return None, None, None
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={place}&key={GOOGLEMAPS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        map_link = f"https://www.google.com/maps/search/?api=1&query={place}".replace(" ", "+")
        return map_link, location['lat'], location['lng']
    else:
        print("Error:", data['status'])
        return None, None, None


# Function to get the weather forecast for a location from OpenWeatherMap API
def get_weather_forecast(latitude, longitude):
    if not latitude or not longitude:
        return None 
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        forecast = f"{data['main']['temp']}°C, Feels Like {data['main']['feels_like']}°C, {data['weather'][0]['description'].title()}"
        return forecast
    else:
        print("Error:", data['message'])
        return None