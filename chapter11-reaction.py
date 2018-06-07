import RPi.GPIO as GPIO
import time
import random
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)  # signal output port
GPIO.setup(4, GPIO.IN)  # signal input port

GPIO.output(22, False)  # set default state
random.seed()

while True:
    time.sleep(random.random() * 10)
    start = datetime.now()
    GPIO.output(22, True)
    while not GPIO.input(4):
        pass
    print("Your reaction time: ", (datetime.now() - start).total_seconds())
    print("Get ready to try again.")
    GPIO.output(22, False)
