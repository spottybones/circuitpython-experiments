# SPDX-FileCopyrightText: 2023 Scott Burns
# SPDX-License-Identifier: MIT

import board
import neopixel

# from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase

# from adafruit_led_animation.animation.blink import Blink
# from adafruit_led_animation.animation.comet import Comet
# from adafruit_led_animation.animation.chase import Chase
# from adafruit_led_animation.animation.colorcycle import ColorCycle
# from adafruit_led_animation.sequence import AnimationSequence
# from adafruit_led_animation.color import (
#     PURPLE,
#     AMBER,
#     JADE,
#     PINK,
#     MAGENTA,
#     ORANGE,
#     TEAL,
# )

pixel_pin = board.D5
pixel_num = 30

BRIGHTNESS = 0.05

pixels = neopixel.NeoPixel(
    pixel_pin, pixel_num, brightness=BRIGHTNESS, auto_write=False
)

# solid = Solid(pixels, color=PINK)
# blink = Blink(pixels, speed=0.5, color=JADE)
# comet = Comet(pixels, speed=0.01, color=PURPLE, tail_length=10)
# chase = Chase(pixels, speed=0.1, size=3, spacing=6, color=AMBER)
# colorcycle = ColorCycle(pixels, speed=0.5, colors=[MAGENTA, ORANGE, TEAL])
#
# animations = AnimationSequence(
#     solid,
#     blink,
#     comet,
#     chase,
#     colorcycle,
#     advance_interval=3,
# )

# anim = Rainbow(pixels, speed=0.1, period=10)
anim = RainbowChase(pixels, speed=0.1, size=5, spacing=4)

while True:
    anim.animate()
