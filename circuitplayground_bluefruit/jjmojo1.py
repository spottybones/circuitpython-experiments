# SPDX-FileCopyrightText: 2023 Scott Burns
# SPDX-License-Identifier: MIT
# SPDX-FileName: jjmojo1.py

""" A rainbow color cycle example using FancyLED
"""

import time

import adafruit_fancyled.adafruit_fancyled as fancy
import board
import neopixel
from adafruit_led_animation import color

BRIGHTNESS = 0.1

rgb = neopixel.NeoPixel(
    board.NEOPIXEL,  # pyright: ignore [reportGeneralTypeIssues]
    10,
    brightness=1.0,
    auto_write=False,
)


def make_gradient(
    colors: list[fancy.CRGB] | tuple[fancy.CRGB], count: int = 24, cycle: bool = True
) -> tuple[fancy.CRGB, ...]:
    values = []
    ratio = 1.0 / len(colors)
    print(ratio)
    for index, my_color in enumerate(colors):
        value = float(index * ratio)
        values.append((value, my_color))

    if cycle:
        values.append((1.0, colors[0]))

    palette = []
    for expanded in fancy.expand_gradient(values, count):
        palette.append(
            fancy.gamma_adjust(
                expanded, brightness=BRIGHTNESS
            ).pack()  # pyright: ignore [reportGeneralTypeIssues]
        )

    return tuple(palette)


gradient = make_gradient(
    [
        fancy.CRGB(*color.RED),  # pyright: ignore[reportGeneralTypeIssues]
        fancy.CRGB(*color.ORANGE),  # pyright: ignore[reportGeneralTypeIssues]
        fancy.CRGB(*color.YELLOW),  # pyright: ignore[reportGeneralTypeIssues]
        fancy.CRGB(*color.GREEN),  # pyright: ignore[reportGeneralTypeIssues]
        fancy.CRGB(*color.BLUE),  # pyright: ignore[reportGeneralTypeIssues]
        fancy.CRGB(*color.PURPLE),  # pyright: ignore[reportGeneralTypeIssues]
    ],
    count=96,
)

print("gradient = ", gradient)

index = 0

while True:
    rgb.fill(gradient[index])
    rgb.show()

    index += 1
    if index > len(gradient) - 1:
        index = 0

    time.sleep(0.2)
