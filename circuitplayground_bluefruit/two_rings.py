# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
# SPDX-FileName: two_rings.py

""" Simple FancyLED example for Circuit Playground Express
"""

import adafruit_fancyled.adafruit_fancyled as fancy
import board
import neopixel
from adafruit_circuitplayground.bluefruit import (  # pyright: ignore [reportMissingImports]
    cpb as cpx,
)
from adafruit_led_animation import color

from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.sequence import AnimationSequence

cpx.pixels.auto_write = False  # Refresh pixels only when we say
cpx.pixels.brightness = 0.1  # We'll use FancyLED's brightness controls

ring = neopixel.NeoPixel(
    board.A1,  # pyright: ignore [reportGeneralTypeIssues]
    24,
    brightness=0.1,
    auto_write=False,
    pixel_order=neopixel.GRBW,
)


def color_to_CRGB(color: tuple) -> fancy.CRGB:
    return fancy.CRGB(color[0], color[1], color[2])


def pack_palette(
    palette: list[fancy.CRGB],
    length: int,
    gamma_levels: tuple[float, float, float] = (1.0, 1.0, 1.0),
) -> list[int]:
    packed_palette = []
    for i in range(length):
        crgb = fancy.palette_lookup(palette, i / length)
        crgb = fancy.gamma_adjust(
            crgb, brightness=gamma_levels  # pyright: ignore [reportGeneralTypeIssues]
        )
        packed_palette.append(crgb.pack())  # pyright: ignore [reportGeneralTypeIssues]
    return packed_palette


# Declare a 4-element color palette, this one happens to be a
# 'blackbody' palette -- good for heat maps and firey effects.
colors = [color.RED, color.YELLOW, color.WHITE, color.BLACK]
palette = [color_to_CRGB(x) for x in colors]

levels = (0.25, 0.3, 0.15)  # Color balance / brightness for gamma function
packed_palette = pack_palette(palette=palette, length=4, gamma_levels=levels)

offset = 0  # Positional offset into color palette to get it to 'spin'

colorcycle = ColorCycle(pixel_object=ring, speed=0.5, colors=packed_palette)

animations = AnimationSequence(colorcycle)

while True:
    animations.animate()
    # for i in range(10):
    #     # Load each pixel's color from the palette using an offset, run it
    #     # through the gamma function, pack RGB value and assign to pixel.
    #     color = fancy.palette_lookup(palette, offset + i / 10)
    #     color = fancy.gamma_adjust(color, brightness=levels)
    #     cpx.pixels[i] = color.pack()
    # cpx.pixels.show()

    # for i in range(24):
    #     color = fancy.palette_lookup(palette, offset + i / 24)
    #     color = fancy.gamma_adjust(color, brightness=levels)
    #     ring[i] = color.pack()
    # ring.show()
    #
    # offset += 0.066  # Bigger number = faster spin
