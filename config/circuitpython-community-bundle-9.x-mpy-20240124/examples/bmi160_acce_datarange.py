# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import bmi160 as BMI160


i2c = board.I2C()  # uses board.SCL and board.SDA
bmi = BMI160.BMI160(i2c)

bmi.acceleration_range = BMI160.ACCEL_RANGE_4G

while True:
    for data_range in BMI160.acc_range_values:
        print("Current Acceleration Data Rate: ", bmi.acceleration_range)
        for _ in range(10):
            accx, accy, accz = bmi.acceleration
            print("x:{:.2f}m/s2, y:{:.2f}m/s2, z{:.2f}m/s2".format(accx, accy, accz))
            time.sleep(0.5)
        bmi.acceleration_range = data_range
