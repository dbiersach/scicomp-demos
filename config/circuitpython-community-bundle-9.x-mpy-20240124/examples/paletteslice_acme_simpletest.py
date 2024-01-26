# SPDX-FileCopyrightText: Copyright (c) 2022 JG for Cedar Grove Maker Studios
# SPDX-License-Identifier: MIT
"""
`paletteslice_acme_simpletest`
================================================================================
A test of the PaletteSlice wrapper class, Acme version.

* Author(s): JG
"""

import time
import random
import board
import terminalio
import displayio
import adafruit_imageload
from adafruit_display_text.label import Label
from cedargrove_paletteslice.paletteslice_acme import PaletteSlice

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

# Test of append()
print("\n" + ("=" * 15))
print("TEST append()")
test_value = 0xF0F0F0
print(f"  value to append: {test_value:#08x}")

(last_color, last_transparency) = pal_sliceable.reference_list[-1]
length = len(pal_sliceable)
print(
    f"length BEFORE append: {length} last item: {last_color:#08x} {last_transparency}"
)

pal_sliceable.append(test_value)

(last_color, last_transparency) = pal_sliceable.reference_list[-1]
length = len(pal_sliceable)
print(
    f"length  AFTER append: {length} last item: {last_color:#08x} {last_transparency}"
)

# Test of insert()
print("\n" + ("=" * 15))
print("TEST insert()")
test_value = 0xA0A0A0
test_index = 100
print(f"  value to insert: {test_value:#08x} at index: {test_index}")

(old_color, old_transparency) = pal_sliceable.reference_list[test_index]
length = len(pal_sliceable)
print(f"length BEFORE insert: {length} item: {old_color:#08x} {old_transparency}")

pal_sliceable.insert(test_index, test_value)

(new_color, new_transparency) = pal_sliceable.reference_list[test_index]
length = len(pal_sliceable)
print(f"length  AFTER insert: {length} item: {new_color:#08x} {new_transparency}")

# Test of is_transparent(), make_transparent(), make_opaque()
print("\n" + ("=" * 15))
test_value = -1  # Index to test
print("TEST is_transparent(), make_transparent(), make_opaque()")
print(f"  index value for test: {test_value}")
print(f"  is_transparent: {pal_sliceable.is_transparent(test_value)}")
pal_sliceable.make_transparent(test_value)
print(
    f"AFTER make_transparent -> is_transparent: {pal_sliceable.is_transparent(test_value)}"
)
pal_sliceable.make_opaque(test_value)
print(
    f"AFTER make_opaque      -> is_transparent: {pal_sliceable.is_transparent(test_value)}"
)

# Test of count()
print("\n" + ("=" * 15))
print("TEST count()")
test_value = 0xFFFFFF  # Color value for search
print(f"  color value for search: {test_value:#08x}")

print(f"number of occurrences: {pal_sliceable.count(test_value)}")

# Test of index()
print("\n" + ("=" * 15))
print("TEST index()")
test_value = 0xFFFFF0  # Color value for search
print(f"  color value for search: {test_value:#08x}")

print(f"first index found: {pal_sliceable.index(test_value)}")

test_value = 0xFFFFFF  # Color value for search
print(f"  color value for search: {test_value:#08x}")

print(f"first index found: {pal_sliceable.index(test_value)}")

# Test of pop()
print("\n" + ("=" * 15))
print("TEST pop()")
test_value = -1  # Remove last item
print(f"  index to pop: {test_value}")

print(f"  length BEFORE pop: {len(pal_sliceable)}")
print(f"value removed: {pal_sliceable.pop(test_value):#08x}")
print(f"  length  AFTER pop: {len(pal_sliceable)}")

# Test of __contains__
print("\n" + ("=" * 15))
print("TEST __contains__")
test_value = 0
print(f"  value to find: {test_value}")

if test_value in pal_sliceable:
    print(f"< {test_value} > in pal_sliceable (True)")
else:
    print(f"< {test_value} > NOT in pal_sliceable (False)")

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
print("\n" + ("=" * 15))
print("TEST of source image")
slice_label.text = "PALETTE SLICE: source image and palette"
time.sleep(2)

# Continuous random slice test
print("\n" + ("=" * 15))
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
