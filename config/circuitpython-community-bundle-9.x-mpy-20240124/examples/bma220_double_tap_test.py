# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from bma220 import bma220_tap_sensing
from bma220 import bma220_const as bma220

i2c = board.I2C()
bma = bma220_tap_sensing.BMA220_TAP(i2c)

bma.latched_mode = bma220.LATCH_FOR_1S
bma.tt_x_enabled = bma220_tap_sensing.TT_X_ENABLED
bma.tt_y_enabled = bma220_tap_sensing.TT_Y_ENABLED
bma.tt_z_enabled = bma220_tap_sensing.TT_Z_ENABLED
bma.tt_duration = bma220_tap_sensing.TIME_500MS

while True:
    print("Double Tap Interrupt Triggered:", bma.tt_interrupt)
    time.sleep(0.5)
