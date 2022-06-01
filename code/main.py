import wifimgr
from time import sleep
import machine
import urequests
from screen_test2 import test_display
from ssd1306_setup import WIDTH, HEIGHT, setup
from writer import Writer
import freesans20
from remoteMonitor import get_training_logs, get_weather_data, get_vehicle_losses

REMOTEMONITOR_ENDPOINT = 'http://192.168.1.217/publish/epoch/end'
VEHICLE_LOSS_ENDPOINT = 'http://192.168.1.217:8080/items/'
OPENWEATHER_KEY = ''
LAT = 57
LON = 2

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

while True:
    
    try:
        get_training_logs(REMOTEMONITOR_ENDPOINT)
        
    except AssertionError:
    
        try:
            #get_weather_data(OPENWEATHER_KEY, LAT, LON)
            get_vehicle_losses(VEHICLE_LOSS_ENDPOINT)
            
        #TODO blind except - not exactly great but honestly probably best here for now 
        except:
            
            test_display(string = 'no api con')
            sleep(30)
            
    except:
        
        test_display(string = 'pi offline')
        sleep(30)
    
    #hard reset every 30 minutes
    if time.ticks_ms() > 1800000:
        machine.reset()
    
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
