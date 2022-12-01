# vim:set ft=make:

# configuration
set positional-arguments

# set some constants
BOARD_PATH := "/Volumes/CIRCUITPY"
PWD := invocation_directory()

# default
_default:
	@just --list --unsorted

# update code.py on board
up FILE:
	@echo Updating code on board...
	@cp {{PWD}}/{{FILE}} {{BOARD_PATH}}/code.py

# copy secrets to the board
copy-secrets:
	cp {{PWD}}/secrets.py {{BOARD_PATH}}/

# connect to the board REPL
repl:
	@exec screen /dev/tty.usb* 115200

# unmount the board before reboot or eject
unmount:
	@diskutil unmount {{BOARD_PATH}}

# install required libraries via circup
install-libraries:
	@-circup --path {{BOARD_PATH}} install -r {{PWD}}/requirements.txt
