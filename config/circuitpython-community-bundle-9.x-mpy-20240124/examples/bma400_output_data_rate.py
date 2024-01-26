# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import bma400

i2c = board.I2C()
bma = bma400.BMA400(i2c)

bma.output_data_rate = bma400.ACCEL_50HZ

while True:
    for output_data_rate in bma400.output_data_rate_values:
        print("Current Output data rate setting: ", bma.output_data_rate)
        for _ in range(10):
            accx, accy, accz = bma.acceleration
            print("x:{:.2f}Gs, y:{:.2f}Gs, z:{:.2f}Gs".format(accx, accy, accz))
            time.sleep(0.5)
        bma.output_data_rate = output_data_rate
