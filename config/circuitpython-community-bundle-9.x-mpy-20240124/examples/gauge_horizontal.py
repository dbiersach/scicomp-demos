# SPDX-FileCopyrightText: Copyright (c) Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import displayio
import board
from gauge import gauge


display = board.DISPLAY

group = displayio.Group()
palette = displayio.Palette(3)
x0 = 5
y0 = 5
points = [(x0, y0), (100, 20), (20, 20), (20, 100)]
palette[0] = 0xFF0000
palette[1] = 0x00FF00
palette[2] = 0x0000FF


gauge1 = gauge(
    20,
    15,
    28,
    100,
    ticks=[10, 50, 90],
    scale_range=[0, 100],
    tick_color=0x0000FF,
    background_color=(0, 3, 39),
    show_text=True,
)

gauge1.set_threshold(value=50, color=0xFF0000)

group.append(gauge1)


gauge2 = gauge(
    60,
    80,
    28,
    100,
    ticks=[10, 50, 90],
    scale_range=[0, 100],
    tick_color=0x0000FF,
    background_color=0x00FF00,
    show_text=True,
    direction="Horizontal",
)

gauge2.set_threshold(value=50, color=0xFF0000)

group.append(gauge2)

display.show(group)

i = 20
gauge1.update(i)
gauge2.update(i)
# we iterate
while True:
    for a in range(5):
        gauge1.update(i)
        gauge2.update(i)
        i = i + 10
        time.sleep(0.1)
    for a in range(5):
        gauge1.update(i)
        gauge2.update(i)
        i = i - 10
        time.sleep(0.1)
    i = 20
