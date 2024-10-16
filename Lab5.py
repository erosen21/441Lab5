import RPi.GPIO as GPIO
from shifter import Shifter
import time
import random

class Bug:
    def __init__(self, timestep = 0.1, x = 3, isWrapOn = False):
        self.timestep = timestep
        self.x = x
        self.isWrapOn = isWrapOn
        self.__shifter = Shifter(23, 24, 25)
        
    def shift(self,p):
        walk = ['0'] * 10
        walk[1] = 'b'
        walk[p+2] = '1'
        self.__shifter.shiftByte(int("".join(walk),2))
        
    def start(self):
        self.shift(self.x)
        mover = random.choice([-1, 1])
        if self.x + mover >=0 and self.x + mover < 8 and self.isWrapOn==False:
            self.x += mover
            time.sleep(self.timestep)
        if self.isWrapOn==True:
            self.x += mover
            if self.x == -1:
                self.x = 7
            if self.x == 8:
                self.x = 0
            time.sleep(self.timestep)
            
    def stop(self):
        self.__shifter.shiftByte(0b00000000)
        

GPIO.setmode(GPIO.BCM)
dataPin, latchPin, clockPin = 23, 24, 25
x = 4

GPIO.setup(dataPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT, initial=0)  # start latch & clock low
GPIO.setup(clockPin, GPIO.OUT, initial=0)

#s1 = Shifter(dataPin, latchPin, clockPin)
