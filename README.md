# CircuitPython Learning Scripts

This project repository contains my copies of CircuitPython scripts
that I'm working through to learn how to program the different
development boards that I've purchased. I started with scripts I've
worked from Adafruit's [CircuitPython on the Arduino Nano RP2040
Connect][1] tutorials.

I've acquired additional boards to use for learning and have
reorganized the project to use subdirectores to hold code and library
configurations for each board. These subdirs are named from the
board.board_id of the target board.

## Running the Scripts

I use [`just`][2] as a command runner to work with the boards. See
the comments in the `Justfile` in the root directory of the project
to see what the recipes do. I run `just` recipes from my editor or
a separate TMUX pane and this essentially provides most the
functionality of the recommended `mu` editor while letting me keep
my code in a Git repo and using Neovim or Vim for editing. My goal
is only have one `Justfile` in the project root that will work in
any of the board subdirectores.

I have also installed and use [Circup][1] for extra libaries on the
board.

This project setup is working fine for what I've tried so far. YMMV!

[1]:https://learn.adafruit.com/circuitpython-on-the-arduino-nano-rp2040-connect
[2]:https://github.com/casey/justt
[3]:https://github.com/adafruit/circup
