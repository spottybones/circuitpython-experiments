# SPDX-FileCopyrightText: 2023 Scott Burns
# SPDX-License-Identifier: MIT
# SPDX-FileName: animination1.py

"""Neopixel Animation Program for Rasperry Pi Pico W

The data pin to the Neopixel BFF is GP15
"""

from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.sparklepulse import SparklePulse
from adafruit_led_animation.color import AMBER, JADE
from adafruit_led_animation.sequence import AnimationSequence

from my_pixels import pixels

pixels.brightness = 0.2

sparkle = Sparkle(pixels, speed=0.05, color=AMBER, num_sparkles=10)
sparkle_pulse = SparklePulse(pixels, speed=0.05, color=JADE, period=3)

animations = AnimationSequence(
    sparkle,
    sparkle_pulse,
    advance_interval=5,
    auto_clear=True,
)

while True:
    animations.animate()
