import board
import busio
import digitalio
import adafruit_rfm9x
import time

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
reset = digitalio.DigitalInOut(board.D18)
cs = digitalio.DigitalInOut(board.D20)
rfm9x = adafruit_rfm9x.RFM9x(spi, cs, reset, 915.0)
rfm9x.tx_power = 23
i = 0

rfm9x.send(check_4)
while True:
	i=i+1
	packet = rfm9x.receive(timeout=5.0)
	if packet is not None:
		packet_text = str(packet, "ascii")
		print("Received: {0}".format(packet_text))
		print("")
		print(f"Sending back: {packet_text}")
		print("")
		rfm9x.send(packet_text)
		time.sleep(.01)
	elif packet is None:
		print("None"+"("+str(i)+")")
		time.sleep(.01)
	if i>=24:
		break   