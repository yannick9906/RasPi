import RPi.GPIO as GPIO
from time import sleep
from time import time

pinIn = 26
pinOut1 = 17
pinOut2 = 27
pinOut3 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinOut1, GPIO.OUT)
GPIO.setup(pinOut2, GPIO.OUT)
GPIO.setup(pinOut3, GPIO.OUT)
GPIO.setup(pinIn, GPIO.IN)

ampel = [[1,0,0],[1,1,0],[0,0,1],[0,1,0]]
currIndex = 0
taster = False

try:
    while True:
        if GPIO.input(pinIn) and not(taster):

            if ampel[currIndex][0] == 1:
                GPIO.+
            currIndex += 1
            taster = True
        elif not(GPIO.input(pinIn)) and taster:
            taster = False
        if zustand == 2:
            elapsed = time()-starttime
            currIndex = int((elapsed//0.5) % len(morse))
            GPIO.output(22, morse[currIndex]==1)
        sleep(0.1)
finally:
    GPIO.cleanup
