# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Thadeus Frazier-Reed for creativecontrol
#
# SPDX-License-Identifier: Unlicense

"""
Write a value to a single DAC channel.
"""

import time
import board
import creativecontrol_circuitpython_ltc166x

ltc1665 = creativecontrol_circuitpython_ltc166x.LTC1665(
    csel=board.GP1, sck=board.GP2, mosi=board.GP3, debug=True
)

dac = ltc1665.DAC_A
dac_value = 127

while True:
    print("writing dac value ", time.monotonic())
    ltc1665.write_dac_value(dac_value, dac)
    time.sleep(4)
    print("off")
    ltc1665.write_dac_value(0, dac)
    time.sleep(4)
