"""
	Example: AnalogInput

	This example shows how to read from analog input modules.
	Analog inputs typically read a voltage or current signal.
  	Ranges can be between 0-10V, 4-20mA, etc.

	This example works with all P1000 Series:
	 - Analog input modules such as P1-04ADL-1, P1-04ADL-2,etc.
	 - Analog combo modules such as P1-4ADL2DAL-1, P1-4ADL2DAL-2 etc.
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

# Use a channel's "real" property instead of its "value" to use real-life units instead of counts
# The "real" property converts the value you enter to the next closest count

def clear_terminal():
    """Escape codes to clear serial terminal such as Tera Term"""
    print(chr(27) + "[2J")

base = P1AM.Base() # Intializes base. Returns the base object.
module = base[1] # module object for slot 1

while True:
	# Loop through channels
	channels = module[1:]
    # channels = module.inputs[1:] # on combos select inputs with module.input
	for idx, channel in enumerate(channels):
		counts = channel.value
		units = channel.real
		print(f"Channel {idx + 1} is reading {counts} counts")
		print(f"Channel {idx + 1} is reading {units} units")
	time.sleep(.5)
	clear_terminal() # Clears the terminal. Remove if your terminal does not support it
