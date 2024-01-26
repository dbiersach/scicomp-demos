# SPDX-FileCopyrightText: Copyright (c) Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
from gauge import gauge

# define the display
display = board.DISPLAY

# we create the gauge object
gauge = gauge(
    50,
    50,
    26,
    100,
    ticks=[10, 50, 90],
    scale_range=[0, 100],
    tick_color=0x440044,
    background_color=0x44FF44,
)

# display the gauge in the screen
display.show(gauge)


# some dummy date to show library capabilities
i = 20

# we iterate
while True:
    for a in range(5):
        gauge.update(i)
        i = i + 10
        time.sleep(0.0005)
    for a in range(5):
        gauge.update(i)
        i = i - 10
        time.sleep(0.005)
    i = 20
