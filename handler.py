import json
import requests
import boto3
from datetime import datetime
import pytz
import os
import csv

s3 = boto3.client('s3')

def store_api_data(event, context):
    try:
        # API URL
        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            # lat and long of Melbourne
            'lat' : '-37.8136',
            'lon' : '144.9631',
            # imperial: Fahrenheit, metric: Celsius, default: Kelvin
            'units' : 'metric',
            'appid' : '58a0c66e12b3ac0d90c63db04f5712e0'    
        }

        # Current time in Australia/Sydney timezone for file's name in S3
        timezone = os.environ['TIMEZONE']
        tz = pytz.timezone(timezone)
        current_time = datetime.now(tz)
        file_name = current_time.strftime("%Y%m%d/%H:%M:%S") + '.csv'

        # Fetch the Melbourne weather data from the openweathermap API
        response = requests.get(url=url, params=params)

        # Parse the response JSON and extract the relevant data
        response_json = response.json()

        weather_location = response_json["name"]
        country = response_json["sys"]["country"]
        weather_date = datetime.fromtimestamp(response_json["dt"], tz=tz).strftime("%Y-%m-%d")
        weather_time = datetime.fromtimestamp(response_json["dt"], tz=tz).strftime("%H:%M")

        temperature = response_json["main"]["temp"]
        feels_like = response_json["main"]["feels_like"]
        temp_min = response_json["main"]["temp_min"]
        temp_max = response_json["main"]["temp_max"]
        pressure = response_json["main"]["pressure"]
        humidity = response_json["main"]["humidity"]
        visibility = response_json["visibility"]

        wind_speed = response_json["wind"]["speed"]
        wind_degree = response_json["wind"]["deg"]
        sun_rise = datetime.fromtimestamp(response_json["sys"]["sunrise"], tz=tz).strftime("%H:%M")
        sun_set = datetime.fromtimestamp(response_json["sys"]["sunset"], tz=tz).strftime("%H:%M")

        # Write the data as a CSV file
        header = ["Location", "Date", "Time", "Temperature", "Feels like", "Lowest", "Highest",  "Pressure", "Humidity", "Visibility", "Wind speed", "Wind degree", "Sunrise", "Sunset"]
        with open("/tmp/mel_weather_data.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerow([weather_location + ', ' + country, weather_date, weather_time, temperature, feels_like, temp_min, temp_max, pressure, humidity, visibility, wind_speed, wind_degree, sun_rise, sun_set])

        # Store the CSV file to S3 bucket
        s3.upload_file("/tmp/mel_weather_data.csv", 'melbourne-weather-bucket', file_name)
        
        response = {
            "statusCode": 200,
            "body": json.dumps({"message": "Openweathermap API data stored in the S3 bucket successfully!"})
        }
    except Exception as e: 
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
    return response
        
    
