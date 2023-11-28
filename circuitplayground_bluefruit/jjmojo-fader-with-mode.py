# SPDX-FileCopyrightText: 2023 Scott Burns
# SPDX-License-Identifier: MIT
# SPDX-Filename: jjmojo-fader-with-mode.py

import board
import neopixel
import time
from digitalio import DigitalInOut, Direction, Pull
from my_palettes import pride, green_to_off

rgb = neopixel.NeoPixel(
    board.NEOPIXEL,  # pyright: ignore [reportGeneralTypeIssues]
    10,
    brightness=0.2,
    auto_write=False,
)


class Button:
    _debounce = 0.1

    def __init__(self, pin, name, onrelease) -> None:
        self.name = name
        self.checkin = time.monotonic()
        self.state = False
        self.onrelease = onrelease
        self.input = DigitalInOut(pin)
        self.input.direction = Direction.INPUT
        self.input.pull = Pull.DOWN

    def press(self):
        print(self.name, "pressed")

    def release(self):
        print(self.name, "released")
        self.onrelease()

    def check(self):
        return self.input.value

    def update(self):
        if time.monotonic() - self.checkin > self._debounce:
            if self.state and not self.check():
                self.release()

            if not self.state and self.check():
                self.press()

            self.state = self.check()

            self.checkin = time.monotonic()


class Fader:
    def __init__(self, palette: tuple[int, ...], interval: float = 0.1) -> None:
        self.checkin = time.monotonic()
        self.color = 0
        self.interval = interval
        self.palette = palette
        self.max = len(self.palette) * interval
        self.epoch = 0
        self.index = 0

    def update(self):
        self.epoch = time.monotonic() - self.checkin

        self.index = round((self.epoch % self.max) / self.interval)

        if self.index > len(self.palette) - 1:
            self.index = 0
            self.checkin = time.monotonic()

        self.color = self.palette[self.index]


class ModeFader(Fader):
    def __init__(self, palette: tuple[int, ...], interval: float = 0.1) -> None:
        self.on = True
        Fader.__init__(self, palette, interval)

    def update(self):
        if not self.on:
            self.color = 0
            return

        Fader.update(self)


class AutoOffFader(ModeFader):
    def reset(self):
        self.epoch = 0
        self.checkin = time.monotonic()
        self.on = True
        self.index = 0

    def update(self):
        ModeFader.update(self)
        if self.on and self.index == len(self.palette) - 1:
            self.on = False


auto_off = AutoOffFader(green_to_off, 0.05)
runner = ModeFader(pride, 0.1)


def fire_auto():
    runner.on = False
    auto_off.reset()


def cycle_toggle():
    auto_off.on = False
    runner.on = not runner.on


button1 = Button(board.D4, "a", fire_auto)
button2 = Button(board.D5, "b", cycle_toggle)

previous = None
fader = auto_off

while True:
    if auto_off.on:
        fader = auto_off
    if runner.on:
        fader = runner

    button1.update()
    button2.update()
    fader.update()

    if fader.color != previous:
        rgb.fill(fader.color)
        rgb.show()
        previous = fader.color
