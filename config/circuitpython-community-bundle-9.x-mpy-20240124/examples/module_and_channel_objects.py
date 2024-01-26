"""
	Example: Addressing modules and channels

	This example shows different ways of referencing IO modules and channels.

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

import P1AM

base = P1AM.Base() # Intializes base. Returns the base object.

print("Module Object")
module = base[1] # Referencing the base object positionally will give the module object
print(module) # module information
# module.values = [True, False, False, True] # Output modules can be set via a list

# print(module.values) # The values property of modules will return a list of channel values
print(module.input_values) # Use input_values on combos to get only input channels

# print(module.reals) # The reals property will return a list of converted channel values in units
print(module.input_reals) # Use input_reals on combos to get only input channels

print("Channel Object")
# channel = module[2]  # Referencing the module object positionally will give the channel object
channel = module.inputs[2] # Use module.inputs or module.outputs on combo modules
print(channel) # channel information
print(channel.value) # Prints the value of the channel
print(channel.real) # Prints the channel value in converted units

same_channel = base[1].inputs[2] # You can also reference the base object as a 2D array
print(same_channel) # channel information
print(same_channel.value) # Prints the value of the channel

while True:
    pass