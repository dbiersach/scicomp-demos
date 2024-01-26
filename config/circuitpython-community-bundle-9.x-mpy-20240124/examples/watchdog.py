"""
	Example: Watchdog

	This example shows how to use the P1AM-200 Watchdog.

	This example works with any P1000 Series Module

    This example shows how to initialize and then use the watchdog. 
    There are 2 modes for the watchdog: TOGGLE and HOLD. 
    - TOGGLE will quickly reset the P1AM CPU and modules then restart the program.
    - HOLD will hold the P1AM CPU in reset and shut off all modules until a full power cycle is performed.   
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
from p1am_200_helpers import get_switch

switch = get_switch() # get the switch digitalio object

while not switch.value:
    pass # wait to put switch in up position

base = P1AM.Base()
ch2 = base[1][2]
base.config_watchdog(1000, mode="TOGGLE") # configure watchdog with 1000ms timeout and "TOGGLE" mode
# base.config_watchdog(1000, mode="HOLD") # using "HOLD" will require a full power cycle for the program to run again after a watchdog timeout
base.start_watchdog()  # start watchdog

while True:
    if switch.value:
        base.pet_watchdog() # Manually resets watchdog
        print(ch2.value) # Any action that reads or writes to the base controller also resets the watchdog
    else: # if the switch is down for more than 1 second, the P1AM-200 will be reset
        pass

