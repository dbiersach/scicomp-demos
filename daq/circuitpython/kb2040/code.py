# debouncer_test

# import time
import board
import digitalio
import neopixel
from adafruit_debouncer import Debouncer

# last_time = time.monotonic()

pixel_builtin = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel_builtin.brightness = 0.2
pixel_builtin.fill((0, 0, 0))

pixel_ext = neopixel.NeoPixel(board.D10, 1)
pixel_ext.brightness = 0.2
pixel_ext.fill((0, 0, 0))
pixel_state = False

pin_raw = digitalio.DigitalInOut(board.D5)
pin_raw.direction = digitalio.Direction.INPUT
pin_raw.pull = digitalio.Pull.UP
pin_button = Debouncer(pin_raw)

while True:
    pin_button.update()
    if pin_button.fell:
        pixel_state = not pixel_state

    if pixel_state:
        pixel_ext.fill((0, 0, 255))
    else:
        pixel_ext.fill((0, 0, 0))
