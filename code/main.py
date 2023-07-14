import wifimgr
from time import sleep
import machine
import urequests
from screen_test2 import test_display
from ssd1306_setup import WIDTH, HEIGHT, setup
from writer import Writer
import freesans20
from remoteMonitor import get_subscribers

api_key = '<key here>'
channel_id = '<channel id here>'

try:
  import usocket as socket
except:
  import socket


wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  

# Main Code goes here, wlan is a working network.WLAN(STA_IF) instance.
print("ESP OK")

test_display()

i = 0

while True:
    
    try:
        test_display(string = 'subs')
        get_subscribers(api_key, channel_id)
        
               
    except:
        
        #test_display(string = 'api offline')
        sleep(30)
        
    i = i+1
    
    #hard reset every 30 minutes
    if i > 9:
        machine.reset()
