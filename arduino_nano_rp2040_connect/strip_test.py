import time

import board
import neopixel
from rainbowio import colorwheel

PIN = board.D3
BRIGHTNESS = 0.1
PIXELS = 60
ORDER = neopixel.GRBW

my_strip = neopixel.NeoPixel(
    PIN, PIXELS, brightness=BRIGHTNESS, auto_write=False, pixel_order=ORDER
)

# Increase the number to slow down the color chase
RAINBOW_CYCLE_WAIT = 0.1


def rainbow_cycle(pixels, wait):
    for j in range(255):
        for i in range(PIXELS):
            rc_index = (i * 256 // PIXELS) + j * 5
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


while True:
    rainbow_cycle(my_strip, RAINBOW_CYCLE_WAIT)
