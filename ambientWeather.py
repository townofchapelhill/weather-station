# Libraries
import json
import requests
import datetime
import csv

# keys
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
    # Do nothing if failure (needs error handling, I'll add later -Luke)
    else:
        return None

#stores response info as a variable
weather_info = get_weather_info()

# if there is data in the response, write CSV headers
if len(weather_info) != 0:
    info_sheet = open("ambient-weather.csv", "w")
    info_sheet.write("Date (utc), Solar Radiation, Wind Gust (mph), Date, Temp (f), Dew Point, Temp in f, Hourly Rain (in), 'Feels Like' (f), UV, Wind Direction, Humidity, Humidity (in), Windspeed Avg. (mph), Daily Rain (in), Yearly Rain (in), Relative Pressure (inHg), Absolute Pressure (inHg), Monthly Rain (in)" + "\n")

# if there's data in the reponse, write CSV rows
if weather_info is not None:
    print("Here's your info: " )
    k = 0
    # This is not an ideal solution, but at the moment it's the only one I have that doesn't write the data 21 times
    # it does however add 2 extra entries and I haven't figured out why yet
    info_sheet.write(str(weather_info[0]['dateutc']) + ", ")
    info_sheet.write(str(weather_info[1]['solarradiation']) + ", ")
    info_sheet.write(str(weather_info[2]['windgustmph']) + ", ")
    info_sheet.write(str(weather_info[3]['date']) + ", ")
    info_sheet.write(str(weather_info[4]['tempf']) + ", ")
    info_sheet.write(str(weather_info[5]['dewPoint']) + ", ")
    info_sheet.write(str(weather_info[6]['tempinf']) + ", ")
    info_sheet.write(str(weather_info[7]['hourlyrainin']) + ", ")
    info_sheet.write(str(weather_info[8]['feelsLike']) + ", ")
    info_sheet.write(str(weather_info[9]['uv']) + ", ")
    info_sheet.write(str(weather_info[10]['winddir']) + ", ")
    info_sheet.write(str(weather_info[11]['humidity']) + ", ")
    info_sheet.write(str(weather_info[12]['humidityin']) + ", ")
    info_sheet.write(str(weather_info[13]['windspeedmph']) + ", ")
    info_sheet.write(str(weather_info[14]['dailyrainin']) + ", ")
    info_sheet.write(str(weather_info[15]['yearlyrainin']) + ", ")
    info_sheet.write(str(weather_info[16]['maxdailygust']) + ", ")
    info_sheet.write(str(weather_info[17]['weeklyrainin']) + ", ")
    info_sheet.write(str(weather_info[18]['baromrelin']) + ", ")
    info_sheet.write(str(weather_info[19]['baromabsin']) + ", ")
    info_sheet.write(str(weather_info[20]['monthlyrainin']) + ", ")
    info_sheet.write("\n")

    # this will write the data, but it repeats itself
    # I'm still working on a more elegant fix
    # while k < len(weather_info):
    #     row = []
    #     for i in weather_info[k].items():
    #         print(i)
    #         # info_sheet.write(str(weather_info[k]) + ", ")
    #         # info_sheet.write("\n")
    #         info_sheet.write("\n")
    #         k = k + 1

# Inform devs of request failure       
else:
    print('[!] Request Failed')