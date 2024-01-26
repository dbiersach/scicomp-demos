"""
	Example: P1AM-200 Helpers

    This example demonstrates the use of the helper functions in p1am_200_helpers.py
    These functions are designed to make it easier to use the P1AM-200 and shields by
    simplifying the initialization of devices.

    If you are not using the P1AM-ETH, change the line "if True:" to "if False:" by the 
    Ethernet section of the code.

	 _____  _____
	|  P  ||  S  |
	|  1  ||  L  |
	|  A  ||  O  |
	|  M  ||  T  |
	|  -  ||     |
	|  2  ||  0  |
	|  0  ||  1  |
	|  0  ||     |
	 ¯¯¯¯¯  ¯¯¯¯¯
	Written by FACTS Engineering
	Copyright (c) 2023 FACTS Engineering, LLC
	Licensed under the MIT license.

"""


import time
import random
import p1am_200_helpers as helper
from rs485_wrapper import RS485


def main():

    # Toggle switch
    switch = helper.get_switch() # get switch object
    print(f"Switch is {'on' if switch.value else 'off'}") # print switch state

    # LED
    led = helper.get_led() # get LED object
    led.value = True

    # RTC
    rtc = helper.get_rtc()
    print(rtc_format_time(rtc)) # print current time

    # Ethernet
    if True: # change to false if not using the P1AM-ETH
        eth = helper.get_ethernet(dhcp=True) # get ethernet object
        print(f"IP Address is: {eth.pretty_ip(eth.ip_address)}") # print IP address
        helper.sync_rtc(-4) # sync RTC with NTP server, offset by -4 hours for EST
        print(rtc_format_time(rtc)) # print current time

    # EEPROM
    eeprom = helper.get_eeprom()
    print(f"MAC Address is: {eeprom.read_mac_address()}") # Print MAC Address
    eeprom[0] = 1 # Set EEPROM address 0 to 1
    print(f"EEPROM address 0 is {eeprom[0]}")

    # P1AM-Serial
    # RS232 returns the UART object
    rs232 = helper.get_serial(1, mode=232, baudrate=9600, settings="8N1") # get serial object for port 1
    rs232.write(b"hello world\r\n")

    # RS485 returns the UART object and the DE pin 
    port2, port2_de = helper.get_serial(2, mode=485, baudrate=115200) # get serial object for port 2
    rs485 = RS485(port2, port2_de)
    rs485.write(b"hello world\r\n")

    # uSD Card
    try:
        helper.mount_sd("/sd") # mount drive with path /sd
        with open("/sd/test.txt", "w+") as f:
            f.write("Hello world!\r\n") 
        helper.unmount_sd() # unmount card
    except OSError as e:
        print(e) # No SD card inserted

    #Neopixel-compatible RGB LED
    pixel = helper.get_neopixel() # get neopixel object
    last_colors = [255, 255, 255] # 8-bit RGB color 
    pixel.brightness = 0.1 # Brightness level

    last_time = time.monotonic() # get current time
    # Infinite loop cycling between random colors
    while True:
        led.value = switch.value # set LED to switch state
        
        colors = [random.randint(0, 255) for _ in range(3)]
        difs = [colors[i] - last_colors[i] for i in range(3)]
        max_dif = max(abs(difs[i]) for i in range(3))

        for _ in range(max_dif):
            for i in range(3):
                last_colors[i] += difs[i] / max_dif
            pixel[0] = [int(color) for color in last_colors] # Write to neopixel
            time.sleep(.01)

        if time.monotonic() - last_time > 5: # Every 5 seconds, print current time
            t = rtc.datetime
            print(f"{t.tm_hour % 12}:{t.tm_min:02}:{t.tm_sec:02}")
            last_time = time.monotonic()
        

def rtc_format_time(rtc):
    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    t = rtc.datetime
    current = f"The date is {days[int(t.tm_wday)]} {t.tm_mon:02}/{t.tm_mday}/{t.tm_year} "
    current += f"The time is {t.tm_hour:02}:{t.tm_min:02}:{t.tm_sec:02}"
    return current


main() # run main function