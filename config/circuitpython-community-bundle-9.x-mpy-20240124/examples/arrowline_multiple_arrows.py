# SPDX-FileCopyrightText: 2023 Jose David M.
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

bitmap = displayio.Bitmap(300, 300, 5)

screen_palette = displayio.Palette(3)
screen_palette[1] = 0x00AA00
screen_tilegrid = displayio.TileGrid(
    bitmap,
    pixel_shader=screen_palette,
    x=0,
    y=0,
)

my_group.append(screen_tilegrid)

a = Line(screen_tilegrid, 40, 32, 45, 60, 12, screen_palette, 1)
my_group.append(a.draw)
b = Line(screen_tilegrid, 60, 22, 33, 14, 6, screen_palette, 1)
my_group.append(b.draw)
c = Line(screen_tilegrid, 100, 102, 150, 150, 14, screen_palette, 1, pointer="C")
my_group.append(c.draw)
d = Line(screen_tilegrid, 0, 102, 0, 150, 12, screen_palette, 1)
my_group.append(d.draw)
e = Line(screen_tilegrid, 239, 319, 220, 30, 12, screen_palette, 1, pointer="C")
my_group.append(e.draw)
display.show(my_group)

while True:
    pass
