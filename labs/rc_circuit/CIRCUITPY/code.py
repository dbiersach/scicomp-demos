# code.py

# RC Circuit experiment
# uses 10K ohm resistor (1/2 watt, 1% tolerance)
# uses 10uF 25V electrolytic capacitor (20% tolerance)

import analogio
import board
import digitalio
import neopixel
import time
import supervisor
import usb_cdc

# Configure NeoPixel
pixel_builtin = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel_builtin.brightness = 0.1
pixel_builtin.fill((255, 255, 0))  # YELLOW

# Configure pins for experiment
pin_adc = analogio.AnalogIn(board.A3)
pin_charge = digitalio.DigitalInOut(board.D2)
pin_charge.direction = digitalio.Direction.OUTPUT

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
    n1 = int(params[0])
    n2 = n1 * 2
    volts = [int] * n2
    times = [int] * n2

    # Drain circuit (discharge capacitor) for five seconds
    pin_charge.value = False
    time.sleep(5)

    # Energize circuit (charge capacitor)
    pin_charge.value = True
    for i in range(n1):
        volts[i] = pin_adc.value
        times[i] = time.monotonic_ns()
        time.sleep(0.001)

    # Drain circuit (discharge capacitor)
    pin_charge.value = False
    for i in range(n1, n2):
        volts[i] = pin_adc.value
        times[i] = time.monotonic_ns()
        time.sleep(0.001)

    # Transfer data over USB
    usb_writeline(n2)  # number of samples
    for val in times:
        usb_writeline(val)  # times array
    for val in volts:
        usb_writeline(val)  # volts array


while True:
    pixel_builtin.fill((0, 255, 0))  # GREEN
    params = usb_readline().split(",")
    pixel_builtin.fill((255, 0, 0))  # RED
    run_experiment(params)
