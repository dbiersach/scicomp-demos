"""
	Example: hsc_inhibit_counting

	This example shows how to set a counter to stop counting based on the state of one 
    of the hsc inputs of the of the P1-02HSC

    This example works with the P1-02HSC

	This example will print the value of each input every second and whether the channel
    is actively being inhibited.

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

cnt1.inhibit_on_input = "3in" # Inhibit counting when 3in input is high
cnt2.inhibit_on_input = "2z" # Inhibit counting when 2z input is high

hsc.update_settings() # Write settings to module

last_time = time.monotonic()
while True:
    if time.monotonic() - last_time > 1:
        if cnt1.inhibit_active:
            print("cnt1 is being inhibited")
        print(f"cnt1 position = {cnt1.position}")

        if cnt2.inhibit_active:
            print("cnt2 is being inhibited")
        print(f"cnt2 position = {cnt2.position}\n")
        last_time = time.monotonic()

