# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import bmp581

i2c = board.I2C()  # uses board.SCL and board.SDA
bmp = bmp581.BMP581(i2c)

while True:
    print("Temperature: {:.2f}C".format(bmp.temperature))
    time.sleep(0.5)
