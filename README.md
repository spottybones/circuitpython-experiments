# CircuitPython Learning Scripts

This project repository contains [CircuitPython][1] scripts that
I'm using to learn how to program several microcontroller development
boards that I've purchased.

My first CircuitPython-supported board was the Arduino Nano RP2040
Connect. I started this project by working through scripts from
Adafruit's [CircuitPython on the Arduino Nano RP2040 Connect][2]
tutorials.

I've since added the following boards to my collection:

 * Pimoroni Tiny2040
 * Adafruit CircuitPlayground Bluefruit
 * Adafruit Feather ESP32-S3 4MB Flash 2MB PSRAM

I've organized the project to use subdirectores to hold code and library
configurations for each of these boards. These subdirs are named from the
board.board_id of the target board.

## Running the Scripts

I use [`just`][3] as a command runner to work with the boards. The
project uses one `Justfile` in the project root directory. See the
comments in that file for the different recipes provided. I run the
recipes from my editor, or a separate TMUX pane. This provides most
the functionality of the recommended `mu` editor while letting me
keep my code in a Git repo and using my preferred editors (Neovim
or Vim.)

I use [Circup][4] for managing extra libaries on the boards.

This project setup is working fine for me so far. YMMV!

[1]:https://circuitpython.org
[2]:https://learn.adafruit.com/circuitpython-on-the-arduino-nano-rp2040-connect
[3]:https://github.com/casey/just
[4]:https://github.com/adafruit/circup
