all:
	@echo Review Makefile for targets

.PHONY: run repl

run:
	cp $(SCRIPT) /Volumes/CIRCUITPY/code.py

repl:
	@exec screen /dev/tty.usb* 115200
