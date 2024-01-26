# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: Unlicense
"""
Simple test to display a boxplot based in some data
"""
import displayio
import board
from uboxplot import Boxplot

display = board.DISPLAY

a = [1, 1, 4, 5, 6, 7, 7, 7, 8, 9, 10, 15, 16, 17, 24, 56, 76, 87, 87]
my_box = Boxplot(a, x=50, y=50, height=100)
my_box.draw()
my_box.print_data()
my_group = displayio.Group()
my_group.append(my_box)
display.show(my_group)

while True:
    pass
