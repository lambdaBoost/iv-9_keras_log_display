#ssd1306 display with font sizing - based entirely on writer library by peter hinch
#available at https://github.com/peterhinch/micropython-font-to-py/tree/master/writer

import machine
from ssd1306_setup import WIDTH, HEIGHT, setup
from writer import Writer

# Font
import freesans20

def test_display(use_spi=False, string='test'):
    ssd = setup(use_spi)  # Create a display instance
    rhs = WIDTH -1
    #ssd.line(rhs - 20, 0, rhs, 20, 1)
    #square_side = 10
    #ssd.fill_rect(rhs - square_side, 0, square_side, square_side, 1)

    wri = Writer(ssd, freesans20)
    Writer.set_textpos(ssd, 10, 0)  # verbose = False to suppress console output
    wri.printstring(string)
    ssd.show()
    
#test_display()