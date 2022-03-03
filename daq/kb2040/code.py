# BNL SciComp Demonstrations
# Data Accquisition (DAQ) Board Controller
# Uses Adafruit CircuitPython runtime & libraries
# Designed for the Adafruit KB2040 Board


import board
import digitalio
import neopixel
import busio
import time
import supervisor
import countio
import sys

# Initialize the on-board (built-in) NeoPixel
pixel_builtin = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel_builtin.brightness = 0.4
pixel_builtin.fill((0, 0, 0))


def run_geiger_counter():
    pixel_builtin.fill((0, 255, 0))
    pin_signal = countio.Counter(board.D9, edge=countio.Edge.FALL)
    # Count decay events over 30 second period
    time.sleep(30)
    sys.stdout.write(f"{pin_signal.count}\n")
    pin_signal.deinit()
    pixel_builtin.fill((0, 0, 0))


while True:
    if supervisor.runtime.serial_bytes_available:
        cmd = sys.stdin.readline().strip()

        if cmd == "run_geiger_counter":
            run_geiger_counter()

