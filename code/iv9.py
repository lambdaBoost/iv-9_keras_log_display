from machine import Pin
from sr_74hc595_bitbang import SR
from time import sleep




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
        sleep(1)
        i=i+1
        
        shift_reg.latch()
        





