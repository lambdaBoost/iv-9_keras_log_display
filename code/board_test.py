from machine import Pin
from sr_74hc595_bitbang import SR
from time import sleep

ser = Pin(16, Pin.OUT)
rclk = Pin(15, Pin.OUT)
srclk = Pin(2, Pin.OUT)

oe = Pin(0, Pin.OUT, value=0)    # low enables output
srclr = Pin(32, Pin.OUT, value=1) # pulsing low clears data

sr = SR(ser, srclk, rclk, srclr, oe)

def display_digit(num, dp, shift_reg):
    
    d = {0:0b11111100,
             1:0b00001100,
             2:0b11011010}
    
    shift_reg.bits(d[num],8)
    shift_reg.latch()


while True:
    display_digit(0,False,sr)
    sleep(1)
    display_digit(1,False,sr)
    sleep(1)
    display_digit(2,False,sr)
    sleep(1)
    


