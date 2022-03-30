import wifimgr
from time import sleep
import machine
import urequests
from screen_test2 import test_display
from ssd1306_setup import WIDTH, HEIGHT, setup
from writer import Writer
import freesans20
from remoteMonitor import get_training_logs, get_weather_data

REMOTEMONITOR_ENDPOINT = 'http://192.168.1.217/publish/epoch/end'
OPENWEATHER_KEY = ''

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
    
    try:
        get_training_logs(REMOTEMONITOR_ENDPOINT)
        
    except AssertionError:
    
        try:
            get_weather_data(OPENWEATHER_KEY)
            
        #TODO blind except - not exactly great but honestly probably best here for now 
        except:
            
            test_display(string = 'no api con')
            sleep(30)
            
    except:
        
        test_display(string = 'pi offline')
        sleep(30)
    
    
"""    
#get btc price
    try:
        r = urequests.get("http://api.coindesk.com/v1/bpi/currentprice/USD.json")
        rate = '%d' % r.json()['bpi']['USD']['rate_float']
        r.close()
    except KeyError:
        rate = "0"
        
        
    #write to oled display
    test_display(string='BTC: ' + rate)
    sleep(30)
"""
