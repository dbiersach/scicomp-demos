# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import h3lis200dl

i2c = board.I2C()  # uses board.SCL and board.SDA
h3lis = h3lis200dl.H3LIS200DL(i2c)

h3lis.interrupt1_threshold = 2  # roughly 1.5 gs
h3lis.interrupt1_duration = 127  # Latch for 127 steps
h3lis.interrupt1_configuration = 42  # 0b101010 See Datasheet for options
h3lis.interrupt1_latched = 1  # 1 for True interrupt 1

while True:
    accx, accy, accz = h3lis.acceleration
    print("x:{:.2f}g, y:{:.2f}g, z:{:.2f}g".format(accx, accy, accz))
    print(h3lis.interrupt1_source_register)
    time.sleep(1)
