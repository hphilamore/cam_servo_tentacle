import serial
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

print("start")

port = serial.Serial("/dev/ttyS0", baudrate=1000000, timeout=3.0)

print("go")

for i in range(10):
    
    GPIO.output(18, GPIO.HIGH)
    port.write(bytearray.fromhex("FF FF 00 05 03 20 FF 00 D8"))
    time.sleep(0.1)
    GPIO.output(18, GPIO.LOW)
    time.sleep(3)
    
    print("next")