# SPDX-FileCopyrightText: 2023 Scott Burns
# SPDX-License-Identifier: MIT
# SPDX-Filename: jjmojo-loopfader-monotonic3.py

import board
import neopixel
import time
import random

rgb = neopixel.NeoPixel(
    board.NEOPIXEL,  # pyright: ignore [reportGeneralTypeIssues]
    10,
    brightness=0.2,
    auto_write=False,
)


class Fader:
    def __init__(self, palette: tuple[int, ...], interval: float = 0.1) -> None:
        self.checkin = time.monotonic()
        self.color = 0
        self.interval = interval
        self.palette = palette
        self.max = len(self.palette) * interval
        self.epoch = 0

    def update(self):
        self.epoch = time.monotonic() - self.checkin

        index = round((self.epoch % self.max) / self.interval)

        if index > len(self.palette) - 1:
            index = 0
            self.checkin = time.monotonic()

        self.color = self.palette[index]
        self.last = index


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

fader = Fader(pride)

sleep = (0, 0.2, 0.3, 0.6, 0.8, 1.0)

previous = None
while True:
    fader.update()
    if fader.color != previous:
        rgb.fill(fader.color)
        rgb.show()
        previous = fader.color

    to_sleep = random.choice(sleep)
    print(f"sleeping for {to_sleep}")
    time.sleep(to_sleep)
