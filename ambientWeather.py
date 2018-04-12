# Libraries
import json
import requests
import datetime
import csv
import secrets2

# sets headers
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(str(secrets2.macAddress) + str(secrets2.apiKey) + str(secrets2.appKey))}

# makes the request
def get_weather_info():
    url = "https://api.ambientweather.net/v1/devices/" + str(secrets2.macAddress) + "?apiKey=" + str(secrets2.apiKey) + "&applicationKey=" + str(secrets2.appKey) + "&limit=21"
    response = requests.get(url)
    # if success then load content
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    # Do nothing if failure (needs better error handling)
    else:
        print(response.status_code)
        return None

# stores response info as a variable
weather_info = get_weather_info()

# if there is data in the response, write CSV headers
if len(weather_info) != 0:
    info_sheet = open("ambient-weather.csv", "a")
    writer = csv.writer(info_sheet)


# if there's data in the reponse, write CSV rows
if weather_info is not None:
    print("Here's your info: " )
    print(weather_info)
    # writes weather data to CSV
    info_sheet.write(str(weather_info[2]['tempf']) + " F, ")
    info_sheet.write(str(weather_info[4]['humidity']) + "%, ")
    info_sheet.write(str(weather_info[5]['windspeedmph']) + " mph, ")
    info_sheet.write(str(weather_info[6]['windgustmph']) + " mph, ")
    info_sheet.write(str(weather_info[9]['baromabsin']) + " inHg, ")
    info_sheet.write(str(weather_info[10]['baromrelin']) + " inHg, ")
    info_sheet.write(str(weather_info[12]['dailyrainin']) + " in, ")
    info_sheet.write(str(weather_info[14]['monthlyrainin']) + " in, ")
    info_sheet.write(str(weather_info[15]['yearlyrainin']) + " in, ")
    info_sheet.write(str(weather_info[17]['uv']) + " (0-11+), ")
    info_sheet.write(str(weather_info[20]['date']) + "\n")


# Inform devs of request failure       
else:
    print('[!] Request Failed')