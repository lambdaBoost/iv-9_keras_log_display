#light all filaments to check voltage regulator

from iv9 import display_digits_slow
from machine import Pin
from sr_74hc595_bitbang import SR
from time import sleep


ser = Pin(16, Pin.OUT)
rclk = Pin(15, Pin.OUT)
srclk = Pin(2, Pin.OUT)

oe = Pin(0, Pin.OUT, value=0)    # low enables output
srclr = Pin(32, Pin.OUT, value=1) # pulsing low clears data
sr = SR(ser, srclk, rclk, srclr, oe)

if __name__ == "__main__":
    
    display_digits_slow([8,8,8,8,8,8],1,sr)
