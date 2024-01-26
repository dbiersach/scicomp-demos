# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import lps28

i2c = board.I2C()
lps = lps28.LPS28(i2c)

while True:
    for resolution in lps28.resolution_values:
        print("Current Resolution setting: ", lps.resolution)
        for _ in range(10):
            press = lps.pressure
            print("Pressure: {:.2f}hPa".format(press))
            time.sleep(0.5)
        lps.resolution = resolution
