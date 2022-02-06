#!/usr/bin/env python3
# get_geiger_counts.py

import numpy as np
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

    # Send MCU the command to (r)un the experiment
    ser.write(b"r")

    # Wait until the MCU responds with the detector count
    count = int(ser.read_until())

    # Determine the path to the CSV file
    file_name = "counts.csv"
    folder_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(folder_path, file_name)

    # Append the count from this run to the array of prior counts
    if not os.path.isfile(file_path):
        counts = np.array(count).reshape(1)
    else:
        counts = np.genfromtxt(f"{file_path}", delimiter=",")
        counts = np.append(counts, count)
        
    # Display counts
    for i, v in enumerate(counts):
        print(f"Run {i + 1}: Count = {int(v):6,}")
    
    # Save the new CSV file as list of integers
    np.savetxt(file_path, counts, fmt="%i")


if __name__ == "__main__":
    main()
