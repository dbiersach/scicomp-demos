# SPDX-FileCopyrightText: Copyright (c) 2022 Phil Underwood for Underwood Underground
#
# SPDX-License-Identifier: Unlicense
import time
import board
from laser_at import Laser


uart = board.UART()
uart.baudrate = 19200
laser = Laser(uart, speed=Laser.FAST)
now = time.monotonic()
print("BEGIN!\n")
print(f"FAST: {laser.distance}cm")
print(f"Time: {time.monotonic()-now}")

laser.speed = Laser.MEDIUM
now = time.monotonic()
print(f"MEDIUM: {laser.distance}cm")
print(f"Time: {time.monotonic()-now}")

laser.speed = Laser.SLOW
now = time.monotonic()
print(f"SLOW: {laser.distance}cm")
print(f"SLOW: {laser.distance}cm")
print(f"Time: {time.monotonic()-now}")


time.sleep(2)
print(f"Laser is {laser.on}")
print("Turning laser on")
laser.on = True
time.sleep(2)
print(f"Laser is {laser.on}")
laser.on = False
print(f"Laser is {laser.on}")
