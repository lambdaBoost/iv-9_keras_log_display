"""
reads logs from keras remotemanager server and logs to screen

"""


import wifimgr
from time import sleep
import machine
import urequests
from screen_test import draw_tank
from screen_test2 import test_display
from ssd1306_setup import WIDTH, HEIGHT, setup
from writer import Writer
from iv9 import display_digits_slow
import freesans20
from machine import Pin
from sr_74hc595_bitbang import SR


try:
  import usocket as socket
except:
  import socket


ser = Pin(16, Pin.OUT)
rclk = Pin(15, Pin.OUT)
srclk = Pin(2, Pin.OUT)

oe = Pin(0, Pin.OUT, value=0)    # low enables output
srclr = Pin(32, Pin.OUT, value=1) # pulsing low clears data

sr = SR(ser, srclk, rclk, srclr, oe)


def get_training_logs(endpoint):
    
    #oe.value(1)
    display_digits_slow(['blank']*6, 10, sr)
    #oe.value(0)

    w=urequests.get(endpoint)
    log_list = w.json()
    
    assert len(log_list) > 0
    
    last_log = log_list[-1]
    epoch = last_log['epoch']
    loss = float(last_log['data']['loss'])
    loss = round(loss,4)
    loss = int(loss * 10000)
    total_epochs = last_log['total_epochs']
    
    #make sure we are on a current training run
    assert total_epochs > epoch + 1
    
    #convert to list to display properly
    epoch_list = [int(x) for x in str(epoch)]
    loss_list =  [int(x) for x in str(loss)]
    
    loss_list = ([0] * (5 - len(loss_list))) + loss_list #zero pad loss list
    
    #write to oled display
    test_display(string='epoch' + '/' + str(total_epochs ))
    #display on numitrons
    #clear display
    #oe.value(1)
    display_digits_slow(['blank']*6, 10, sr)
    #oe.value(0)
    display_digits_slow(epoch_list, 10, sr)
    
    sleep(10)
    
    test_display(string='loss: ')
    #clear display
    #oe.value(1)
    display_digits_slow(['blank']*6, 10, sr)
    #oe.value(0)
    display_digits_slow(loss_list, 4, sr)
    sleep(10)


def get_weather_data(key, lat, lon):
    
    #oe.value(1)
    display_digits_slow(['blank']*6, 10, sr)
    #oe.value(0)
    
    w=urequests.get('https://api.openweathermap.org/data/2.5/weather?lat=' +str(lat) +' &lon=' + str(lon) +'&appid='+ key)
    temp = w.json().get('main').get('temp')-273.15
    temp = round(temp,1)
    temp = int(temp*10)
    hum = w.json().get('main').get('humidity')
    hum = int(round(hum))
    wind = w.json().get('wind').get('speed')
    wind = int(round(wind,1))
    wind = wind*10
    w.close()
    
    #get digits
    temp_list = [int(x) for x in str(temp)]
    hum_list = [int(x) for x in str(hum)]
    wind_list = [int(x) for x in str(wind)]
    
    print(temp_list)
    #clear display
    #oe.value(1)
    display_digits_slow(['blank']*6, 10, sr)
    #oe.value(0)
    
    #write to oled display
    test_display(string='temp')
    #display to numitrons
    display_digits_slow(temp_list, len(temp_list)-1, sr)
    sleep(30)
    
    
    #clear display
    #oe.value(1)
    display_digits_slow(['blank']*6, 10, sr)
    #oe.value(0)
    test_display(string = 'hum')
    display_digits_slow(hum_list, 10, sr)
    sleep(30)
    
    #oe.value(1)
    display_digits_slow(['blank']*6, 10, sr)
    #oe.value(0)
    test_display(string = 'wind')
    display_digits_slow(wind_list, len(wind_list)-1, sr)
    sleep(30)
    
    

def get_vehicle_losses(endpoint):
    
    #oryx vehicle losses
    
    
    display_digits_slow(['blank']*6, 10, sr)
    w=urequests.get(endpoint)
    response = w.text
    response = response.replace("\"","")
    response = response.split(',')
    total = response[0]
    destroyed = response[1]
    damaged = response[2]
    abandoned = response[3]
    captured = response[4]
    
    
    lst = [int(x) for x in str(total)]
    test_display(string='total', tank=True)
    #display to numitrons
    display_digits_slow(lst, 10, sr)
    sleep(30)
    
    lst = [int(x) for x in str(destroyed)]
    test_display(string='destroyed', tank=True)
    #display to numitrons
    display_digits_slow(lst, 10, sr)
    sleep(30)
    
    lst = [int(x) for x in str(damaged)]
    test_display(string='damaged', tank=True)
    #display to numitrons
    display_digits_slow(lst, 10, sr)
    sleep(30)
    
    lst = [int(x) for x in str(abandoned)]
    test_display(string='abandoned', tank=True)
    #display to numitrons
    display_digits_slow(lst, 10, sr)
    sleep(30)
    
    lst = [int(x) for x in str(captured)]
    test_display(string='captured', tank=True)
    #display to numitrons
    display_digits_slow(lst, 10, sr)
    sleep(30)
    
    