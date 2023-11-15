from adafruit_led_animation.animation.sparklepulse import SparklePulse
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import (
    RED,
    YELLOW,
    ORANGE,
    GREEN,
    TEAL,
    CYAN,
    BLUE,
    PURPLE,
    MAGENTA,
)

import board
import neopixel

pixels = neopixel.NeoPixel(board.D5, 30, brightness=0.2, auto_write=False)

sparkles = [
    SparklePulse(pixels, speed=0.05, period=3, color=color)
    for color in [RED, ORANGE, YELLOW, GREEN, TEAL, CYAN, BLUE, PURPLE, MAGENTA]
]

animations = AnimationSequence(
    sparkles[0],
    sparkles[1],
    sparkles[2],
    sparkles[3],
    sparkles[4],
    sparkles[5],
    sparkles[6],
    sparkles[7],
    sparkles[8],
    advance_interval=5,
    auto_clear=False,
)

while True:
    animations.animate()
