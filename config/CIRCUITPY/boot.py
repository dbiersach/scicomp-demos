import usb_cdc
import usb_hid
import usb_midi
usb_midi.disable()
usb_hid.disable()
storage.disable_usb_drive()
usb_cdc.enable(console=True, data=True)
print("BNL SciComp-Demos")

