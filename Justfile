# vim:set ft=just:

# set some constants
BOARD_PATH := "/Volumes/CIRCUITPY"
# BOARD_PATH := "/Volumes/RPI-RP2"
BOARD_ID := `awk -F: '$1=="Board ID"{print $2}' /Volumes/CIRCUITPY/boot_out.txt | tr -d '\r\n'`
PWD := invocation_directory()

# default
_default:
	@echo BOARD_ID: {{BOARD_ID}}
	@just --list --unsorted

# update code.py on board
up FILE:
	@echo Updating code on board...
	@cp {{PWD}}/{{FILE}} {{BOARD_PATH}}/code.py

# push code to board
push:
  echo Pushing code to board...
  cp {{PWD}}/*.py {{BOARD_PATH}}/
  if test -f {{PWD}}/settings.toml; then cp {{PWD}}/settings.toml {{BOARD_PATH}}/; fi

# copy secrets to the board
copy-secrets:
	cp {{PWD}}/settings.toml {{BOARD_PATH}}/

# connect to the board REPL
repl:
	@exec tio -b 115200 /dev/tty.usb*

# unmount the board before reboot or eject
unmount:
	@diskutil unmount {{BOARD_PATH}}

# install required libraries via circup
install-libraries:
	@-circup --path {{BOARD_PATH}} install -r {{PWD}}/requirements.txt

# copy my simple libraries
install-my-libraries:
	@echo Updating my libraries
	@cp {{PWD}}/my_*.py {{BOARD_PATH}}/

# per https://learn.adafruit.com/welcome-to-circuitpython/troubleshooting#macos-sonoma-14-dot-x-disk-errors-writing-to-circuitpy-3160304
# remount {{BOARD_PATH}} for MacOS Sonoma
remount-board:
	#!/bin/bash
	DISKY=$(df | grep {{BOARD_PATH}} | cut -d" " -f1)
	sudo diskutil unmount {{BOARD_PATH}}
	sudo mkdir {{BOARD_PATH}}
	sleep 2
	sudo mount -v -o noasync -t msdos "${DISKY}" {{BOARD_PATH}}
