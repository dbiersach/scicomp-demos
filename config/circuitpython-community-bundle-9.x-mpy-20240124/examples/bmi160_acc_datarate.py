# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import bmi160 as BMI160


i2c = board.I2C()  # uses board.SCL and board.SDA
bmi = BMI160.BMI160(i2c)

bmi.acceleration_output_data_rate = BMI160.BANDWIDTH_25_32

while True:
    for data_rate in BMI160.bandwidth_values:
        print("Current Acceleration Data Rate: ", bmi.acceleration_output_data_rate)
        for _ in range(10):
            accx, accy, accz = bmi.acceleration
            print("x:{:.2f}m/s2, y:{:.2f}m/s2, z{:.2f}m/s2".format(accx, accy, accz))
            time.sleep(0.5)
        bmi.acceleration_output_data_rate = data_rate
