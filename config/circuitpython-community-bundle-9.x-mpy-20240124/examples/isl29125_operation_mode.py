# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import board
import isl29125


i2c = board.I2C()  # uses board.SCL and board.SDA
isl = isl29125.ISL29125(i2c)


print("Red Luminance: ", isl.red)
print("Current Operation Mode Value: ", bin(isl.operation_mode))
# Changing Operation Mode to Blue Only
isl.operation_mode = isl29125.BLUE_ONLY
print("Changed Operation mode to Blue Only:", bin(isl.operation_mode))
print("Red Luminance after change: ", isl.red)
