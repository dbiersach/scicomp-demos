# sig_gen.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import FormatStrFormatter
import serial
import adafruit_board_toolkit.circuitpython_serial

# Open the USB data port
cdc_data = adafruit_board_toolkit.circuitpython_serial.data_comports()[0]
ser = serial.Serial(None, 115200, 8, "N", 1, timeout=120)
ser.port = cdc_data.device
ser.open()


def usb_readline():
    return ser.readline().decode("utf-8").strip()


def usb_writeline(x):
    ser.write(bytes(str(x) + "\n", "utf-8"))
    ser.flush()


# Set experiment parameters
num_samples = 2000
freq = 5  # Wave frequency in Hz
wave_type = "sine"  # Also "triangle" and "square"

# Send to MCU the command to run the experiment
params = f"{num_samples},{freq},{wave_type}"
usb_writeline(params)
print("Signal Generator experiment is running...")

# Read from MCU the times and volts samples into arrays
n = int(usb_readline())
times = np.zeros(n, float)
volts = np.zeros(n, float)
for i in range(n):
    times[i] = int(usb_readline())
for i in range(n):
    volts[i] = int(usb_readline())
print(f"Received {n} time and volt samples...")
ser.close()

# Set times to be elapsed time since experiment stared
times -= times[0]  # first value is time since MCU booted
# Scale to seconds
times *= 1e-9  # time from MCU is in nanoseconds

# Scale volts to fall between 0 and 3.3V
volts *= 3.3 / 65535

# Create a plot window with a black background
plt.figure("sig_gen.py")
plt.gca().set_facecolor("black")

# Plot actual voltage vs time
plt.plot(times, volts, color="magenta", linewidth=2)

# Give the graph a title, axis labels, and display the grid
plt.title("AD9833 Signal Generator")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.grid(which="both", color="gray", linestyle="dotted", alpha=0.5)

# Set tick marks
plt.gca().xaxis.set_major_locator(MaxNLocator(11))
plt.gca().xaxis.set_major_formatter(FormatStrFormatter("%.3f"))
plt.gca().xaxis.set_minor_locator(AutoMinorLocator(5))
plt.gca().yaxis.set_minor_locator(AutoMinorLocator(5))

plt.show()
