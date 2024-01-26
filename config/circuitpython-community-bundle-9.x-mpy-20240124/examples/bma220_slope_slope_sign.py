# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from bma220 import bma220_slope
from bma220 import bma220_const as bma220

i2c = board.I2C()
bma = bma220_slope.BMA220_SLOPE(i2c)

bma.latched_mode = bma220.LATCH_FOR_1S
bma.slope_x_enabled = bma220_slope.SLOPE_X_ENABLED
bma.slope_y_enabled = bma220_slope.SLOPE_Y_ENABLED
bma.slope_z_enabled = bma220_slope.SLOPE_Z_ENABLED
bma.slope_sign = bma220_slope.SLOPE_SIGN_NEGATIVE
bma.slope_threshold = 8

bma.slope_sign = bma220_slope.SLOPE_SIGN_NEGATIVE

while True:
    for slope_sign in bma220_slope.slope_sign_values:
        print("Current Slope sign setting: ", bma.slope_sign)
        for _ in range(10):
            print("Slope Interrupt Triggered:", bma.slope_interrupt)
            infox, infoy, infoz = bma.slope_interrupt_info
            print("Slope First interrupt x:{} y:{} z:{}".format(infox, infoy, infoz))
            time.sleep(0.5)
        bma.slope_sign = slope_sign
