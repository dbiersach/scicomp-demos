"""
	Example: hsc_counting_mode

	This example shows how to configure an HSC channel with different counting modes.

    This example works with the P1-02HSC

	This example will configure channel 1 as a Quadrature 1X counter and channel 2 as
    a Quadrature 4X counter. The default mode before configuring is Step Direction.
    It will then print the position of each channel every second.

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

cnt1.counting_mode = "quadrature_1x"
cnt2.counting_mode = "quadrature_4x"

hsc.update_settings() # Write settings to module

last_time = time.monotonic()
while True:
    if time.monotonic() - last_time > 1:
        print(f"cnt1 position = {cnt1.position}")
        print(f"cnt2 position = {cnt2.position}\n")
        last_time = time.monotonic()

