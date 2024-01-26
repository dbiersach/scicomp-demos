# SPDX-FileCopyrightText: 2023 Jose D. Montoya
# SPDX-License-Identifier: MIT

"""
This is an animation to demonstrate the use of color_fader function.
This example is heavily based in adafruit_display_shapes/examples/display_shapes_circle_animation.py

"""

import time
import gc
import board
import displayio
from adafruit_display_shapes.circle import Circle
from cedargrove_colorfader import color_fader

display = board.DISPLAY
main_group = displayio.Group()
color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
main_group.append(bg_sprite)

posx = 0
posy = 0

# Define Circle characteristics
circle_radius = 20
circle = Circle(posx, posy, circle_radius, fill=0x00FF00, outline=0xFF00FF)
main_group.append(circle)

# Define Circle Animation Steps
delta_x = 2
delta_y = 2

# Showing the items on the screen
display.root_group = main_group

circle.fill = 0xFF0000
brightness = 0

bright_delta = 1 / display.width
while True:
    if circle.y + circle_radius >= display.height - circle_radius:
        delta_y = -1
    if circle.x + circle_radius >= display.width - circle_radius:
        delta_x = -1
    if circle.x - circle_radius <= 0 - circle_radius:
        delta_x = 1
    if circle.y - circle_radius <= 0 - circle_radius:
        delta_y = 1

    circle.x = circle.x + delta_x
    circle.y = circle.y + delta_y
    brightness = brightness + bright_delta * delta_x
    # pylint: disable=consider-using-max-builtin, consider-using-min-builtin
    if brightness > 1:
        brightness = 1
    if brightness < 0:
        brightness = 0
    circle.fill = color_fader(source_color=0x00FF00, brightness=brightness, gamma=1.0)
    time.sleep(0.02)
    gc.collect()
