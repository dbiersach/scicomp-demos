"""measure_reflectance.py"""

import numpy as np
import matplotlib.pyplot as plt

import serial
import traceback
import sys

# AS7341 Channel Wavelengths
# 0 = 415nm : Violet
# 1 = 445nm : Indigo
# 2 = 480nm : Blue
# 3 = 515nm : Cyan
# 4 = 555nm : Green
# 5 = 590nm : Yellow
# 6 = 630nm : Orange
# 7 = 680nm : Red
# 8 = 910nm : Near-IR


def wavelength_to_rgb(wavelength, gamma=0.8):
    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        r = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        g = 0.0
        b = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        r = 0.0
        g = ((wavelength - 440) / (490 - 440)) ** gamma
        b = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        r = 0.0
        g = 1.0
        b = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        r = ((wavelength - 510) / (580 - 510)) ** gamma
        g = 1.0
        b = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        r = 1.0
        g = (-(wavelength - 645) / (645 - 580)) ** gamma
        b = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        r = (1.0 * attenuation) ** gamma
        g = 0.0
        b = 0.0
    else:
        r = 0.0
        g = 0.0
        b = 0.0
    return (r, g, b)


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

        # Save samples to data file
        print("Enter the sample name: ", end=" ")
        sample_name = input()
        file_name = sample_name + ".csv"
        np.savetxt(file_name, channels, fmt="%6.3f", delimiter=", ")
        print(f"{file_name} created.")

        wavelengths = [415, 445, 480, 515, 555, 590, 630, 680, 910]
        colors = []
        for wavelength in wavelengths:
            r, g, b = wavelength_to_rgb(wavelength)
            colors.append((r, g, b))

        # Create plot window
        plt.figure(__file__)
        ax = plt.axes()
        ax.bar(wavelengths, channels, color=colors, width=5)
        ax.set_title(f"Spectrophotometry ({sample_name})")
        ax.set_xlabel("Wavelength (mm)")
        ax.set_ylabel("% Reflectance Level (Normalized)")
        ax.figure.savefig(sample_name + ".png")
        plt.show()

    except:
        print("Error with MCU serial I/O")
        traceback.print_exc()

    if ser.is_open:
        # Close the serial port connection to the MCU
        ser.close()


main()
