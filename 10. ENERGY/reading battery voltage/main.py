#!/usr/bin/env python
#
# Copyright (c) 2019, IT university of Copenhagen
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file
#


import time
import pycom      
import machine    
from machine import I2C
from scd30 import SCD30
from machine import ADC
pycom.heartbeat(False)  # disable the heartbeat LED
i2c = I2C(2) # create and use default PIN assignments (P9=SDA, P10=SCL)
# NOTE: Could not make it work using the ESP32 hardware I2C buses (0 & 1), 
# but the bitbanged software bus (2) works
adc = ADC()
bat_voltage = adc.channel(attn=ADC.ATTN_11DB, pin='P16')
sensor = SCD30(i2c, 0x61)
# note that the expansionboard 2.0 has a voltage divider of 115K / 56K to account for
# 115K / 56K, ratio =~ 1:3
while True:
    if sensor.get_status_ready() != 1:
        time.sleep_ms(200) 
    (co2, temperature, hum) = sensor.read_measurement()
         # Adjust for PCB heating effect. 
    #reading the battery voltage    
    vbat = bat_voltage.voltage()
    temperature -= 3 # NOTE: Found this value somewhere online
    data=[co2,temperature,hum] # put in array the sensor data
        #make the prediction
    print(round(co2,2),';',round(temperature,2),';',round(hum,2),';',vbat*1.5)
    time.sleep(5)

    
