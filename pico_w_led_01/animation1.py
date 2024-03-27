# SPDX-FileCopyrightText: 2023 Scott Burns
# SPDX-License-Identifier: MIT
# SPDX-FileName: animination1.py

"""Neopixel Animation Program for Rasperry Pi Pico W

The data pin to the Neopixel BFF is GP15
"""

from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.color import (
    AMBER,
    JADE,
    MAGENTA,
    ORANGE,
    PINK,
    PURPLE,
    TEAL,
)
from adafruit_led_animation.sequence import AnimationSequence

from my_pixels import pixels

pixels.brightness = 0.1

solid = Solid(pixels, color=PINK)
blink = Blink(pixels, speed=0.5, color=JADE)
comet = Comet(pixels, speed=0.01, color=PURPLE, tail_length=10)
chase = Chase(pixels, speed=0.1, size=3, spacing=6, color=AMBER)
colorcycle = ColorCycle(pixels, speed=0.5, colors=[MAGENTA, ORANGE, TEAL])

animations = AnimationSequence(
    solid,
    blink,
    comet,
    chase,
    colorcycle,
    advance_interval=3,
)

while True:
    animations.animate()
