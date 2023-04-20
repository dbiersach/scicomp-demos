import board
import digitalio
import storage
import usb_cdc
import usb_hid
import usb_midi

usb_hid.disable()
usb_midi.disable()

button = digitalio.DigitalInOut(board.D5)
button.pull = digitalio.Pull.DOWN

# Note: Connect GPIO pin D5 to +3.3V (HIGH)
# to re-enable CIRCUITPY drive and REPL serial port

if not button.value:
    usb_cdc.disable()
    storage.disable_usb_drive()

    usb_cdc.enable(console=False, data=True)
    storage.enable_usb_drive()
