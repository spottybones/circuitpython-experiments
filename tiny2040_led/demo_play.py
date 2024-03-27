# SPDX-FileCopyrightText: 2023 Scott Burns
# SPDX-License-Identifier: MIT
# SPDX-FileName: animination1.py

"""Neopixel Animation Program for Pimoroni Tiny2040
"""

from my_pixels import pixels

from adafruit_led_animation import color
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.sequence import AnimationSequence

pixels.brightness = 0.05

colors = [color.RED, color.PINK, color.BLACK]

color_cycle = ColorCycle(pixels, speed=0.5, colors=colors)
solid = Solid(pixels, color=color.RED)

seq = AnimationSequence(
    Solid(pixels, color=color.RED),
    Solid(pixels, color=color.BLUE),
    Solid(pixels, color=color.GREEN),
    advance_interval=2,
    auto_clear=False,
)

while True:
    seq.animate()
