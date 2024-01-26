# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import mc3479 as MC3479


i2c = board.I2C()  # uses board.SCL and board.SDA
mc3479 = MC3479.MC3479(i2c)

while True:
    accx, accy, accz = mc3479.acceleration
    print("x:{:.2f}m/s^2, y:{:.2f}m/s^2, z{:.2f}m.s^2".format(accx, accy, accz))
    time.sleep(0.5)
