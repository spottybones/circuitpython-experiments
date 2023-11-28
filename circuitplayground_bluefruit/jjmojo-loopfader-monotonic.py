# SPDX-FileCopyrightText: 2023 Scott Burns
# SPDX-License-Identifier: MIT
# SPDX-Filename: jjmojo-loopfader-monotonic.py

import board
import neopixel
import time

rgb = neopixel.NeoPixel(
    board.NEOPIXEL,  # pyright: ignore [reportGeneralTypeIssues]
    10,
    brightness=0.2,
    auto_write=False,
)


class LoopFader:
    def __init__(self, palette) -> None:
        self.palette = palette
        self.index = 0
        self.checkin = time.monotonic()

    @property
    def color(self):
        color = self.palette[self.index]

        if time.monotonic() - self.checkin > 0.1:
            self.index += 1
            if self.index > len(self.palette) - 1:
                self.index = 0
            self.checkin = time.monotonic()

        return color


pride = (
    4980736,
    4980736,
    4981248,
    4982272,
    4984064,
    4986880,
    4990720,
    4996096,
    3951616,
    1592320,
    412672,
    19456,
    13312,
    5126,
    1048,
    60,
    76,
    65612,
    327756,
    852044,
    1507367,
    2359309,
    3538946,
    4980736,
)

fader = LoopFader(pride)

while True:
    rgb.fill(fader.color)
    rgb.show()
