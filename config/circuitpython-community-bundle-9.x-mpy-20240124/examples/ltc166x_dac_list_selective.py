# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Thadeus Frazier-Reed for creativecontrol
#
# SPDX-License-Identifier: Unlicense

"""
Write random values to all DAC channels from a list. Only update value if it has changed.
"""

import random
import time
import board
import creativecontrol_circuitpython_ltc166x

ltc1665 = creativecontrol_circuitpython_ltc166x.LTC1665(
    csel=board.GP1, sck=board.GP2, mosi=board.GP3, debug=True
)

dac_values = [1, 3, 7, 15, 31, 63, 127, 255]
last_values = []

while True:
    print("writing dac values ", time.monotonic())
    ltc1665.write_dac_values(dac_values)
    time.sleep(4)
    print("off")
    ltc1665.write_dac_values([0] * 8)
    time.sleep(4)
    last_values = dac_values.copy()
    for index, _ in enumerate(dac_values):
        dac_values[index] = random.randint(0, ltc1665.get_device_range() - 1)
        if dac_values[index] == last_values[index]:
            dac_values[index] = -1
