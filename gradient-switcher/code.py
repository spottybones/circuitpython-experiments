# SPDX-FileCopyrightText: 2023 Scott Burns
# SPDX-License-Identifier: MIT
# SPDX-Filename: gradient-switcher.py

import board
import neopixel

# import time
from my_lib.button import Button, Switch
from my_lib.colors import halloween, ireland, pride
from my_lib.fader import Fader

rgb = neopixel.NeoPixel(
    board.NEOPIXEL,  # pyright: ignore[reportArgumentType]
    10,
    brightness=1.0,
    auto_write=False,
)


class State:
    def __init__(self) -> None:
        self.button_a = Button(board.D4, "A", None, self.change)
        self.button_b = Button(board.D5, "B", None, self.dim)
        self.switch = Switch(board.D7, "S", self.on, self.off)

        self.switch.update()
        self.enabled = self.switch.state

        self.color = 0

        self.previous = 0

        self.gradients = (
            ireland,
            pride,
            halloween,
        )

        self.level = len(self.gradients[0]) - 1

        self.fader = Fader(self.gradient, 0.1)

    @property
    def gradient(self):
        return self.gradients[self.color][self.level]

    def on(self):
        self.enabled = True

    def off(self):
        self.enabled = False

    def change(self):
        self.color += 1
        if self.color > len(self.gradients) - 1:
            self.color = 0

        self.fader.palette = self.gradient

    def dim(self):
        self.level -= 1
        if self.level < 0:
            self.level = len(self.gradients[0]) - 1

        self.fader.palette = self.gradient

    def update(self):
        self.button_a.update()
        self.button_b.update()
        self.switch.update()
        self.fader.update()

        if not self.enabled:
            rgb.fill(0)
            rgb.show()
        elif self.fader.color != self.previous:
            rgb.fill(self.fader.color)
            rgb.show()
            self.previous = self.fader.color


state = State()
rgb.fill(0)
rgb.show()
while True:
    state.update()
