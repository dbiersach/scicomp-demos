# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import bma400

i2c = board.I2C()
bma = bma400.BMA400(i2c)

bma.power_mode = bma400.LOW_POWER_MODE

while True:
    for power_mode in bma400.power_mode_values:
        print("Current Power mode setting: ", bma.power_mode)
        for _ in range(10):
            accx, accy, accz = bma.acceleration
            print("x:{:.2f}Gs, y:{:.2f}Gs, z:{:.2f}Gs".format(accx, accy, accz))
            time.sleep(0.5)
        bma.power_mode = power_mode
