# SPDX-FileCopyrightText: 2023 Scott Burns
# SPDX-License-Identifier: MIT
# SPDX-FileName: my_led_strip.py

""" Set up pixels for Pico W with a strip of 60 RGB Neopixels
"""

import board
import neopixel

pixels = neopixel.NeoPixel(
    board.GP15,  # pyright: ignore [reportGeneralTypeIssues]
    60,
    brightness=1.0,
    auto_write=False,
    pixel_order=neopixel.GRB,
)
