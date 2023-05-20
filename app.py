from flask import Flask, request, Request, jsonify
import json
import sys
from suggestion_db import query_suggestion
import requests
from flask import make_response

app = Flask(__name__)
api_key = '9548a6803dc1bb21607ca8df16793289'  # replace with your actual API key


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

@app.route('/vxml/main.xml', methods = ['GET'])
def vxml_main():
    with open('vxml/main.xml', 'r') as f:
        xml_str = f.read()
    response = make_response(xml_str)
    response.headers['Content-Type'] = 'application/xml'

    return response


@app.route('/vxml/suggestion/<city>/<weather>.xml', methods = ['GET'])
def vxml_get_suggestion(city: str, weather: str):
    
    suggested = 'weed' # TODO: populate db and get from db

    with open('templates/suggestion_response.xml', 'r') as f:
        xml_str = f.read()
        xml_str = xml_str.format(city=city, weather=weather, suggested=suggested)
    # Create a response object with the XML data and headers
    response = make_response(xml_str)
    response.headers['Content-Type'] = 'application/xml'

    return response


@app.route('/suggestion/<weather>/<plant>/<language>', methods = ["GET"])
def get_suggestion(weather:int, plant:int, language:int):
    sug = query_suggestion(weather=weather, plant=plant, language=language)
    return jsonify({"suggestion": sug})

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port= 60000,
        debug=True
    )