"""
	Example: Module Configuration
 
 This example shows how to configure modules.
 Configuration is written to a module to change things such as:
 - number of active channels
 - type of input e.g. thermocouple type
 - input or output range
 
 This example works with all P1000 Series:
  - Analog input modules that can be configured such as P1-04ADL-1, P1-04ADL-2, etc.
  - Other modules that can be configured
  
  This example will configure channel 1 of a P1-04AD to the 0-10V sensing range. 
  Afterwards it will print the configuration status to the serial terminal and then the
  converted units from each channel.
 
 Configuration data for P1000 modules can be found on https://facts-engineering.github.io/config.html 
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

# Config module channel 1 sensing to 0-10V, channels 2-4 be the default of 0-20mA
module.configure_module((0x40, 0x03, 0x00, 0x00, 0x20, 0x01, 0x00, 0x00, 0x21, 
                         0x03, 0x00, 0x00, 0x22, 0x03, 0x00, 0x00, 0x23, 0x03))

print(module.current_config) # Print current config

while True:
	# Loop through channel reals
    for idx, real in enumerate(module.reals):
        print(f"Channel {idx + 1} is reading {real} units")
    time.sleep(.5)
