import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

while True:
    
    GPIO.output(8,True)
    sleep(1)
    GPIO.output(10,True)
    sleep(1)
    GPIO.output(8,False)
    GPIO.output(10,False)
    GPIO.output(12,True)
    sleep(1)
    GPIO.output(12,False)
    GPIO.output(10,True)
    sleep(1)
    GPIO.output(10,False)
GPIO.cleanup()
