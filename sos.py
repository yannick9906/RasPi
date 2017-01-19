import RPi.GPIO as GPIO
from time import sleep
from time import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.IN)

zustand = 0
taster = False
morse = [1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,0,0,0]
starttime = 0

try:
    while True:
        if GPIO.input(10) and not(taster):
            if zustand < 2:
               zustand += 1
            else:
               zustand = 0
            taster = True
            if zustand == 1:
                print("LED an")
                GPIO.output(8, True)
            elif zustand == 2:
                print("SOS")
                starttime = time() 
            else:
                GPIO.output(8, False)
                print("LED aus")
        elif not(GPIO.input(10)) and taster:
            taster = False
        if zustand == 2:
            elapsed = time()-starttime
            currIndex = int((elapsed//0.5)%len(morse))
            GPIO.output(8, morse[currIndex]==1)
        sleep(0.1)
finally:
    GPIO.cleanup
