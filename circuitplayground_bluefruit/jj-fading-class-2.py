# SPDX-FileCopyrightText: 2023 Scott Burns
# SPDX-License-Identifier: MIT
# SPDX-FileName: jj-fading-class-2.py

import board
import neopixel
import time

rgb = neopixel.NeoPixel(
    board.NEOPIXEL,  # pyright: ignore [reportGeneralTypeIssues]
    10,
    brightness=1.0,
    auto_write=False,
)


class LoopFader:
    def __init__(self, palette) -> None:
        self.palette = palette
        self.index = 0

    @property
    def color(self):
        color = self.palette[self.index]
        self.index += 1
        if self.index > len(self.palette) - 1:
            self.index = 0
        return color


green_to_off = (
    19456,
    15360,
    11520,
    8448,
    6144,
    4096,
    2560,
    1536,
    768,
    256,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
)

pastels = (
    4983563,
    4986133,
    4989988,
    4995128,
    4738120,
    3230769,
    2051103,
    1199122,
    936974,
    1723418,
    2772010,
    4148287,
    4144972,
    2763340,
    1710668,
    921164,
    1184332,
    2039628,
    3223884,
    4737100,
    4995128,
    4989988,
    4986133,
    4983563,
)

halloween = (
    4983552,
    4458752,
    3999232,
    3540226,
    3146500,
    2753032,
    2359565,
    2097172,
    1769500,
    1507367,
    1245236,
    1048644,
    1048644,
    1245236,
    1507367,
    1769500,
    2097172,
    2359565,
    2753032,
    3146500,
    3540226,
    3999232,
    4458752,
    4983552,
)

faders = [
    LoopFader(green_to_off),
    LoopFader(pastels),
    LoopFader(green_to_off),
    LoopFader(pastels),
    LoopFader(halloween),
    LoopFader(pastels),
    LoopFader(green_to_off),
    LoopFader(pastels),
    LoopFader(green_to_off),
    LoopFader(halloween),
]

while True:
    rgb[::] = [f.color for f in faders]
    rgb.show()
    time.sleep(0.1)
