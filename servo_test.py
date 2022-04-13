#https://pypi.org/project/pyax12/
from pyax12.connection import Connection
import RPi.GPIO as GPIO
GPIO.setwarnings(False) 

# Connect to the serial port
serial_connection = Connection(port="/dev/ttyS0", rpi_gpio=True)

dynamixel_id = 1

# Ping the third dynamixel unit
is_available = serial_connection.ping(dynamixel_id)

print(is_available)

# print("done")
# # Close the serial connection
# serial_connection.close()

