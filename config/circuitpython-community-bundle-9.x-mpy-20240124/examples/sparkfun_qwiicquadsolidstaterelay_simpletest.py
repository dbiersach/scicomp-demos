""" QuadRelayTest """
# QuadRelayTest: Copyright (c) 2022 Graham Beland
#
# SPDX-License-Identifier: MIT
# import the CircuitPython board and busio libraries
# CircuitPython board
import board

# the sparkfun_qwiicquadsolidstaterelay
import sparkfun_qwiicquadsolidstaterelay

# Create bus object using the board's I2C port
i2c = board.I2C()

# Note: default i2c address is 8
theRelay = sparkfun_qwiicquadsolidstaterelay.Sparkfun_QwiicQuadSolidStateRelay(i2c)
print("Opened: Relay Controller")
if theRelay.connected:
    print("Relay connected. ")
    theRelay.relay_on(1)
    theRelay.relay_off(1)
else:
    print("Relay does not appear to be connected. Please check wiring.")
