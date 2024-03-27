# SPDX-FileCopyrightText: 2023 Scott Burns
# SPDX-License-Identifier: MIT
# SPDX-Filename: gradient-generator.py

"""Script to generate gradients for LED Animations """

import time

import adafruit_fancyled.adafruit_fancyled as fancy
import board
import neopixel

from fader import Fader

rgb = neopixel.NeoPixel(
    board.NEOPIXEL,  # pyright: ignore [reportGeneralTypeIssues]
    10,
    brightness=1.0,
    auto_write=False,
)

DIM_LEVELS = (1.0, 0.7, 0.5, 0.3, 0.1, 0.05)
COLORS = 24

WHITE = fancy.CRGB(255, 255, 255)  # pyright: ignore [reportGeneralTypeIssues]
BLACK = fancy.CRGB(0, 0, 0)  # pyright: ignore [reportGeneralTypeIssues]
GRAY = fancy.CRGB(127, 127, 127)  # pyright: ignore [reportGeneralTypeIssues]
RED = fancy.CRGB(255, 0, 0)  # pyright: ignore [reportGeneralTypeIssues]
GREEN = fancy.CRGB(0, 255, 0)  # pyright: ignore [reportGeneralTypeIssues]
YELLOW = fancy.CRGB(255, 255, 0)  # pyright: ignore [reportGeneralTypeIssues]
BLUE = fancy.CRGB(0, 0, 255)  # pyright: ignore [reportGeneralTypeIssues]
ORANGE = fancy.CRGB(255, 127, 0)  # pyright: ignore [reportGeneralTypeIssues]
VIOLET = fancy.CRGB(139, 0, 255)  # pyright: ignore [reportGeneralTypeIssues]
INDIGO = fancy.CRGB(46, 43, 95)  # pyright: ignore [reportGeneralTypeIssues]

PINK = fancy.CRGB(255, 127, 127)  # pyright: ignore [reportGeneralTypeIssues]
MINT = fancy.CRGB(127, 255, 127)  # pyright: ignore [reportGeneralTypeIssues]
ROBIN = fancy.CRGB(127, 127, 255)  # pyright: ignore [reportGeneralTypeIssues]


def make_gradient(colors, steps=24, brightness=0.1, wrap=True):
    values = []
    ratio = 1.0 / len(colors)
    for index, color in enumerate(colors):
        value = float(index * ratio)
        values.append((value, color))

    if wrap:
        values.append((1.0, colors[0]))

    palette = []
    for expanded in fancy.expand_gradient(values, steps):
        palette.append(
            fancy.gamma_adjust(
                expanded, brightness=brightness
            ).pack()  # pyright: ignore [reportGeneralTypeIssues]
        )

    return tuple(palette)


gradients = {
    "pride": ([RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET], True),
    "halloween": ([ORANGE, VIOLET], True),
    "anna_howard_shaw": ([RED, WHITE, PINK, WHITE], True),
    "pastels": ([PINK, WHITE, MINT, WHITE, ROBIN, WHITE], True),
    "rgb": ([RED, GREEN, BLUE], True),
    "july4": ([RED, WHITE, WHITE, BLUE], True),
    "ireland": ([GREEN, WHITE, ORANGE], True),
    "icy": ([BLUE, ROBIN, WHITE, YELLOW, GRAY, BLUE, ROBIN, WHITE], False),
    "gray": ([WHITE, GRAY, BLACK, GRAY, WHITE], True),
    "white_to_off": ([WHITE, BLACK], False),
    "green_to_off": ([GREEN, BLACK], False),
    "blue_to_off": ([BLUE, BLACK], False),
    "red_to_off": ([RED, BLACK], False),
}

rgb.fill(0)
rgb.show()


def generate():
    while True:
        for data in gradients.values():
            colors, wrap = data
            for brightness in DIM_LEVELS:
                yield make_gradient(colors, COLORS, brightness, wrap)


cycler = generate()

for name, data in gradients.items():
    colors, wrap = data
    print(f"{name} = (")
    for brightness in DIM_LEVELS:
        gradient = make_gradient(colors, COLORS, brightness, wrap)
        print("\t", gradient, ",", sep="")
    print(")")

checkin = time.monotonic()
previous = 0

fader = Fader(next(cycler), 0.1)

rgb.fill(0)
rgb.show()

while True:
    if time.monotonic() - checkin > 4:
        fader.palette = next(cycler)
        rgb.fill(0)
        rgb.show()
        checkin = time.monotonic()
        time.sleep(1)

    fader.update()

    if fader.color != previous:
        previous = fader.color
        rgb.fill(fader.color)
        rgb.show()
