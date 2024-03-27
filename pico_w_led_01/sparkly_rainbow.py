from adafruit_led_animation.animation.sparklepulse import SparklePulse
from adafruit_led_animation.sequence import AnimationSequence

from my_pixels import pixels
from my_colors import pride as colors

sparkles = [
    SparklePulse(pixels, speed=0.05, period=3, color=color) for color in colors[2]
]

animations = AnimationSequence(
    *sparkles,
    advance_interval=3,
    auto_clear=False,
)

while True:
    animations.animate()
