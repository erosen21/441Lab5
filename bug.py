from shifter import Shifter
from Lab5 import Bug
import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
s1 = 17
s2 = 27
GPIO.setup(s1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(s2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

bug_init = Bug()

try:
    while 1:
        state1 = GPIO.input(s1)
        state2 = GPIO.input(s2)
        if state1 == 0:
            bug_init.stop()
            time.sleep(.1)
        if state1 == 1 and state2 == 0:
            bug_init.isWrapOn = True
            bug_init.start()
        if state1 == 1 and state2 == 1:
            bug_init.isWrapOn = False
            bug_init.start()
                  
except:
    GPIO.cleanup()
        
