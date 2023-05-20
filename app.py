from flask import Flask, request, Request, jsonify, send_from_directory
import json
import sys
from suggestion_db import query_suggestion
import requests
from flask import make_response

app = Flask(__name__)
api_key = '9548a6803dc1bb21607ca8df16793289'  # replace with your actual API key


# Get weather by city.
@app.route('/vxml/weather/<city>.xml', methods = ['GET'])
def vxml_get_weather(city: str):
    api_url = f'https://api.openweathermap.org/data/2.5/forecast?q={city},GH&cnt=9&appid={api_key}'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        tomorrow_weather = data["list"][8]["weather"][0]["main"]
    else:
        tomorrow_weather = 'Error'

    with open('templates/weather_response.xml', 'r') as f:
        xml_str = f.read()
        xml_str = xml_str.format(city=city, weather=tomorrow_weather)
    # Create a response object with the XML data and headers
    response = make_response(xml_str)
    response.headers['Content-Type'] = 'application/xml'

    return response

# entry.xml is served on vxml platform, other static vxml is returned by this method.
@app.route('/vxml/static/<filename>', methods = ['GET'])
def vxml_main(filename: str):
    with open(f'vxml/{filename}', 'r') as f:
        xml_str = f.read()
    response = make_response(xml_str)
    response.headers['Content-Type'] = 'application/xml'

    return response

# Get suggestion menu from weather, becaues I can't put 2 menus in one vxml
@app.route('/vxml/<weather>/suggestion_menu.xml', methods = ['GET'])
def vxml_suggestion_menu(weather: str):
    with open('templates/suggestion_menu.xml', 'r') as f:
        xml_str = f.read()
        xml_str = xml_str.format(weather=weather)
    # Create a response object with the XML data and headers
    response = make_response(xml_str)
    response.headers['Content-Type'] = 'application/xml'

    return response

# Get suggestion from weather and crop
@app.route('/vxml/suggestion/<weather>/<crop>.xml', methods = ['GET'])
def vxml_get_suggestion(weather: str, crop: str):
    
    suggestion = 'Very good, plant!!' # TODO: populate db and get from db

    with open('templates/suggestion_response.xml', 'r') as f:
        xml_str = f.read()
        xml_str = xml_str.format(suggestion=suggestion)
    # Create a response object with the XML data and headers
    response = make_response(xml_str)
    response.headers['Content-Type'] = 'application/xml'

    return response

# Get french audio
@app.route('/french/<path:filename>')
def send_report(filename):
    return send_from_directory('French', filename)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port= 60000,
        debug=True
    )