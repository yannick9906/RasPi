import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.IN)

zustand = False
taster = False

try:
    while True:
        if GPIO.input(10) and not(taster):
            zustand = not(zustand)
            taster = True
            if zustand:
                print("LED an")
            else:
                print("LED aus")
        elif not(GPIO.input(10)) and taster:
            taster = False
        
        GPIO.output(8, zustand)
        sleep(0.1)
finally:
    GPIO.cleanup()
