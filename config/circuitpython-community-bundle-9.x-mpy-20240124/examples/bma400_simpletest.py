# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import bma400

i2c = board.I2C()  # uses board.SCL and board.SDA
bma = bma400.BMA400(i2c)

while True:
    accx, accy, accz = bma.acceleration
    print("x:{:.2f}G y:{:.2f}G z:{:.2f}G".format(accx, accy, accz))
    time.sleep(0.5)
