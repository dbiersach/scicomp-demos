# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Thadeus Frazier-Reed for creativecontrol
#
# SPDX-License-Identifier: Unlicense

"""
Write a value to a single DAC channel ramping from min to max and back.
"""

import time
import board
import creativecontrol_circuitpython_ltc166x

ltc1665 = creativecontrol_circuitpython_ltc166x.LTC1665(
    csel=board.GP1, sck=board.GP2, mosi=board.GP3, debug=True
)

dac = ltc1665.DAC_A
dac_value = 0
direction = 1

while True:
    print("writing dac value ", time.monotonic())
    ltc1665.write_dac_value(dac_value, dac)
    time.sleep(0.01)
    dac_value += 1 * direction
    if 0 >= dac_value or dac_value >= ltc1665.get_device_range() - 1:
        direction *= -1
