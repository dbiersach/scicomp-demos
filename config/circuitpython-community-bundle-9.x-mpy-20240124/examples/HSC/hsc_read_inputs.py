"""
	Example: hsc_read_inputs

	This example shows how to read the inputs of the of the P1-02HSC

    This example works with the P1-02HSC

	This example will print the value of each input every second.

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

hsc_inputs = ("1a", "1b", "1z", "3in", "2a", "2b", "2z", "4in") # HSC channel names

last_time = time.monotonic()
while True:
    if time.monotonic() - last_time > 1:
        current_reading = hsc.values # Get reading of HSC inputs as a last
        for idx, val in enumerate(current_reading):
            print(f"{hsc_inputs[idx]} is {val}")
        print()
        last_time = time.monotonic()
