# light_sensor for KB2040

# Uses AS7341 10-Channel Light Sensor

import board
import neopixel
import supervisor
import usb_cdc
from adafruit_as7341 import AS7341, Gain

# Wait until USB console port is ready
while not supervisor.runtime.usb_connected:
    pass

# Initialize I2C bus
i2c_bus = board.I2C()

# Configure AS7341 10-Channel Light Sensor
sensor = AS7341(i2c_bus)

# Default is Gain.GAIN_128X
# sensor.gain = Gain.GAIN_2X
sensor.gain = Gain.GAIN_256X

# Default LED Current is 50
sensor.led_current = 80

# Configure NeoPixel
pixel_builtin = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel_builtin.brightness = 0.1
pixel_builtin.fill((0, 255, 0))  # Green

# Create USB data port
ser = usb_cdc.data


def usb_writeline(usb_data_port, x):
    usb_data_port.write(bytes(str(x) + "\n", "utf-8"))
    usb_data_port.flush()


def read_samples():
    pixel_builtin.fill((255, 0, 0))  # RED

    # Set number of samples (NOT number of seconds!)
    n = 9
    channels = [float] * n
    for i in range(n):
        channels[i] = 0.0

    # Sum value of AS7341 Sensor Value per channel
    num_trials = 13
    sensor.led = True  # Turn on White LED
    for _ in range(num_trials):
        channels[0] += sensor.channel_415nm
        channels[1] += sensor.channel_445nm
        channels[2] += sensor.channel_480nm
        channels[3] += sensor.channel_515nm
        channels[4] += sensor.channel_555nm
        channels[5] += sensor.channel_590nm
        channels[6] += sensor.channel_630nm
        channels[7] += sensor.channel_680nm
        channels[8] += sensor.channel_nir  # 910nm
    sensor.led = False  # Turn off White LED

    # Calculate average reading per channel over all trials
    for i in range(n):
        channels[i] /= num_trials
        
    # Transfer data over USB
    pixel_builtin.fill((255, 255, 0))  # YELLOW
    usb_writeline(ser, n)  # number of samples
    for val in channels:
        usb_writeline(ser, val)  # samples list
    pixel_builtin.fill((0, 255, 0))  # Green


while True:
    cmd = ser.readline().strip().decode("utf-8")
    if cmd == "r":
        read_samples()
