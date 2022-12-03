# CircuitPython Learning Scripts

This project repository contains scripts for exploring how to
program several different microcontroller development boards using
[CircuitPython][1].

The following boards are supported:

 * Arduino Nano RP2040 Connect
 * Pimoroni Tiny2040
 * Adafruit CircuitPlayground Bluefruit
 * Adafruit Feather ESP32-S3 4MB Flash 2MB PSRAM

The project is organized into subdirectores to hold the code and
library configurations for each board. These subdirs are named
from the board.board_id of the target board.

## Running the Scripts

I use [`just`][3] as a command runner to work with the boards. The
project uses one `Justfile` in the project root directory. See the
comments in that file for the different recipes provided. The recipes
can be run from the editor or a separate TMUX pane. This provides
most of the functionality of the recommended `mu` editor while
enabling storing the code in a Git repo and using other editors
(e.g.: Neovim, Vim) for editing.

[Circup][4] is used for managing extra libaries on the boards.

This project setup is working fine for me so far. YMMV!

[1]:https://circuitpython.org
[2]:https://learn.adafruit.com/circuitpython-on-the-arduino-nano-rp2040-connect
[3]:https://github.com/casey/just
[4]:https://github.com/adafruit/circup
