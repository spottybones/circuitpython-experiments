import adafruit_fancyled.adafruit_fancyled as fancy

my_palettes = {
    "fire": [
        0xFFFFFF,  # white
        fancy.CHSV(1 / 6),  # yellow
        fancy.CRGB(255, 0, 0),  # pyright: ignore [reportGeneralTypeIssues)]
    ],
    "water": [
        fancy.CHSV(-2 / 3),  # greeen
        fancy.CHSV(-1 / 3),  # blue
        fancy.CHSV(-1 / 6),  # purple
    ],
    "rgb": [
        fancy.CHSV(-0 / 6),  # red
        fancy.CHSV(-4 / 6),  # green
        fancy.CHSV(-2 / 6),  # blue
    ],
    "cym": [
        fancy.CHSV(-3 / 6),  # cyan
        fancy.CHSV(-5 / 6),  # yellow
        fancy.CHSV(-1 / 6),  # magenta
    ],
    "rainbow6": [
        fancy.CHSV(-0 / 6),  # red
        fancy.CHSV(-1 / 6),  # magenta
        fancy.CHSV(-2 / 6),  # blue
        fancy.CHSV(-3 / 6),  # cyan
        fancy.CHSV(-4 / 6),  # green
        fancy.CHSV(-5 / 6),  # yellow
    ],
    "rainbow12": [
        fancy.CHSV(-0 / 12),  # red
        fancy.CHSV(-1 / 12),
        fancy.CHSV(-2 / 12),  # magenta
        fancy.CHSV(-3 / 12),
        fancy.CHSV(-4 / 12),  # blue
        fancy.CHSV(-5 / 12),
        fancy.CHSV(-6 / 12),  # cyan
        fancy.CHSV(-7 / 12),
        fancy.CHSV(-8 / 12),  # green
        fancy.CHSV(-9 / 12),
        fancy.CHSV(-10 / 6),  # yellow
        fancy.CHSV(-11 / 6),
    ],
}

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
