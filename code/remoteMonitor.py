"""
reads logs from keras remotemanager server and logs to screen

"""


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



def get_training_logs(endpoint):
    
    

    w=urequests.get(endpoint)
    log_list = w.json()
    
    assert len(log_list) > 0
    
    last_log = log_list[-1]
    epoch = last_log['epoch']
    loss = float(last_log['data']['loss'])
    loss = round(loss,3)
    total_epochs = last_log['total_epochs']
    
    #make sure we are on a current training run
    assert total_epochs > epoch + 1
    
    #write to oled display
    test_display(string='epoch:' + str(epoch) + '/' + str(total_epochs ))
    sleep(10)
    test_display(string='loss: ' + str(loss))
    sleep(10)


def get_weather_data(key):
    
    w=urequests.get('https://api.openweathermap.org/data/2.5/weather?lat=57&lon=2&appid='+ key)
    temp = w.json().get('main').get('temp')-273.15
    temp = round(temp,1)
    temp = str(temp)
    hum = w.json().get('main').get('humidity')
    hum = str(hum)
    wind = w.json().get('wind').get('speed')
    wind = str(wind)
    w.close()
    #write to oled display
    test_display(string='temp: ' + temp)
    sleep(30)
    test_display(string = 'hum: ' + hum + '%')
    sleep(30)
    test_display(string = 'wind: ' + wind + 'm/s')
    sleep(30)
    