#ssd1306 display with font sizing - based entirely on writer library by peter hinch
#available at https://github.com/peterhinch/micropython-font-to-py/tree/master/writer

import machine
from ssd1306_setup import WIDTH, HEIGHT, setup
from writer import Writer

# Font
import freesans20


def draw_tank(ssd, rhs):
    
    ssd.line(126,30,111,30,1)
    ssd.line(127,29,127,28,1)
    ssd.line(110,29,110,28,1)
    ssd.line(126,27,111,27,1)
    ssd.fill_rect(112, 26, 13, 2, 1)
    ssd.fill_rect(117, 23, 6, 3, 1)
    ssd.line(116,24,103,24,1)
    
    ssd.fill_rect(124, 28, 2,2, 1)
    ssd.fill_rect(121, 28, 2,2, 1)
    ssd.fill_rect(118, 28, 2,2, 1)
    ssd.fill_rect(115, 28, 2,2, 1)
    ssd.fill_rect(112, 28, 2,2, 1)
    

def draw_tractor(ssd,rhs):
    
    ssd.line(95,29,84,29,1)
    ssd.line(84,29,84,25,1)
    ssd.line(84,25,91,25,1)
    ssd.line(91,25,91,20,1)
    ssd.line(91,20,95,20,1)
    ssd.line(95,20,95,29,1)
    ssd.line(87,25,87,21,1)
    ssd.line(95,29,109,29,1)
    
    ssd.fill_rect(91, 28, 4,4, 1)
    ssd.fill_rect(86, 29, 3,3, 1)
    
    


def test_display(use_spi=False, string='test', tank=False, tractor=False):
    ssd = setup(use_spi)  # Create a display instance
    rhs = WIDTH -1
    #ssd.line(rhs - 20, 0, rhs, 20, 1)
    #square_side = 10
    #ssd.fill_rect(rhs - square_side, 0, square_side, square_side, 1)

    wri = Writer(ssd, freesans20)
    Writer.set_textpos(ssd, 10, 0)  # verbose = False to suppress console output
    wri.printstring(string)
    
    if(tank):
        draw_tank(ssd,rhs)
        
    if(tractor):
        draw_tractor(ssd,rhs)
    
    ssd.show()
    
#test_display()