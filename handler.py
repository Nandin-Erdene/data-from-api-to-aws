import json
import requests
import boto3
from datetime import datetime
import pytz
import os

s3 = boto3.client('s3')

def store_api_data(event, context):
    # Latitude and longitude of Melbourne
    lat = -37.8136
    lon = 144.9631
    # openweathermap api key
    api_key = "58a0c66e12b3ac0d90c63db04f5712e0"
    # imperial: Fahrenheit, metric: Celsius, default: Kelvin 
    units = "metric"
    url = "https://api.openweathermap.org/data/2.5/weather"

    # Append attributes to the URL
    url_with_attrs = url + "?lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + api_key + "&units=" + units

    # Fetch the data from the URL
    response = requests.get(url_with_attrs)

    # Store data in S3
    timezone = os.environ['TIMEZONE']
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz)
    s3.put_object(Bucket='melbourne-weather-bucket', Key=current_time.strftime("%Y%m%d/%H:%M:%S") + '.json', Body=json.dumps(response.json()))

    return {
        'statusCode': 200,
        'body': 'Data stored in S3'
    }
    
