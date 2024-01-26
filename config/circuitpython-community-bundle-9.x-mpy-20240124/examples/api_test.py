# ----------------------------------------------------------------------------
# api_test.py: library functions
#
# Author: Bernhard Bablok
# License: GPL3
#
# Website: https://github.com/bablokb/circuitpython-segment-display
#
# ----------------------------------------------------------------------------

import time
import board
from e_ink_seg_display import SegmentDisplay

# config (Blinka-board)
# i2c = board.I2C()
# PIN_RST = board.D27
# PIN_BUSY = board.D17

# config (Pico)
i2c = board.STEMMA_I2C()
PIN_RST = board.GP16
PIN_BUSY = board.GP17

# test value-range
VALUES = [-123.4, -56.7, -8.95, -8.9, 0.0, 2.2, 2.25, 34.5, 167.8, 234.5]
DELAY = 3

# --- tests   ----------------------------------------------------------------


def test_temp():
    print("temperature...")
    for val in VALUES:
        print(f"... {val}°C ...")
        display.set_temperature(val)
        display.update()
        time.sleep(DELAY)


def test_hum():
    print("humidity...")
    for val in VALUES:
        print(f"... {val}% ...")
        display.set_humidity(val)
        display.update()
        time.sleep(DELAY)


def test_clear():
    print("clear")
    display.clear()
    time.sleep(DELAY)


def test_clean():
    print("clean")
    display.clean()
    time.sleep(DELAY)


def test_normal():
    print("set temperature to 96.5°F")
    display.set_unit(SegmentDisplay.DEG_F)
    display.set_temperature(96.5)
    print("set humidity to 55.0%")
    display.set_humidity(55.0)
    display.update()
    time.sleep(DELAY)


def test_bluetooth():
    print("toggle BT-symbol")
    print("on...")
    display.show_bluetooth(True)
    display.update()
    time.sleep(DELAY)
    print("off...")
    display.show_bluetooth(False)
    display.update()
    time.sleep(DELAY)


def test_power():
    print("toggle power-symbol")
    print("on...")
    display.show_power(True)
    display.update()
    time.sleep(DELAY)
    print("off...")
    display.show_power(False)
    display.update()
    time.sleep(DELAY)


def test_sleep():
    print("sleep")
    display.sleep()


# main program   -------------------------------------------------------------

display = SegmentDisplay(i2c, rst_pin=PIN_RST, busy_pin=PIN_BUSY)
display.init()
display.update_mode(full=False)

test_temp()
test_hum()
test_clear()
test_normal()
test_bluetooth()
test_power()
test_clean()
test_sleep()
