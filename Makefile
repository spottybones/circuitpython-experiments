all:
	@echo Review Makefile for targets

.PHONY: run repl

run:
	cp $(SCRIPT) /Volumes/CIRCUITPY/code.py

.PHONY: pdm_microphone.py
pdm_microphone.py:
	cp pdm_microphone.py /Volumes/CIRCUITPY/code.py

.PHONY: wifi.py
wifi.py:
	cp wifi.py /Volumes/CIRCUITPY/code.py
	cp secrets.py /Volumes/CIRCUITPY/

repl:
	@exec screen /dev/tty.usb* 115200
