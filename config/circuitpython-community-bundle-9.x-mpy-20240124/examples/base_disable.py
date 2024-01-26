"""
	Example: Base Disable

	This example shows how use the disable method in a try/except clause to turn
	off output modules in the case of an unexpected error.

	Discrete ouputs are any output that is only ON or OFF such as a relay.
	This example works with all P1000 Series:
	 - Discrete ouput modules such as P1-08TRS, P1-08TD1, P1-16TR, etc.
	 - Discrete combo modules such as P1-15CDD1, P1-15CDD2, P1-16CDR, etc.

	This example will toggle channel 2 of slot 1 on and off 4 times and then trigger
	an error at which point it will turn off the output.
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
import traceback

def main(base):
    
    output = base[1][2] # set output object to slot 1 channel 2
    for i in range(4):	# blink 4 times
        output.value = 0 # off
        time.sleep(1)
        output.value = 1 # on
        time.sleep(1)

    import this_module_doesnt_exist # force an import error error


try:
    base = P1AM.Base() # init base object
    main(base) # call our main function
except Exception as e: # if our main function throws an exception
    traceback.print_exception(e) # print out the error
    base.deinit() # disable the base and turn off outputs

while True:
    pass