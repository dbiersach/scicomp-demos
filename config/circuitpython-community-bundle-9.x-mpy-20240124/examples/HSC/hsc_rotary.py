"""
	Example: hsc_rotary

	This example shows how to use the rotary setting of the of the P1-02HSC

    This example works with the P1-02HSC

	This example will print the position of each counter every second. 

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
import P1AM

base = P1AM.Base()
hsc = base[1] # P1-02HSC module in slot 1
cnt1 = hsc[1] # Channel 1
cnt2 = hsc[2] # Channel 2

cnt1.is_rotary = True
cnt2.is_rotary = True

cnt1.rollover_position = 5000
cnt2.rollover_position = 1000

cnt2.positive_polarity = False # Channel 2 counts backwards

hsc.update_settings() # Write new settings to module

last_time = time.monotonic()
while True:
    if time.monotonic() - last_time > 1:
        print(f"Channel 1 position is {cnt1.position}")
        print(f"Channel 2 position is {cnt2.position}")
        last_time = time.monotonic()
