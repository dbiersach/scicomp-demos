# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import bma400

i2c = board.I2C()
bma = bma400.BMA400(i2c)

bma.source_data_registers = bma400.ACC_FILT_LP

while True:
    for source_data_registers in bma400.source_data_registers_values:
        print("Current Source data registers setting: ", bma.source_data_registers)
        for _ in range(10):
            accx, accy, accz = bma.acceleration
            print("x:{:.2f}Gs, y:{:.2f}Gs, z:{:.2f}Gs".format(accx, accy, accz))
            time.sleep(0.5)
        bma.source_data_registers = source_data_registers
