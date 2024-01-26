# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import lps28

i2c = board.I2C()
lps = lps28.LPS28(i2c)

while True:
    for data_rate in lps28.data_rate_values:
        print("Current Data rate setting: ", lps.data_rate)
        for _ in range(10):
            press = lps.pressure
            print("Pressure: {:.2f}hPa".format(press))
            time.sleep(0.5)
        lps.data_rate = data_rate
