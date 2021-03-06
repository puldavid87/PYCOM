
#!/usr/bin/env python
#
# Copyright (c) 2019, IT university of Copenhagen
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file
# Code: io4.py -> button configuration avoiding rebounds
# IoT course
#

from machine import Pin
import time
led = Pin('P9', mode = Pin.OUT) # pin 9 as output
button = Pin('P8', mode = Pin.IN) # pin 8 as output
on=False  #bool variable
while True:
    if(button() == 0):         # state change condition
        time.sleep_ms(200)     # anti-bounce delay
        on=on^1                # on changes state 
        if on == True:         # condition
            print("led on")
            led.value(1)       # led on
        else:
            print("led off")
            led.value(0)       # led off
