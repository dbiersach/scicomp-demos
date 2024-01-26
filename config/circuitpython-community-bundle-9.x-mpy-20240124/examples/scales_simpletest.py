# SPDX-FileCopyrightText: Copyright (c) 2023 Jose David M.
#
# SPDX-License-Identifier: MIT
#############################
"""
This is a basic demonstration of a Scale Class.
"""

import time
import board
import displayio
from scales import Scale

display = board.DISPLAY
group = displayio.Group()

values = [56, 58, 60, 65, 63, 60, 56, 54, 53, 42, 43, 44, 45, 52, 54]

my_scale = Scale(
    x=50,
    y=220,
    length=200,
    direction="vertical",
    limits=(0, 80),
    ticks=[16, 32, 48, 64, 80],
)

group.append(my_scale)

my_scale2 = Scale(
    x=150,
    y=100,
    length=200,
    direction="horizontal",
    limits=(0, 80),
    ticks=[16, 32, 48, 64, 80],
)
group.append(my_scale2)
display.show(group)


while True:
    for val in values:
        my_scale.animate_pointer(val)
        my_scale2.animate_pointer(val)
        time.sleep(0.1)
