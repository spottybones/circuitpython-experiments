from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.sparklepulse import SparklePulse
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import JADE, AMBER

import board
import neopixel

pixels = neopixel.NeoPixel(board.D5, 30, brightness=0.2, auto_write=False)

sparkle = Sparkle(pixels, speed=0.05, color=AMBER, num_sparkles=10)
sparkle_pulse = SparklePulse(pixels, speed=0.05, period=3, color=JADE)

animations = AnimationSequence(
    sparkle, sparkle_pulse, advance_interval=5, auto_clear=False
)

while True:
    animations.animate()
