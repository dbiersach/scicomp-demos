# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Thadeus Frazier-Reed for creativecontrol
#
# SPDX-License-Identifier: Unlicense

"""
Example of using a DAC daisy-chain as described in the LTC166X datasheet
https://www.analog.com/media/en/technical-documentation/data-sheets/166560fa.pdf
"""

import time
import board
import creativecontrol_circuitpython_ltc166x

ltc1665 = creativecontrol_circuitpython_ltc166x.LTC1665(
    csel=board.GP1, sck=board.GP2, mosi=board.GP3, debug=True
)

dac_values = [[1, 3, 7, 15, 31, 63, 127, 255], [255, 127, 63, 31, 15, 7, 3, 1]]

while True:
    print("writing dac values ", time.monotonic())
    ltc1665.write_chained_dac_values(dac_values)
    time.sleep(4)
    print("off")
    ltc1665.write_chained_dac_values([[0] * 8, [0] * 8])
    time.sleep(4)
