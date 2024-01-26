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

a = Line(
    screen_tilegrid,
    100,
    100,
    150,
    200,
    12,
    screen_palette,
    1,
    solid_line=False,
    line_length=5,
    line_space=5,
)
my_group.append(a.draw)
b = Line(
    screen_tilegrid,
    100,
    100,
    200,
    200,
    12,
    screen_palette,
    1,
    solid_line=False,
    line_length=5,
    line_space=5,
)
my_group.append(b.draw)
c = Line(
    screen_tilegrid,
    100,
    100,
    50,
    200,
    12,
    screen_palette,
    1,
    solid_line=False,
    line_length=5,
    line_space=5,
)
my_group.append(c.draw)
d = Line(
    screen_tilegrid,
    40,
    90,
    150,
    40,
    12,
    screen_palette,
    1,
    solid_line=False,
    line_length=5,
    line_space=5,
)
my_group.append(d.draw)
display.show(my_group)

while True:
    pass
