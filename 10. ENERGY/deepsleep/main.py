#!/usr/bin/env python
#
# Copyright (c) 2019, IT university of Copenhagen
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file
# Code: project -> Binary classification algorithm
# IoT course
#
# Thanks Niels..!!
#


import time
import pycom      
import machine  
from machine import Pin    
from machine import I2C
from scd30 import SCD30
pycom.heartbeat(False)  # disable the heartbeat LED
wake_pins = [Pin('P10', mode=Pin.IN, pull=Pin.PULL_DOWN)]
machine.pin_sleep_wakeup(wake_pins, machine.WAKEUP_ANY_HIGH, True)
i2c = I2C(2) # create and use default PIN assignments (P9=SDA, P10=SCL)
# NOTE: Could not make it work using the ESP32 hardware I2C buses (0 & 1), 
# but the bitbanged software bus (2) works
# Yay for libraries!
sensor = SCD30(i2c, 0x61)
time_to_sleep=20

while True:
    print("awake :)")
    machinestarts=time.ticks_ms()
    if sensor.get_status_ready() != 1:
        time.sleep_ms(200)
    time.sleep_ms(500)    
    (co2, temperature, hum) = sensor.read_measurement()
         # Adjust for PCB heating effect. 
    temperature -= 3 # NOTE: Found this value somewhere online
    data=[co2,temperature,hum] # put in array the sensor data
        #make the prediction

    print(round(co2,2),';',round(temperature,2),';',round(hum,2))
    machinefinishes=time.ticks_ms()-machinestarts
    print("machine time "+ str(machinefinishes))
    print("sleep :( ")
    time.sleep(5)
    machine.deepsleep(1000*time_to_sleep)
    print("sleeping_time"+ (machinefinishes-str(machinefinishes)))
    