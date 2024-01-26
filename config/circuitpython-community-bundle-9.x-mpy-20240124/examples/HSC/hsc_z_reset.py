"""
	Example: hsc_z_reset

	This example shows how to use the z reset functionality of the of the P1-02HSC

    This example works with the P1-02HSC

	This example will print the position of each counter every second. 
    If the z reset input is triggered, each channel will have its potition reset
    to the specified value
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

cnt1.enable_z_reset = True # Enable z reset functionality
cnt2.enable_z_reset = True

cnt1.z_reset_position = 1234 # Set positions to reset to when triggered
cnt2.z_reset_position = 5678

hsc.update_settings() # Write settings to module

last_time = time.monotonic()
while True:
    if time.monotonic() - last_time > 1:
        print(f"cnt1 position = {cnt1.position}")
        print(f"cnt2 position = {cnt2.position}\n")
        last_time = time.monotonic()
