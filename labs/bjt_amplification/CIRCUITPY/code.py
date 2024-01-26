# code.py

# uses (1) PN2222A NPN BJT
# uses (1) MCP4725 12-bit DAC

import analogio
import board
import busio
import neopixel
import time
import supervisor
import usb_cdc
import adafruit_mcp4725


# Configure NeoPixel
pixel_builtin = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel_builtin.brightness = 0.1
pixel_builtin.fill((255, 255, 0))  # YELLOW

# Configure pins for experiment
pin_adc = analogio.AnalogIn(board.A3)

# Initialize I2C bus
# board.D23 (CIPO) -> I2C CLK
# board.D22 (SCK)  -> I2C SDA
i2c_bus = busio.I2C(board.D23, board.D22)

# Configure MCP4725 DAC
dac = adafruit_mcp4725.MCP4725(i2c_bus)
dac.raw_value = 0

# Wait until USB cable is connected
while not supervisor.runtime.usb_connected:
    pass

# Create USB data port
ser = usb_cdc.data


def usb_readline():
    return ser.readline().decode("utf-8").strip()


def usb_writeline(x):
    ser.write(bytes(str(x) + "\n", "utf-8"))
    ser.flush()


def run_experiment(params):
    # Set total number of samples (NOT number of seconds!)
    n = int(params[0])
    step_size = int(params[1])

    # Declare integer arrays to hold measurement values
    volts_be = [int] * n  # Base-Emitter voltage
    volts_ce = [int] * n  # Collector-Emitter voltage

    # Read volts from built-in ADC
    for i in range(n):
        # Set DAC output voltage which is the volts between
        # the BJT base and emitter as emitter is at GND
        dac.raw_value = i * step_size        
        volts_be[i] = dac.raw_value
        time.sleep(0.005)

        # Calculate the average collector voltage
        total = 0
        for _ in range(50):            
            total += pin_adc.value
            time.sleep(0.002) # Give ADC time to settle
        volts_ce[i] = int(total / 50)

    # Turn off DAC voltage to circuit
    dac.raw_value = 0

    # Transfer data over USB
    usb_writeline(n)  # number of samples
    for val in volts_be:
        usb_writeline(val)  # Base-Emitter volts array
    for val in volts_ce:
        usb_writeline(val)  # Collector-Emitter volts array


while True:
    pixel_builtin.fill((0, 255, 0))  # GREEN
    params = usb_readline().split(",")
    pixel_builtin.fill((255, 0, 0))  # RED
    run_experiment(params)
