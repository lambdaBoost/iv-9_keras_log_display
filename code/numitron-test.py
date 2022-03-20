from time import sleep
import machine

s1 = machine.Pin(15, machine.Pin.OUT)
s2 = machine.Pin(19, machine.Pin.OUT)
s3 = machine.Pin(25, machine.Pin.OUT)
s4 = machine.Pin(26, machine.Pin.OUT)
s5 = machine.Pin(27, machine.Pin.OUT)
s6 = machine.Pin(12, machine.Pin.OUT)
s7 = machine.Pin(13, machine.Pin.OUT)

pins = [s1,s2,s3,s4,s5,s6,s7]

while True:
    
    states=[1,1,1,1,1,0,1]
    for s,p in zip(states,pins):
        p.value(s)
    sleep(1)
    
    states=[0,1,0,0,1,0,0]
    for s,p in zip(states,pins):
        p.value(s)
    sleep(1)
    
    states=[1,1,0,1,0,1,1]
    for s,p in zip(states,pins):
        p.value(s)
    sleep(1)
    
    states=[1,0,1,1,0,1,1]
    for s,p in zip(states,pins):
        p.value(s)
    sleep(1)
    
    states=[1,0,1,0,1,1,0]
    for s,p in zip(states,pins):
        p.value(s)
    sleep(1)
    
    states=[0,0,1,1,1,1,1]
    for s,p in zip(states,pins):
        p.value(s)
    sleep(1)
    
    states=[0,1,1,1,1,1,1]
    for s,p in zip(states,pins):
        p.value(s)
    sleep(1)
    
    states=[1,0,1,1,0,0,0]
    for s,p in zip(states,pins):
        p.value(s)
    sleep(1)
    
    states=[1,1,1,1,1,1,1]
    for s,p in zip(states,pins):
        p.value(s)
    sleep(1)
    
    states=[1,0,1,1,1,1,1]
    for s,p in zip(states,pins):
        p.value(s)
    sleep(1)
    
    
    
    
    
        
