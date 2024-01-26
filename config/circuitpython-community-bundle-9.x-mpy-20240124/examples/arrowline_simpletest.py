# SPDX-FileCopyrightText: 2021 Jose David M.
#
# SPDX-License-Identifier: MIT
#############################
"""
This is a simple example of the use of the arrowline function.
"""

import displayio
import board
from arrowline import Line


display = board.DISPLAY

my_group = displayio.Group()

bitmap = displayio.Bitmap(100, 100, 5)

screen_palette = displayio.Palette(3)
screen_palette[1] = 0x00AA00
screen_tilegrid = displayio.TileGrid(
    bitmap,
    pixel_shader=screen_palette,
    x=50,
    y=50,
)

my_group.append(screen_tilegrid)

line = Line(screen_tilegrid, 40, 90, 90, 60, 12, screen_palette, 1)
my_group.append(line.draw)
display.show(my_group)

while True:
    pass
