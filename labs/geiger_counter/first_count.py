# first_count.py

import numpy as np
import serial
import traceback
import sys


def usb_readline(usb_data_port):
    s = usb_data_port.readline().decode("ASCII").strip()
    return s


ser = serial.Serial(None, 115200, 8, "N", 1, timeout=120)
try:
    # Open the USB data port
    port = "COM3"
    if sys.platform == "linux":
        port = "/dev/ttyACM1"
    if sys.platform == "darwin":
        port = "/dev/tty.usbserial-110"
    ser.port = port
    ser.open()

    # Send to MCU the command to (r)un the experiment
    ser.write(b"r\n")
    ser.flush()
    print("Geiger Counter experiment is running...")

    # Read from MCU the number of ticks
    ticks = int(usb_readline(ser))
    print(f"Received {ticks:,} ticks...")

    # Create new data file with this row
    counts = np.array([[0, ticks]])
    np.savetxt("counts.csv", counts, delimiter=",", fmt="%i")
    print("Created new data file...")
    print(counts)


except:
    print("Error with MCU serial I/O")
    traceback.print_exc()

if ser.is_open:
    # Close the serial port connection to the MCU
    ser.close()
