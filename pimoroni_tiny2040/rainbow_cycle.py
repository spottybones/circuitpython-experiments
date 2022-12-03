# SPDX-FileCopyrightText: 2022 Scott Burns <scott@lentigo.net>
# SPDX-License-Identifier: MIT

import time
import board
from rainbowio import colorwheel
import neopixel


PIN = board.GP0
BRIGHTNESS = 0.05
PIXELS = 24
ORDER = neopixel.GRBW

my_ring = neopixel.NeoPixel(
    PIN, PIXELS, brightness=BRIGHTNESS, auto_write=False, pixel_order=ORDER
)


def rainbow_cycle(pixels, wait):
    for j in range(255):
        for i in range(PIXELS):
            rc_index = (i * 256 // PIXELS) + j * 5
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


# Increase the number to slow down the color chase
RAINBOW_CYCLE_WAIT = 0.05

while True:
    rainbow_cycle(my_ring, RAINBOW_CYCLE_WAIT)
