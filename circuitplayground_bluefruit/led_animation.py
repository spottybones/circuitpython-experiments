import board
import neopixel
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation import color

pixel_pin = board.NEOPIXEL
num_pixels = 10

pixels = neopixel.NeoPixel(
    pixel_pin,  # pyright: ignore [reportGeneralTypeIssues]
    num_pixels,
    brightness=0.02,
    auto_write=False,
)

colorcycle = ColorCycle(pixels, speed=2, colors=color.RAINBOW)

while True:
    colorcycle.animate()
