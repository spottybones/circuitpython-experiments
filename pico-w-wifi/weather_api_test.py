# SPDX-FileCopyrightText: 2022 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import os
import ssl
import wifi  # pyright: ignore [reportMissingImports]
import socketpool  # pyright: ignore [reportMissingImports]
import microcontroller
import adafruit_requests

# connect to our SSID
wifi.radio.connect(
    os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD")
)

# location
api_endpoint = "https://api.openweathermap.org/data/2.5/weather"
location = "falls church,va,us"

# openweathermap URL and token
url = f"{api_endpoint}?q={location}&appid={os.getenv("OPENWEATHER_API_KEY")}"

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

while True:
    try:
        # pings openweathermap
        response = requests.get(url)
        # packs the response into json
        response_as_json = response.json()
        print()
        # prints the entire JSON
        print(response_as_json)
        # gets the location name
        place = response_as_json['name']
        # gets weather type
        weather = response_as_json["weather"][0]["main"]
        # gets humidity %
        humidity = response_as_json["main"]["humidity"]
        # gets air pressure in hPa
        pressure = response_as_json["main"]["pressure"]
        # gets temp in kelvin
        temperature = response_as_json["main"]["temp"]
        # converts temp from Kelvin to Farenheight
        converted_temp = (temperature - 273.15) * 9/5 + 32
        # converts temp from Kelvin to Celsius
        # converted_temp = temperature - 273.15

        # prints out weather nicely as pulled from JSON
        print(f"""The current weather in {place} is:
        {weather}
        {converted_temp}°F
        {humidity}% Humidity 
        {pressure} hPa
        """)
        # delay for 5 minutes
        time.sleep(300)

    except Exception as e:
        print(f"Error:\n{str(e)}")
        print("Resetting microcontroller in 10 seconds")
        time.sleep(10)
        microcontroller.reset() # pyright: ignore [reportGeneralTypeIssues]
