# Libraries
import json
import requests
import datetime
import csv

# keys, will be stored in a secrets file
appKey = "93b8237f9d7f487c8e08d08fbef51400eb4d1073e9d549b9bc2821bdf13c73d2"
apiKey = "783ff6a8d19744f6a05a7e61e7bbf9b21db3b39f44e74146b338bde4b2a15aa2"
macAddress = "C0:21:0D:1F:04:EC"
urlBase = "https://api.ambientweather.net/v1/devices/"

# sets headers
headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(macAddress + apiKey + appKey)}

# makes the request
def get_weather_info():
    url = "https://api.ambientweather.net/v1/devices/" + macAddress + "?apiKey=" + apiKey + "&applicationKey=" + appKey + "&limit=21"
    response = requests.get(url)
    # if success then load content
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    # Do nothing if failure (needs better error handling)
    else:
        return None

# stores response info as a variable
weather_info = get_weather_info()

# if there is data in the response, write CSV headers
if len(weather_info) != 0:
    info_sheet = open("ambient-weather.csv", "w")
    info_sheet.write("Temp (f), Humidity, Windspeed Avg. (mph), Wind Gust (mph), Absolute Pressure (inHg), Relative Pressure (inHg), Daily Rain (in), Monthly Rain (in), Yearly Rain (in), UV Radiation Index" + "\n")

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
    info_sheet.write(str(weather_info[17]['uv']) + " (0-10), ")


# Inform devs of request failure       
else:
    print('[!] Request Failed')