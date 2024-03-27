# SPDX-FileCopyrightText: 2023 Scott Burns
# SPDX-License-Identifier: MIT
# SPDX-FileName: fancy2.py

"""
Cycle through all HSV values and output fully saturated colors to
the LED ring on the CPB
"""

import time

import adafruit_fancyled.adafruit_fancyled as fancy
from adafruit_circuitplayground.bluefruit import (  # pyright: ignore [reportMissingImports]
    cpb,
)

from my_boardcheck import check_board

# from my_palettes import my_palettes

check_board("circuitplayground_bluefruit")

cpb.pixels.auto_write = False  # update only when we say
cpb.pixels.brightness = 0.1  # make less blinding

GAMMA_LEVELS = (0.25, 0.3, 0.15)

SIZE = 255

while True:
    for x in range(SIZE):
        color = fancy.CHSV(x / SIZE)
        color = fancy.gamma_adjust(
            color, brightness=GAMMA_LEVELS  # pyright: ignore [reportGeneralTypeIssues]
        )
        for i in range(10):
            cpb.pixels[i] = color.pack()  # pyright: ignore [reportGeneralTypeIssues]
        cpb.pixels.show()
        time.sleep(0.03)
