# SPDX-FileCopyrightText: Copyright (c) 2023 Tod Kurt
#
# SPDX-License-Identifier: Unlicense

import time
import board

# works on any board
encoder = None
try:
    import rotaryio

    encoder = rotaryio.IncrementalEncoder(board.A3, board.A1)
except (RuntimeError, ImportError):
    print("ruhroh")
    import ruhrohrotaryio as rotaryio

    encoder = rotaryio.IncrementalEncoder(board.A3, board.A1)

while True:
    print(encoder.position)
    time.sleep(0.1)
