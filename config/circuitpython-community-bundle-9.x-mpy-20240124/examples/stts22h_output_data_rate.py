# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import stts22h

i2c = board.I2C()
stts = stts22h.STTS22H(i2c)

stts.output_data_rate = stts22h.ODR_200_HZ

while True:
    for output_data_rate in stts22h.output_data_rate_values:
        print("Current Output data rate setting: ", stts.output_data_rate)
        for _ in range(10):
            temp = stts.temperature
            print("Temperature :{:.2f}CC".format(temp))
            time.sleep(0.5)
        stts.output_data_rate = output_data_rate
