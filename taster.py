import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(26, GPIO.IN)

try:
    while True:
        if GPIO.input(26):
            print("LED an")
            GPIO.output(22, True)
        else:
            print("LED aus")
            GPIO.output(22, False)

        sleep(0.1)
finally:
    GPIO.cleanup()
