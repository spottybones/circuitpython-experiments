# SPDX-FileCopyrightText: 2017 John Edgar Park for Adafruit Industries
# SPDX-License-Identifier: MIT

# Circuit Playground NeoPixel
import time
import board
from rainbowio import colorwheel
import neopixel


BRIGHTNESS = 0.05

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=BRIGHTNESS, auto_write=False)

# choose which demos to play
# 1 means play, 0 means don't!
color_chase_demo = 0
flash_demo = 0
rainbow_demo = 0
rainbow_cycle_demo = 1


def color_chase(color, wait):
    for i in range(10):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        pixels[0] = colorwheel(j & 255)
        pixels.show()
        time.sleep(wait)


def rainbow(wait):
    for j in range(255):
        for i in range(len(pixels)):
            idx = int(i + j)
            pixels[i] = colorwheel(idx & 255)
        pixels.show()
        time.sleep(wait)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

COLOR_CHASE_SPEED = 0.1
FLASH_DEMO_SPEED = 0.5
RAINBOW_CYCLE_WAIT = 0.05
RAINBOW_WAIT = 0.01

while True:
    if color_chase_demo:
        color_chase(
            RED, COLOR_CHASE_SPEED
        )  # Increase the number to slow down the color chase
        color_chase(YELLOW, COLOR_CHASE_SPEED)
        color_chase(GREEN, COLOR_CHASE_SPEED)
        color_chase(CYAN, COLOR_CHASE_SPEED)
        color_chase(BLUE, COLOR_CHASE_SPEED)
        color_chase(PURPLE, COLOR_CHASE_SPEED)
        color_chase(OFF, COLOR_CHASE_SPEED)

    if flash_demo:
        pixels.fill(RED)
        pixels.show()
        # Increase or decrease to change the speed of the solid color change.
        time.sleep(FLASH_DEMO_SPEED)
        pixels.fill(GREEN)
        pixels.show()
        time.sleep(FLASH_DEMO_SPEED)
        pixels.fill(BLUE)
        pixels.show()
        time.sleep(FLASH_DEMO_SPEED)
        pixels.fill(WHITE)
        pixels.show()
        time.sleep(FLASH_DEMO_SPEED)

    if rainbow_cycle_demo:
        rainbow_cycle(
            RAINBOW_CYCLE_WAIT
        )  # Increase the number to slow down the rainbow.

    if rainbow_demo:
        rainbow(RAINBOW_WAIT)  # Increase the number to slow down the rainbow.
