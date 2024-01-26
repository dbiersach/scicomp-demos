# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
# SPDX-License-Identifier: MIT
"""
`gradient_shape`
================================================================================
A test of gradient color fill in a vectorio shape.

* Author(s): JG
"""

import time
import board

# from vectorio import Rectangle, Circle
# from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
import displayio
from cedargrove_rgb_spectrumtools.n_color import Spectrum

OBJ_WIDTH = 35
OBJ_HEIGHT = 25

FRAME_DELAY = 0.5

# Define the display and primary display group and show
display = board.DISPLAY
display.brightness = 0.005

primary_group = displayio.Group()
display.root_group = primary_group

# Create Red/Yellow/Green light-style spectrum
spectrum_1 = Spectrum([0xFF0000, 0xFFFF00, 0x00FF00], mode="continuous", gamma=0.6)
gradient_palette_1 = displayio.Palette(OBJ_WIDTH)
for i in range(0, OBJ_WIDTH):
    gradient_palette_1[i] = spectrum_1.color(index=i / OBJ_WIDTH)

# Create a second spectrum
spectrum_2 = Spectrum([0xFF00FF, 0x00FF00, 0xF0FFF0], mode="continuous", gamma=0.6)
gradient_palette_2 = displayio.Palette(OBJ_WIDTH)
for i in range(0, OBJ_WIDTH):
    gradient_palette_2[i] = spectrum_2.color(index=i / OBJ_WIDTH)

# Create a third spectrum
spectrum_3 = Spectrum([0xFF00FF, 0xFF0000], mode="continuous", gamma=0.6)
gradient_palette_3 = displayio.Palette(OBJ_WIDTH)
for i in range(0, OBJ_WIDTH):
    gradient_palette_3[i] = spectrum_3.color(index=i / OBJ_WIDTH)

for i in range(OBJ_WIDTH, -1, -1):
    """gradient_object = Rectangle(
        pixel_shader=gradient_palette_1,
        width=1,
        height=OBJ_HEIGHT,
        x=i + 5,
        y=5,
        color_index=i,
    )"""
    """gradient_object = Circle(
        pixel_shader=gradient_palette_1,
        radius=(OBJ_WIDTH - i+1)*2,
        x=i + 100,
        y=100,
        color_index=i,
    )"""
    gradient_object = Circle(160, 120, ((i + 1) * 2), outline=0x000000, stroke=3)

    primary_group.append(gradient_object)

while True:
    for i in range(OBJ_WIDTH):
        # primary_group[i].pixel_shader = gradient_palette_1
        primary_group[i].outline = gradient_palette_1[i]

    time.sleep(FRAME_DELAY)

    for i in range(OBJ_WIDTH):
        # primary_group[i].pixel_shader = gradient_palette_2
        primary_group[i].outline = gradient_palette_2[i]

    time.sleep(FRAME_DELAY)

    for i in range(OBJ_WIDTH):
        # primary_group[i].pixel_shader = gradient_palette_3
        primary_group[i].outline = gradient_palette_3[i]

    time.sleep(FRAME_DELAY)
