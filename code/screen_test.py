import machine
from ssd1306_setup import WIDTH, HEIGHT, setup
import random
import time

def test_display(use_spi=False, size=10):
    ssd = setup(use_spi)  # Create a display instance
    rhs = WIDTH -1
    
    for i in range(size):
        ssd.line(random.randrange(WIDTH), random.randrange(HEIGHT), random.randrange(WIDTH), random.randrange(HEIGHT), 1)
        square_side = random.randrange(size)
        ssd.fill_rect(random.randrange(WIDTH), random.randrange(HEIGHT), square_side, square_side, 1)

    ssd.show()


def draw_tank(use_spi=False, size=10):
    ssd = setup(use_spi)  # Create a display instance
    rhs = WIDTH -1
    
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
    
    ssd.show()
    
