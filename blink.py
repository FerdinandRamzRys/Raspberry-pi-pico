# Import library for everytype variables like random, time and for the circuit
from time import sleep
from machine import Pin

# Principal function to switch the blink of leds
def change(num,t1):
    led[num].value(1)
    sleep(t1)
    led[num].value(0)

# Dictionary for the output in order to choice the led 
led={0: Pin(15, Pin.OUT), 1: Pin(14, Pin.OUT), 2: Pin(13, Pin.OUT)}
# Input variable for the push-buttom
inpt = Pin(12, Pin.IN, Pin.PULL_DOWN)

# Initialize the loop for the leds
while True:
    led[2].value(1) if inpt.value() == 1 else led[2].value(0)
    
    change(1,0.1)
    change(0,0.1)
