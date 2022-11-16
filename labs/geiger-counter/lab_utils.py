# lab_utils.py

import os
import sys

import numpy as np
import serial
import traceback

class DataFile:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.folder_path = os.path.dirname(os.path.realpath("__file__"))
        self.file_path = os.path.join(self.folder_path, self.file_name)

    def create_slots(self, number_slots: int):
        # Delete existing datafile if it exists
        if os.path.isfile(self.file_path):
            os.remove(self.file_path)

        # Pre-create slots with an intitial value of zero
        slots = [0] * (number_slots + 1)

        # Save initialized datafile
        np.savetxt(self.file_path, slots, fmt="%i")

    def update_slot(self, slot_num, value):
        # Provide feedback to user
        print(f"Run # {slot_num}, counts per minute = {value:>5,}")
        
        # Update datafile with value for given slot
        counts = np.genfromtxt(f"{self.file_path}", delimiter=",")
        counts[slot_num] = value
        np.savetxt(self.file_path, counts, fmt="%i")


class GeigerCounter:
    def __init__(self):
        pass

    def get_count():
        print(f"Measuring counts (decay events) over 30 seconds...")

        count = -1

        # Connect to the MCU based upon local OS
        ser = serial.Serial(None, 115200, 8, "N", 1, timeout=120)
        try:
            port = "COM4"
            if sys.platform == "linux":
                port = "/dev/ttyAMA0"
            if sys.platform == "darwin":
                port = "/dev/tty.usbserial-110"

            ser.port = port
            ser.open()

            # Send MCU the command to (r)un the experiment
            ser.write(b"run_geiger_counter\n")

            # Wait until the MCU responds with the detector count
            count = int(ser.readline().strip())

            # Adjust count units to be per minute
            count = count * 2

        except:
            print("Error with GeigerCounter I/O")
            traceback.print_exc()

        if ser.is_open:
            # Close the serial port connection to the MCU
            ser.close()

        return count
