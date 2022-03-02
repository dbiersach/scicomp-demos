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


pixel_builtin = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel_builtin.brightness = 0.4
pixel_builtin.fill((0, 0, 0))


def run_geiger_counter():
    pixel_builtin.fill((0, 255, 0))
    pin_signal = countio.Counter(board.D9, edge=countio.Edge.FALL)
    time.sleep(3)
    print(f"{pin_signal.count}")
    pin_signal.deinit()
    pixel_builtin.fill((0, 0, 0))


while True:
    if supervisor.runtime.serial_bytes_available:
        cmd = input().strip()
        if cmd == "":
            continue
        if cmd == "r":
            # if cmd == "run_geiger_counter":
            run_geiger_counter()
