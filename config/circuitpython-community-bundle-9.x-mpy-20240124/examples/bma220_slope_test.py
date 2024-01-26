# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from bma220 import bma220_slope
from bma220 import bma220_const as bma220

i2c = board.I2C()  # uses board.SCL and board.SDA
bma = bma220_slope.BMA220_SLOPE(i2c)

bma.latched_mode = bma220.LATCH_FOR_2S
bma.slope_x_enabled = bma220_slope.SLOPE_X_ENABLED

while True:
    print("Slope Interrupt Triggered:", bma.slope_interrupt)
    time.sleep(0.5)
