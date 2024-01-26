"""
  Example: PWMOutput

  This example shows how to use the P1-04PWM module.
  This example sets duty cycle, frequency on the P1-04PWM.

  The P1-04PWM module will output a pulse width modulated signal on channel 2.
  The duty cycle is set to 50.15 and the frequency is set to 10kHz.
  The output being active is shown by the LED being on.
  The output of the module can be verified by using an oscilloscope.
 
  This example works with the P1-04PWM in slot 1.
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
ch2 = module[2] # channel object for slot 1 channel 2

ch2.frequency = 10000 # set frequency to 10kHz
ch2.duty_cycle = 50.15 # set duty cycle to 50.15%

while True:
    time.sleep(1)
