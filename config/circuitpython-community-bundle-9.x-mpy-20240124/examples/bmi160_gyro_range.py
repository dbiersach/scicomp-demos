# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import bmi160 as BMI160


i2c = board.I2C()  # uses board.SCL and board.SDA
bmi = BMI160.BMI160(i2c)

bmi.gyro_range = BMI160.GYRO_RANGE_500

while True:
    for data_range in BMI160.gyro_values:
        print("Current Gyro Data Range: ", bmi.gyro_range)
        for _ in range(10):
            gyrox, gyroy, gyroz = bmi.gyro
            print("x:{:.2f}°/s, y:{:.2f}°/s, z{:.2f}°/s".format(gyrox, gyroy, gyroz))
            time.sleep(0.5)
        bmi.gyro_range = data_range
