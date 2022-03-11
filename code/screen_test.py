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

while True:
    
    test_display()
    time.sleep(1)