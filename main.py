import requests
import json
import os

print(("Enter the name of the City"))
os.system(f"PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Enter the name of the City')\"")
city = input()

url = f"https://api.weatherapi.com/v1/current.json?key=22c812ca095a42c1aaf193446232107&q={city}"

r = requests.get(url)

weatherdict = json.loads(r.text)

# Extracting relevant information from the dictionary
location_data = weatherdict["location"]
current_weather_data = weatherdict["current"]

# Creating a dictionary to store the extracted information with their respective dictionary names
output_dict = {
    "Location Data": {
        "name": location_data["name"],
        "region": location_data["region"],
        "country": location_data["country"],
        "latitude": location_data["lat"],
        "longitude": location_data["lon"],
        "timezone_id": location_data["tz_id"],
    },
    "Current Weather Data": {
        "last_updated_epoch": current_weather_data["last_updated_epoch"],
        "last_updated": current_weather_data["last_updated"],
        "temperature_c": current_weather_data["temp_c"],
        "temperature_f": current_weather_data["temp_f"],
        "condition": current_weather_data["condition"]["text"],
        "wind_mph": current_weather_data["wind_mph"],
        "wind_kph": current_weather_data["wind_kph"],
        "wind_degree": current_weather_data["wind_degree"],
        "wind_direction": current_weather_data["wind_dir"],
        "pressure_mb": current_weather_data["pressure_mb"],
        "pressure_in": current_weather_data["pressure_in"],
        "precipitation_mm": current_weather_data["precip_mm"],
        "precipitation_in": current_weather_data["precip_in"],
        "humidity": current_weather_data["humidity"],
        "cloud_coverage": current_weather_data["cloud"],
        "feelslike_c": current_weather_data["feelslike_c"],
        "feelslike_f": current_weather_data["feelslike_f"],
        "visibility_km": current_weather_data["vis_km"],
        "visibility_miles": current_weather_data["vis_miles"],
        "uv_index": current_weather_data["uv"]
    }
}

# Printing the output in a vertical format
for dict_name, data in output_dict.items():
    print(f"{dict_name}:")
    for key, value in data.items():
        print(f" {key}: {value}")

os.system(f"PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Here is the data')\"")

w = (weatherdict["current"]["temp_c"])

print(f"The current weather in {city} is {w} degree")
os.system(f"PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(' And the current weather in {city} is {w} degree')\"")
