"""
  Example: Read Temperature
  
  This example shows how to read temperature values in degrees from a temperature input module. 
  
  Temperature inputs are analog inputs that read data from a temperature sensor and convert it into a 
  temperature reading. These include thermistors, thermocouples and resistance temperature detectors (RTDs) 
  
  This example works with all P1000 Series:
   - Temperature input modules such as P1-04NTC, P1-04RTD, and P1-04THM.
  
  The default ranges are:
   - P1-04THM: J-Type
   - P1-04RTD: Pt100
   - P1-04NTC: 2252
  
  This example will print every channel's temperature to the serial monitor every second.
  This can be tested by:
   - Using an appropriate temperature probe for the module
   - Shorting the positive and negative inputs of a THM module to read room temperature.
   - Using a potentiometer to simulate thermistor/RTD signal on an NTC or RTD
      module and using a temp. vs. resistance chart to verify values. 
     
  The reported temperature defaults to degrees Fahrenheit. 
	 _____  _____ 
	|  P  ||  S  |
	|  1  ||  L  |
	|  A  ||  O  |
	|  M  ||  T  |
	|  -  ||     |
	|  1  ||  0  |
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

while module.not_ready:
    pass # Wait for temperature module to be ready

while True:
	# Loop through channel values
    for idx, value in enumerate(module.values):
        print(f"Channel {idx + 1} is reading {value} degrees F")
    time.sleep(1)
