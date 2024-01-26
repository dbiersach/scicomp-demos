# SPDX-FileCopyrightText: Copyright (c) Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import displayio
import board
from adafruit_as7341 import AS7341
from gauge import gauge

i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = AS7341(i2c)

display = board.DISPLAY
group = displayio.Group()

gauge1 = gauge(
    40,
    50,
    26,
    100,
    ticks=[0, 3000],
    scale_range=[0, 3000],
    tick_color=0x440044,
    box_color=0x9B26B6,
    background_color=0x9B26B6,
)
gauge2 = gauge(
    90,
    50,
    26,
    100,
    ticks=[0, 3000],
    scale_range=[0, 3000],
    tick_color=0x440044,
    box_color=0x4B0082,
    background_color=0x4B0082,
)
gauge3 = gauge(
    140,
    50,
    26,
    100,
    ticks=[0, 3000],
    scale_range=[0, 3000],
    tick_color=0x440044,
    box_color=0x0000FF,
    background_color=0x0000FF,
)
gauge4 = gauge(
    190,
    50,
    26,
    100,
    ticks=[0, 3000],
    scale_range=[0, 3000],
    tick_color=0x440044,
    box_color=0x00FFFF,
    background_color=0x00FFFF,
)
gauge5 = gauge(
    240,
    50,
    26,
    100,
    ticks=[0, 3000],
    scale_range=[0, 3000],
    tick_color=0x440044,
    box_color=0x00FF00,
    background_color=0x00FF00,
)
gauge6 = gauge(
    290,
    50,
    26,
    100,
    ticks=[0, 3000],
    scale_range=[0, 3000],
    tick_color=0x440044,
    box_color=0xFFFF00,
    background_color=0xFFFF00,
)
gauge7 = gauge(
    340,
    50,
    26,
    100,
    ticks=[0, 3000],
    scale_range=[0, 3000],
    tick_color=0x440044,
    box_color=0xFF6500,
    background_color=0xFF6500,
)
gauge8 = gauge(
    390,
    50,
    26,
    100,
    ticks=[0, 3000],
    scale_range=[0, 3000],
    tick_color=0x440044,
    box_color=0xFF0000,
    background_color=0xFF0000,
)

group.append(gauge1)
group.append(gauge2)
group.append(gauge3)
group.append(gauge4)
group.append(gauge5)
group.append(gauge6)
group.append(gauge7)
group.append(gauge8)
display.show(group)

while True:
    gauge1.update(sensor.channel_415nm)
    gauge2.update(sensor.channel_445nm)
    gauge3.update(sensor.channel_480nm)
    gauge4.update(sensor.channel_515nm)
    gauge5.update(sensor.channel_555nm)
    gauge6.update(sensor.channel_590nm)
    gauge7.update(sensor.channel_630nm)
    gauge8.update(sensor.channel_680nm)

    time.sleep(0.001)
