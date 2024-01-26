# rc_circuit.py

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


# Send parameters and start experiment
num_samples = 1000  # for seperate charge and discharge periods
params = f"{num_samples}"
usb_writeline(params)
print("RC Circuit experiment is running...")

# Read from MCU the number of samples
n = int(usb_readline())

# Declare numpy arrays to store the samples
times = np.zeros(n, float)
volts = np.zeros(n, float)

# Read from MCU the times and volts samples into arrays
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
# Find the middle time value
mid_time = times[n // 2]

# Scale volts to fall between 0 and 3.3V
volts *= 3.3 / 65535

# Calculate theoretical performance curve
V_s = 3.3  # Volts
R = 10_121  # Ohms
C = 0.00001069  # Farads
t = np.linspace(0, mid_time, 100)
v_c = V_s * (1 - np.exp(-t / (R * C)))  # Charge
v_d = v_c[-1] * np.exp(-t / (R * C))  # Decay

# Create a plot window with a black background
plt.figure("rc_decay.py")
plt.gca().set_facecolor("black")

# Plot theoretical voltage
plt.plot(t, v_c, color="cyan", linewidth=2, label="Theory")
plt.plot(t + mid_time, v_d, color="cyan", linewidth=2)

# Plot actual voltage vs time
plt.plot(times, volts, color="magenta", linewidth=2, label="Actual")

# Draw the "middle" time vertical line
plt.axvline(mid_time, color="yellow", linestyle="dotted")

# Give the graph a title, axis labels, and display the legend & grid
plt.title("Capacitor Voltage vs. Time")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.ylim(0, 3.4)  # Plot voltage up to 3.4 V
plt.legend()
plt.grid(which="both", color="gray", linestyle="dotted", alpha=0.5)

# Set tick marks
plt.gca().xaxis.set_major_locator(MaxNLocator(11))
plt.gca().xaxis.set_major_formatter(FormatStrFormatter("%.3f"))
plt.gca().xaxis.set_minor_locator(AutoMinorLocator(5))
plt.gca().yaxis.set_minor_locator(AutoMinorLocator(5))

plt.show()
