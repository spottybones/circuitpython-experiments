# SPDX-FileCopyrightText: 2023 Scott Burns
# SPDX-License-Identifier: MIT
# SPDX-FileName: jjred-gradient.py

""" Red Gradient Pulse (jjnomojjnomo examples)
"""

import time

import adafruit_fancyled.adafruit_fancyled as fancy
import board
import neopixel
from adafruit_led_animation import color

BRIGHTNESS = 0.1
COLOR = fancy.CRGB(*color.RED)  # pyright: ignore [reportGeneralTypeIssues]
BLACK = fancy.CRGB(*color.BLACK)  # pyright: ignore [reportGeneralTypeIssues]

rgb = neopixel.NeoPixel(
    board.NEOPIXEL,  # pyright: ignore [reportGeneralTypeIssues]
    10,
    brightness=1.0,
    auto_write=False,
)

point = 0.0
increment = 0.005

while True:
    my_color = fancy.gamma_adjust(fancy.mix(COLOR, BLACK, point), brightness=BRIGHTNESS)

    point += increment

    if point >= 1.0 or point <= 0.0:
        increment *= -1

    rgb.fill(my_color.pack())  # pyright: ignore [reportGeneralTypeIssues]
    rgb.show()

    time.sleep(0.01)
