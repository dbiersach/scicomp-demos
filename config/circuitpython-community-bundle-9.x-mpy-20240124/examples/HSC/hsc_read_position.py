"""
	Example: hsc_read_position

	This example shows how to read the position of each channel of a P1-02HSC

    This example works with the P1-02HSC

	This example will print the position of each counter every second.
    If the toggle switch is up, will reset the position to zero
	 _____  _____
	|  P  ||  S  |
	|  1  ||  L  |
	|  A  ||  O  |
	|  M  ||  T  |
	|  -  ||     |
	|  2  ||  0  |
	|  0  ||  1  |
	|  0  ||     |
	 ¯¯¯¯¯  ¯¯¯¯¯
	Written by FACTS Engineering
	Copyright (c) 2023 FACTS Engineering, LLC
	Licensed under the MIT license.

"""

import time
import digitalio
import board
import P1AM

sw = digitalio.DigitalInOut(board.SWITCH)
sw.switch_to_input()

base = P1AM.Base()
hsc = base[1] # P1-02HSC module in slot 1
cnt1 = hsc[1] # Channel 1
cnt2 = hsc[2] # Channel 2

last_time = time.monotonic()
while True:
    if sw.value: # reset position to zero when switch is up
        cnt1.position = 0
        cnt2.position = 0
    if time.monotonic() - last_time > 1:
        print(f"cnt1 position = {cnt1.position}")
        print(f"cnt2 position = {cnt2.position}\n")
        last_time = time.monotonic()
