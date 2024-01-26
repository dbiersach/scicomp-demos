# geiger_counter for KB2040


import analogio
import board
import digitalio
import neopixel
import time
import supervisor
import usb_cdc
import countio

# Wait until USB console port is ready
while not supervisor.runtime.usb_connected:
    pass

# Create USB data port
ser = usb_cdc.data

# Configure NeoPixel
pixel_builtin = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel_builtin.brightness = 0.1
pixel_builtin.fill((0, 255, 0))  # GREEN


def usb_writeline(usb_data_port, x):
    usb_data_port.write(bytes(str(x) + "\n", "utf-8"))
    usb_data_port.flush()


def read_samples():
    # Count Geiger Tube ticks for 10 seconds
    pixel_builtin.fill((255, 0, 0))  # RED
    pin_tick = countio.Counter(board.A3, edge=countio.Edge.FALL)
    time.sleep(20)

    # Send number of ticks over USB
    pixel_builtin.fill((255, 255, 0))  # YELLOW
    usb_writeline(ser, pin_tick.count)

    # Return to ready state
    pin_tick.deinit()
    pixel_builtin.fill((0, 255, 0))  # GREEN


while True:
    cmd = ser.readline().strip().decode("utf-8")
    if cmd == "r":
        read_samples()
