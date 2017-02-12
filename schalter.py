import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(26, GPIO.IN)

zustand = False
taster = False

try:
    while True:
        if GPIO.input(26) and not(taster):
            zustand = not(zustand)
            taster = True
            if zustand:
                print("LED an")
            else:
                print("LED aus")
        elif not(GPIO.input(26)) and taster:
            taster = False
        
        GPIO.output(22, zustand)
        sleep(0.1)
finally:
    GPIO.cleanup()
