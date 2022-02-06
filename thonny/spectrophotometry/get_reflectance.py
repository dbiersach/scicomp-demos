#!/usr/bin/env python3
# get_reflectance.py

import os, serial, time
import sys


def main():
    print("Running...")

    # Connect to the MCU
    port = "COM3"
    if sys.platform == "linux":
        port = "/dev/ttyUSB0"
    if sys.platform == "darwin":
        port = "/dev/tty.usbserial-110"
    ser = serial.Serial(port, 115200, 8, "N", 1, timeout=120)
    time.sleep(2)

    # Send MCU command to (r)un the experiment
    ser.write(b"r")

    # Wait until the MCU responds with the detector readings
    readings = ser.read_until().decode("utf-8").rstrip()
    print(f"Readings = {readings}")

    # Determine the path to the CSV file
    file_name = "Unknown.csv"
    folder_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(folder_path, file_name)

    # Save the readings to the CSV file
    text_file = open(file_path, "wt", newline="\n")
    text_file.write(readings + "\n")
    text_file.flush()
    text_file.close()
    print(f"Saved readings to {file_path}")


if __name__ == "__main__":
    main()
