"""
	Example: Toggle Switch

	This example shows how to use the P1AM-200 Toggle Switch

	This example uses a discrete output module, but can be adapted to other modules
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

base = P1AM.Base()
ch2 = base[1][2]

while True:
    ch2.value = switch.value
