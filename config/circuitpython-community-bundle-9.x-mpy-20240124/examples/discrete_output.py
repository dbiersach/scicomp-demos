"""
	Example: Discrete Output

	This example shows how to write to discrete output modules.

	Discrete ouputs are any output that is only ON or OFF such as a relay.
	This example works with all P1000 Series:
	 - Discrete ouput modules such as P1-08TRS, P1-08TD1, P1-16TR, etc.
	 - Discrete combo modules such as P1-15CDD1, P1-15CDD2, P1-16CDR, etc.

	This example will toggle channel 2 of slot 1 on and off every second.
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
    output.value = True
    time.sleep(1)
    output.value = False
    time.sleep(1)
