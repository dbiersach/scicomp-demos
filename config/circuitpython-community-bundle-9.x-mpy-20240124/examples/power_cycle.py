"""
	Example: Power Cycle

    
	This example shows how to re-init the base after power has been cycled.
    
    When powering your device with both USB and external power, this example can
    be used to catch and handle errors produced by a temporary loss of external 24V.

	This example uses a discrete output module, but can be adapted to other modules.
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

base = P1AM.Base() # Intializes base. Returns the base object.
module = base[1] # module object for slot 1
output = module[2] # 2nd channel object for our output module.
# output = module.outputs[2] # on combos select outputs with module.outputs

while True:
    try:
        # removing external 24V here will raise a RuntimeError
        output.value = True
        time.sleep(1)
        output.value = False
        time.sleep(1)
    except RuntimeError:
        while True:
        	# loop until base is re-initialized
            try:
                base.init()	# must be called if external 24V is interrupted
                break
            except RuntimeError:
                pass