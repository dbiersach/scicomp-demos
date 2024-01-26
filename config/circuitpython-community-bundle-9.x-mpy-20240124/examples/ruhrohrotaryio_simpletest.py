# SPDX-FileCopyrightText: Copyright (c) 2023 Tod Kurt
#
# SPDX-License-Identifier: Unlicense

import os
import time
import board

# works on both QTPY M0 and QTPY RP2040

if os.uname().machine.find("rp2040") > 0:  # RP2040
    from ruhrohrotaryio import IncrementalEncoder
else:
    from rotaryio import IncrementalEncoder

encoder = IncrementalEncoder(board.A3, board.A1)

while True:
    print(encoder.position)
    time.sleep(0.1)
