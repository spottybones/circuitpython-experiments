from my_boardcheck import check_board

check_board("circuitplayground_bluefruit")

from adafruit_circuitplayground.bluefruit import cpb
import adafruit_fancyled.adafruit_fancyled as fancy
from my_palettes import my_palettes

cpb.pixels.auto_write = False  # update only when we say
cpb.pixels.brightness = 0.25  # make less blinding

palette = my_palettes.get("rainbow6", [0xFFFFFF])

offset = 0  # position offset into palette to make it "spin"
levels = (0.25, 0.3, 0.15)

while True:
    for i in range(10):
        color = fancy.palette_lookup(palette, offset + i / 9)
        color = fancy.gamma_adjust(color, brightness=levels)
        cpb.pixels[i] = color.pack()
    cpb.pixels.show()

    offset += 0.005  # bigger number = fast spin
