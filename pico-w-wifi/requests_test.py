# SPDX-FileCopyrightText: 2022 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import os
import time
import ssl
import wifi  # pyright: ignore [reportMissingImports]
import socketpool  # pyright: ignore [reportMissingImports]
import microcontroller
import adafruit_requests

# Adafruit quotes URL
quotes_url = "https://www.adafruit.com/api/quotes.php"

# connect to our SSID
wifi.radio.connect(
    os.getenv("CIRCUITPY_WIFI_SSID"), os.getenv("CIRCUITPY_WIFI_PASSWORD")
)

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

while True:
    try:
        # pings adafruit quotes
        print(f"Fetching text from {quotes_url}")
        # gets the quote form adafruit quotes
        response = requests.get(quotes_url)
        print("-" * 40)
        # print response to the REPL
        print("Text response: ", response.text)
        print("-" * 40)
        response.close()
        # delays for 1 minute
        time.sleep(60)
    except Exception as e:
        print(f"Error:\n{str(e)}")
        print("Resetting microcontroller in 10 seconds")
        time.sleep(10)
        microcontroller.reset()  # pyright: ignore [reportGeneralTypeIssues]
