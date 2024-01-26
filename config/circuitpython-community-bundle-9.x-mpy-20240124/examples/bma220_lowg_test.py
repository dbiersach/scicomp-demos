# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from bma220 import bma220_lowg_detection
from bma220 import bma220_const as bma220

i2c = board.I2C()
bma = bma220_lowg_detection.BMA220_LOWG_DETECTION(i2c)

bma.latched_mode = bma220.LATCH_FOR_1S

while True:
    print("Low G Interrupt Triggered:", bma.lowg_interrupt)
    time.sleep(0.5)
