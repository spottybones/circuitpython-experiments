# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
# SPDX-FileName: fancyled_cpx_rotate.py

"""Simple FancyLED example for Circuit Playground Express"""

from adafruit_circuitplayground.bluefruit import (  # pyright: ignore [reportMissingImports]
    cpb as cpx,
)
import adafruit_fancyled.adafruit_fancyled as fancy

cpx.pixels.auto_write = False  # Refresh pixels only when we say
cpx.pixels.brightness = 0.2  # We'll use FancyLED's brightness controls

# Declare a 4-element color palette, this one happens to be a
# 'blackbody' palette -- good for heat maps and firey effects.
palette = [
    fancy.CRGB(1.0, 1.0, 1.0),  # pyright: ignore [reportArgumentType] White
    fancy.CRGB(1.0, 1.0, 0.0),  # pyright: ignore [reportArgumentType] Yellow
    fancy.CRGB(1.0, 0.0, 0.0),  # pyright: ignore [reportArgumentType] Red
    fancy.CRGB(0.0, 0.0, 0.0),  # pyright: ignore [reportArgumentType] Black
]

offset = 0  # Positional offset into color palette to get it to 'spin'
levels = (0.25, 0.3, 0.15)  # Color balance / brightness for gamma function

while True:
    for i in range(10):
        # Load each pixel's color from the palette using an offset, run it
        # through the gamma function, pack RGB value and assign to pixel.
        color = fancy.palette_lookup(palette, offset + i / 10)
        color = fancy.gamma_adjust(
            color,
            brightness=levels,  # pyright: ignore [reportArgumentType]
        )
        cpx.pixels[i] = color.pack()  # pyright: ignore [reportAttributeAccessIssue]
    cpx.pixels.show()

    offset += 0.033  # Bigger number = faster spin
