"""
	Example: AnalogOutput

	This example shows how to write to analog output modules.
	Analog ouputs generate a voltage or current signal.
    Ranges can be between 0-10V, 4-20mA, etc.
	This example works with all P1000 Series:
	 - Analog ouput modules such as P1-04DAL-1, P1-04DAL-2,etc.
	 - Analog combo modules such as P1-4ADL2DAL-1, P1-4ADL2DAL-2 etc.

	This example has an option for an interactive mode where you can select a channel
	and value as well as a automatic mode where channel 2 automatically increments.
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
 To confirm the analog output value you can use either a P1 analog input module or a multimeter.

 Written by FACTS Engineering
 Copyright (c) 2023 FACTS Engineering, LLC
 Licensed under the MIT license.

"""

import time
import P1AM

# Use a channel's "real" property instead of its "value" to use real-life units instead of counts
# The "real" property converts the value you enter to the next closest count

def interactive():
    """Select a channel and a value to write to"""
    sel = int(input("Select a channel: "))
    channel = module[sel] 
    # channel = module.outputs[sel] # on combos select outputs with module.outputs
    
	# the range_bottom and range_top properties are in mA or V depending on module type
    target = float(input(f"Enter a value between {channel.range_bottom}-{channel.range_top} units: "))
    channel.real = target
    print(channel.real) # print units
    print(channel.value) # print counts

def automatic():
    """Automatically increment channel 2"""    
    if ch2.real <= ch2.range_top - 1:
        ch2.real = round(ch2.real + 1.0) # round to account for count error

    else:
        ch2.real = ch2.range_bottom
    print(ch2.real) # print units
    print(ch2.value) # print counts
    time.sleep(1)

base = P1AM.Base() # Intializes base. Returns the base object.
module = base[1] # module object for slot 1
ch2 = module[2] # channel object for slot 1 channel 2
# ch2 = module.outputs[2] # on combos select outputs with module.outputs

while True:
    automatic() # Automatically increment channel 2
    # interactive() # Select a channel and value. Requires a serial terminal program.
    
