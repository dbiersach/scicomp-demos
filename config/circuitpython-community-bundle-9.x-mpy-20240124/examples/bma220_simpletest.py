# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from bma220 import bma220

i2c = board.I2C()  # uses board.SCL and board.SDA
bma = bma220.BMA220(i2c)

while True:
    accx, accy, accz = bma.acceleration
    print("x:{:.2f}g, y:{:.2f}g, z:{:.2f}g".format(accx, accy, accz))
    time.sleep(0.1)
