# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import h3lis200dl

i2c = board.I2C()
h3lis = h3lis200dl.H3LIS200DL(i2c)

h3lis.high_pass_filter_cutoff = h3lis200dl.HPCF32

while True:
    for high_pass_filter_cutoff in h3lis200dl.high_pass_filter_cutoff_values:
        print(
            "Current High pass filter cutoff setting: ", h3lis.high_pass_filter_cutoff
        )
        for _ in range(10):
            accx, accy, accz = h3lis.acceleration
            print("x:{:.2f}g, y:{:.2f}g, z:{:.2f}g".format(accx, accy, accz))
            time.sleep(0.5)
        h3lis.high_pass_filter_cutoff = high_pass_filter_cutoff
