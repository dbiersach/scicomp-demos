# ----------------------------------------------------------------------------
# simple_test.py: Usage example with AHT20 temperature sensor
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
import adafruit_ahtx0

# config (Pico)
i2c = board.STEMMA_I2C()
PIN_RST = board.GP16
PIN_BUSY = board.GP17
INTERVAL = 20

# main program   -------------------------------------------------------------

display = SegmentDisplay(i2c, rst_pin=PIN_RST, busy_pin=PIN_BUSY)
display.init()
display.update_mode(full=False)
display.clear()

aht20 = adafruit_ahtx0.AHTx0(i2c)

while True:
    t, h = aht20.temperature, aht20.relative_humidity
    print(f"{t=}, {h=}")
    display.set_temperature(t)
    display.set_humidity(h)
    display.update()
    time.sleep(INTERVAL)
