# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import h3lis200dl

i2c = board.I2C()  # uses board.SCL and board.SDA
h3lis = h3lis200dl.H3LIS200DL(i2c)

while True:
    accx, accy, accz = h3lis.acceleration
    print("x:{:.2f}m/s2, y:{:.2f}m/s2, z{:.2f}m/s2".format(accx, accy, accz))
    time.sleep(0.5)
