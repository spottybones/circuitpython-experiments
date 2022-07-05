# CircuitPython Learning Scripts

This repo contains my copies of CircuitPython scripts that I'm
working through to learn how to program my Arduino RP2040 Nano
Connect. They are based on scripts I've worked through on Adafruit's
[CircuitPython on the Arduino Nano RP2040 Connect][1] tutorials.

## Running the Scripts

I use a Makefile that has a target for each script that copies it
over the existing `code.py` file on the mounted CIRCUITPY drive on
my Mac. I also have a target that runs `screen` to connect to the
board's REPL for serial output and debugging. I typically run this
in a separate TMUX pane and this essentially duplicates the
functionality of the recommended `mu` editor while letting me keep
my code in a Git repo and using Neovim or Vim for editing.

I have installed and use [Circup][2] for extra libaries on the board.

This project setup is working fine for what I've tried so far. YMMV!

[1]:https://learn.adafruit.com/circuitpython-on-the-arduino-nano-rp2040-connect
[2]:https://github.com/adafruit/circup
