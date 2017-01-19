import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.IN)

try:
    while True:
        if GPIO.input(10):
            print("LED an")
            GPIO.output(8, True)
        else:
            print("LED aus")
            GPIO.output(8, False)
        sleep(0.1)
finally:
    GPIO.cleanup()
