# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import bma400

i2c = board.I2C()
bma = bma400.BMA400(i2c)

bma.acc_range = bma400.ACC_RANGE_16

while True:
    for acc_range in bma400.acc_range_values:
        print("Current Acc range setting: ", bma.acc_range)
        for _ in range(10):
            accx, accy, accz = bma.acceleration
            print("x:{:.2f}Gs, y:{:.2f}Gs, z:{:.2f}Gs".format(accx, accy, accz))
            time.sleep(0.5)
        bma.acc_range = acc_range
