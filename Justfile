# vim:set ft=just:

# configuration
set positional-arguments

# set some constants
BOARD_PATH := "/Volumes/CIRCUITPY"
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

# copy my simple libraries
install-my-libraries:
	@echo Updating my libraries
	@cp my_palettes.py {{BOARD_PATH}}/
	@cp my_boardcheck.py {{BOARD_PATH}}/
