# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
# SPDX-License-Identifier: MIT
"""
`paletteslice_simpletest`
================================================================================
A test of the PaletteSlice wrapper class, minimal version.

* Author(s): JG
"""

import time
import random
import board
import terminalio
import displayio
import adafruit_imageload
from adafruit_display_text.label import Label
from cedargrove_paletteslice.paletteslice import PaletteSlice

BKG_IMAGE_FILE = "orchid.bmp"
FRAME_DURATION = 1  # seconds


def print_palette(new_palette):
    print("print_palette object:", new_palette)
    print("print_palette object length:", len(new_palette))
    for i, color in enumerate(new_palette):
        print(
            f"index: {i:03.0f} color: {color:#08x} transparency: {new_palette.is_transparent(i)}"
        )


# Define the display and primary display group
display = board.DISPLAY
display.brightness = 0.1
primary_group = displayio.Group()

# Display the test image and source color palette
test_bitmap, test_palette_source = adafruit_imageload.load(
    BKG_IMAGE_FILE, bitmap=displayio.Bitmap, palette=displayio.Palette
)

# Instantiate a sliceable copy of the reference palette
pal_sliceable = PaletteSlice(test_palette_source)

# Test of __get__
print("\n" + ("=" * 15))
print("TEST __get__()")
start = 0  # Slice start
stop = 5  # Slice stop
step = 1  # Slice step
print(f"  slice object: [{start}:{stop}:{step}]")
get_palette = pal_sliceable[start:stop:step]
print_palette(get_palette)

# Test of __set__
print("\n" + ("=" * 15))
print("TEST __set__()")
start = 1  # Slice start
stop = 6  # Slice stop
step = 1  # Slice step
print(f"  slice object: [{start}:{stop}:{step}]")
pal_sliceable[start:stop:step] = get_palette
print_palette(pal_sliceable[0:8])

# Test of is_transparent(), make_transparent(), make_opaque()
print("\n" + ("=" * 15))
test = -1  # Index to test
print("TEST is_transparent(), make_transparent(), make_opaque()")
print(f"  index value for test: {test}")
print(f"  is_transparent: {pal_sliceable.is_transparent(test)}")
pal_sliceable.make_transparent(test)
print(f"AFTER make_transparent -> is_transparent: {pal_sliceable.is_transparent(test)}")
pal_sliceable.make_opaque(test)
print(f"AFTER make_opaque      -> is_transparent: {pal_sliceable.is_transparent(test)}")

# Place the test image into a tile and append to the primary display group
test_tile = displayio.TileGrid(test_bitmap, pixel_shader=test_palette_source)
primary_group.append(test_tile)

# Define on-screen label for slice object and palette length
slice_label = Label(terminalio.FONT, text="", color=0xFFFFFF)
slice_label.anchor_point = (0, 0.5)
slice_label.anchored_position = (10, 225)
primary_group.append(slice_label)

# Show the test image and label
display.root_group = primary_group
print("TEST of source image")
slice_label.text = "PALETTE SLICE: source image and palette"
time.sleep(2)

# Continuous random slice test
print("TEST of random slices")
while True:
    # Create a random slice object; prohibit step == 0
    start = random.randrange(0, 255)
    stop = random.randrange(0, 255)
    step = random.randrange(-5, 6)
    if step == 0:
        step = 1

    # Slice the palette and use for bkg_tile
    test_tile.pixel_shader = pal_sliceable[start:stop:step]

    if len(pal_sliceable.palette) != 0:
        # Display slice object and pause to view
        slice_label.text = f"[{start}:{stop}:{step}]  \nLENGTH={len(pal_sliceable)}"
        time.sleep(FRAME_DURATION)
