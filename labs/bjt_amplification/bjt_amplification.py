# bjt_amplification.py

import numpy as np
import matplotlib.pyplot as plt
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
num_samples = 200
step_size = 5
params = f"{num_samples},{step_size}"
usb_writeline(params)
print("Transistor Amplification experiment is running...")

# Read from MCU the number of samples
n = int(usb_readline())

# Declare numpy arrays to store the samples
volts_be = np.zeros(n, float)
volts_ce = np.zeros(n, float)

# Read from MCU the BE volt and CE volt samples into arrays
for i in range(n):
    volts_be[i] = int(usb_readline())
for i in range(n):
    volts_ce[i] = int(usb_readline())
print(f"Received {n} BE volt and CE volt samples...")
ser.close()

# Scale volts to fall between 0 and 3.3V
volts_be *= 3.3 / 4096
volts_ce *= 3.3 / 65535

volts_be = volts_be + 0.65 # VBE voltage drop is ~650mV
volts_ce = 3.3 - volts_ce # VCE voltage drop increases as BJT amplifies

# Plot the transistor amplification curve
plt.figure("bjt_amplification.py")
plt.gca().set_facecolor("black")
plt.plot(volts_be, volts_ce, color="yellow", linewidth=2)

plt.title("PN2222A (NPN) BJT Amplification")
plt.xlabel("Base-Emitter Voltage (V)")
plt.ylabel("Collector-Emitter Voltage (V)")
plt.grid(which="both", color="gray", linestyle="dotted", alpha=0.5)
plt.show()
