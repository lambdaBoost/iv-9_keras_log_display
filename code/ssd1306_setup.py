import machine
from ssd1306 import SSD1306_SPI, SSD1306_I2C

WIDTH = const(128)
HEIGHT = const(32)

def setup(use_spi=False, soft=True):
    if use_spi:
        # Pyb   SSD
        # 3v3   Vin
        # Gnd   Gnd
        # X1    DC
        # X2    CS
        # X3    Rst
        # X6    CLK
        # X8    DATA
        pdc = machine.Pin('X1', machine.Pin.OUT_PP)
        pcs = machine.Pin('X2', machine.Pin.OUT_PP)
        prst = machine.Pin('X3', machine.Pin.OUT_PP)
        if soft:
            spi = machine.SPI(sck=machine.Pin('X6'), mosi=machine.Pin('X8'), miso=machine.Pin('X7'))
        else:
            spi = machine.SPI(1)
        ssd = SSD1306_SPI(WIDTH, HEIGHT, spi, pdc, prst, pcs)
    else:  # I2C
        # Pyb   SSD
        # 3v3   Vin
        # Gnd   Gnd
        # Y9    CLK
        # Y10   DATA
        if soft:
            pscl = machine.Pin(5, machine.Pin.OPEN_DRAIN)
            psda = machine.Pin(4, machine.Pin.OPEN_DRAIN)
            i2c = machine.I2C(scl=pscl, sda=psda)
        else:
            i2c = machine.I2C(2)
        ssd = SSD1306_I2C(WIDTH, HEIGHT, i2c)
    return ssd