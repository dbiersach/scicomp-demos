"""
	Example: DiscreteInput

	This example shows how to read from discrete input modules.
	Discrete intputs are any input that is only ON or OFF such as a proximity sensor.

	This example works with all P1000 Series:
	 - Discrete input modules such as P1-08SIM, P1-08ND3, P1-08NA, etc
	 - Discrete combo modules such as P1-15CDD1, P1-15CDD2, P1-16CDR, etc.

	This example will use a discrete input in slot 1 and will print out the value of channel 2.
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
input_channel = module[2] # 2nd channel object for our output module.
# input_channel = module.inputs[2] # on combos select inputs with module.inputs

while True:
    print(input_channel.value) # print channel 2 value
    print(module.input_values) # print all input values
    time.sleep(1) # wait 1 second
