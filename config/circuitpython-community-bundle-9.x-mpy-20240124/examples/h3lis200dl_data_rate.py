# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import h3lis200dl

i2c = board.I2C()
h3lis = h3lis200dl.H3LIS200DL(i2c)

h3lis.data_rate = h3lis200dl.RATE_400HZ

while True:
    for data_rate in h3lis200dl.data_rate_values:
        print("Current Data rate setting: ", h3lis.data_rate)
        for _ in range(10):
            accx, accy, accz = h3lis.acceleration
            print("x:{:.2f}g, y:{:.2f}g, z:{:.2f}g".format(accx, accy, accz))
            time.sleep(0.5)
        h3lis.data_rate = data_rate
