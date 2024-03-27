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
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
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

pixels.brightness = 0.2

solid_pink = Solid(pixels, color=PINK)
solid_amber = Solid(pixels, color=AMBER)
blink = Blink(pixels, speed=0.5, color=JADE)
comet_purple = Comet(pixels, speed=0.05, color=PURPLE, tail_length=25)
comet_pink = Comet(pixels, speed=0.05, color=PINK, tail_length=25)
comet_teal = Comet(pixels, speed=0.01, color=TEAL, tail_length=10)
chase = Chase(pixels, speed=0.05, size=3, spacing=6, color=AMBER)
chase2 = Chase(pixels, speed=0.1, size=5, spacing=6, color=PINK)
colorcycle = ColorCycle(pixels, speed=0.5, colors=[MAGENTA, ORANGE, TEAL])
rainbow = Rainbow(pixels, speed=0.2, step=1, period=10)
rainbow_chase = RainbowChase(pixels, speed=0.02, size=5, spacing=3)
rainbow_comet_up = RainbowComet(
    pixels, speed=0.05, reverse=False, bounce=True, tail_length=25
)
rainbow_comet_down = RainbowComet(pixels, speed=0.1, reverse=True)

comet_down = Comet(pixels, speed=0.05, color=PURPLE, tail_length=25, reverse=True)
comet_up = Comet(pixels, speed=0.05, color=PURPLE, tail_length=25, reverse=False)


class MyComet:
    def __init__(self, reverse: bool = False) -> None:
        self.comet = Comet(
            pixels, speed=0.05, color=PURPLE, tail_length=25, reverse=reverse
        )


comet_up = MyComet().comet
comet_down = MyComet(True).comet

animations = AnimationSequence(
    rainbow_comet_up,
    rainbow_comet_down,
    advance_interval=None,
)

# animations2 = AnimationSequence(
#     advance_interval=6,
# )

while True:
    animations.animate()
    # animations2.animate()
