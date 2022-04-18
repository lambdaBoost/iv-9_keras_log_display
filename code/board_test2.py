from machine import Pin
from sr_74hc595_bitbang import SR
from time import sleep

ser = Pin(16, Pin.OUT)
rclk = Pin(15, Pin.OUT)
srclk = Pin(2, Pin.OUT)

oe = Pin(0, Pin.OUT, value=0)    # low enables output
srclr = Pin(32, Pin.OUT, value=1) # pulsing low clears data

sr = SR(ser, srclk, rclk, srclr, oe)

s1 = Pin(14, Pin.OUT)
s2 = Pin(17, Pin.OUT)
s3 = Pin(18, Pin.OUT)
s4 = Pin(19, Pin.OUT)
s5 = Pin(21, Pin.OUT)
s6 = Pin(22, Pin.OUT)
s7 = Pin(23, Pin.OUT)

pins = [s1,s2,s3,s4,s5,s6,s7]




def display_digits(num_list, dp, shift_reg):
    """
displays a list of digits to numitron. Arguments:

num_list - list of single digits to display
dp - index of dp
shift_reg - shift register object from sr_74hc595 library

"""

    
    d = {0:0b11111100,
             1:0b00001100,
             2:0b11011010,
             3:0b11110010,
             4:0b01100110,
             5:0b10110110,
             6:0b10111110,
             7:0b11100000,
             8:0b11111110,
             9:0b11110110,
             0:0b11111100,
             'blank':0b00000000}
    
    #reverse the list so least sig digit is displayed first
    num_list.reverse()
    
    i=0
    for num in num_list:
        val = d[num]
        
        #add decimal place if correct index
        if(i==dp):
            val = val+1
        
        shift_reg.bits(val,8)
        
        if num_list == ['blank']*6:
            sleep(0.5)
        else:
            sleep(1)
        
        
        i=i+1
        
        shift_reg.latch()
        
    


display_digits([1,2,3,4,5,6],2,sr)