import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.IN)

zustand = False

try:
    while True:
        if GPIO.input(10) != zustand:
            GPIO.output(8, not(zustand))
            zustand = not(zustand)
            if zustand:
                print("LED an")
            else:
                print("LED aus")
        sleep(0.1)
finally:
    GPIO.cleanup()
