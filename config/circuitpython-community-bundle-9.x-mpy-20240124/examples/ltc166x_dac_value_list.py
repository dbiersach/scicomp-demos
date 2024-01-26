# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Thadeus Frazier-Reed for creativecontrol
#
# SPDX-License-Identifier: Unlicense

"""
Write individual values to all DAC channels from a list.
"""

import time
import board
import creativecontrol_circuitpython_ltc166x

ltc1665 = creativecontrol_circuitpython_ltc166x.LTC1665(
    csel=board.GP1, sck=board.GP2, mosi=board.GP3, debug=True
)

dac_values = [1, 3, 7, 15, 31, 63, 127, 255]

while True:
    print("writing dac values ", time.monotonic())
    ltc1665.write_dac_values(dac_values)
    time.sleep(4)
    print("off")
    ltc1665.write_dac_values([0] * 8)
    time.sleep(4)
