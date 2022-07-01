# Import libraries that were used in this code converter ADC and time
from machine import ADC
from time import sleep

# Initialize the analog-digital converter
potentiometer = ADC(26) #Raspberry Pi Pico ADC0

# Start the loop to transform the value of bits to voltage
while True:   
    volts_16 = potentiometer.read_u16() * 3.3 / (65535)
    print('Value in 16 bits: {}, and volts: {:.1f}'.format(potenciometro.read_u16(), volts_16))
    sleep(0.1)
