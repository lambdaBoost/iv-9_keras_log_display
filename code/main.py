import wifimgr
from time import sleep
import machine
import urequests
from screen_test2 import test_display
from ssd1306_setup import WIDTH, HEIGHT, setup
from writer import Writer
import freesans20

try:
  import usocket as socket
except:
  import socket

s1 = machine.Pin(2, machine.Pin.OUT)
s2 = machine.Pin(0, machine.Pin.OUT)

s1.value(1)
s2.value(1)

wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  

# Main Code goes here, wlan is a working network.WLAN(STA_IF) instance.
print("ESP OK")

while True:
#get btc price
    try:
        r = urequests.get("http://api.coindesk.com/v1/bpi/currentprice/USD.json")
        rate = '%d' % r.json()['bpi']['USD']['rate_float']
        r.close()
    except KeyError:
        rate = "0"
        
        
    #write to oled display
    test_display(string=rate)
    
    sleep(120)
