# Basic Example to read and write from AT24MACx02 EEPROM Devices

# Written by FACTS Engineering
# Copyright (c) 2023 FACTS Engineering, LLC
# Licensed under the MIT license.

#

import board
import busio
import at24mac_eeprom

# Create EEPROM Object
i2c = busio.I2C(board.ATMAC_SCL, board.ATMAC_SDA)
# i2c = busio.I2C(board.SCL, board.SDA) # For external I2C devices
eeprom = at24mac_eeprom.AT24MAC(i2c)

# Address lines default to 0b100. They can be specified if needed.
# eeprom = at24mac_eeprom.AT24MAC(i2c, 0b101)

# Print out MAC address and serial number
print(eeprom.mac)  # Format for use with Wiznet5k
print([hex(val) for val in eeprom.mac])  # Readable format
print(eeprom.serial_number)
print()

# Write and read to address 0 using the device object like an array
eeprom[0] = 76
print(eeprom[0])
print()

# Write and read to address 100 using array slices
eeprom[100] = [6, 7, 8, 9, 10]
print([val for val in eeprom[100:105]])
print()

while True:
    pass
