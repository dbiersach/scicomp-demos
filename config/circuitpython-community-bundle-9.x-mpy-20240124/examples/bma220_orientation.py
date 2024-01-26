# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from bma220 import bma220_orientation
from bma220 import bma220_const as bma220

i2c = board.I2C()
bma = bma220_orientation.BMA220_ORIENTATION(i2c)

bma.latched_mode = bma220.LATCH_FOR_1S
bma.orientation_blocking = bma220_orientation.MODE1


while True:
    for orientation_blocking in (1, 2, 3):
        print("Current Orientation blocking setting: ", bma.orientation_blocking)
        for _ in range(50):
            print("Orientation Interrupt Triggered:", bma.orientation_interrupt)
            time.sleep(0.1)
        bma.orientation_blocking = orientation_blocking
