# SPDX-FileCopyrightText: 2022 Scott Burns scott@lentigo.net
# SPDX-License-Identifier: MIT

import board
import neopixel
import time


pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.05, auto_write=False)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
OFF = (0, 0, 0)

while True:
    for color in (RED, GREEN, BLUE):
        for i in range(10):
            pixels[i] = color
            pixels.show()
            time.sleep(1)
            pixels[i] = OFF
            pixels.show()
