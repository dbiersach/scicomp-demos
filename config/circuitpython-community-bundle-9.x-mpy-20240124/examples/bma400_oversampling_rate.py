# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import bma400

i2c = board.I2C()
bma = bma400.BMA400(i2c)

bma.oversampling_rate = bma400.OVERSAMPLING_2

while True:
    for oversampling_rate in bma400.oversampling_rate_values:
        print("Current Oversampling rate setting: ", bma.oversampling_rate)
        for _ in range(10):
            accx, accy, accz = bma.acceleration
            print("x:{:.2f}Gs, y:{:.2f}Gs, z:{:.2f}Gs".format(accx, accy, accz))
            time.sleep(0.5)
        bma.oversampling_rate = oversampling_rate
