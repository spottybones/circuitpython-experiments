# SPDX-FileCopyrightText: 2023 Scott Burns
# SPDX-License-Identifier: MIT
# SPDX-FileName: strip_test.py

""" Example use of 'colorwheel' function
"""

import time

import board
import neopixel
from rainbowio import colorwheel

my_strip = neopixel.NeoPixel(
    board.D3,  # pyright: ignore [reportGeneralTypeIssues]
    60,
    brightness=0.1,
    auto_write=False,
    pixel_order=neopixel.GRBW,
)


def rainbow_cycle(pixels, wait):
    for j in range(255):
        for i in range(len(pixels)):
            rc_index = (i * 256 // pixels) + j * 5
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


# Increase the number to slow down the color chase
RAINBOW_CYCLE_WAIT = 0.05

while True:
    rainbow_cycle(my_strip, RAINBOW_CYCLE_WAIT)
