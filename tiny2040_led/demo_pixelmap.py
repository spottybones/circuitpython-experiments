# SPDX-FileCopyrightText: 2023 Scott Burns
# SPDX-License-Identifier: MIT
# SPDX-FileName: animination1.py

"""Neopixel Animation Program for Rasperry Pi Pico W

The data pin to the Neopixel BFF is GP15
"""

from my_pixels import pixels

from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation import helper
from adafruit_led_animation import color


pixels.brightness = 0.025

grid_width = 24
grid_height = 1

strip_vertical = helper.PixelMap.vertical_lines(
    pixels,
    grid_width,
    grid_height,
    helper.horizontal_strip_gridmap(grid_width, alternating=False),
)
strip_horizontal = helper.PixelMap.horizontal_lines(
    pixels,
    grid_width,
    grid_height,
    helper.horizontal_strip_gridmap(grid_width, alternating=False),
)

comet_h = Comet(
    strip_horizontal, speed=0.1, color=color.PURPLE, tail_length=3, bounce=True
)

comet_v = Comet(
    strip_horizontal, speed=0.1, color=color.AMBER, tail_length=3, bounce=True
)

chase_h = Chase(strip_horizontal, speed=0.1, size=3, spacing=6, color=color.JADE)

rainbow_chase_v = RainbowChase(strip_vertical, speed=0.1, size=3, spacing=2, step=8)

rainbow_comet_v = RainbowComet(
    strip_vertical, speed=0.1, tail_length=24, bounce=False, ring=True
)

rainbow_v = Rainbow(strip_vertical, speed=0.1, period=2)

rainbow_chase_h = RainbowChase(strip_horizontal, speed=0.1, size=3, spacing=3)

rainbow_chase = RainbowChase(pixels, speed=0.05, size=23, spacing=1)


class CometFactory:
    def make_comet(self, color: tuple) -> Comet:
        return Comet(pixels, speed=0.1, color=color, tail_length=24, ring=True)


comet_factory = CometFactory()

comets = []

for _color in [
    color.RED,
    color.ORANGE,
    color.YELLOW,
    color.GREEN,
    color.BLUE,
    color.PURPLE,
]:
    comets.append(comet_factory.make_comet(_color))

animation = AnimationSequence(
    *comets,
    advance_interval=5,
)

while True:
    rainbow_chase.animate()
