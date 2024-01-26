# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import h3lis200dl

i2c = board.I2C()
h3lis = h3lis200dl.H3LIS200DL(i2c)

h3lis.full_scale_selection = h3lis200dl.SCALE_100G

while True:
    for full_scale_selection in h3lis200dl.full_scale_selection_values:
        print("Current Full scale selection setting: ", h3lis.full_scale_selection)
        for _ in range(10):
            accx, accy, accz = h3lis.acceleration
            print("x:{:.2f}g, y:{:.2f}g, z:{:.2f}g".format(accx, accy, accz))
            time.sleep(0.5)
        h3lis.full_scale_selection = full_scale_selection
