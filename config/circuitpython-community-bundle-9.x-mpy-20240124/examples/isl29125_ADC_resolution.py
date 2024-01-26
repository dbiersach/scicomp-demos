# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import isl29125


i2c = board.I2C()  # uses board.SCL and board.SDA
isl = isl29125.ISL29125(i2c)

print("Current Sensing Range Value: ", bin(isl.adc_resolution))
isl.sensing_range = isl29125.RES_16BITS
print("Changed ADC Resolution to 16 BITS:", bin(isl.adc_resolution))
red, green, blue = isl.colors
print("Red Luminance: ", red)
print("Green Luminance: ", green)
print("Blue Luminance:", blue)
time.sleep(1)

isl.sensing_range = isl29125.RES_12BITS
print("Changed ADC Resolution to 12 BITS:", bin(isl.adc_resolution))
red, green, blue = isl.colors
print("Red Luminance: ", red)
print("Green Luminance: ", green)
print("Blue Luminance:", blue)
time.sleep(1)
