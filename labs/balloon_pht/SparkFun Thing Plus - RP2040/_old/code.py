# ground

#from socket import timeout
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

def main():
    print("Ground running!")
    i=0
    print("Initiating GPS...")
    check_1= input()
    rfm9x.send(check_1)
    
    print("")
    print("Checking GPS... ")
    gps_check = rfm9x.receive(timeout=1000000000.0)
    if gps_check is not None:
        gps_check_text = str(gps_check, "ascii")
        print("Received: {0}".format(gps_check_text))
    check_2= input()
    rfm9x.send(check_2)

    print("")
    print("Enabling IMU...")
    print("Checking IMU... ")
    imu_check = rfm9x.receive(timeout=1000000000.0)
    if imu_check is not None:
        imu_check_text = str(imu_check, "ascii")
        print("Received: {0}".format(imu_check_text))
    check_3= input()
    rfm9x.send(check_3)

    print("")
    print("Ready for Lift Off... ")
    check_4= input()
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
        
main()


