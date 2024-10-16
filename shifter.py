import RPi.GPIO as GPIO
import time

class Shifter:
    def __init__(self, dataPin, latchPin, clockPin):
        self.dataPin = dataPin
        self.latchPin = latchPin
        self.clockPin = clockPin
        
    def __ping(self,p):
        GPIO.output(p,1)
        time.sleep(0.001)
        GPIO.output(p,0)
        
    def shiftByte(self, b): # send a byte of data to the output
        for i in range(8):
            GPIO.output(self.dataPin, b & (1<<i))
            self.__ping(self.clockPin) # add bit to register
        self.__ping(self.latchPin) # send register to output