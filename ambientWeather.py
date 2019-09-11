# Error log
ambientweatherlog = open("ambientweatherlog.txt","w")


# Libraries
try: 
	import json
	import requests
	import csv
	import secrets
	import os
	import traceback
	import filename_secrets
except: 
	ambientweatherlog.write("Issue importing. \n")


# makes the request
def get_weather_info():
	url = "https://api.ambientweather.net/v1/devices/" + str(secrets.macAddress) + "?apiKey=" + str(secrets.apiKey) + "&applicationKey=" + str(secrets.appKey) + "&limit=21"
	response = requests.get(url)
	# if success then load content
	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	# Do nothing if failure (needs better error handling)
	else:
		print(response.status_code)
		return None

# get data and style it for csv writing
def get_data(info_sheet):
	
	# stores response info as a variable
	weather_info = get_weather_info()
	print("Here's your info: " )
	print(weather_info)
	
	# writes weather data to CSV
	info_sheet.write(str(weather_info[2]['tempf']) + " F, ")
	info_sheet.write(str(weather_info[4]['humidity']) + "%, ")
	info_sheet.write(str(weather_info[5]['windspeedmph']) + " mph, ")
	info_sheet.write(str(weather_info[6]['windgustmph']) + " mph, ")
	info_sheet.write(str(weather_info[12]['dailyrainin']) + " in, ")
	info_sheet.write(str(weather_info[14]['monthlyrainin']) + " in, ")
	info_sheet.write(str(weather_info[15]['yearlyrainin']) + " in, ")
	info_sheet.write(str(weather_info[17]['uv']) + " (0-11+), ")
	info_sheet.write(str(weather_info[20]['date']) + "\n")
	
	
# main function to create log and call get_data	
def main():
	infofilename = os.path.join(filename_secrets.productionStaging, "ambient-weather.csv")
	info_sheet = open(infofilename, "a")

	# if there is data in the response, write CSV headers
	if os.stat(infofilename).st_size == 0:
		info_sheet.write("Temperature (f), Humidity, Wind Speed (mph), Wind Gust (mph), Daily Rain (in), Monthly Rain (in), Yearly Rain (in), UV, Date \n")
		
	get_data(info_sheet)
	info_sheet.close()


# main
main()