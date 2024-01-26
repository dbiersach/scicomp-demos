# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import lps28

i2c = board.I2C()
lps = lps28.LPS28(i2c)

while True:
    print("Pressure: {:.2f}hPa".format(lps.pressure))
    time.sleep(0.5)
