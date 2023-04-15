# Call Openweathermap API according to args
import requests

api_key = '9548a6803dc1bb21607ca8df16793289'  # replace with your actual API key
city_name = 'Tingoli'  # replace with the name of the city you want to retrieve weather data for
api_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={api_key}'

response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
    print(data)
    # do something with the weather data
else:
    print('Error:', response.status_code)
