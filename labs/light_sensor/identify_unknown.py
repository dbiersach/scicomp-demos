"""identify_unknown.py"""

 import numpy as np
from pathlib import Path

import serial
import traceback
import sys

def sum_rel_errors(observed, expected):
    rel_err = 0.0
    for n in range(len(observed)):
        # Relative error = Absolute Error / Known Value
        rel_err += abs(observed[n] - expected[n]) / expected[n]
    return rel_err

def usb_readline(usb_data_port):
    s = usb_data_port.readline().decode("ASCII").strip()
    return s

def main():    
    ser = serial.Serial(None, 115200, 8, "N", 1, timeout=120)
    try:        
        port = "COM3"
        if sys.platform == "linux":
            port = "/dev/ttyAMA0"
        if sys.platform == "darwin":
            port = "/dev/tty.usbserial-110"

        ser.port = port
        ser.open()

        # Send MCU the command to (r)un the experiment
        ser.write(b"r\n")
        print("Measuring light sensor values...")

        # Read number of samples from USB
        n = int(usb_readline(ser))

        # Declare numpy arrays to store the samples
        channels = np.zeros(n, float)

        # Read samples from USB into array
        for i in range(n):
            channels[i] = float(usb_readline(ser))

        # Normalize sample data
        max_reading = channels.max()
        channels = channels / max_reading * 100

        # Compare this unknown sample to existing sample data files
        sample_names = []
        sample_scores = []
        samples_folder = Path(__file__).parent / "samples"        
        for sample_file in samples_folder.iterdir():
            sample_names.append(sample_file.stem)
            sample_data = np.genfromtxt(sample_file, delimiter=",")            
            sample_scores.append(sum_rel_errors(channels, sample_data))
    
        # Print sample names by increasing score (lower is better)
        print(f"{'Sample':<32}{'Score':>7}")
        print(f"{'------':<32}{'-----':>7}")
        sorted_scores = np.argsort(sample_scores)
        for i in range(len(sorted_scores)):
            k = sorted_scores[i]
            print(f"{sample_names[k]:<32}{sample_scores[k]:>7.4f}")
            
        # Display the known sample having the least difference to the unknown sample
        match_index = sample_scores.index(min(sample_scores))
        print(f"\nBest match: {sample_names[match_index]}")
            

        

    except:
        print("Error with MCU serial I/O")
        traceback.print_exc()

    if ser.is_open:
        # Close the serial port connection to the MCU
        ser.close()


main()
