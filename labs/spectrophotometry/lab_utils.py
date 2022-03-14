# lab_utils.py

import os
import sys

import numpy as np
import serial
import traceback
import time


class DataFile:
    def __init__(self, sample_name: str):
        self.sample_name = sample_name
        self.file_name = sample_name + ".csv"
        self.image_name = sample_name + ".png"
        self.folder_path = os.path.dirname(os.path.realpath("__file__"))
        self.file_path = os.path.join(self.folder_path, self.file_name)
        self.image_path = os.path.join(self.folder_path, self.image_name)

    def read(self):
        return np.genfromtxt(self.file_path, delimiter=",")

    def save(self, spectra: list):
        # Delete existing datafile if it exists
        if os.path.isfile(self.file_path):
            os.remove(self.file_path)

        np.savetxt(self.file_path, spectra, fmt="%.2f")


class TriadSensor:
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

    def __init__(self):
        self.ser = None
        self.readings = None
        self.wavelengths = np.array(
            [
                "410",  # AS72653(A) - Ultraviolet
                "435",  # AS72653(B) - Violet
                "460",  # AS72653(C) - Blue
                "485",  # AS72653(D) - Cyan
                "510",  # AS72653(E) - Green
                "535",  # AS72651(F) - Green
                "560",  # AS72652(G) - Yellow Green
                "585",  # AS72652(H) - Yellow
                "610",  # AS72651(R) - Orange
                "645",  # AS72652(I) - Red
                "680",  # AS72651(S) - Red
                "705",  # AS72652(J) - Near Infrared (NIR)
                "730",  # AS72651(T) - Near Infrared (NIR)
                "760",  # AS72651(U) - Near Infrared (NIR)
                "810",  # AS72651(V) - Infrared (IR-A)
                "860",  # AS72651(W) - Infrared (IR-A)
                "900",  # AS72652(K) - Infrared (IR-A)
                "940",  # AS72652(L) - Infrared (IR-A)
            ]
        )
        # Convert wavelengths to RGB colors
        self.colors = []
        for wavelength in self.wavelengths:
            r, g, b = TriadSensor.wavelength_to_rgb(wavelength)
            self.colors.append((r, g, b))

    def send_cmd(self, cmd: str) -> str:
        # Append newline character to terminate command
        # Then convert string to bytes() array which is what pySerial expects
        cmd_with_newline = bytes(cmd, "ASCII") + bytes("\n", "ASCII")
        # Send command (Hayes Modem AT format) to device
        self.ser.write(cmd_with_newline)
        # Read status line from device, convert bytes() to ASCII, and remove whitespace
        status = self.ser.readline().decode("ASCII").strip()
        return status

    def get_spectra(self) -> list:
        print("Averaging 18-wavelength spectra over 10 runs...")
        self.readings = None
        try:
            # Connect to the SparkFun Triad Spectroscopy Sensor
            # See https://www.sparkfun.com/products/15050
            port = "COM3"
            if sys.platform == "linux":
                port = "/dev/ttyUSB0"
            if sys.platform == "darwin":
                port = "/dev/tty.usbserial-110"
            self.ser = serial.Serial(port, 115200, 8, "N", 1, timeout=120)
            time.sleep(2)  # Wait two seconds for sensor to wake up

            # Configure the sensor per the product's datasheet
            # See https://cdn.sparkfun.com/assets/learn_tutorials/8/3/0/AS7265x_Datasheet.pdf
            self.send_cmd("ATINTTIME=35")  # Set 100ms integration time
            self.send_cmd("ATGAIN=2")  # Set gain at 16x

            # Set each of the three LEDs (WHT, IR, NIR) on the sesnor
            # to use a 4mA indicator current and 500 mA driver current
            self.send_cmd("ATLEDC=0x22")  # WHT (AS72651 sensor)
            self.send_cmd("ATLEDD=0x22")  # IR  (AS72652 sensor)
            self.send_cmd("ATLEDE=0x22")  # NIR LED (AS7265 sensor)

            # Turn the blue indicator LED off on the sensor
            # and turn on the other three indicator LEDs
            self.send_cmd("ATLED0=0")  # Turn off blue indicator
            self.send_cmd("ATLED1=1")  # Turn on WHT LED
            self.send_cmd("ATLED2=1")  # Turn on IR LED
            self.send_cmd("ATLED3=1")  # Turn on NIR LED
            time.sleep(2)  # Wait two seconds sensor to warm up

            # Create list of 18 floats to hold the sum of each wavelength levels
            total_readings = [0.0] * 18

            # Perform 10 runs of the experiment
            for n in range(1, 11):
                print(f"Run #{n:>3}: ", end="")
                status = self.send_cmd("ATCDATA")  # Read all 18 wavelength levels
                # All successful commands return a string with "OK" at the end
                print(status)
                # Remove the "OK" then split the CSV string into a list of 18 floats
                readings = [float(s) for s in status.replace("OK", "").split(",")]
                # Accumulate the readings for each wavelength over each run
                for i in range(18):
                    total_readings[i] += readings[i]
                # Sleep for two seconds between each run to let sensors settle
                time.sleep(2)

            # Return Sparkfun Triad Sensor to initial condition
            self.send_cmd("ATLED1=0")  # Turn on WHT LED
            self.send_cmd("ATLED2=0")  # Turn on IR LED
            self.send_cmd("ATLED3=0")  # Turn on NIR LED
            self.send_cmd("ATLED0=1")  # Turn off blue indicator

            # Close the serial port connection to the sensor
            self.ser.close()

            # Calculate the average of each frequency level over 10 runs
            readings = np.array(total_readings) / 10

            # Reorder levels by increasing wavelength (for the histogram)
            self.readings = readings[
                [12, 13, 14, 15, 16, 17, 6, 7, 0, 8, 1, 9, 2, 3, 4, 5, 10, 11]
            ]

        except:
            print("Error with TriadSensor I/O")
            traceback.print_exc()

        if self.ser.is_open:
            # Close the serial port connection to the MCU
            ser.close()

        return self.readings
