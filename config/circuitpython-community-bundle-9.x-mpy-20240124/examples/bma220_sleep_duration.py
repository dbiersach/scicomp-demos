# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from bma220 import bma220

i2c = board.I2C()
bma = bma220.BMA220(i2c)

bma.sleep_duration = bma220.SLEEP_10MS

while True:
    for sleep_duration in bma220.sleep_duration_values:
        print("Current Sleep duration setting: ", bma.sleep_duration)
        for _ in range(10):
            accx, accy, accz = bma.acceleration
            print("x:{:.2f}g, y:{:.2f}g, z:{:.2f}g".format(accx, accy, accz))
            time.sleep(0.5)
        bma.sleep_duration = sleep_duration
