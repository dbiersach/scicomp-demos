# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import h3lis200dl

i2c = board.I2C()
h3lis = h3lis200dl.H3LIS200DL(i2c)

h3lis.operation_mode = h3lis200dl.LOW_POWER_ODR0_5

while True:
    for operation_mode in h3lis200dl.operation_mode_values:
        print("Current Operation mode setting: ", h3lis.operation_mode)
        for _ in range(10):
            accx, accy, accz = h3lis.acceleration
            print("x:{:.2f}g, y:{:.2f}g, z:{:.2f}g".format(accx, accy, accz))
            time.sleep(0.5)
        h3lis.operation_mode = operation_mode
