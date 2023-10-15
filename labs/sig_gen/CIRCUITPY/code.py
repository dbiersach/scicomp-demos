# code.py

# Signal Generator experiment
# uses AITRIP AD9833 Signal Generator


import analogio
import board
import digitalio
import neopixel
import time
import supervisor
import usb_cdc
import ad9833

# Configure NeoPixel
pixel_builtin = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel_builtin.brightness = 0.1
pixel_builtin.fill((255, 255, 0))  # YELLOW

# Configure pins for experiment
pin_adc = analogio.AnalogIn(board.A0)

# Configure AITRIP AD9833 Signal Generator
# Note: chip select (*CS) is GPIO Pin 21 on SparkFun Pro Micro 2040
wave_gen = ad9833.AD9833(select="D21")

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
    n = int(params[0])  # number of samples
    freq = int(params[1])  # Wave frequency in Hz
    wave_type = params[2]  # "sine" / "triangle" / "square"

    # Set number of samples (NOT number of seconds!)
    volts = [int] * n
    times = [int] * n

    # Start generating 10 Hz sine waves
    wave_gen.reset()
    wave_gen.update_freq(freq)
    wave_gen.wave_type = wave_type
    wave_gen.start()

    # Read voltage samples
    for i in range(n):
        times[i] = time.monotonic_ns()
        volts[i] = pin_adc.value
        time.sleep(0.001)

    # Transfer data over USB
    usb_writeline(n)  # number of samples
    for val in times:
        usb_writeline(val)  # times array
    for val in volts:
        usb_writeline(val)  # volts array


while True:
    pixel_builtin.fill((0, 255, 0))  # GREEN
    params = usb_readline().split(",")
    pixel_builtin.fill((255, 0, 0))  # RED
    run_experiment(params)
