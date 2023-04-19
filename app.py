from flask import Flask, request, Request, jsonify
import json
import sys
from suggestion_db import query_suggestion
import requests


app = Flask(__name__)
api_key = '9548a6803dc1bb21607ca8df16793289'  # replace with your actual API key
city_name = 'Tingoli'

@app.route('/weather/<city>', methods = ["GET"])
def get_weather(city:str):
    city_name = city
    api_url = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name},GH&cnt=9&appid={api_key}'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        tomorrow_weather = data["list"][8]["weather"][0]["main"]
        return jsonify({"weather": tomorrow_weather})
    else:
        return 'Error', response.status_code

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