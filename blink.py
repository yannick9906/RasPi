import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
while True:
    GPIO.output(10,True)
    sleep(0.01)
    GPIO.output(10,False)
    sleep(0.01)
GPIO.cleanup()
