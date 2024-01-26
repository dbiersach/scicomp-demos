"""
	Example: Object indexing

	This example shows how to begin P1AM object references at 0 instead of at 1.

	This example works with all P1000 Series Modules
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

# Pass in the zero_indexing argument as True to start indexing at 0 for channels and
# slots. This makes it easier to do iterable loops through objects.
# With the default indexing the base and module objects will have their zero index
# element as None i.e. base[0] = None

base = P1AM.Base(zero_indexing=True) # Intializes base. Returns the base object.

first_module = base[0] # this is the module next to the CPU
first_channel = first_module[0] # this is the first channel on the module

# Print a list of every channel and module in the base. All prints will be 0 referenced
# as well so they match what is seen in the code
for module in base:
    print(module)
    for channel in module.inputs:
        print(channel)
    for channel in module.outputs:
        print(channel)

while True:
    pass