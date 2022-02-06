#!/usr/bin/env python3
# get_field_strength.py

import os, serial, time
import sys


def main():
    print("Running...")

    # Open the data file
    file_name = "strength.csv"
    folder_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(folder_path, file_name)
    text_file = open(file_path, "wt", newline="\n")
    print(f"Saving readings to {file_path}")

    # Connect to MCU
    port = "COM3"
    if sys.platform == "linux":
        port = "/dev/ttyUSB0"
    if sys.platform == "darwin":
        port = "/dev/tty.usbserial-110"
    ser = serial.Serial(port, 115200, 8, "N", 1, timeout=120)
    time.sleep(2)

    # Send MCU command to (r)un the experiment
    ser.write(b"r")

    # Read 512 strength indicators from the MCU
    for i in range(512):
        reading = ser.read_until().decode("utf-8").rstrip()
        print(reading)
        text_file.write(reading + "\n")
        text_file.flush()

    text_file.close()
    print(f"Saved readings to {file_path}")


if __name__ == "__main__":
    main()
