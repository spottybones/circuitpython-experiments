# vim:set ft=make:

# configuration
set positional-arguments

# set some constants
BOARD_PATH := "/Volumes/CIRCUITPY"

# default
_default:
	@just --list --unsorted

# update code.py on board
up FILE:
	@echo Updating code on board...
	cp {{FILE}} {{BOARD_PATH}}/code.py

# copy secrets to the board
copy-secrets:
	cp secrets.py {{BOARD_PATH}}/

# connect to the board REPL
repl:
	@exec screen /dev/tty.usb* 115200

# unmount the board before reboot or eject
unmount:
	@diskutil unmount {{BOARD_PATH}}

# install required libraries
install-libraries:
	@-circup --path {{BOARD_PATH}} install -r requirements.txt
