# SPDX-FileCopyrightText: 2023 Scott Burns
# SPDX-License-Identifier: MIT
# SPDX-FileName: pico_w_30_rgb.py

""" Set up pixels for Tiny2040 with a strip of 30 RGB Neopixels
"""

import board
import neopixel

pixels = neopixel.NeoPixel(
    board.GP29,  # pyright: ignore [reportGeneralTypeIssues]
    30,
    brightness=1.0,
    auto_write=False,
    pixel_order=neopixel.GRB,
)
