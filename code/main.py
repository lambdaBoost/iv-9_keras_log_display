import wifimgr
from time import sleep
import machine
import urequests
from screen_test2 import test_display
from ssd1306_setup import WIDTH, HEIGHT, setup
from writer import Writer
import freesans20

OPENWEATHER_KEY = '<openweather-api-key>'

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
        w=urequests.get('https://api.openweathermap.org/data/2.5/weather?lat=57&lon=2&appid='+ OPENWEATHER_KEY)
        temp = w.json().get('main').get('temp')-273.15
        temp = round(temp,1)
        temp = str(temp)
        hum = w.json().get('main').get('humidity')
        hum = str(hum)
        wind = w.json().get('wind').get('speed')
        wind = str(wind)
        w.close()
    except KeyError:
        temp = 'NA'
        hum = 'NA'
        wind = 'NA'
        
    #write to oled display
    test_display(string='temp: ' + temp)
    sleep(30)
    test_display(string = 'hum: ' + hum + '%')
    sleep(30)
    test_display(string = 'wind: ' + wind + 'm/s')
    sleep(30)
    
    
    
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

